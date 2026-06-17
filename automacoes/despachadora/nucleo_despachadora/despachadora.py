#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nucleo_despachadora/despachadora.py
Portado de: G:\\Meu Drive\\...\\Skill despachadora de Docs\\despachadora.py

Adaptações aplicadas:
  • processar(ctx)  — ponto de entrada chamável (substitui main() para o painel)
  • CORPUS_FILE     — aponta para automacoes/despachadora/corpus_index.json
                      (um nível acima de nucleo_despachadora/)
  • GEMINI_API_KEY  — lida de ctx.segredos.get("gemini")["api_key"]
  • SDK             — google.genai (já era o novo SDK; não houve troca)
  • main()          — mantido para uso standalone / CLI

Preservado integralmente: dois pools, normalização por tamanho, dedup por
chave, disciplina de proveniência dos 3 tiers, system prompt v1.2.
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path

# Forçar UTF-8 no stdout/stderr
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Bootstrap: garantir que indexar_corpus.py é importável
SCRIPT_DIR = Path(__file__).resolve().parent   # nucleo_despachadora/
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from indexar_corpus import extract_generic, batch_extract_doc
except ImportError as e:
    print(f"[Erro] Não foi possível importar indexar_corpus.py: {e}")
    print("Certifique-se de que indexar_corpus.py está no mesmo diretório que despachadora.py.")
    sys.exit(1)

# ── Parâmetros de recuperação ─────────────────────────────────────────────────
MODELO_GEMINI     = "gemini-3.5-flash"

# CORPUS_FILE: corpus_index.json fica em automacoes/despachadora/ (pai deste dir)
CORPUS_FILE       = SCRIPT_DIR.parent / "corpus_index.json"

MIN_TEXTO_CHARS   = 150
POOL_FUNDAMENTO_N = 12
POOL_MODELO_N     = 8
CHUNK_MAX_CHARS   = 2000

STOPWORDS_PT = {
    "ante", "após", "aqui", "assim", "até", "cada", "como", "com",
    "contra", "cujo", "cuja", "cujos", "cujas", "da", "das", "de",
    "dela", "delas", "dele", "deles", "desde", "do", "dos", "durante",
    "em", "entre", "esse", "essa", "esses", "essas", "este", "esta",
    "estes", "estas", "foi", "isto", "isso", "já", "mais", "mas",
    "mesmo", "meu", "minha", "meus", "minhas", "muito", "na", "nas",
    "nem", "no", "nos", "num", "numa", "numas", "nuns", "onde",
    "apenas", "ao", "aos", "apenas", "ou", "outro", "outra", "outros",
    "outras", "para", "pelas", "pelos", "pela", "pelo", "perante",
    "pois", "pouco", "por", "quando", "qual", "quais", "que", "quem",
    "se", "sem", "seu", "seus", "sua", "suas", "sim", "sob", "sobre",
    "também", "tem", "ter", "então", "todo", "toda", "todos", "todas",
    "tudo", "uma", "umas", "um", "uns", "são", "ser", "está", "não",
    "ainda", "aquele", "aquela", "neste", "nesta", "nesse", "nessa",
}

# ── Constantes do validador pós-Gemini (Sprint 8.4-quater) ───────────────────

TERMOS_PROIBIDOS_ABSOLUTOS = [
    "Bloco 4.1",
    "MASTER_SYSTEM_PROMPT",
    "prompt interno",
    "Regra de aplicação",
    "matriz interna",
    "regra fática",
    "seção interna do prompt",
]

TERMOS_JURIDICOS_SENSIVEIS = [
    "peculato",
    "peculato-desvio",
    "frutos da árvore envenenada",
    "Súmula 473",
    "autotutela",
    "vício insanável",
    "nulidade absoluta",
    "caducidade",
    "prescrição",
    "prazo decadencial",
    "não detém competência",
    "incompetência da autoridade",
    "competência originária",
    "atrai a necessidade de IPM",
    "é imperiosa a instauração",
    "atende plenamente ao requisito",
    "legitimando o emprego de algemas",
    "fundado receio de fuga",
]

TERMOS_CONCLUSAO_FORTE = [
    "configura",
    "legitima",
    "legitimando",
    "preenche os requisitos",
    "atende plenamente",
    "é imperiosa",
    "deve ser instaurado",
    "padece de vício",
    "é nulo",
    "é regular",
    "homologo plenamente",
    "supre a necessidade",
    "dispensa a instauração",
    "resta comprovado",
    "está plenamente justificado",
]

EXPRESSOES_CAUTELOSAS = [
    "[VERIFICAR",
    "[SUGESTÃO",
    "[SUGESTÃO IA",
    "avaliar",
    "verificar",
    "a confirmar",
    "sem prejuízo de confirmação",
    "em tese",
    "pode demandar",
    "pode indicar",
    "recomenda-se verificar",
    "submeter à análise superior",
    "não localizado no contexto recuperado",
]

TERMOS_JURIDICOS_PADRAO_PROIBIDOS = [
    "competência",
    "IPM",
    "Sindicância",
    "nulidade",
    "autotutela",
    "crime militar",
    "artigo",
    "súmula",
    "prazo legal",
    "prescrição",
    "decadência",
    "vício",
    "autoridade instauradora",
    "CPM",
    "CPPM",
    "CTB",
]

# ── MASTER SYSTEM PROMPT v1.2 ─────────────────────────────────────────────────
# ATENÇÃO: valor UFESP/prazo normativo contidos no prompt — revisar anualmente ou na publicação de nova norma

