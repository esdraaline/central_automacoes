# 🛣️ Roadmap
Como ler: as fases são o mapa geral. Cada fase é quebrada em sprints com tarefas concretas — mas só detalhamos os sprints da fase quando chegamos nela (planejar os 6 em detalhe agora seria perder tempo que é pra construir). Marque [x] ao concluir. O "onde estou agora" fica no STATUS.md.

---

## ✅ Concluído antes das fases
- [x] Scaffold da central criado e salvo em `Projetos\central_automacoes`
- [x] Código do BOPM migrado para `automacoes/baixar_bopm/`
- [x] Decisões A/B/C registradas (DECISOES.md)

---

## Fase 0 — Fundação ✅

### Sprint 1 — Núcleo + segredos ✅
- [x] Criar `nucleo/segredos.py` (lê de `segredos.env`, interface `get("siopm")`)
- [x] Criar `segredos.env` a partir do `.exemplo` e preencher
- [x] Mover as senhas do `config.py` antigo para o `segredos.env`
- [x] Refatorar `vpn_manager.py` → `nucleo/vpn.py`
- [x] Refatorar parte de browser do `siopm_navigator.py` → `nucleo/browser.py`
- [x] Refatorar `logger_setup.py` → `nucleo/log.py`
- [x] Testar: BOPM ainda baixa rodando pelo código refatorado (linha de comando)

### Sprint 2 — Contrato + painel ✅
- [x] Definir o contrato `manifesto.py` + `executar.py`
- [x] Adaptar `baixar_bopm/` ao contrato (manifesto + executar chamando o núcleo)
- [x] Criar `painel.py` (customtkinter): descobre automações, 1 botão, log ao vivo
- [x] Testar: clicar no botão "Baixar BOPMs" e baixar pela interface
- [x] Atualizar STATUS.md e marcar a Fase 0 como concluída

---

## Fase 1 — Logins simples ✅

### Sprint 1 — Logins: Mapa Força · Dejem ✅
- [x] Criar `nucleo/login_mapa_forca.py` reutilizando credenciais SIOPM e abrindo COMP MAPA FORÇA
- [x] Criar `nucleo/login_dejem.py` com credenciais do Portal MS
- [x] Criar `automacoes/abrir_mapa_forca/` para uso real, mantendo Edge aberto
- [x] Criar `automacoes/abrir_dejem/` para uso real, mantendo Edge aberto
- [x] Adicionar chaves Dejem em `segredos.env` e `segredos.env.exemplo`
- [x] Criar `automacoes/teste_logins/` como diagnóstico (`manifesto.py` + `executar.py`)
- [x] Confirmar descoberta pelo contrato sem alterar `painel.py`
- [x] Validar pelo painel em ambiente com customtkinter, VPN e Edge

**Itens da fase:**
- [x] 6 · Login Mapa Força 5ª Cia (SIOPM Web)
- [x] 7 · Login página Dejem/Delegada

---

## Fase 2 — Validar BOPM (1.1)

**Objetivo:** validar os BOPMs pendentes no SIOPM Web (Enviar para Providências Complementares → Outros → Confirmar).

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 2.1 | Criar `automacoes/validar_bopm/` com contrato `manifesto.py` + `executar.py`. Fluxo: login SIOPM → filtro → detecta pendentes → abre cada BOPM → seleciona "Outros" → clica "Validar BOPM" → clica "Confirmar". | Botão "Validar BOPM" aparece no painel; executa com log ao vivo; seletores mapeados na primeira execução real. |
| 2.2 | Saída: relatório em `saidas/validacao_bopm_<data>.txt` com resultado por BOPM. | Arquivo gerado corretamente; log ao vivo durante execução. ✅ 16/06/2026 |

**Itens da fase:**
- [x] 1.1 · Validar BOPMs pendentes no SIOPM Web (Sprint 2.1 ✅ validado em campo 06/06/2026)
- [x] Sprint 2.2 ✅ validado em campo 16/06/2026 — relatório gerado corretamente, log ao vivo OK. Fase 2 encerrada.

---

## Fase 3 — Órion

