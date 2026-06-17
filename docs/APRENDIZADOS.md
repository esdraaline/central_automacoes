# Aprendizados da Central de Automações

> Registro curto de erros, acertos e cuidados técnicos para orientar sprints futuros.

---

## 08/06/2026 — Despachadora · OCR de PDFs imagem

### Contexto
67 dos 714 arquivos do corpus_index.json estavam marcados como `error: "pdf_imagem_sem_ocr"` com texto vazio — PDFs escaneados que PyMuPDF e pypdf não conseguem ler. A Despachadora os ignorava na busca (score = 0).

### Solução entregue
Script `automacoes/despachadora/nucleo_despachadora/ocr_pdfs_imagem.py`:
- Lê corpus_index.json e filtra só entradas com `error == "pdf_imagem_sem_ocr"`
- Localiza o arquivo físico via `Segredos().get("corpus")["path"]` — igual ao indexar_corpus.py
- Aplica OCR com `pdf2image.convert_from_path(dpi=300)` + `pytesseract.image_to_string(lang="por")` por página
- Salva corpus_index.json via arquivo temporário + `os.replace` (atomic write — sem risco de corrupção)
- Resultado: 67/67 OK, 552.992 chars adicionados ao índice

### Arquivos agora visíveis para a Despachadora (que antes eram cegos)
- NI_001_02_15_resolução 57.pdf — 84.442 chars (P3)
- DTZ PM3_002_02_16 DEJEM.pdf — 36.514 chars (Notebooklm)
- NI PM3-002-02-17.pdf — 25.062 chars (P3)
- Oitiva como testemunha acusacao sd garcia.pdf — 16.130 chars (JD)
- Resolução CONTRAN nº 432-13.pdf — 13.670 chars (P3)
- Ata Reunião com Prefeito Assinada.pdf — 10.105 chars (P3)

### Regras para manutenção futura
- O script é idempotente: só processa entradas com `error == "pdf_imagem_sem_ocr"` e texto vazio — rodar de novo não reprocessa o que já foi extraído.
- Novos PDFs escaneados adicionados ao corpus: rodar `indexar_corpus.py` primeiro (marca como `pdf_imagem_sem_ocr`) e depois `ocr_pdfs_imagem.py`.
- O corpus_index.json fica no Google Drive junto com o corpus físico — sincroniza automaticamente para outras máquinas. Não é necessário instalar pdf2image/pytesseract nas demais máquinas para usar a Despachadora.
- O Tesseract detecta automaticamente via PATH ou `C:/Program Files/Tesseract-OCR/tesseract.exe` — sem configuração manual.

---

## 06/06/2026 — Fase 2 · Sprint 2.1 · Validar BOPM — fluxo real mapeado em campo

### Acertos
- O contrato `manifesto.py` + `executar.py` funcionou: botão "Validar BOPM" apareceu no painel sem editar `painel.py`.
- Diagnóstico automático (log de frames + elementos visíveis) foi decisivo para mapear cada seletor sem acesso ao código-fonte do SIOPM.
- `page.once("dialog", ...)` registrado antes do clique capturou o `window.confirm` nativo sem race condition.
- `keep_open=True` no `BrowserManager` manteve o Edge aberto na listagem filtrada após a automação — útil para inspeção.

### Erros encontrados
- **Ícone errado:** o código clicava no 1º ícone da linha (visualizar). O ícone correto é o 2º (Editar Ocorrência).
- **"Validar BOPM" vs "Validar BO-e":** o botão real tem `value='Validar BO-e'` e `name='W0236BTNVALIDARTCO'` — nome diferente do planejado.
- **Confirmação não é HTML:** após clicar em "Validar BO-e" o SIOPM dispara `window.confirm` nativo do browser, não um elemento HTML. Seletor CSS nunca funcionaria.
- **"Outros" não é checkbox:** o GeneXus implementa o checkbox "Outros" como `<img id='W0236CHK_OUT'>` clicável. `input[type='checkbox']` nunca o encontraria. Estado (marcado/desmarcado) verificado pelo `src` da imagem: `UnChecked` = desmarcado.
- **Scroll necessário:** a seção "Providências Preliminares" fica abaixo do fold. `window.scrollTo(0, document.body.scrollHeight)` antes do Passo 2 garante que o elemento esteja no viewport.
- **BOs nunca visualizados:** se o BO nunca foi aberto em PDF, o botão "Validar BO-e" não aparece. Solução: clicar em "Visualiza PDF" primeiro e fechar a aba que abre.