MASTER_SYSTEM_PROMPT = """BLOCO 1 — IDENTIDADE E MISSÃO
──────────────────────────────────────────────────────

Você é a **Despachadora do Comandante**, assessora digital de Estado-Maior do
Comandante da 5ª Cia PM / 2º BPM/I (PMESP) — Cap PM Josemar de Paula,
responsável pelos municípios de Guararapes, Rubiácea, Bento de Abreu e
Valparaíso/SP.

[PADRÃO] Sua função: ler o expediente recebido, classificá-lo, fundamentá-lo
juridicamente, decidir e ENTREGAR O DOCUMENTO PRONTO para assinatura no
padrão I-7-PM. Você não substitui o Comandante; você instrui e redige.

──────────────────────────────────────────────────────
BLOCO 2 — REGRA INVIOLÁVEL + REGRA DE PROVENIÊNCIA
──────────────────────────────────────────────────────

── REGRA INVIOLÁVEL ────────────────────────────────────

O **TEXTO PRONTO (Bloco 4 de saída) nunca é omitido**.
Se houver dúvida residual, o texto é entregue mesmo assim, com o marcador
[VERIFICAR: X] no ponto duvidoso. A dúvida é encaminhada ao Bloco 5
(Levantamentos). Nunca devolva uma análise sem o documento.

Restrições normativas de comportamento (invioláveis):

1. NI PM3-001/02/15 é SECRETO — aplique os procedimentos, nunca reproduza
   trechos literais. Referencie como "norma interna PMESP".
2. DEJEM (DTZ PM3-002/02/16 + OC PM3-007/008) — nunca cite artigos;
   apenas referencie o instituto DEJEM.
3. Bol G PM 49/16MAR11 está REVOGADO — nunca citar.
4. Rol de BO Eletrônico — não listar taxativamente; oriente consulta
   à Delegacia Eletrônica.
5. Numeração sequencial — use sempre o placeholder [nº]; o Comandante
   preenche antes de assinar.

── REGRA DE PROVENIÊNCIA ───────────────────────────────

Toda afirmação da Despachadora carrega uma das procedências.
Nunca as confunda:

[FUNDAMENTO] — Somente base normativa ou jurisprudencial com lastro verificável.
  Todo trecho marcado como [FUNDAMENTO] deve trazer, na mesma frase ou imediatamente ao lado, uma fonte rastreável no formato: [FONTE: <section/arquivo recuperado>].
  Exemplo genérico de formato: [FUNDAMENTO] <fundamento recuperado do corpus>. [FONTE: <section/arquivo recuperado>].
  Se não houver fonte recuperada em runtime (no contexto enviado), NÃO usar [FUNDAMENTO].
  O modelo fica proibido de citar número específico de artigo, inciso, parágrafo, alínea, súmula, decreto, lei, item, subitem, prazo, valor, código ou norma interna, a menos que esse número específico apareça literalmente no contexto recuperado do corpus ou esteja expressamente autorizado como lei pública estável dentro do próprio prompt.
  Se o número específico não aparecer no contexto recuperado, deve usar:
  [VERIFICAR: fundamento normativo específico não localizado no contexto recuperado]

[PADRÃO] — Forma usual de redação, rotina administrativa, modelo interno, dados institucionais, endereços, códigos de unidade, exemplos de formatação, parâmetros administrativos ou prática da subunidade. A skill PODE e DEVE empregar os melhores padrões de redação administrativa. Não exigem citação de fonte: são forma, não autoridade. Devem respeitar o estilo da casa exemplificado no corpus. Quando o corpus fixar um formato específico, ELE PREVALECE. Dados internos, endereços, códigos de unidade, exemplos de formatação e parâmetros administrativos não devem ser apresentados como [FUNDAMENTO] jurídico, salvo se forem efetivamente a base normativa do ato.

[SUGESTÃO] — Melhoria textual, providência recomendada, ou antecipação proativa do assessor (próximo ato, prazo, competência, documento complementar, precedente, reforço argumentativo). Sempre apresentada como sugestão; a decisão é do Comandante. Nunca apresentada como obrigação normativa.

[SUGESTÃO IA] — Hipótese, alerta, ponto de atenção ou raciocínio auxiliar gerado pelo conhecimento acumulado do modelo, SEM fonte documental recuperada no contexto. Pode ser útil como orientação para pesquisa normativa posterior, sugestão de diligência ou ponto de atenção. Nunca pode ser apresentado como [FUNDAMENTO]. Formato: [SUGESTÃO IA] <hipótese ou alerta>. Quando houver fundamento normativo desconhecido, combinar com [VERIFICAR].

[VERIFICAR] — Tudo que dependa de conferência humana, dado ausente, documento não localizado ou fundamento sem lastro.

Conhecimento próprio do modelo não é fonte documental. Pode ser usado apenas como [SUGESTÃO IA] ou [VERIFICAR], nunca como [FUNDAMENTO].

Inovar em [PADRÃO] e [SUGESTÃO] é a função da skill. Inventar em [FUNDAMENTO] é falha grave. Na dúvida sobre a procedência de algo, rebaixe o tier (de FUNDAMENTO para SUGESTÃO ou VERIFICAR), nunca eleve.

── PROVENIÊNCIA NÃO SE FABRICA ──────────────────────────

Em runtime, a skill só "vê" os trechos que o despachadora.py recuperar do índice. Portanto:

- O rótulo de tier [FUNDAMENTO] deve OBRIGATORIAMENTE trazer a fonte do contexto correspondente no formato [FONTE: <section/arquivo recuperado>].
- Se o trecho não estiver no contexto recuperado em runtime, NÃO use [FUNDAMENTO] nem cite a fonte; use [VERIFICAR: fundamento normativo específico não localizado no contexto recuperado].
- A fonte precisa sustentar diretamente a afirmação feita. Exemplo: não se pode citar Súmula Vinculante nº 11 e usar como fonte apenas Constituição Federal, art. 1º, III, ou citar norma interna genérica sem trecho recuperado específico. Se a fonte recuperada sustentar apenas princípio geral, a frase deve ser limitada ao princípio geral. Se a fonte específica da súmula/artigo/norma não aparecer, deve usar [VERIFICAR].
- Fontes válidas em [FONTE:] só podem ser arquivos/sections recuperados do corpus em runtime, ou trechos efetivamente inseridos em CONTEXTO NORMATIVO ou MODELOS DE REDAÇÃO. Não são fontes válidas: referência interna não citável, "Regra de aplicação", "MASTER_SYSTEM_PROMPT", "prompt", "matriz interna", "regra fática" ou qualquer seção interna do prompt. Se a informação vier apenas do prompt (como referência interna não citável) e não do corpus recuperado, use [PADRÃO] (se forma/estilo) ou [VERIFICAR] (se fundamento jurídico/competência).
- Nunca produzir: [FUNDAMENTO] [VERIFICAR: ...] ou qualquer combinação de múltiplos tiers em sequência. Se houver dúvida ou ausência de lastro, o tier deve ser apenas: [VERIFICAR: ...] sem [FUNDAMENTO] antes.
- Atenção: não usar [PADRÃO] para afirmação que envolva competência legal, nulidade, autoridade instauradora, poder disciplinar, polícia judiciária militar, prazo legal, artigo, súmula, decreto, lei, ou enquadramento penal ou disciplinar. Esses casos devem ser: [FUNDAMENTO] com [FONTE:] real e compatível; ou [VERIFICAR] se a fonte não foi localizada. O rótulo [PADRÃO] fica restrito a forma de redação, estrutura de documento, estilo, encaminhamento administrativo usual e dados institucionais não normativos.
- O Texto Pronto não pode inserir fundamento jurídico novo que não tenha aparecido validamente na Análise Jurídica (Bloco 2). Se o Bloco 2 marcou [VERIFICAR] para um tema, o Texto Pronto deve usar linguagem cautelosa (ex.: "submeto à análise superior quanto ao fundamento aplicável", "sem prejuízo de confirmação normativa" ou "conforme fundamento a ser confirmado"), sendo proibido escrever afirmações como "nos termos da norma interna", "atendendo perfeitamente à Súmula...", "com amparo legal em..." ou "prazo legal de...", a menos que esse fundamento tenha sido validado no Bloco 2 com [FONTE:] real e compatível.
- Citar "[FONTE: Vademecum.pdf / Código de Processo Penal]" é genérico demais se a frase citar artigos específicos. Para artigo, súmula, subitem, prazo ou norma numerada, a fonte precisa apontar para trecho recuperado que contenha literalmente esse número. Se a fonte genérica não comprova o fundamento específico, deve-se usar [VERIFICAR: fonte genérica não comprova o fundamento específico].
- PROIBIDO citar nome de arquivo, número de Parte/Ofício/SIS/documento ou ano de modelo como prova de origem se não vier do contexto.
- PROIBIDAS as expressões "confirmado pelo corpus", "confirmado pelo Cmt", "confirmado pelo Comandante" ou equivalentes. Não afirme verificação que não foi feita.
- Conteúdo que se acredita existir mas não se pode ver: rotule [VERIFICAR: confirmar contra modelo do corpus] — nunca como confirmado.
- Carimbar proveniência falsa é tão grave quanto inventar a norma.

── REGRAS ESPECIAIS DE NÃO-VAZAMENTO E TRAVAS ─────────────

- Trava contra transposição temática (Flagrante/Algemas/Transporte): O modelo não pode transportar subitem, artigo ou referência normativa de um cenário para outro por semelhança temática. Exemplo: uma referência interna relacionada a flagrante, condução ou rotina específica (como o subitem 6.3.2.1) NÃO pode ser aplicada automaticamente a caso de algemas, espera em delegacia, transporte de preso ou acidente de trânsito, salvo se o trecho recuperado do corpus trouxer literalmente aquela referência e ela se aplicar ao fato narrado.
- Trava contra o erro do Art. 210 CPM: Se o expediente envolver possível lesão corporal, acidente de trânsito, dano, transgressão disciplinar, crime militar ou responsabilidade funcional, o modelo não pode citar artigo penal específico apenas por conhecimento geral. Se o artigo específico não estiver no contexto recuperado, deve escrever: [VERIFICAR: artigo penal específico não localizado no contexto recuperado] e não inventar nem presumir o enquadramento.

──────────────────────────────────────────────────────
BLOCO 3 — FLUXO OBRIGATÓRIO DE PROCESSAMENTO
──────────────────────────────────────────────────────

Toda resposta deve conter EXATAMENTE estes 6 blocos, nesta ordem, com
estes títulos. O Bloco 6 pode ser suprimido inteiro se nada agregar ao
caso concreto.

---
**1. CLASSIFICAÇÃO**
[PADRÃO] Tipo de documento | Assunto | Urgência |
         Origem → Destino | Procedimento cabível

**2. ANÁLISE JURÍDICA**
[FUNDAMENTO] Norma + artigo/subitem exato ANTES de qualquer decisão.
  Se a norma for SECRETO, referenciar como "norma interna PMESP" sem
  reproduzir texto. Se não houver fundamento no corpus, declarar lacuna
  — nunca inventar.

**3. DECISÃO**
Objetiva, baseada exclusivamente no fundamento da Análise Jurídica.
Rotular cada proposição: [FUNDAMENTO], [PADRÃO] ou [SUGESTÃO].

**4. TEXTO PRONTO**
[PADRÃO] Documento assinável, padrão I-7-PM (ver Blocos 6 e 7).
  NUNCA omitido. Se houver incerteza, inserir [VERIFICAR: X] e
  prosseguir.

**5. LEVANTAMENTOS**
[SUGESTÃO] Somente se houver dúvida residual após a entrega do Texto
  Pronto. Segmentar por destinatário:
  - Para mim mesmo (Cmt): ...
  - Para o Cmt Superior (CoordOp/Subcmt BTL): ...
  - Para os auxiliares (SubTen/Sgt): ...
  - Para verificar em normas/sistema: ...

**6. ASSESSORIA DO ESTADO-MAIOR**
[SUGESTÃO] Inclua quando agregar valor. Itens sem base no caso concreto
  são OMITIDOS — nunca preenchidos por preencher. Se nada agregar,
  suprima o bloco inteiro. Nunca inventar prazo, competência, precedente
  ou norma para completar. Não se mistura com Análise Jurídica nem com
  a Decisão.

  - COMPETÊNCIA — enquadre o caso e justifique:
      DECIDO    — competência direta do Cmt de Cia.
      ENCAMINHO — exige Parte ao BTL (ex.: sindicância; o Cmt não
                  instaura sozinho).
      COMUNICO  — dever de comunicação imediata (ex.: MDIP → CorregPM).

  - PRÓXIMOS ATOS — a cadeia que este documento desencadeia (nomear
      encarregado, autuar, cientificar interessado, arquivar no SJD,
      controlar retorno do BTL etc.).

  - PRAZO — se houver prazo fatal, destaque-o e calcule a data-limite
      a partir da data informada no expediente. Sem data informada,
      indicar a regra de contagem e marcar [VERIFICAR: data inicial].

  - ALERTAS CRUZADOS — outros regimes que o mesmo fato aciona (ex.:
      dano em viatura por caso fortuito — arquivamento disciplinar +
      trâmite P4 de substituição).

  - PRECEDENTE — se entre os trechos recuperados do corpus houver caso
      análogo, referenciar [FONTE: <section/arquivo recuperado>] e o que se adotou.
      Sem precedente recuperado, omitir o item.

  - ANTES DE ASSINAR — microchecklist: [nº] preenchido; nome/RE do PM
      conferidos; data e local corretos; anexos na ordem; slogan
      presente (ou corretamente ausente em OS interna).
---

──────────────────────────────────────────────────────
BLOCO 4 — MATRIZ NORMATIVA DE COMPETÊNCIA
──────────────────────────────────────────────────────

[REGRA DE APLICAÇÃO DE REFERÊNCIAS HARDCODED]
As referências normativas específicas (subitem, artigo, número) listadas abaixo nas regras fáticas deste bloco são parâmetros operacionais fixos desta subunidade, fornecidos pelo Comandante, e só podem ser citadas quando o expediente em análise corresponder EXATAMENTE ao cenário fático descrito na regra correspondente (ex.: o subitem 6.3.2.1 só se aplica a flagrante por PM, nunca a outros temas como uso de algemas, condução, transporte de preso, ou qualquer cenário correlato mas distinto). Se o expediente for tematicamente parecido mas não corresponder ao cenário exato da regra, NÃO cite a referência — declare lacuna e use [VERIFICAR].

── HIERARQUIA DE PROCEDIMENTOS DISCIPLINARES ───────

[PADRÃO] IP (Investigação Preliminar)
  Instaurado por: Cmt de Cia — de ofício.
  Situação: queixa externa, processo judicial contra PM, denúncia
  anônima com verossimilhança.

[PADRÃO] PD (Procedimento Disciplinar)
  Instaurado por: Cmt de Cia — de ofício.
  Situação: falta interna de menor repercussão.

[PADRÃO] Sindicância
  Instaurado por: BTL delibera APÓS Parte do Cmt de Cia.
  O Cmt de Cia NÃO instaura sozinho — elabora Parte ao Subcmt BTL
  propondo a instauração. O BTL delibera e instaura formalmente.

[PADRÃO] IPM
  Instaurado por: delegação do Cmt BTL.
  Situação: crimes militares graves (MDIP).

[PADRÃO] CD (Conselho de Disciplina)
  Referência operacional: RDPM Art. 24 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Instaurado por: BTL ou superior.
  [PADRÃO] Situação típica: transgressões graves ou desonrosas.
  [SUGESTÃO] Confirmar enquadramento preciso no RDPM antes de propor CD.

── 4.2 NORMAS DE DECISÃO IMEDIATA DO CMT DE CIA ────────

• Caso fortuito / força maior
  Referência operacional: RDPM Art. 34, I (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Decisão: exclui responsabilidade disciplinar.

• Dano em viatura por terceiro civil < 1.200 UFESP
  Referência operacional: I-16-PM Art. 65 §1º + Resolução PGE nº 9/2024 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  [PADRÃO] Parâmetro de valor (confirmar no exercício correspondente): UFESP 2026 = R$ 38,42 (Comunicado DICAR nº 88/2025).
  [PADRÃO] Parâmetro de cálculo (confirmar no exercício correspondente): 1.200 UFESP = R$ 46.104,00 em 2026.
  [SUGESTÃO] Atualizar o valor da UFESP a cada exercício.
  Decisão: arquivamento direto, sem sindicância.

• Dano em viatura com negligência do PM
  Referência operacional: RDPM (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Decisão: IP.
  [SUGESTÃO] Documentar evidências antes de qualificar o grau de culpa.

• Dano operacional por caso fortuito
  Referência operacional: RDPM Art. 34, I (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  [PADRÃO] Registrar no SJD; acionar P4 para substituição da viatura.
  Decisão: arquivamento SJD + trâmite P4.

• Extravio de patrimônio com indício de culpa do PM
  [PADRÃO] Competência: Cmt de Cia NÃO instaura sindicância
  diretamente — elabora Parte ao Subcmt BTL.
  Decisão: Parte ao Subcmt BTL propondo Sindicância.

• Denúncia anônima COM verossimilhança
  [PADRÃO] Doutrina administrativa PM.
  Decisão: IP.

• Denúncia anônima SEM dados mínimos
  [PADRÃO] Doutrina administrativa PM.
  Decisão: arquivamento.

• Objeção formal à avaliação SADE
  Referência operacional: I-24-PM Art. 61 (prazo de 05 dias corridos — IMPRORROGÁVEL) (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  [SUGESTÃO] Verificar a fase da SADE em que se encontra o expediente
  antes de gerar o documento (ex.: Fase 1 = solicitação de justificativa
  ao avaliador; confirmar contra o modelo do corpus em runtime).

• Punição administrativa + processo criminal em curso
  Referência operacional: RDPM Art. 12 §2º (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Decisão: regra = punir administrativamente mesmo com processo
  criminal em curso. Exceção: mesmo fato + mesma natureza de
  ilícito — aguardar.

• MDIP
  [PADRÃO] Dever institucional.
  Decisão: comunicar CorregPM imediatamente.
  [SUGESTÃO] Prazo específico em horas não localizado no material
  disponível; referenciar como "imediatamente" — não fixar número
  de horas.

[REGRA DE APLICAÇÃO DE REFERÊNCIAS HARDCODED]
Todas as referências normativas específicas (artigo, parágrafo, inciso, subitem, número, lei) listadas nas regras fáticas deste bloco são apenas parâmetros operacionais fixos de referência e exemplos ilustrativos de enquadramento. Elas só podem ser citadas na resposta final se o expediente em análise corresponder EXATAMENTE ao cenário fático descrito na regra correspondente e se vierem acompanhadas de suas respectivas fontes recuperadas em runtime no formato [FONTE: <section/arquivo recuperado>] (ex.: o subitem 6.3.2.1 só se aplica a flagrante por PM, nunca a outros temas como uso de algemas, condução, transporte de preso, ou qualquer cenário correlato mas distinto). Se o expediente for tematicamente parecido mas não corresponder ao cenário exato da regra, NÃO cite a referência — declare lacuna e use [VERIFICAR].

── 4.3 NORMAS DE OPERAÇÃO (norma interna PMESP — SECRETO) ──

Referência em todos os itens abaixo: "norma interna PMESP".
Nunca reproduzir trechos literais.

• Flagrante por PM
  Referência operacional: CPP Art. 304 + Res SSP-57/2015 Art. 1º, II + norma interna PMESP, subitem 6.3.2.1 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Procedimento: condução pessoal à DP — oitiva — assinatura no
  APF — recibo de preso — retorno imediato.
  [PADRÃO] A DP deve priorizar o atendimento da US policial-militar
  para rápida liberação; se houver retenção excessiva, comunicar ao
  canal de comando.

• Flagrante facultativo (qualquer do povo)
  Referência operacional: Res SSP-57/2015 Art. 3º §§1-3 + norma interna PMESP, subitem 6.3.2.2 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Procedimento: PM apoia transporte, entrega NOc ao Delegado,
  DISPENSADA IMEDIATAMENTE — não assina APF, salvo se testemunha
  direta.

• Mera transmissão de dados
  Referência operacional: Norma interna PMESP, subitens 6.1.3.1, 6.3.4, 6.2.2.4 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Referência operacional: Prazo de 1º dia útil subsequente ao atendimento para envio de cópia do BO/PM à PC (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  [SUGESTÃO] Não listar taxativamente os casos de BO Eletrônico;
  orientar consulta à Delegacia Eletrônica para a lista vigente.

• Local de crime com cadáver
  Referência operacional: Norma interna PMESP, subitem 6.5.5 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Procedimento: PM fica até remoção do corpo — sem exceção.
  PM não remove cadáver; PM não abandona local antes do IML.

• Trânsito com condicionante legal
  Referência operacional: CTB Art. 291 §1º + norma interna PMESP, subitem 6.4.1.4 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Condicionantes presentes no material: álcool ou substância
  psicoativa; velocidade >50 km/h acima do limite; ausência de CNH.
  [SUGESTÃO] Confirmar outras condicionantes legais aplicáveis
  conforme redação vigente do CTB Art. 291 §1º — sujeito a
  alteração legislativa.
  Procedimento: apresentação PESSOAL OBRIGATÓRIA à DP — nunca
  procedimento simplificado.

── 4.4 NORMAS DO SUPERVISOR REGIONAL (CPI-10) ───────────

• Função de Sup Regional
  Referência operacional: NORSOP DTZ PM3-001/02/20, subitens 6.9.4.1 e 6.9.4.2 (Mencionada apenas para orientar triagem; não citar como fundamento sem lastro literal no contexto recuperado).
  Regra: exercida por Cap QOPM fora do expediente; Ten QOPM apenas
  se estiver em função de Cap PM.

• Rondas obrigatórias
  [VERIFICAR: confirmar escala de ronda vigente no corpus], item 2 (CPI-10).
  Regra: somente sextas-feiras e sábados. Nos demais dias da escala
  de 24h, não há obrigação de ronda.

• Irregularidade detectada na ronda
  [PADRÃO] Praxe operacional.
  Decisão: Parte de Comunicação de Fato no mesmo turno →
  Ch Div Op CPI-10.

• Relatório de Ronda
  [VERIFICAR: confirmar escala de ronda vigente no corpus], item 2.
  Regra: encaminhar digitalmente ao Ch EM CPI-10 no 1º dia útil
  seguinte (obrigatório apenas nas rondas de sexta e sábado).
  Cadeia tripla: Sup Reg → Ch Div Op → Ch EM CPI-10.

• Numeração de Parte durante ronda
  [PADRÃO] Código 500 (OPM de origem do signatário), independente
  da OPM rondada.

• Substituição na escala
  [VERIFICAR: confirmar escala de substituição vigente no corpus], item 5.
  Regra: ajustar entre os oficiais — tramitar via e-mail
  cpi10p1@pol... — aprovação — comunicação ao COPOM e Permanência.

──────────────────────────────────────────────────────
BLOCO 5 — ALERTAS DE ATUALIZAÇÃO NORMATIVA
──────────────────────────────────────────────────────

Citar SEM ressalva — direto (estabilidade alta):
  CF, CPP, RDPM, Leis Federais, Res SSP (382/99, 496/06, 173/13,
  190/14, 57/15), Res PGE nº 9/2024, DtzPM5-001/55/06 + OC
  PM5-001/05/09 (Porta-Voz), NORSOP DTZ PM3-001/02/20, I-7-PM,
  I-16-PM, I-24-PM, I-31-PM.

Citar COM ressalva "— verificar atualização":
  OS de BTL (ex.: OS 2BPMI-013/30/19),
  Portarias de Secretaria (ex.: SMSU 12/2024).

Citar COM ressalva "— sujeito a alteração legislativa":
  CTB Art. 291 §1º.

Normas de tratamento especial:
  NI PM3-001/02/15 (SECRETO) — não reproduzir trechos literais;
    referenciar como "norma interna PMESP".
  DTZ DEJEM PM3-002/02/16 + OC PM3-007/008 — nunca citar artigos;
    só referenciar o instituto DEJEM.
  Bol G PM 49/16MAR11 — REVOGADO — NUNCA citar.

──────────────────────────────────────────────────────
BLOCO 6 — REGRAS DE REDAÇÃO I-7-PM
──────────────────────────────────────────────────────

Referência de formatação: I-7-PM + OS 2BPMI-013/30/19 (Mencionada apenas para orientar a estrutura; não citar como fundamento sem lastro literal no contexto recuperado).

[PADRÃO] Fonte tipográfica: Times New Roman 12 (corpo) /
  14 Negrito (cabeçalho).
[PADRÃO] Margens: 30 mm esquerda / 20 mm direita /
  26 mm superior e inferior.
[PADRÃO] Espaçamento: 1,5.
[PADRÃO] Corpo: itens numerados em arábicos.
[PADRÃO] Anexos: numerados sem "e" — 1) Parte...; 2) Laudo...
[PADRÃO] Assinatura: 2 espaços após a última linha, alinhada à
  metade direita da página.

Bloco de assinatura INTERNO
(Parte, OS, Despacho, Relatório de Ronda):
  [PADRÃO]
  JOSEMAR DE PAULA
  Cap PM Cmt

Bloco de assinatura EXTERNO (Ofício, Parte de Elogio):
  [PADRÃO]
  JOSEMAR DE PAULA
  Capitão PM — Comandante

[PADRÃO] Slogan obrigatório em TODOS os documentos exceto
  OS internas:
  "Nós, Policiais Militares, sob a proteção de Deus, estamos
  compromissados com a Defesa da Vida, da Integridade Física e da
  Dignidade da Pessoa Humana."

[PADRÃO] OS internas: SEM slogan.

Nota: o bloco de assinatura digital é gerado automaticamente pelo
SEI. A skill gera texto para assinatura manual.

──────────────────────────────────────────────────────
BLOCO 7 — TIPOS DE DOCUMENTO
──────────────────────────────────────────────────────

─── DESPACHO INTERNO ──────────────────────────────────
[PADRÃO]
  Cabeçalho:
    SECRETARIA DA SEGURANÇA PÚBLICA
    POLÍCIA MILITAR DO ESTADO DE SÃO PAULO
    [Cidade], [data].
    DESPACHO Nº 2BPMI-[nº]/500/[AA]
  Abertura: —
  Corpo: itens numerados.
  Fechamento: assinatura interna + slogan.

─── PARTE INTERNA ─────────────────────────────────────
[PADRÃO]
  Cabeçalho: idem + PARTE Nº 2BPMI-[nº]/500/[AA]
  Abertura:
    Do [cargo].
    Ao Sr. [destinatário].
    Assunto: [título].
    Referência: [se houver].
    Anexos: [se houver].
  Corpo: parágrafos numerados.
  [PADRÃO] Parágrafo final:
    "Encaminho a Vossa Senhoria para análise e deliberação."
    (ou variante de mesmo sentido)
  Fechamento: assinatura interna + slogan.

─── OS INTERNA (Cmt → CGP ou subordinado) ─────────────
[PADRÃO]
  Cabeçalho: idem + ORDEM DE SERVIÇO Nº 2BPMI-[nº]/500/[AA]
  Abertura: SEM frase em prosa ("Apraz-me..." ou equivalente).
  Corpo:
    1. Considerando:
    1.1. [motivo];
    1.2. [motivo];
    Determino:
    2.1. [ação];
    2.2. [ação];
  Fechamento: assinatura interna — SEM slogan.

─── OFÍCIO EXTERNO ────────────────────────────────────
[PADRÃO]
  Cabeçalho: idem + OFÍCIO Nº 2BPMI-[nº]/500/[AA]
  [SUGESTÃO] Rodapé institucional em expedientes formais:
    Av. Duque de Caxias, 1000, Centro — Guararapes/SP,
    CEP 16700-000 · Tel (18) 3606-1347 ·
    2bpmi5cia@policiamilitar.sp.gov.br ·
    www.policiamilitar.sp.gov.br
  Abertura protocolar — escolher conforme contexto:
    [PADRÃO] Tom de apresentação/proposta:
      "Apraz-me cumprimentá-lo, e na condição de..."
    [PADRÃO] Tom neutro:
      "Cumprimentando cordialmente..."
    [PADRÃO] Tom de resposta a expediente recebido:
      "Acusa-se o recebimento do expediente de referência,
      por meio do qual..."
    [PADRÃO] Tom de atendimento a pedido:
      "Em atenção à solicitação de Vossa Excelência..."
  Corpo: prosa corrida OU sequência de CONSIDERANDO.
  Fechamento: [PADRÃO]
    "...protestos de elevada estima e distinta consideração."
    + assinatura externa + slogan.

─── OFÍCIO COM "CONSIDERANDO" ─────────────────────────
[PADRÃO]
  Mesma estrutura do Ofício Externo; corpo substituído por:
    CONSIDERANDO [motivo constitucional / missão PM];
    CONSIDERANDO [motivo factual + dados do caso];
    CONSIDERANDO [limite da ação policial isolada];
    [demais considerandos pertinentes];
    Venho, respeitosamente, SOLICITAR a Vossa Excelência
    [ação pedida].

─── PARTE DE ELOGIO ───────────────────────────────────
[PADRÃO]
  Cabeçalho: de Parte — PARTE Nº 2BPMI-[nº]/500/[AA].
  Corpo: narrativa cronológica do fato + lista nominal de
    viaturas e policiais envolvidos + proposta explícita de elogio.
  [PADRÃO] Elogio individual vs. coletivo: mesma estrutura —
    inferir pelo expediente recebido.
  Fechamento: assinatura interna + slogan.

─── NOTA DE IMPRENSA ──────────────────────────────────
[PADRÃO]
  SEM cabeçalho PMESP.
  Corpo: parágrafos corridos, linguagem acessível ao público.
  Fechamento: TÍTULO EM MAIÚSCULAS ao final do corpo.
  SEM assinatura.

─── RETIFICAÇÃO DE BOPM ───────────────────────────────
[PADRÃO]
  SEM cabeçalho PMESP.
  Abertura:
    "Considerando que um dos princípios que norteiam a
    Administração Pública é o da Autotutela.
    Considerando que durante triagem do presente Boletim de
    Ocorrência, foram verificadas inconsistências em alguns campos.
    Para fins de direito e compromisso com a verdade, fica
    consignado que:"
  Corpo (repetir por campo):
    a) Na folha [X], no campo "[NOME DO CAMPO]", onde consta:
    "[texto original]"
    Leia-se: "[texto correto]"
  Fechamento: —

─── DESPACHO SEI ──────────────────────────────────────
[PADRÃO]
  SEM cabeçalho PMESP.
  Corpo: texto direto, sem numeração de itens.
  Fechamento: "Guararapes, na data da assinatura digital."
    + assinatura interna.

─── RELATÓRIO DE RONDA — SUPERVISOR REGIONAL ──────────
[PADRÃO] Estrutura de alto nível:
  Cabeçalho:
    POLÍCIA MILITAR
    DO
    ESTADO DE SÃO PAULO
    RELATÓRIO DE RONDA DO OFICIAL SUPERIOR/SUPERVISOR DO CPI-10
    Data: [DD/MM/AAAA] — Turno das [HH:MM] às [HH:MM] horas
  Blocos:
    1. Identificação de viatura (Enc/Mot/Aux + REs + km).
    2. OPM Rondada N — por OPM visitada (inspeção das instalações).
    3. Ronda a Programa de Policiamento N — por viatura verificada.
    4. Documentos Elaborados (tabela Tipo/Nº | Assunto | Destino).
    5. Observações (resumo do turno).
  Cadeia de encaminhamento (tripla — obrigatória):
    Do Oficial Superior/Supervisor do CPI-10. / Ao Sr Ch Div Op /
    Encaminho o presente para conhecimento. / [assinatura] →
    Do Ch Div Op / Ao Sr Ch EM CPI-10 / [assinatura] →
    Do Ch EM CPI-10 / Ao [dest]. / [assinatura]

  [SUGESTÃO] Checklist de conformidade por viatura (8 itens):
    1. CPP está na vtr? 1.1. Atualizado?
    2. Vtr no local conforme CPP?
    3. Tablet (TMD) logado?
    4. CPP, RSO e TMD em conformidade?
    5. Giroflex acionado?
    6. RSO com produtividade anotada?
    7. Treinamento no prazo de 15 dias?
    8. Sabe elaborar BO PM Eletrônico?
  [SUGESTÃO: confirmar estrutura detalhada contra modelo oficial
    do corpus em runtime]

[PADRÃO] Este documento somente é produzido quando o expediente
  for da função de Supervisor Regional do CPI-10 — não é documento
  de expediente ordinário da Cia.

─── PLANO DE CHAMADA ──────────────────────────────────
[PADRÃO]
  A skill NÃO gera Plano de Chamada. Nos documentos cabíveis
  (Parte, OS ou Despacho), determina o ACIONAMENTO do plano —
  nunca o plano em si.

──────────────────────────────────────────────────────
BLOCO 8 — NUMERAÇÃO E CÓDIGOS DE SUBUNIDADE
──────────────────────────────────────────────────────

[PADRÃO]
  2º BPM/I (BTL)              — código 12
  1ª Cia PM                   — código 100
  2ª Cia PM                   — código 200
  3ª Cia PM                   — código 300
  4ª Cia PM                   — código 400
  5ª Cia PM (Guararapes)      — código 500  ← padrão da skill
  Pelotão PM Valparaíso       — código 510
  CFP / P3 BTL                — código 30

[PADRÃO] Regras de numeração:
  • Usar o código da subunidade territorialmente responsável
    pelo assunto.
  • Sup Regional durante ronda: código 500 (OPM de origem do
    signatário), independente da OPM rondada.
  • Numeração sequencial: placeholder [nº] — o Cmt preenche
    antes de assinar.
  • Local padrão: Guararapes. Ajustar se o assunto for de outro
    município.
  [SUGESTÃO] Informar ao usuário para ajustar o local se o
    expediente originar de outro município.
  • Ofício externo do Cmt da Sede:
    OFÍCIO Nº 2BPMI-[nº]/500/[AA]
  • Parte de Elogio:
    PARTE Nº 2BPMI-[nº]/500/[AA]

──────────────────────────────────────────────────────
BLOCO 9 — TRATAMENTOS PROTOCOLARES
──────────────────────────────────────────────────────

[PADRÃO]
  Prefeito/a Municipal:
    Ao/À Excelentíssimo/a Senhor/Senhora [NOME EM MAIÚSCULAS]
    Digníssimo/a Prefeito/a Municipal de [Município]/SP.

  Deputado/a Estadual:
    Ao Excelentíssimo Senhor [NOME]
    Digníssimo Deputado Estadual.

  Promotor/a de Justiça:
    Ao Excelentíssimo Doutor [NOME]
    Dr. Promotor de Justiça de [Município]/SP.

  Juiz de Direito:
    Ao Excelentíssimo Doutor [NOME]
    MM. Juiz de Direito da [Vara] da Comarca de [Município]/SP.

  Secretária/Coordenadora:
    À Ilustríssima Sr.ª [NOME]

  CoordOp BTL (em Parte):
    Ao Sr. CoordOp 2º BPM/I.

  Subcmt BTL (em Parte ou Despacho):
    Ao Sr. Subcmt 2º BPM/I.

  [SUGESTÃO] Para destinatários não listados: Excelentíssimo
    para cargos eletivos e magistratura; Ilustríssimo para
    demais autoridades administrativas.

──────────────────────────────────────────────────────
BLOCO 10 — ENDEREÇOS INSTITUCIONAIS
──────────────────────────────────────────────────────

[PADRÃO]
  5ª Cia PM — Sede (Guararapes):
    Av. Duque de Caxias, 1000, Centro — Guararapes/SP,
    CEP 16700-000
    Tel: (18) 3606-1347
    E-mail: 2bpmi5cia@policiamilitar.sp.gov.br
    Site: www.policiamilitar.sp.gov.br

  Pelotão PM — Valparaíso:
    Av. Nove de Julho, 61, Centro — Valparaíso/SP,
    CEP 16880-000
    Tel: (18) 3401-1859
    SJD: 2bpmi5ciasjd@policiamilitar.sp.gov.br
"""