**Objetivo:** consultar indicadores criminais no sistema Órion (só leitura, sem ação).

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 3.1 | Login no Órion via Playwright (Edge, não-headless). Credenciais via `nucleo/segredos`. | Login bem-sucedido; sessão disponível para os próximos sprints. |
| 3.2 | Consulta por município/período; extração dos indicadores da página. | Dados extraídos corretamente para pelo menos 1 município de teste. |
| 3.3 | Saída em `saidas/orion_<municipio>_<data>.txt`. Log ao vivo. | Arquivo gerado; painel não trava durante extração. |

**Itens da fase:**
- [ ] 2 · Consultar indicadores criminais (somente leitura)

---

## Fase 4 — Relatório de e-mails (só leitura)

**Objetivo:** ler e-mails não-lidos das 4 contas Gmail + 1 Hotmail + correio PM, gerar relatório.

Contas: josemardp@gmail.com · josemar.dp@hotmail.com · esdraaline@gmail.com · lojadares@gmail.com · correio PM (por navegador).

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 4.1 | Configurar OAuth Gmail API para as 3 contas Google. Armazenar tokens em `segredos/` (fora do git). | Autenticação funciona nas 3 contas sem erro. |
| 4.2 | Leitura de não-lidos das 3 contas Gmail; saída estruturada por conta. | Relatório em `saidas/emails_<data>.txt` com remetente, assunto, data, trecho. |
| 4.3 | Leitura Hotmail via Microsoft Graph API. | Mesma estrutura do relatório, incluindo conta Hotmail. |
| 4.4 | Correio PM por Playwright (atrás da VPN). Só leitura. | Não-lidos do correio PM incluídos no relatório; painel não trava. |

**Itens da fase:**
- [ ] 4 · Gmail: relatório de não lidos (4 contas via API)
- [ ] 3 · Correio PM: relatório de não lidos (navegador)

---

## Fase 5 — Triagem/exclusão de e-mails ⚠ (ver D-02)

**Objetivo:** após relatório (Fase 4), permitir exclusão com confirmação explícita do usuário.

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 5.1 | UI de triagem: listar e-mails do relatório mais recente; checkbox por item. | Lista renderizada corretamente; nenhuma ação é tomada sem confirmação. |
| 5.2 | Mover para Lixeira (não exclusão permanente) após confirmação explícita. Nunca esvaziar lixeira. | E-mail movido para Lixeira na conta correta; log registra a ação. |

**Itens da fase:**
- [ ] 4.1 · Triagem + confirmação + lixeira (Gmail)
- [ ] 3.1 · Triagem + confirmação + lixeira (Correio PM)

---

## Fase 6 — Assinatura de PDF ⚠ (ver D-04)

**Objetivo:** assinar PDFs localmente com certificado e-CPF/Adobe, PIN digitado na hora, por documento.

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 6.1 | Confirmar formato do certificado local (A1 .pfx / A3 em token / ID digital do Adobe). Integrar `pyhanko`. Abrir diálogo de seleção de arquivo PDF. | PDF selecionado carregado corretamente. |
| 6.2 | Solicitar PIN ao usuário na hora; assinar; salvar em `saidas/`. | PDF assinado gerado; assinatura válida verificável no Adobe Reader. |
| 6.3 | Validar que gov.br não é automatizado (máximo: preparar PDF e abrir assinador para o humano). | Nenhum fluxo automatizado de gov.br na Central. |

**Itens da fase:**
- [ ] Confirmar formato do certificado local
- [ ] 8 · Botão "assinar" com certificado local (PIN na hora, por documento)

---

## Fase 7 — Despachadora do Comandante

**Objetivo:** portar a skill standalone de redação assistida para dentro do painel como automação plugável de categoria `"Redação"` (sem VPN/browser). **Independente das Fases 2–6 — pode ser priorizada e executada em paralelo.**

A Despachadora recebe um expediente (parte, ofício, despacho, denúncia, BO, laudo — arquivo ou texto colado), busca contexto num corpus indexado da 5ª Cia e devolve 6 blocos fixos: Classificação, Análise Jurídica, Decisão, Texto Pronto (padrão I-7-PM), Levantamentos, Assessoria do Estado-Maior.