### Regras para próximas automações no SIOPM/GeneXus
- **Nunca assumir que checkboxes são `<input type='checkbox'>`** — o GeneXus usa `<img>` clicável com `id` padronizado. Inspecionar pelo diagnóstico antes de escrever seletores.
- **Confirmar tipo de dialog antes de escrever seletor:** dialogs nativos do browser (`alert`, `confirm`, `prompt`) exigem `page.once("dialog", ...)` — não são elementos HTML.
- **Usar o diagnóstico ampliado** (tags `img`, `span`, `td`; campos `onclick`, `src`, `checked`) para revelar elementos GeneXus não-padrão.
- **Sempre verificar o número de ícones na linha** antes de assumir qual clicar.
- **`keep_open=True`** no `BrowserManager.close()` desvincula o Playwright sem fechar o browser — sessão e cookies intactos, janela permanece aberta.
- **Filtro GeneXus é POST-based:** `page.goto(url)` após filtro aplicado faz GET e exibe formulário vazio. Nunca navegar de volta via goto — usar apenas o botão "Retornar" que o SIOPM fornece na tela.
- **Double-Retornar bug:** se `_validar_bopm` clicar "Retornar" (Passo 5) E o `go_back_to_list()` do finally também clicar, o Edge fica 2 níveis acima do esperado. Delegue o retorno a um único ponto (o finally do loop).

---

## 06/06/2026 — Fix Baixar BOPM · Detecção de "BO Informal"

### Erro encontrado
`get_pending_bopms` não detectava BOPMs com status **"BO Informal"** — só reconhecia "Não Formalizado". BOPMs com esse status eram silenciosamente ignorados na listagem.

### Causa raiz
A detecção opera em 3 camadas independentes (JavaScript na listagem, método `_row_has_orange_indicator` e log de abertura), e todas usavam apenas a string `'nao formalizado'` como critério de texto.

### Correção aplicada
Três pontos em `siopm_navigator.py`:
1. Filtro JavaScript (`byText`): adicionado `|| norm.includes('bo informal')`.
2. Keywords de `_row_has_orange_indicator`: adicionados `"bo informal"` e `"b.o. informal"`.
3. Log de abertura: atualizado para refletir os dois status detectados.

### Regra para próximas automações
Ao listar BOPMs por status textual, nunca assumir que existe um único valor possível — o SIOPM usa ao menos dois: "Não Formalizado" e "BO Informal". Qualquer futura automação que filtre por status deve cobrir ambos.

---

## 05/06/2026 — Fase 1 · Sprint 1 · Logins Mapa Força e Dejem

### Acertos
- O contrato `manifesto.py` + `executar.py` funcionou: o botão **Teste de Logins** apareceu no painel sem editar `painel.py`.
- Depois da validação, o uso real ficou separado do diagnóstico: **Abrir Mapa Força** e **Abrir Dejem/Delegada** deixam o navegador aberto; **Teste de Logins** apenas valida e fecha.
- `ctx.segredos` centralizou credenciais sem hardcode nos módulos de login.
- `ctx.browser.launch(headless=False)` abriu Edge visível, adequado para validação assistida.
- O Mapa Força ficou estável ao reproduzir o fluxo real: login SIOPM → CAD Araçatuba → categoria `COMP MAPA FORÇA` → OPM `610025000` → `Procurar`.
- SEI foi removido do escopo por decisão D-06; melhor manter gov.br/2FA manual.

### Erros Encontrados
- A VPN foi desconectada ao fim do teste mesmo já estando conectada manualmente.
  Correção: `VPNManager` agora só desconecta quando a própria execução abriu a conexão.