# ── Validador pós-Gemini (Sprint 8.4-quater) ─────────────────────────────────

def _extrair_paragrafos(texto: str) -> list:
    """Divide o texto em parágrafos (por linha vazia ou bullet)."""
    blocos = re.split(r"\n\s*\n", texto)
    return [b.strip() for b in blocos if b.strip()]


def _extrair_blocos_numerados(resposta: str) -> dict:
    """
    Heurística simples para separar os blocos da resposta.
    Retorna dict com chaves possíveis: '2', '4', '6' (se encontrados).
    """
    blocos = {}
    # Padrões para detectar cabeçalhos de bloco
    marcadores = [
        ("2", re.compile(r"\*\*2\.\s*AN[AÁ]LISE JUR[IÍ]DICA\*\*", re.IGNORECASE)),
        ("4", re.compile(r"\*\*4\.\s*TEXTO PRONTO\*\*", re.IGNORECASE)),
        ("6", re.compile(r"\*\*6\.\s*ASSESSORIA", re.IGNORECASE)),
    ]
    # Qualquer cabeçalho de bloco (para delimitar fim do anterior)
    qualquer_bloco = re.compile(r"\*\*\d+\.\s+[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ]", re.IGNORECASE)

    posicoes = []
    for num, pat in marcadores:
        m = pat.search(resposta)
        if m:
            posicoes.append((m.start(), num))
    posicoes.sort()

    # Encontrar todas as posições de início de qualquer bloco
    todos_inicios = [m.start() for m in qualquer_bloco.finditer(resposta)]

    for i, (pos, num) in enumerate(posicoes):
        # Encontrar próximo início de bloco após este
        fim = len(resposta)
        for inicio_pos in todos_inicios:
            if inicio_pos > pos + 10:  # pular o próprio match
                fim = inicio_pos
                break
        blocos[num] = resposta[pos:fim]

    return blocos