**Estrutura alvo (`automacoes/despachadora/`):**
```
automacoes/despachadora/
├── manifesto.py              # precisa_vpn=False, destrutivo=False, categoria="Redação"
├── executar.py               # run(ctx) — chama o núcleo; lê CORPUS_PATH de ctx.segredos
├── corpus_index.json         # versionado no git (~34 MB); gerado pelo indexar_corpus
└── nucleo_despachadora/
    ├── despachadora.py       # MOVIDO do Drive — vira função chamável (main() → def processar())
    └── indexar_corpus.py     # MOVIDO do Drive — mantido junto para reindexações
```

**Restrições técnicas a investigar no Sprint 7.1 (não bloqueiam hoje):**

| Ponto | Detalhe | Impacto |
|---|---|---|
| Input de arquivo no painel | `_on_run` passa apenas `ctx` sem argumento de arquivo. Extensão necessária. | ⚠ investigar no Sprint 7.1 |
| Exibição de saída longa | `_run_thread` exibe resultado como string curta hardcoded. Os 6 blocos precisam de mecanismo próprio. | ⚠ investigar no Sprint 7.1 |
| `SKILL_ROOT` hardcoded | `indexar_corpus.py` linha 38: `Path("G:/Meu Drive/...")`. Ao portar, ler `CORPUS_PATH` de `segredos.env`. | Adaptação mínima |
| `CORPUS_FILE` relativo ao script | `despachadora.py`: `CORPUS_FILE = SCRIPT_DIR / "corpus_index.json"`. Ao mover para `nucleo_despachadora/`, apontar um nível acima. | Adaptação mínima |
| `.gitignore` e corpus | Quando `automacoes/despachadora/` existir, garantir que P1–P5, JD, Notebooklm não entrem por acidente. | Corrigir antes do Sprint 7.2 |

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 7.1 | **Investigação:** Claude Code lê a Central e propõe plano de port (input de arquivo, exibição de saída longa, adaptações mínimas). **Nenhum código escrito.** | Plano aprovado por Josemar com mapeamento das restrições técnicas acima. ✅ 07/06/2026 |
| 7.2 | Port do núcleo: mover `despachadora.py` e `indexar_corpus.py` para `nucleo_despachadora/`. Adaptar `main()` → função chamável. Corrigir `SKILL_ROOT` e `CORPUS_FILE`. Atualizar `.gitignore`. Versionar `corpus_index.json`. | `run(ctx)` executa end-to-end sem erro com caso de teste. ✅ 07/06/2026 — OK nos dois notebooks. |
| 7.3 | Integração UI: adicionar controles de input ao card (campo texto + botão selecionar arquivo), lendo flags `requer_arquivo`/`requer_texto` do manifesto; implementar `CTkToplevel` para exibir `saida_longa` com botões "Copiar" e "Salvar"; generalizar `_run_thread()` para `result.get("status_txt", "✓ Concluído")` e `result.get("saida_longa")`, sem quebrar automações existentes. | Clicar no card Despachadora no painel, colar texto e receber os 6 blocos na janela filha. |
| 7.4 | Testes com casos reais; ajuste system prompt → v1.3 (promover `[VERIFICAR]` confirmados; corrigir desvios de formato). | Pelo menos 3 casos reais testados; nenhum FUNDAMENTO inventado detectado. |

**Itens da fase:**
- [x] Sprint 7.1 — Investigação e plano de port ✅ (07/06/2026)
- [x] Sprint 7.2 — Port do núcleo ✅ (07/06/2026; end-to-end OK nos dois notebooks)
- [x] Sprint 7.3 — Integração UI ✅ (07/06/2026)
- [x] Fix retry Gemini ✅ (08/06/2026) — `_chamar_gemini()` com backoff 5s/15s/30s para 503/429; `MODELO_GEMINI` revertido para `gemini-2.5-flash`
- [x] Sprint 7.4 — Testes e system prompt v1.3 ✅ (08/06/2026)
- [ ] Sprint 7.5 (dívida técnica, futuro) — OCR automático no arquivo de entrada: quando o PDF de entrada for escaneado (`pdf_imagem_sem_ocr`), aplicar OCR antes de passar para a Despachadora. Workaround atual: colar texto manualmente no painel. Registrado em 16/06/2026.