- O Mapa Força não encontrou a categoria de primeira porque faltava selecionar o CAD intermediário.
  Correção: `login_mapa_forca.py` seleciona CAD Araçatuba antes de procurar `COMP MAPA FORÇA`.
- Abrir um segundo Playwright sem fechar o primeiro causou erro de Sync API.
  Correção: o smoke-test fecha o navegador do Mapa Força antes de iniciar o Dejem.
- O Dejem tentou preencher um `input type="button"` como usuário.
  Correção: `login_dejem.py` separa busca de campos preenchíveis da busca de botões clicáveis.
- Um erro de indentação em `login_dejem.py` foi detectado por `py_compile`.
  Regra prática: rodar `python -m py_compile` antes de reabrir o painel.

### Regras Para Próximas Automações
- Separar botões de uso real de botões de diagnóstico. Testes podem fechar navegador; automações de uso devem manter a tela aberta quando o operador precisa continuar manualmente.
- Não assumir que VPN conectada pelo operador pode ser encerrada pela automação.
- Em sistemas antigos com muitos `input`, separar claramente seletores de campos e seletores de botões.
- Fechar cada instância de Playwright antes de iniciar outra dentro da mesma automação sequencial.
- Registrar no log a URL atual e opções visíveis quando um dropdown esperado não for encontrado.
- Validar pelo painel, não só por linha de comando, quando o critério envolve thread, VPN e Edge visível.

---

## 16/06/2026 — PDF escaneado como entrada da Despachadora

### Contexto
PDF escaneado usado como entrada na Despachadora pelo painel retorna `pdf_imagem_sem_ocr`
e erro fatal: "Nenhum texto extraído dos arquivos de entrada." O expediente não é processado.

### Causa
O extrator do arquivo de entrada usa a mesma cadeia do indexador (PyMuPDF → pypdf),
que falha em PDF imagem. O `ocr_pdfs_imagem.py` existe mas só opera sobre o corpus,
não sobre arquivo avulso de entrada.

### Workaround atual
Colar o texto do expediente manualmente no campo de texto do painel. Funciona sem
nenhuma alteração no código.

### Melhoria futura registrada (Sprint 7.5)
Quando `pdf_imagem_sem_ocr` for detectado no input, a Despachadora roda OCR
(pdf2image + pytesseract, lang=por, 300 DPI) no arquivo avulso e prossegue com
o texto extraído. Não exige nova dependência — já estão instaladas para o corpus.

---

## 16/06/2026 — Despachadora · Prompt Hardening (Sprint 8.4-bis — Patch aplicado / hipótese de correção / aguardando validação em campo)

### Contexto
Algumas execuções reais da Despachadora apresentavam citações normativas erradas (como referenciar o subitem `6.3.2.1` sob o caso de algemas). O diagnóstico revelou que o `MASTER_SYSTEM_PROMPT` possuía 19 referências normativas e fáticas específicas escritas de forma rígida (hardcoded) no prompt do sistema (ex: subitem de flagrante, valores UFESP antigos, escalas de ronda Nov/Dez 2025). O modelo de linguagem as incorporava por associação temática mesmo quando ausentes do corpus recuperado.

### Soluções aplicadas
1. **Regra de Aplicação Inviolável (Categoria A):** Adicionada instrução explícita anti-vazamento imediatamente antes dos blocos de regras fáticas do prompt de sistema, proibindo o modelo de citar referências hardcoded caso o expediente não corresponda exatamente ao cenário da regra (completando a Regra Inviolável de "nada de fundamento inventado").
2. **Eliminação de Dados Temporais Vencidos (Categoria B):** Substituição das menções à escala `Nov/Dez 2025` por placeholders explícitos de pendência no prompt, instruindo o operador a preenchê-la ou atualizá-la anualmente/publicação.
3. **Readequação de Metadados e Rótulos (Categoria C):** Alteração de rótulos de `[FUNDAMENTO]` para `[PADRÃO]` em blocos estáticos (endereços da 5ª Cia, códigos de subunidades), pois representam regras de formatação tipográfica/organizacional, e não fundamentos dinâmicos oriundos do corpus. Inserção de comentários de manutenção no código Python para alertar revisões de UFESP/prazos.