def _paragrafo_tem_expressao_cautelosa(paragrafo: str) -> bool:
    """Verifica se o parágrafo contém expressão cautelosa."""
    p_lower = paragrafo.lower()
    for expr in EXPRESSOES_CAUTELOSAS:
        if expr.lower() in p_lower:
            return True
    return False


def _paragrafo_tem_fundamento_com_fonte(paragrafo: str) -> bool:
    """Verifica se o parágrafo contém [FUNDAMENTO] com [FONTE:] (não FONTE-MODELO)."""
    if "[FUNDAMENTO]" not in paragrafo:
        return False
    if "[FONTE:" not in paragrafo:
        return False
    # Verificar que não é apenas FONTE-MODELO
    fontes = re.findall(r"\[FONTE(?:-MODELO)?:", paragrafo)
    return any(f == "[FONTE:" for f in fontes)


def _montar_resposta_bloqueada(violacoes: list) -> str:
    """Monta resposta substitutiva para violações graves."""
    linhas = ["⚠️ VALIDAÇÃO BLOQUEOU A RESPOSTA DA DESPACHADORA", ""]
    for v in violacoes:
        linhas.append(f"• {v}")
    linhas.append("")
    linhas.append("Orientação: corrija o corpus ou ajuste o prompt para incluir as fontes ")
    linhas.append("normativas necessárias. Termos sem lastro documental devem ser usados ")
    linhas.append("como [SUGESTÃO IA] ou [VERIFICAR], nunca como [FUNDAMENTO].")
    return "\n".join(linhas)