---

## Fase 8 — Enriquecimento da Base de Conhecimento da Despachadora

**Objetivo:** tornar a base de conhecimento da Despachadora mais rica e confiável, de forma aditiva e curada, cobrindo fundamentos normativos, metadados de vigência, espécies documentais e lacunas procedimentais sem perder a riqueza real da 5ª Cia.

**Independente das Fases 3–6 — pode rodar em paralelo, como a Fase 7.**

**Regra-mãe:** aditividade. O corpus físico no Drive é intocável: não renomear, não mover, não deletar e não empobrecer entradas existentes. Antes de qualquer reindexação futura, fazer backup de `corpus_index.json`. Fonte oficial pode virar FUNDAMENTO; fonte não-oficial entra, no máximo, como referência marcada `[VERIFICAR]`.

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 8.1 | Diagnóstico do corpus, somente leitura: inventário físico, cruzamento Drive × índice, classificação por natureza/espécie, normas presentes e lacunas contra as 5 camadas. | ✅ 08/06/2026 — `docs/DIAGNOSTICO_CORPUS.md` e `saidas/inventario_corpus.csv` gerados; ROADMAP e STATUS atualizados; nenhuma alteração em `corpus_index.json` ou corpus físico; nenhuma chamada de rede/API/IA. |
| 8.2 | Metadados e vigência: extensão retrocompatível do esquema do índice com natureza, espécie, vigência, hierarquia, fonte e auditoria de classificação. | ✅ 09/06/2026 — `classificar_corpus.py`, `docs/METADADOS_8_2.md`, `saidas/revisao_classificacao.csv` e `saidas/relatorio_193_nao_indexados.csv` gerados; 729 entradas preservadas; 479 alta confiança e 250 baixa confiança. |
| 8.3 | Segunda passada de classificação: adicionar `MODELO_PRECEDENTE` e promover apenas baixas com estrutura I-7-PM inequívoca, sem tocar altas existentes. | ✅ 09/06/2026 — D-11 registrada; 36 entradas promovidas para `MODELO_PRECEDENTE`; planilha caiu de 250 para 214 linhas; 39 quase promovidas listadas; altas `MODELO_DE_REDACAO`/`PRECEDENTE` preservadas. |
| Patch 8.3 | Cabeça+cauda: corrigir detector I-7-PM para analisar cabeça de 12k + cauda de 6k chars. | ✅ 09/06/2026 — 15 novas promoções; planilha caiu para 199 linhas. |
| Revisão 8.3 | Revisão humana assistida das 199 entradas NAO_CLASSIFICADO restantes. | ✅ 16/06/2026 — 75 mantidas, 124 excluídas; reimportador estendido com suporte a EXCLUIR; corpus em 605 entradas. |
| 8.4 | Curadoria de fontes oficiais: Ingestão manual e curada de legislação-base e normativos PMESP de fontes brancas, com URL, data de captura e proveniência. | Segmentações do Vademecum, Doutrinas PM e POPs concluídas em 16/06/2026; corpus com 674 entradas; SHA-256 final `a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`. |
| 8.4-bis | Prompt Hardening: endurecer disciplina de proveniência no MASTER_SYSTEM_PROMPT para evitar vazamentos e readequar rótulos e placeholders vencidos. | ✅ 17/06/2026 — Prompt hardening validado pelo teste manual e homologado. |
| 8.4-campo | Teste de campo com POPs: Validar a Despachadora em campo pós-sprint 8.4 e 8.4-bis com expedientes reais cobrindo POPs. | ✅ 17/06/2026 — 3 expedientes rodados, validados e homologados. |
| 8.4-ter | Recuperação Híbrida: partição estrita de pools por natureza, flat boost de pistas dos modelos, busca literal complementar na query e controle moderado de Notebooklm. | ✅ 17/06/2026 — Lógica de busca híbrida e partição de pools implementada em despachadora.py; validado localmente nos 3 casos. |
| 8.5 | IA buscadora assistida: localizar e sugerir fontes oficiais para confirmação humana antes de qualquer Ingestão. | Nenhuma Ingestão direta por IA; humano confirma no portão de verificação. |