### Regra para manutenção futura
* **Nunca inserir exemplos ou regras com artigos/subitens específicos diretamente no system prompt sem bloqueá-los com regras de aplicabilidade rígidas**, sob o risco do LLM aplicá-los incorretamente por associação conceitual de palavras.
* **Dados dinâmicos e temporais (escalas, valores anuais de UFESP) pertencem ao corpus**, não ao prompt do sistema. Quando precisarem habitar o prompt, devem vir acompanhados de comentários Python claros exigindo auditoria anual.


---

## 17/06/2026 — Despachadora · Recuperação Híbrida (Sprint 8.4-ter)

### Contexto
A divisão teórica da Despachadora entre `CONTEXTO NORMATIVO` (normas/POPs) e `MODELOS DE REDAÇÃO` (precedentes) estava esvaziada em runtime porque ambos os pools eram calculados sem restrição de natureza e o primeiro pool engolia todos os matches não-Notebooklm. Além disso, arquivos compilados grandes do Notebooklm dominavam por acúmulo de termos e modelos validados concorriam diretamente com normas no pool normativo.

### Soluções aplicadas e Aprendizados

1. **Evitar Acúmulo Runaway de Busca em Chunks Gigantes (Flat Boost):**
   * *Problema:* Ao extrair referências operacionais de modelos e buscar no corpus, um boost cumulativo (`boost += 3.0` por pista encontrada) fazia com que arquivos consolidados (como manuais ou constituições contendo centenas de números) acumulassem pontuações gigantescas (ex. +600.0), expulsando POPs específicos limpos da lista.
   * *Solução:* O boost derivado de pistas de modelos deve ser **flat/único** (`entry["_score"] += 3.0` uma única vez se contiver qualquer uma das pistas, em vez de acumular por pista distinta). Isso garante que o metadado de relevância funcione sem criar distorções matemáticas.

2. **Separação Rígida por Metadado `natureza`:**
   * *Acerto:* Separar estritamente o `pool_f` (restrito a `NORMA`, `PROCEDIMENTAL`, `DOUTRINA`, `JURISPRUDENCIA`) e `pool_m` (restrito a `MODELO_DE_REDACAO`, `MODELO_PRECEDENTE`, `PRECEDENTE`) garantiu a preservação da seção "MODELOS DE REDAÇÃO" no prompt enviado ao LLM, fornecendo ao mesmo tempo a base operacional e o exemplo estrutural sem sobreposição.

3. **Accent-Insensitivity em Busca Literal Complementar:**
   * *Problema:* Buscas literais rígidas no corpus para termos digitados pelo operador (ex: `sumula`) falhavam se no corpus a palavra estivesse grafada com acentuação (`súmula`).
   * *Solução:* Normalizar as buscas e utilizar regexes tolerantes a variações de acentuação (ex. `s[uú]mula`) para garantir match de termos de alta relevância jurídica.

---

## 17/06/2026 — Despachadora · Validador Pós-Gemini (Sprint 8.4-quater)

### Contexto
Auditoria dos prompts finais mostrou que expressões jurídicas sensíveis como `peculato-desvio`, `frutos da árvore envenenada`, `Súmula 473` e `padece de vício insanável de competência` não estavam no prompt montado para o Gemini — vinham do conhecimento acumulado do modelo. Isso não é inútil, mas não é fonte documental auditável.

### Aprendizados

1. **Modelo validado é fonte de redação, não fonte normativa.** Um despacho anterior pode orientar estrutura, tom e encaminhamento, mas não pode sustentar sozinho competência legal, prazo, nulidade ou capitulação penal.

2. **Conhecimento próprio do Gemini é útil como hipótese.** Pode servir como alerta, sugestão de diligência, ponto de atenção ou orientação para pesquisa normativa posterior. Deve ser marcado como `[SUGESTÃO IA]` ou `[VERIFICAR]`, nunca como `[FUNDAMENTO]`.