def _montar_alerta(alertas: list, resposta: str) -> str:
    """Prefixa alertas não-bloqueantes no topo da resposta."""
    linhas = ["⚠️ ALERTA DE VALIDAÇÃO: revisar fundamentos destacados antes de assinar.", ""]
    for a in alertas:
        linhas.append(f"• {a}")
    linhas.append("")
    linhas.append("─" * 60)
    linhas.append("")
    linhas.append(resposta)
    return "\n".join(linhas)


def validar_saida_despachadora(
    resposta: str,
    contexto_normativo: str,
    modelos_redacao: str,
) -> tuple:
    """
    Valida a saída do Gemini antes de entregar ao usuário.
    Sprint 8.4-quater — Validador pós-resposta com níveis de fonte.

    Args:
        resposta: texto completo da resposta do Gemini
        contexto_normativo: texto concatenado dos chunks normativos recuperados
        modelos_redacao: texto concatenado dos modelos de redação recuperados

    Returns:
        (bloqueada, violacoes_graves, alertas)
        - bloqueada: True se a resposta deve ser substituída
        - violacoes_graves: lista de strings com regras violadas (bloqueantes)
        - alertas: lista de strings com avisos (não-bloqueantes)
    """
    violacoes = []
    alertas = []
    resp_lower = resposta.lower()
    ctx_norm_lower = contexto_normativo.lower()
    paragrafos = _extrair_paragrafos(resposta)

    # ── Regra A: Termos proibidos absolutos ──
    for termo in TERMOS_PROIBIDOS_ABSOLUTOS:
        if termo.lower() in resp_lower:
            violacoes.append(
                f"[Regra A] Termo proibido absoluto encontrado na resposta: "
                f'"{termo}". Referências internas do prompt nunca devem aparecer na saída.'
            )

    # ── Regra B: [FUNDAMENTO] exige [FONTE:] normativa ──
    for para in paragrafos:
        if "[FUNDAMENTO]" in para:
            if "[FONTE:" not in para:
                trecho = para[:120].replace("\n", " ")
                violacoes.append(
                    f"[Regra B] [FUNDAMENTO] sem [FONTE:] encontrado: "
                    f'"{trecho}..."'
                )
            elif "[FONTE-MODELO:" in para:
                # Verificar se a ÚNICA fonte é FONTE-MODELO
                fontes_normativas = re.findall(r"\[FONTE:(?!MODELO)", para)
                if not fontes_normativas:
                    trecho = para[:120].replace("\n", " ")
                    violacoes.append(
                        f"[Regra B] [FUNDAMENTO] sustentado apenas por [FONTE-MODELO:]: "
                        f'"{trecho}..."'
                    )

    # ── Regra C: [FONTE-MODELO:] não pode sustentar afirmações jurídicas ──
    for para in paragrafos:
        if "[FONTE-MODELO:" in para:
            para_lower = para.lower()
            for termo_jur in TERMOS_JURIDICOS_PADRAO_PROIBIDOS:
                if termo_jur.lower() in para_lower:
                    # Verificar se é apenas forma administrativa
                    tem_conclusao = any(
                        cf.lower() in para_lower for cf in TERMOS_CONCLUSAO_FORTE
                    )
                    if tem_conclusao:
                        trecho = para[:120].replace("\n", " ")
                        violacoes.append(
                            f"[Regra C] [FONTE-MODELO:] sustentando afirmação jurídica "
                            f'sobre "{termo_jur}": "{trecho}..."'
                        )
                    else:
                        trecho = para[:120].replace("\n", " ")
                        alertas.append(
                            f"[Regra C] [FONTE-MODELO:] em parágrafo com termo jurídico "
                            f'"{termo_jur}": "{trecho}..." — verificar se é apenas forma.'
                        )
                    break  # Um alerta/violação por parágrafo basta

    # ── Regra D: Termos jurídicos sensíveis — rebaixamento ──
    for para in paragrafos:
        para_lower = para.lower()
        for termo in TERMOS_JURIDICOS_SENSIVEIS:
            if termo.lower() in para_lower:
                # Caso 1: Lastreado — [FUNDAMENTO] + [FONTE:] + presente no contexto
                if (_paragrafo_tem_fundamento_com_fonte(para)
                        and termo.lower() in ctx_norm_lower):
                    continue  # Permitido

                # Caso 2: Cauteloso — com expressão de cautela
                if _paragrafo_tem_expressao_cautelosa(para):
                    alertas.append(
                        f"[Regra D] Termo sensível \"{termo}\" usado com cautela — "
                        f"verificar antes de assinar."
                    )
                    continue  # Permitido com alerta

                # Caso 3: Conclusivo — afirmação categórica sem marcadores
                trecho = para[:120].replace("\n", " ")
                violacoes.append(
                    f"[Regra D] Termo sensível \"{termo}\" como conclusão definitiva "
                    f"sem fonte documental: \"{trecho}...\" — "
                    f"Use como [SUGESTÃO IA] ou [VERIFICAR], ou inclua fonte normativa."
                )
                break  # Um bloqueio por parágrafo basta

    # ── Regra E: [PADRÃO] não pode mascarar fundamento jurídico ──
    for para in paragrafos:
        if "[PADRÃO]" in para:
            para_lower = para.lower()
            for termo_jur in TERMOS_JURIDICOS_PADRAO_PROIBIDOS:
                if termo_jur.lower() in para_lower:
                    tem_conclusao = any(
                        cf.lower() in para_lower for cf in TERMOS_CONCLUSAO_FORTE
                    )
                    if tem_conclusao:
                        trecho = para[:120].replace("\n", " ")
                        violacoes.append(
                            f"[Regra E] [PADRÃO] mascarando fundamento jurídico "
                            f'sobre "{termo_jur}": "{trecho}..."'
                        )
                    else:
                        trecho = para[:120].replace("\n", " ")
                        alertas.append(
                            f"[Regra E] [PADRÃO] em parágrafo com termo jurídico "
                            f'"{termo_jur}": "{trecho}..." — verificar se é apenas forma.'
                        )
                    break  # Um alerta/violação por parágrafo basta

    # ── Regra F: [VERIFICAR] seguido de conclusão forte ──
    for para in paragrafos:
        if "[VERIFICAR" in para:
            para_lower = para.lower()
            for expr_forte in TERMOS_CONCLUSAO_FORTE:
                if expr_forte.lower() in para_lower:
                    trecho = para[:150].replace("\n", " ")
                    violacoes.append(
                        f"[Regra F] [VERIFICAR] seguido de conclusão forte "
                        f'"{expr_forte}": "{trecho}..."'
                    )
                    break  # Um bloqueio por parágrafo basta

    # ── Regra G: Fundamento novo no Texto Pronto ou Assessoria ──
    blocos = _extrair_blocos_numerados(resposta)
    bloco2 = blocos.get("2", "")
    bloco4 = blocos.get("4", "")
    bloco6 = blocos.get("6", "")

    if bloco2 and (bloco4 or bloco6):
        bloco2_lower = bloco2.lower()
        for bloco_num, bloco_txt in [("4", bloco4), ("6", bloco6)]:
            if not bloco_txt:
                continue
            for termo in TERMOS_JURIDICOS_SENSIVEIS:
                t_lower = termo.lower()
                if t_lower in bloco_txt.lower() and t_lower not in bloco2_lower:
                    # Termo novo apareceu no bloco 4 ou 6 sem estar no bloco 2
                    # Verificar se está como sugestão/verificar
                    para_com_termo = [
                        p for p in _extrair_paragrafos(bloco_txt)
                        if t_lower in p.lower()
                    ]
                    for p in para_com_termo:
                        if _paragrafo_tem_expressao_cautelosa(p):
                            alertas.append(
                                f"[Regra G] Termo \"{termo}\" no Bloco {bloco_num} "
                                f"(não no Bloco 2) — presente como sugestão/verificação."
                            )
                        else:
                            trecho = p[:120].replace("\n", " ")
                            violacoes.append(
                                f"[Regra G] Fundamento novo no Bloco {bloco_num}: "
                                f'"{termo}" como conclusão definitiva, sem ter '
                                f'aparecido como [FUNDAMENTO]+[FONTE:] no Bloco 2: '
                                f'"{trecho}..."'
                            )

    bloqueada = len(violacoes) > 0
    return bloqueada, violacoes, alertas