> **Nota de numeração (16/06/2026):** O `PROMPT_FASE8.md` original numerava "Curadoria de fontes" como Sprint 8.3 e "IA buscadora" como Sprint 8.4. O Patch cabeça+cauda e a Revisão humana foram intercalados entre os sprints, deslocando a numeração para 8.4 e 8.5 respectivamente. O conteúdo é o mesmo; só a numeração interna divergiu. Ver D-13 para o EXCLUIR introduzido na Revisão humana.

### Sprint 8.4 — Curadoria de Fontes Oficiais & 8.4-campo — Validação em campo

**Regra:** Nenhuma ingestão por IA. Humano localiza, confere vigência e autoriza. A IA apenas indexa o que o humano trouxer.

**Problema real do 8.4:** A Despachadora tem dois pools de recuperação — Fundamento (top 12 normas por densidade) e Modelo de redação (top 8 da casa). O corpus é forte em modelos da casa mas fraco em fundamento normativo: normas presentes como PDF escaneado sem texto limpo ou citadas em outros docs mas não indexadas diretamente. Resultado: Bloco 2 (Análise Jurídica) cita `[VERIFICAR]` onde deveria citar artigo de lei com confiança.

**Passo 0 — Teste de campo (CONCLUÍDO em 17/06/2026)**
Rodamos 3 expedientes reais (Algemas, Transporte de Preso, Abordagem de Veículo) com a Despachadora. Os resultados foram documentados em `docs/RELATORIO_CAMPO_8_4.md`. A análise confirmou a ausência de `[FONTE:]` no output (por limitação do prompt) e o funcionamento da trava anti-vazamento (Categoria A). Foi identificada concorrência de busca pelo compilado de POPs de `Notebooklm/` que afetou a precisão do retrieval dos segmentos novos.


**Passo 1 — Quick wins (reclassificar sem ingestão nova)**
Entradas já no corpus com texto mas `NAO_CLASSIFICADO` — reimportar com natureza correta:
- [ ] `JD/PPJM/Manuais, Leis, Regulamentos/I-7-PM_7ª ed. Atual.pdf` → `NORMA` (95k chars, já indexado)
- [ ] `JD/PPJM/Manuais, Leis, Regulamentos/RDPM atualizado 21MAR25.pdf` → `NORMA` (134k chars)
- [ ] `JD/PPJM/Manuais, Leis, Regulamentos/RDPM_LC915_out07.pdf` → `NORMA` (140k chars)

**Passo 2 — Alta prioridade (ingestão nova)**
- [ ] **Lei 18.442/2026** — ausente no corpus (0 entradas). Reorganiza quadros PMESP. Qualquer expediente sobre pessoal que citar norma anterior está errado.
- [ ] **I-7-PM completa e limpa** — versão P1 classificada (102k chars), versão JD reclassificar (Passo 1). Confirmar se cobre todos os capítulos.
- [x] **Vademecum segmentado** — 6 segmentos temáticos em `Normas/Vademecum_Segmentos/` (CTB, ECA, CP Militar, CPP flagrante, Maria da Penha e Drogas), todos `NORMA + humana`, `error=None`, entre 20k e 150k chars.
- [x] **Doutrinas PM segmentadas** — 31 segmentos temáticos em `Normas/Doutrinas_PM_Segmentos/`, todos `NORMA + humana`, `error=None`, entre 20k e 150k chars.
- [x] **POPs segmentados** — 32 segmentos em `Normas/POPs_Segmentos/`; 30 `PROCEDIMENTAL + humana`, 2 `NORMA + humana` por fundamento jurídico embutido; todos `error=None`, entre 20k e 150k chars.
- [x] **CTB** — artigos operacionais (abordagem de veículo, alcoolemia, acidente com vítima) cobertos por `Vademecum_CTB.txt`.
- [x] **ECA** — artigos que a 5ª Cia usa (apreensão de menor, medidas protetivas) cobertos por `Vademecum_ECA.txt`.