3. **Fundamento jurídico assinável precisa de fonte documental recuperada.** Toda afirmação rotulada `[FUNDAMENTO]` deve trazer `[FONTE: <section/arquivo recuperado>]` que sustente diretamente a afirmação. Se a fonte não foi recuperada, não é fundamento — é hipótese.

4. **Validador pós-Gemini impede conclusão jurídica definitiva sem fonte.** A função `validar_saida_despachadora()` aplica 7 regras determinísticas (A–G) antes de devolver a resposta ao usuário. Bloqueia termos proibidos absolutos, fundamento sem fonte, modelo mascarando norma, termo sensível conclusivo sem lastro e fundamento novo no Texto Pronto que não apareceu na Análise Jurídica.

### Regra de ouro implementada
- **Norma recuperada** → `[FUNDAMENTO]` + `[FONTE:]`
- **Modelo recuperado** → `[PADRÃO]` + `[FONTE-MODELO:]`
- **Conhecimento do Gemini** → `[SUGESTÃO IA]` ou `[VERIFICAR]`
- **Conclusão jurídica definitiva sem fonte** → bloqueada pelo validador

---

## 17/06/2026 — Despachadora · Curadoria do Corpus, Fontes Autônomas e Segmentação (Sprint 8.5)

### Contexto
Saneamento e curadoria da base de conhecimento da Despachadora para evitar desvios no pool normativo (documentos fáticos marcados como norma) e preencher lacunas de fundamentos críticos (algemas, autotutela, competência de IPM/Sindicância e acidentes de viaturas).

### Soluções e Aprendizados

1. **Curadoria do Corpus Reduz Contaminação:**
   * A curadoria proativa com manifesto ativo (`curadoria_corpus.json`) para excluir do índice arquivos pessoais transitórios (como holerites, escalas de serviço e defesas prévias) e precedentes fáticos isolados remove ruídos e limpa o pool de fundamentos, prevenindo falsos positivos de alta pontuação.

2. **Fontes Autônomas Resolvem Lacunas Críticas Melhor que Compilados:**
   * Em vez de depender que o LLM extraia regras detalhadas de PDF consolidados gigantescos, criar pequenas fontes oficiais autônomas (`corpus_manual/`) com transcrição literal da regra exata (ex: Súmula Vinculante 11, Súmula 473, regras do CPPM de competência) garante que o recuperador local selecione a norma correta em Rank 1 com altíssimo score.

3. **Segmentação de Fonte Gigante Deve Preservar Literalidade:**
   * A segmentação de arquivos grandes (como `orientações direito militar.pdf`) em partes de 20k a 150k caracteres deve ser puramente literal. Não se deve resumir, parafrasear ou inventar texto, pois a despachadora e o LLM exigem o texto original cru para auditabilidade de proveniência.

4. **Boost de Domínio Deve Ser Cirúrgico e Condicionado:**
   * Ao ajustar rankings para casos específicos (como acidente com viatura no Caso 2), a aplicação de boost de score deve ser **estritamente condicional** e direcionada apenas a arquivos chaves (ex: ativada apenas se as keywords `"acidente"` e `"viatura"` estiverem presentes simultaneamente), para evitar efeitos colaterais e falsos positivos em outros casos.

5. **Expressões de Busca Literal Devem Ficar Separadas do Texto Oficial:**
   * Ao criar fontes autônomas, os termos de busca auxiliares não devem ser misturados com as citações e textos oficiais literais da norma, garantindo integridade e evitando confusão conceitual durante a geração da resposta pela IA.

6. **Doutrinas e Modelos Nunca Devem Virar Normas:**
   * Textos acadêmicos, jurisprudências ou modelos da casa devem ser classificados rigorosamente como `DOUTRINA`, `JURISPRUDENCIA` ou `MODELO_PRECEDENTE`, e nunca como `NORMA` ou `PROCEDIMENTAL` (reservados exclusivamente para a legislação oficial e POPs vigentes). Isso impede que interpretações opinativas passem por regras vinculantes absolutas no validador.