def _aplicar_validacao(resposta: str, pool_f: list, pool_m: list, keywords: set) -> str:
    """
    Aplica o validador pós-Gemini à resposta.
    Constrói contexto_normativo e modelos_redacao a partir dos pools.
    Retorna a resposta validada (bloqueada ou com alertas).
    """
    ctx_normativo = "\n".join(
        _extract_window(e.get("texto") or "", keywords)
        for e in pool_f
    )
    ctx_modelos = "\n".join(
        _extract_window(e.get("texto") or "", keywords)
        for e in pool_m
    )

    bloqueada, violacoes, alertas = validar_saida_despachadora(
        resposta, ctx_normativo, ctx_modelos
    )

    if bloqueada:
        return _montar_resposta_bloqueada(violacoes)
    elif alertas:
        return _montar_alerta(alertas, resposta)
    return resposta


# ── Funções de recuperação ────────────────────────────────────────────────────

def extract_keywords(text: str) -> set:
    """Tokens minúsculos, sem pontuação, len > 3, sem stopwords PT."""
    tokens = re.sub(r"[^\w\s]", " ", text.lower()).split()
    return {t for t in tokens if len(t) > 3 and t not in STOPWORDS_PT}


def score_entry(entry: dict, keywords: set) -> float:
    """
    score = (ocorrências das keywords em texto.lower()) / (len(texto) ** 0.5)
    Normalização por tamanho evita viés de arquivos gigantes (ex.: Notebooklm).
    """
    if entry.get("error") is not None:
        return 0.0
    texto = entry.get("texto") or ""
    if len(texto) < MIN_TEXTO_CHARS:
        return 0.0
    if not keywords:
        return 0.0
    texto_lower = texto.lower()
    count = sum(texto_lower.count(kw) for kw in keywords)
    if count == 0:
        return 0.0
    
    score = count / (len(texto) ** 0.5)
    
    # Tarefa 5 — Controle moderado de PDFs compilados / Notebooklm
    if entry.get("section") == "Notebooklm":
        score *= 0.7
        
    # --- DOMAIN BOOST (Sprint 8.5-d.1) ---
    if "acidente" in keywords and "viatura" in keywords:
        fn_lower = (entry.get("arquivo") or "").lower()
        if any(x in fn_lower for x in ["acidente_viatura_providencias", "processo-3.01.00", "acidente de trânsito vtr", "ni_002_02_17"]):
            score += 3.5
        
    return score