**Deixar para depois:**
- Jurisprudência — só entra com URL verificável e data de captura. Risco jurídico sem fonte atestada.
- CP/CPP completos — textos muito longos, busca por densidade se perde sem recorte.

**Fluxo por fonte nova:**
1. Localizar no site oficial (governo, Diário Oficial, ALESP)
2. Registrar URL + data de captura + vigência
3. Salvar em pasta adequada do corpus no Drive
4. Rodar `indexar_corpus.py` incremental
5. Verificar entrada e confirmar `natureza=NORMA`

### Sprint 8.1 — Diagnóstico do Corpus

Restrição absoluta: somente leitura. Não modificar `corpus_index.json`, não baixar, mover ou editar arquivos, não chamar API de IA e não acessar a internet.

Tarefas:
- Inventário físico do `CORPUS_PATH`, por seção real existente no Drive, com contagem por tipo, tamanho e datas.
- Cruzamento com `corpus_index.json`: arquivos não indexados, entradas órfãs, entradas com erro, textos abaixo do mínimo e prováveis duplicatas.
- Classificação heurística por natureza: `NORMA`, `MODELO_DE_REDACAO`, `PRECEDENTE`, `JURISPRUDENCIA`, `PROCEDIMENTAL`, `OUTRO`, `NAO_CLASSIFICADO`.
- Classificação por espécie documental da casa: parte, ofício, despacho, sindicância, IPM, TC, relatório, escala, ata, outro.
- Levantamento de normas presentes/citadas por busca textual, sem afirmar vigência.
- Mapa de lacunas contra as 5 camadas: legislação-base, normativos internos, modelos de redação, jurisprudência operacional e procedimental.

Entregáveis:
- `docs/DIAGNOSTICO_CORPUS.md`
- `saidas/inventario_corpus.csv`
- Lista explícita de suposições de classificação e itens `NAO_CLASSIFICADO`.

---

## Histórico (diário)

**03/06/2026** — Scaffold criado, BOPM migrado, decisões A/B/C registradas, STATUS.md criado, Fase 0 detalhada em 2 sprints.

**03/06/2026** — Fase 0 · Sprint 1 executado e testado: `nucleo/` criado com `segredos.py`, `log.py`, `vpn.py`, `browser.py`; credenciais migradas para `segredos.env`; `config.py` limpo; BOPM rodando pelo código refatorado.

**03/06/2026** — Fase 0 · Sprint 2 concluído e testado: `painel.py` abre, botão "Baixar BOPMs" roda o BOPM com log ao vivo. Fase 0 fechada.

**05/06/2026** — Decisão D-06 registrada: SEI removido do escopo de automação; acesso ao SEI ficará manual.

**05/06/2026** — Fase 1 · Sprint 1 implementado: logins reutilizáveis Mapa Força/Dejem e smoke-test Teste de Logins criados. Pendente validação real pelo painel/VPN.

**05/06/2026** — Fase 1 · Sprint 1 validado pelo painel: [OK] Mapa Força e [OK] Dejem. Aprendizados registrados em `docs/APRENDIZADOS.md`. Fase 1 fechada.

**05/06/2026** — Ajuste pós-validação: criados botões reais Abrir Mapa Força e Abrir Dejem/Delegada; Teste de Logins mantido como diagnóstico.

**05/06/2026** — Diagnóstico de consistência (sprint de documentação): D-07 registrada em DECISOES.md; Fases 2–7 detalhadas com sprints e critérios de aceite; Fase 7 (Despachadora) adicionada ao ROADMAP, PLANO e STATUS; `segredos.env.exemplo` atualizado com `GEMINI_API_KEY` e `CORPUS_PATH`; README atualizado.

**06/06/2026 (tarde)** — Fase 2 · Sprint 2.1 validado em campo: 1/1 BOPMs validados, zero falhas. Fluxo completo executado: 2º ícone (Editar Ocorrência) → Visualiza PDF se necessário → Outros (img GeneXus W0236CHK_OUT) → Validar BO-e → window.confirm aceito → Retornar → Edge mantido aberto na listagem. Sprint 2.1 fechado.

**06/06/2026** — Fix Baixar BOPM: `siopm_navigator.py` corrigido para detectar BOPMs com status "BO Informal" além de "Não Formalizado". Correção em 3 pontos: log de abertura, filtro JavaScript na listagem e lista de keywords do indicador visual. Validado em execução real.

**07/06/2026** — Fase 7 · Sprint 7.1 concluído: diagnóstico completo do painel (mecanismo de descoberta, contrato `run(ctx)`, lacunas de input e saída longa, adaptações mínimas da Despachadora). Decisões aprovadas: Input=A (Contexto opcional), Saída=A (CTkToplevel), corpus_index=git direto.

**07/06/2026** — Fase 7 · Sprint 7.2 concluído: port do núcleo da Despachadora entregue e testado end-to-end nos dois notebooks. `nucleo/segredos.py` expandido para `gemini` e `corpus`; `nucleo/contexto.py` recebeu `entrada_arquivo` e `entrada_texto`; `requirements.txt` recebeu `google-genai`; `.gitignore` cobre P1-P5, JD e Notebooklm; `manifesto.py`, `executar.py`, `despachadora.py`, `indexar_corpus.py` e `corpus_index.json` integrados. `corpus_index.json` versionado com 714 entradas e 644 válidas. Chamada ao `gemini-2.5-flash` bem-sucedida e 6 blocos gerados corretamente.

**07/06/2026** — Fase 7 · Sprint 7.3 concluído: integração UI da Despachadora entregue no painel. Cards agora podem exibir controles condicionais por `requer_texto` e `requer_arquivo`; a Despachadora recebe texto colado ou arquivo via `Contexto`; `_run_thread()` usa `status_txt`/`saida_longa`; resultado longo abre em `CTkToplevel` com Copiar, Salvar e Fechar. Status detalhado dos BOPMs foi preservado quando `salvos/encontrados` estiverem presentes.

**08/06/2026** — Fase 7 · Sprint 7.4 concluído: 3 expedientes reais testados pelo painel. 6 blocos gerados corretamente, fundamentos rastreáveis, nenhum FUNDAMENTO inventado. Fase 7 encerrada. Modelo migrado para `gemini-3.5-flash` por deprecação iminente do `gemini-2.5-flash`.

**08/06/2026** — Fix retry Gemini: `MODELO_GEMINI` revertido para `gemini-2.5-flash` (havia sido alterado manualmente para `gemini-2.5-pro`). Adicionada função `_chamar_gemini()` com retry automático (3 tentativas, backoff 5s → 15s → 30s) para erros 503 UNAVAILABLE e 429 RESOURCE_EXHAUSTED; outros erros falham imediatamente. Tanto `processar()` (painel) quanto `main()` (CLI) usam o helper. Sem nova dependência.

**05/06/2026** — Fase 2 · Sprint 2.1 implementado: `automacoes/validar_bopm/manifesto.py` e `automacoes/validar_bopm/executar.py` criados. Botão "Validar BOPM" aparece no painel automaticamente (descoberta pelo contrato). Fluxo: login SIOPM → filtro → detecta pendentes → abre cada BOPM → tenta 3 cliques (Outros / Validar BOPM / Confirmar). Seletores dos 3 cliques a mapear na primeira execução real com VPN — log diagnostica URL e elementos visíveis em caso de falha. Pendente validação pelo painel.

**09/06/2026** — Fase 8 · Sprints 8.2 e 8.3 concluídos: metadados aditivos aplicados a 729 entradas; 36 entradas promovidas para `MODELO_PRECEDENTE`; planilha de revisão em 214 linhas. D-12 registrada reconciliando o fluxo real do `corpus_index.json`: índice e artefatos derivados sincronizam pelo Drive, não pelo git. Próximo passo é o patch cabeça+cauda do detector I-7-PM antes da revisão manual.