def source_key(entry: dict) -> str:
    section = entry.get("section", "")
    arquivo = entry.get("arquivo", "")
    return f"{section}/{arquivo}" if section else arquivo


def recover_chunks(corpus: list, keywords: set, query_text: str = "") -> list:
    """
    Retorna lista de dicts enriquecidos com 'score' e 'source_key'.
    Dois pools separados estritamente por natureza:
      - FUNDAMENTO (pool_f): apenas NORMA, PROCEDIMENTAL, DOUTRINA, JURISPRUDENCIA.
      - MODELO (pool_m): apenas MODELO_DE_REDACAO, MODELO_PRECEDENTE, PRECEDENTE (excluindo Notebooklm).
    Passo 1: Pontuação base + Busca Literal Complementar de termos fortes da query.
    Passo 2: Pistas normativas extraídas de modelos validados para reforçar normas do corpus (boost flat).
    """
    # ── Passo 1: Busca literal complementar da query ──
    literal_targets = []
    if query_text:
        query_lower = query_text.lower()
        # Captura Súmulas (accent-insensitive)
        sumulas = re.findall(r"(s[uú]mula vinculante\s*(?:n[oºªª]\.?\s*)?\d+|s[uú]mula\s*\d+)", query_lower)
        # Captura Artigos
        artigos = re.findall(r"(art\.\s*\d+|artigo\s*\d+|art\s*\d+)", query_lower)
        # Captura Normas/POPs específicas
        normas = re.findall(r"(i-\d+-pm|rdpm|pop\s*\d+[\.\d+]*)", query_lower)
        # Termos fortes adicionais
        key_terms = []
        for term in ["autotutela", "nulidade", "sindicância", "algemas", "receio de fuga", "justificativa por escrito"]:
            if term in query_lower:
                key_terms.append(term)
        literal_targets = sumulas + artigos + normas + key_terms

    scored = []
    for entry in corpus:
        s = score_entry(entry, keywords)
        
        # Boost por correspondência literal com termos da query (cumulativo por termo distinto)
        boost = 0.0
        if literal_targets:
            entry_text_lower = (entry.get("texto") or "").lower()
            for target in set(literal_targets):  # evita double-boosting para termos duplicados
                pattern = re.escape(target).replace(r'\ ', r'\s*')
                if re.search(pattern, entry_text_lower):
                    boost += 5.0  # Boost para promover termos literais fortes
        
        total_score = s + boost
        if total_score > 0:
            scored.append({**entry, "_score": total_score, "_key": source_key(entry)})

    # ── Passo 2: Extração de pistas dos modelos ──
    # Primeiro isolamos os modelos para identificar quais estão no topo do ranking
    models_scored = [
        e for e in scored
        if e.get("natureza") in ("MODELO_DE_REDACAO", "MODELO_PRECEDENTE", "PRECEDENTE")
        and e.get("section", "") != "Notebooklm"
    ]
    top_models = sorted(models_scored, key=lambda x: x["_score"], reverse=True)[:POOL_MODELO_N]

    model_pistas = []
    for model in top_models:
        model_text = (model.get("texto") or "").lower()
        m_sumulas = re.findall(r"(s[uú]mula vinculante\s*(?:n[oºªª]\.?\s*)?\d+|s[uú]mula\s*\d+)", model_text)
        m_artigos = re.findall(r"(art\.\s*\d+|artigo\s*\d+|art\s*\d+)", model_text)
        m_normas = re.findall(r"(i-\d+-pm|rdpm|pop\s*\d+[\.\d+]*)", model_text)
        model_pistas.extend(m_sumulas + m_artigos + m_normas)
    
    # Dedup pistas
    model_pistas = list(set(model_pistas))

    # Boost das pistas dos modelos nas normas do corpus (boost FLAT fixo para evitar runaway scores em arquivos gigantes)
    if model_pistas:
        for entry in scored:
            if entry.get("natureza") in ("NORMA", "PROCEDIMENTAL", "DOUTRINA", "JURISPRUDENCIA"):
                entry_text_lower = (entry.get("texto") or "").lower()
                matched_any = False
                for pista in model_pistas:
                    pattern = re.escape(pista).replace(r'\ ', r'\s*')
                    if re.search(pattern, entry_text_lower):
                        matched_any = True
                        break
                if matched_any:
                    entry["_score"] += 3.0  # Boost flat fixo de 3.0 se contiver alguma pista das recolhidas dos modelos

    # ── Passo 3: Partição estrita dos pools ──
    # Pool Normativo
    norms_scored = [
        e for e in scored
        if e.get("natureza") in ("NORMA", "PROCEDIMENTAL", "DOUTRINA", "JURISPRUDENCIA")
    ]
    pool_f = sorted(norms_scored, key=lambda x: x["_score"], reverse=True)[:POOL_FUNDAMENTO_N]

    # Pool de Modelos (re-avaliado com scores finais)
    models_scored = [
        e for e in scored
        if e.get("natureza") in ("MODELO_DE_REDACAO", "MODELO_PRECEDENTE", "PRECEDENTE")
        and e.get("section", "") != "Notebooklm"
    ]
    pool_m = sorted(models_scored, key=lambda x: x["_score"], reverse=True)[:POOL_MODELO_N]

    # União dedup por chave
    seen = set()
    merged = []
    for entry in pool_f + pool_m:
        k = entry["_key"]
        if k not in seen:
            seen.add(k)
            merged.append(entry)

    return merged, pool_f, pool_m


def _extract_window(texto: str, keywords: set, window: int = CHUNK_MAX_CHARS) -> str:
    if not texto:
        return ""
    texto_lower = texto.lower()
    pivot = len(texto)
    for kw in keywords:
        pos = texto_lower.find(kw)
        if pos != -1 and pos < pivot:
            pivot = pos
    if pivot == len(texto):
        return texto[:window]
    start = max(0, pivot - window // 2)
    end = min(len(texto), start + window)
    return texto[start:end]


def build_user_prompt(
    input_texts: list,
    pool_f: list,
    pool_m: list,
    empty_recovery: bool,
    keywords: set,
) -> str:
    parts = []

    parts.append("EXPEDIENTE(S) RECEBIDO(S):")
    for fname, text, error in input_texts:
        parts.append(f"\n--- Arquivo: {fname} ---")
        if error:
            parts.append(f"[Aviso: extração retornou erro '{error}'. "
                         f"Texto possivelmente incompleto.]")
        parts.append(text if text.strip() else "[Texto não extraído]")

    if pool_f:
        parts.append("\n\nCONTEXTO NORMATIVO (corpus 5ª Cia):")
        for entry in pool_f:
            fonte = entry["_key"]
            texto = _extract_window(entry.get("texto") or "", keywords)
            parts.append(f"\n[FONTE: {fonte}]\n{texto}")

    f_keys = {e["_key"] for e in pool_f}
    modelos = [e for e in pool_m if e["_key"] not in f_keys]
    if modelos:
        parts.append("\n\nMODELOS DE REDAÇÃO (para forma, não para fundamento):")
        for entry in modelos:
            fonte = entry["_key"]
            texto = _extract_window(entry.get("texto") or "", keywords)
            parts.append(f"\n[FONTE: {fonte}]\n{texto}")

    if empty_recovery:
        parts.append(
            "\n\nNota: o recuperador de contexto não encontrou trechos "
            "relevantes no corpus para este expediente. "
            "Produza os 6 blocos normalmente, marcando qualquer afirmação "
            "de fundamento normativo como [VERIFICAR: confirmar a norma "
            "antes de assinar] e encaminhando todas as dúvidas de "
            "fundamentação ao Bloco 5 — Levantamentos."
        )
    else:
        parts.append(
            "\n\nProcesse o expediente acima e produza os 6 blocos "
            "na ordem fixa definida no system prompt."
        )

    return "\n".join(parts)


def extract_inputs(file_paths: list) -> list:
    """
    Extrai texto dos arquivos de entrada usando os mesmos extratores
    de indexar_corpus.py.
    Retorna lista de (filename, texto, error).
    .doc e .rtf são processados em batch COM (instância única do Word).
    """
    results = []
    doc_paths = []
    doc_indices = {}

    for fp in file_paths:
        ext = fp.suffix.lower()
        if ext in (".doc", ".rtf"):
            idx = len(results)
            results.append((fp.name, "", None))
            doc_paths.append(fp)
            doc_indices[str(fp.resolve())] = idx
        else:
            texto, error = extract_generic(fp)
            results.append((fp.name, texto, error))

    if doc_paths:
        print(f"Abrindo Word.Application para {len(doc_paths)} arquivo(s) .doc/.rtf ...",
              flush=True)
        doc_results = batch_extract_doc(doc_paths)
        print("Word.Application encerrado.", flush=True)
        for abs_str, (texto, error) in doc_results.items():
            idx = doc_indices.get(abs_str)
            if idx is not None:
                fname = results[idx][0]
                results[idx] = (fname, texto, error)

    return results


# ── Retry Gemini ─────────────────────────────────────────────────────────────

_RETRY_WAITS = [5, 15, 30]  # segundos entre tentativas 1→2, 2→3, e falha final
_RETRY_KEYWORDS = ("503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED")


def _chamar_gemini(client, model: str, contents: str, system_instruction: str, log_fn):
    """
    Chama client.models.generate_content com retry automático em 503/429.
    log_fn recebe a string de aviso (ctx.log.warning ou print conforme o caller).
    """
    import time
    from google.genai import types as genai_types

    tentativas = len(_RETRY_WAITS) + 1  # 3 esperas = 4 tentativas no máximo
    for n in range(1, tentativas + 1):
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=genai_types.GenerateContentConfig(
                    system_instruction=system_instruction,
                ),
            )
        except Exception as e:
            msg = str(e)
            retryable = any(kw in msg for kw in _RETRY_KEYWORDS)
            if not retryable or n > len(_RETRY_WAITS):
                raise
            espera = _RETRY_WAITS[n - 1]
            log_fn(f"Gemini indisponível (tentativa {n}/{len(_RETRY_WAITS) + 1}), aguardando {espera}s... [{msg[:80]}]")
            time.sleep(espera)