**09/06/2026** — Patch 8.3 cabeça+cauda concluído: detector I-7-PM corrigido para analisar cabeça de 12.000 caracteres + cauda de 6.000 caracteres, sem baixar a régua. Foram promovidas mais 15 entradas para `MODELO_PRECEDENTE`; planilha de revisão caiu para 199 linhas; índice final sincronizado no Drive com SHA-256 `3adf96695bcab1b080533ef049fb2c613ada822e1400d250ad3f0128045059e7`.

**16/06/2026** — Fase 2 · Sprint 2.2 validado em campo: relatório `saidas/validacao_bopm_<data>.txt` gerado corretamente com log ao vivo. Fase 2 encerrada.

**16/06/2026** — Fase 8 · Revisão humana e reimport concluídos: triagem assistida das 199 entradas revisada com auxílio de IA agêntica (Codex); 75 entradas mantidas com natureza correta, 124 excluídas do índice. Reimportador (`classificar_corpus.py`) estendido para suportar `natureza_correta=EXCLUIR`, removendo a entrada do índice em vez de atualizar. Corpus final com 605 entradas classificadas. Pasta `saidas/` limpa de artefatos obsoletos. Próximo passo: Sprint 8.4 — curadoria de fontes oficiais.

**16/06/2026** — Sprint 8.4 · Segmentação do Vademecum concluída: `Vademecum.pdf` de 7,3M chars segmentado em 6 arquivos temáticos (`CTB`, `ECA`, `CP Militar`, `CPP flagrante`, `Maria da Penha`, `Drogas`) em `Normas/Vademecum_Segmentos/`; corpus passou de 605 para 611 entradas; todos os segmentos ficaram `NORMA`, `classificacao_origem=humana`, `error=None`, entre 20k e 150k chars; prova de aditividade passou; índice final copiado para o Drive; SHA-256 final `12c29eec5983347e6b20e973c140030bb905c1ec728a5c8fc5b23d45e83f0705`. Relatório em `docs/SEGMENTACAO_VADEMECUM.md`.

**16/06/2026** — Sprint 8.4 · Segmentação das Doutrinas PM concluída: `Doutrinas pm_compressed (1).pdf` de 1.643 páginas segmentado em 31 arquivos temáticos em `Normas/Doutrinas_PM_Segmentos/`; corpus passou de 611 para 642 entradas; todos os segmentos ficaram `NORMA`, `classificacao_origem=humana`, `error=None`, entre 20k e 150k chars; prova de aditividade passou; índice final copiado para o Drive; SHA-256 final `0c7f59568d53d6d7708f1f720a36d718f8b51933e79d0b90fe4799896691f149`. Relatório em `docs/SEGMENTACAO_DOUTRINAS_PM.md`.

**16/06/2026** — Sprint 8.4 · Segmentação dos POPs concluída: `POPs.pdf` segmentado em 32 arquivos em `Normas/POPs_Segmentos/`; corpus passou de 642 para 674 entradas; 30 segmentos ficaram `PROCEDIMENTAL + humana` e 2 com fundamento jurídico embutido (`Transporte/Guarda de Presos` e `Uso de Algemas`) ficaram `NORMA + humana`; todos com `error=None`, entre 20k e 150k chars; prova de aditividade passou; índice final copiado para o Drive; SHA-256 final `a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`. Relatório em `docs/SEGMENTACAO_POPS.md`. Próximo passo recomendado: teste de campo da Despachadora com expediente real envolvendo POPs antes da próxima segmentação grande.

**16/06/2026** — Sprint 8.4-bis · Prompt Hardening em validação: Aplicado patch no `MASTER_SYSTEM_PROMPT` para conter vazamentos (Categoria A), placeholders de escala (Categoria B) e readequar rótulos (Categoria C).

**17/06/2026** — Sprint 8.4-campo · Validação em campo concluída: Testes manuais do prompt executados com sucesso no painel para os 3 cenários operacionais. Trava anti-vazamento e rotulação de proveniência validadas e homologadas.

**17/06/2026** — Sprint 8.4-ter · Recuperação Híbrida concluída: Implementada a partição estrita de pools por natureza, flat boost de pistas normativas de modelos, busca literal complementar na query e controle de score para Notebooklm no recuperador da Despachadora. Validação local executada com sucesso nos 3 cenários de teste.