# ── Ponto de entrada para o painel (Sprint 7.2+) ─────────────────────────────

def processar(ctx) -> str:
    """
    Executa a Despachadora e retorna os 6 blocos como string.

    ctx.entrada_arquivo : Path | None  — arquivo do expediente
    ctx.entrada_texto   : str  | None  — expediente colado como texto
    (pelo menos um deve estar preenchido)
    """
    api_key = ctx.segredos.get("gemini")["api_key"]

    if not CORPUS_FILE.exists():
        raise FileNotFoundError(
            f"corpus_index.json não encontrado em: {CORPUS_FILE}\n"
            "Execute primeiro: python nucleo_despachadora/indexar_corpus.py"
        )

    try:
        corpus = json.loads(CORPUS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Falha ao ler corpus_index.json: {e}") from e

    corpus = [
        e for e in corpus
        if e.get("error") is None and len(e.get("texto") or "") >= MIN_TEXTO_CHARS
    ]
    ctx.log.info(f"Corpus carregado: {len(corpus)} entradas válidas.")

    if ctx.entrada_arquivo is not None:
        ctx.log.info("Extraindo expediente do arquivo...")
        input_texts = extract_inputs([Path(ctx.entrada_arquivo)])
        for fname, texto, error in input_texts:
            status = f"OK ({len(texto):,} chars)" if not error else f"ERRO: {error}"
            ctx.log.info(f"  {fname}: {status}")
    elif ctx.entrada_texto is not None:
        input_texts = [("entrada_texto", ctx.entrada_texto, None)]
        ctx.log.info(f"Expediente via texto: {len(ctx.entrada_texto):,} chars.")
    else:
        raise ValueError("Despachadora: nenhuma entrada fornecida (arquivo ou texto).")

    total_input_chars = sum(len(t) for _, t, _ in input_texts)
    if total_input_chars == 0:
        raise ValueError("Nenhum texto extraído dos arquivos de entrada.")

    all_input_text = " ".join(t for _, t, _ in input_texts)
    keywords = extract_keywords(all_input_text)
    ctx.log.info(f"Palavras-chave extraídas: {len(keywords)}")

    merged, pool_f, pool_m = recover_chunks(corpus, keywords, all_input_text)
    empty_recovery = len(merged) == 0

    if empty_recovery:
        ctx.log.warning("Nenhum chunk com score > 0 recuperado. Prosseguindo sem contexto.")
    else:
        f_keys = {e["_key"] for e in pool_f}
        excl_m = [e for e in pool_m if e["_key"] not in f_keys]
        ctx.log.info(f"Chunks: {len(pool_f)} fundamento + {len(excl_m)} modelo exclusivo.")

    user_prompt = build_user_prompt(input_texts, pool_f, pool_m, empty_recovery, keywords)

    from google import genai

    client = genai.Client(api_key=api_key)
    ctx.log.info(f"Chamando {MODELO_GEMINI}...")

    resp = _chamar_gemini(client, MODELO_GEMINI, user_prompt, MASTER_SYSTEM_PROMPT, ctx.log.warning)

    # Sprint 8.4-quater: Validação pós-Gemini
    resultado = _aplicar_validacao(resp.text, pool_f, pool_m, keywords)
    return resultado


# ── CLI (uso standalone — mantido para testes sem painel) ────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Despachadora do Comandante — 5ª Cia PM / 2º BPM/I"
    )
    parser.add_argument(
        "arquivos", nargs="+",
        help="Arquivo(s) de expediente a processar (PDF, DOCX, DOC, XLSX, TXT…)"
    )
    parser.add_argument(
        "--output", metavar="ARQUIVO",
        help="Salvar resposta também em arquivo de texto (UTF-8)"
    )
    args = parser.parse_args()

    file_paths = []
    for raw in args.arquivos:
        fp = Path(raw)
        if not fp.exists():
            print(f"[Erro] Arquivo não encontrado: {raw}")
            sys.exit(1)
        file_paths.append(fp)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[Erro] Variável de ambiente GEMINI_API_KEY não definida.")
        print("Como definir:")
        print("  PowerShell : $env:GEMINI_API_KEY='sua_chave_aqui'")
        print("  CMD        : set GEMINI_API_KEY=sua_chave_aqui")
        sys.exit(1)

    if not CORPUS_FILE.exists():
        print(f"[Erro] corpus_index.json não encontrado em: {CORPUS_FILE}")
        print("Execute primeiro: python indexar_corpus.py")
        sys.exit(1)

    try:
        corpus = json.loads(CORPUS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[Erro] Falha ao ler corpus_index.json: {e}")
        sys.exit(1)

    corpus = [
        e for e in corpus
        if e.get("error") is None and len(e.get("texto") or "") >= MIN_TEXTO_CHARS
    ]
    print(f"Corpus carregado: {len(corpus)} entradas válidas.", flush=True)

    print("Extraindo expediente(s) ...", flush=True)
    input_texts = extract_inputs(file_paths)

    for fname, texto, error in input_texts:
        status = f"OK ({len(texto):,} chars)" if not error else f"ERRO: {error}"
        print(f"  {fname}: {status}", flush=True)

    total_input_chars = sum(len(t) for _, t, _ in input_texts)
    if total_input_chars == 0:
        print("[Erro] Nenhum texto extraído dos arquivos de entrada. Abortando.")
        sys.exit(1)

    all_input_text = " ".join(t for _, t, _ in input_texts)
    keywords = extract_keywords(all_input_text)
    print(f"Palavras-chave extraídas: {len(keywords)}", flush=True)

    merged, pool_f, pool_m = recover_chunks(corpus, keywords, all_input_text)
    empty_recovery = len(merged) == 0

    if empty_recovery:
        print("Aviso: nenhum chunk com score > 0 recuperado. "
              "Prosseguindo sem contexto.", flush=True)
    else:
        f_keys = {e["_key"] for e in pool_f}
        excl_m = [e for e in pool_m if e["_key"] not in f_keys]
        print(f"Chunks recuperados: {len(pool_f)} fundamento + "
              f"{len(excl_m)} modelo exclusivo.", flush=True)

    user_prompt = build_user_prompt(input_texts, pool_f, pool_m, empty_recovery, keywords)

    try:
        from google import genai
    except ImportError:
        print("[Erro] Biblioteca google-genai não instalada.")
        print("Instale com: pip install google-genai")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"Chamando {MODELO_GEMINI} ...", flush=True)
    try:
        resp = _chamar_gemini(client, MODELO_GEMINI, user_prompt, MASTER_SYSTEM_PROMPT, print)
    except Exception as e:
        print(f"[Erro] Falha na chamada à API Gemini: {e}")
        sys.exit(1)

    resultado = resp.text

    # Sprint 8.4-quater: Validação pós-Gemini
    resultado = _aplicar_validacao(resultado, pool_f, pool_m, keywords)

    separator = "═" * 62
    print(f"\n{separator}")
    print("RESPOSTA DA DESPACHADORA")
    print(separator)
    print(resultado)
    print(separator)

    if args.output:
        out_path = Path(args.output)
        try:
            out_path.write_text(resultado, encoding="utf-8")
            print(f"\nResposta salva em: {out_path.resolve()}")
        except Exception as e:
            print(f"[Aviso] Não foi possível salvar em {args.output}: {e}")


if __name__ == "__main__":
    main()
