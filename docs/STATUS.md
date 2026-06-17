# Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint.
**Ultima atualizacao: 17/06/2026**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execucao** | Fase 8 concluída; próxima fase em planejamento |
| **Ultima fase concluida** | Fase 8 — Enriquecimento da Base (17/06/2026) |
| **Sprint atual** | Pós-sprint 8.4-ter (Recuperação Híbrida) concluído e validado localmente; pronto para congelamento |
| **Ultimo sprint concluido** | Sprint 8.4-ter — Recuperação Híbrida (17/06/2026) |
| **Proximo passo (trilha principal)** | Iniciar Fase 3 — Órion (consulta de indicadores criminais) |
| **Proxima fase** | Fase 3 — Órion (consulta de indicadores criminais) |

---

## Ja feito

- **Sprint 8.4-ter — Recuperação Híbrida (CONCLUÍDO em 17/06/2026)** — Implementada a partição estrita dos pools de contexto Fundamento (`NORMA`, `PROCEDIMENTAL`, `DOUTRINA`, `JURISPRUDENCIA`) e Modelos (`MODELO_DE_REDACAO`, `MODELO_PRECEDENTE`, `PRECEDENTE`). Implementados a busca literal complementar da query, o boost flat fixo de pistas normativas extraídas de modelos e o controle de score de PDFs compilados do Notebooklm. Validação local concluída nos 3 casos operacionais com sucesso.
- **Sprint 8.4-bis & 8.4-campo — Prompt Hardening & Validação em Campo (CONCLUÍDO em 17/06/2026)** — Patch aplicado no `MASTER_SYSTEM_PROMPT` homologado e validado manualmente com os 3 expedientes sugeridos (Algemas, Transporte de Preso, Abordagem de Veículo). Relatório final em `docs/RELATORIO_CAMPO_8_4.md`.
- Scaffold, migracao do BOPM, decisoes A/B/C
- **Fase 0 - Sprint 1 concluida** - `nucleo/` criado (segredos, log, vpn, browser), credenciais migradas para `segredos.env`, BOPM testado pela linha de comando
- **Fase 0 - Sprint 2 concluida** - Contrato (`manifesto.py` + `executar.py`), `painel.py` com customtkinter; botao "Baixar BOPMs" roda o BOPM com log ao vivo na janela
- **Fase 1 - Sprint 1 concluida** - modulos `nucleo/login_mapa_forca.py` e `nucleo/login_dejem.py` criados; botoes reais Abrir Mapa Forca e Abrir Dejem/Delegada criados; Teste de Logins mantido como diagnostico
- **Decisao D-06 concluida** - SEI removido do escopo de automacao; acesso ao SEI sera manual
- **Decisao D-07 concluida** - Despachadora: codigo na Central, corpus no Drive; `GEMINI_API_KEY` e `CORPUS_PATH` via `segredos.env`
- **Fase 2 - Sprint 2.1 concluida** - validado em campo em 06/06/2026: fluxo completo (2o icone -> Visualiza PDF se necessario -> Outros -> Validar BO-e -> dialog -> Retornar). "Outros" e `<img id='W0236CHK_OUT'>` GeneXus, nao checkbox HTML. Edge mantido aberto na listagem ao fim.
- Aprendizados da validacao registrados em `docs/APRENDIZADOS.md`
- **Fix Baixar BOPM concluido** - `siopm_navigator.py` corrigido para detectar tambem BOPMs com status "BO Informal"; validado com sucesso em execucao real
- **Fase 7 - Sprint 7.1 concluida em 07/06/2026** - diagnostico completo: mecanismo de descoberta/contrato mapeado; lacunas de input e saida longa identificadas; adaptacoes minimas de `despachadora.py` descritas; `.gitignore` e `segredos.env.exemplo` verificados. Decisoes aprovadas: Input=A (Contexto opcional), Saida=A (CTkToplevel), `corpus_index.json`=git direto.
- **Fase 7 - Sprint 7.2 concluida em 07/06/2026** - nucleo da Despachadora portado para a Central e testado end-to-end nos dois notebooks.
- **Fase 7 - Sprint 7.3 concluida em 07/06/2026** - painel agora exibe input de texto e seletor de arquivo para automacoes que declaram `requer_texto`/`requer_arquivo`; `saida_longa` abre em janela filha com Copiar, Salvar e Fechar; `_run_thread()` usa `status_txt` sem quebrar o status detalhado dos BOPMs.
- **Fix retry Gemini concluido em 08/06/2026** - `despachadora.py`: `MODELO_GEMINI` revertido para `gemini-2.5-flash`; funcao `_chamar_gemini()` adicionada com retry 3 tentativas (5s, 15s, 30s) para erros 503/429; `processar()` e `main()` usam o helper; sem nova dependencia.
- **Fase 7 - Sprint 7.4 concluida em 08/06/2026** - 3 expedientes reais testados pelo painel; 6 blocos gerados corretamente com fundamentos rastreáveis; nenhum FUNDAMENTO inventado detectado; Fase 7 encerrada.
- **Migracao de modelo Gemini em 08/06/2026** - `MODELO_GEMINI` migrado de `gemini-2.5-flash` para `gemini-3.5-flash` em `despachadora.py` por deprecacao iminente do 2.5-flash.
- **OCR corpus Despachadora concluído em 08/06/2026** — `ocr_pdfs_imagem.py` criado em `automacoes/despachadora/nucleo_despachadora/`; 67 PDFs imagem processados com OCR (pdf2image + pytesseract, lang=por, 300 DPI); 67/67 OK, zero erros; 552.992 chars novos adicionados ao índice; corpus_index.json atualizado. Dependências instaladas: pdf2image, pytesseract, Tesseract OCR UB-Mannheim, idioma por, Poppler.
- **Enriquecimento do corpus concluído em 08/06/2026** — varredura de 7.845 arquivos em `G:\Meu Drive\Arquivos Josemar\Trabalho`; 14 documentos novos adicionados ao corpus (8 em Normas/, 6 em JD/): I-1-PM Publicações, 5 NIs operacionais, I-15-PM, I-36-PM, 3 modelos de despacho/portaria IPM e 3 ofícios a autoridade judicial. Total do corpus: 728 entradas indexadas.
- **Fase 8 - Sprint 8.2 concluído em 09/06/2026** — `classificar_corpus.py` criado; 729 entradas receberam metadados aditivos; 479 alta confiança, 250 baixa confiança; `vigencia=nao_avaliado` em 100%; reimportador testado e idempotente.
- **Fase 8 - Sprint 8.3 concluído em 09/06/2026** — D-11 registrada; `MODELO_PRECEDENTE` adicionado; segunda passada promoveu 36 entradas de baixa para alta confiança; planilha de revisão caiu de 250 para 214 linhas; 39 entradas ficaram no grupo "quase".
- **Decisão D-12 registrada em 09/06/2026** — `corpus_index.json` deixou de ir pelo git; fluxo atual é Drive + `.gitignore`, com backups fora do `CORPUS_PATH`.
- **Patch 8.3 cabeça+cauda concluído em 09/06/2026** — detector I-7-PM passou a analisar cabeça de 12.000 chars + cauda de 6.000 chars; 15 novas entradas promovidas para `MODELO_PRECEDENTE`; planilha caiu de 214 para 199 linhas; SHA-256 final do índice: `3adf96695bcab1b080533ef049fb2c613ada822e1400d250ad3f0128045059e7`.
- **Triagem Assistida das 199 concluída em 09/06/2026** — Planilha de sugestões `saidas/triagem_assistida_199.csv` gerada a partir da leitura do texto completo do índice; 10 lotes non-JD e 5 lotes JD processados de forma consistente, com JD ordenado por último, atenção redobrada no grupo JD, e justificativas curtas citando trechos/sinais concretos.
- **Fase 2 - Sprint 2.2 concluído em 16/06/2026** — validado em campo com BO pendente real; relatório `saidas/validacao_bopm_<data>.txt` gerado corretamente; log ao vivo funcionando. Fase 2 encerrada.
- **Revisão humana e reimport concluídos em 16/06/2026** — 199 entradas revisadas com auxílio de IA agêntica: 75 mantidas com natureza correta, 124 excluídas do índice. Reimportador estendido para suportar `natureza_correta=EXCLUIR` (remove entrada do índice). Corpus final: 605 entradas classificadas com `classificacao_origem=humana` ou `alta`. Pasta `saidas/` limpa de artefatos obsoletos.
- **Sprint 8.4 - Segmentação do Vademecum concluída em 16/06/2026** — Vademecum de 7,3M chars segmentado em 6 arquivos temáticos em `Normas/Vademecum_Segmentos/`; corpus passou de 605 para 611 entradas; todos os segmentos ficaram `NORMA`, `classificacao_origem=humana`, `error=None`, entre 20k e 150k chars; prova de aditividade passou; SHA-256 final do índice: `12c29eec5983347e6b20e973c140030bb905c1ec728a5c8fc5b23d45e83f0705`.
- **Sprint 8.4 - Segmentação das Doutrinas PM concluída em 16/06/2026** — compilado de 1.643 páginas segmentado em 31 arquivos temáticos em `Normas/Doutrinas_PM_Segmentos/`; corpus passou de 611 para 642 entradas; todos os segmentos ficaram `NORMA`, `classificacao_origem=humana`, `error=None`, entre 20k e 150k chars; prova de aditividade passou; SHA-256 final do índice: `0c7f59568d53d6d7708f1f720a36d718f8b51933e79d0b90fe4799896691f149`.
- **Sprint 8.4 - Segmentação dos POPs concluída em 16/06/2026** — compilado `POPs.pdf` segmentado em 32 arquivos em `Normas/POPs_Segmentos/`; corpus passou de 642 para 674 entradas; 30 POPs ficaram `PROCEDIMENTAL + humana` e 2 POPs com fundamento jurídico embutido ficaram `NORMA + humana`; todos com `error=None`, entre 20k e 150k chars; prova de aditividade passou; índice final sincronizado no Drive; SHA-256 final: `a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`.

---

## Sprint 7.2 - resultado

Arquivos entregues:

| Arquivo | Resultado |
|---|---|
| `nucleo/segredos.py` | `_SCHEMA` expandido com `gemini` e `corpus` |
| `nucleo/contexto.py` | `entrada_arquivo` e `entrada_texto` adicionados |
| `requirements.txt` | `google-genai>=1.0.0` adicionado |
| `.gitignore` | Pastas P1-P5, JD e Notebooklm cobertas |
| `automacoes/despachadora/manifesto.py` | Novo manifesto da categoria `Redacao`, sem VPN |
| `automacoes/despachadora/executar.py` | Novo ponto de entrada chamando `processar(ctx)` |
| `automacoes/despachadora/nucleo_despachadora/despachadora.py` | Codigo real do Drive integrado |
| `automacoes/despachadora/nucleo_despachadora/indexar_corpus.py` | Indexador real integrado, com modo incremental |
| `automacoes/despachadora/corpus_index.json` | Versionado no git; 714 entradas, 644 validas |

Teste end-to-end:

- Corpus carregado com 641-644 entradas validas, conforme notebook/execucao.
- Chamada ao `gemini-2.5-flash` bem-sucedida.
- Os 6 blocos foram gerados corretamente com fundamentacao real do corpus.
- `segredos.env` preenchido manualmente nos dois notebooks com `GEMINI_API_KEY` e `CORPUS_PATH`.
- `google-genai` instalado nos dois notebooks.
- `corpus_index.json` sincronizado via git; remoto com 644 validas.

---

## Proximo passo

**Trilha principal:** Fase 3 — Órion (consulta de indicadores criminais).

Escopo imediato:

- Login no Órion via Playwright (Edge, não-headless) usando credenciais seguras centralizadas em `nucleo/segredos`.
- Desenvolvimento da consulta automática de indicadores por município/período e extração correta de dados.
- Escrita de relatórios em `saidas/orion_<municipio>_<data>.txt`.

---

## Bloqueios / pendencias

**Fase 8 - Sprint 8.4 — concluído:**
- Revisão humana das 199 entradas concluída em 16/06/2026.
- Segmentações de Vademecum, Doutrinas e POPs concluídas em 16/06/2026.

**Fase 8 - Concluída:**
- Prompt Hardening (8.4-bis), Validação em campo (8.4-campo) e Recuperação Híbrida (8.4-ter) concluídos e integrados.
- O índice de corpus do Drive foi sincronizado (SHA-256 `a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`).

**Fase 8 - Sprint 8.5 — em aberto/planejado:**
- IA buscadora assistida (localizar e sugerir fontes operacionais no portal da ALESP/PMESP) pendente para o futuro se necessário.

**Dívida técnica — Despachadora:**
- PDF escaneado como entrada retorna erro `pdf_imagem_sem_ocr`. Workaround: colar texto no painel. Sprint 7.5 registrado no ROADMAP para OCR automático no input.
- Slogan institucional (linha 447 de `despachadora.py`): permaneceu com o rótulo `[FUNDAMENTO]`, devendo ser readequado para `[PADRÃO]` em sprints futuros de saneamento.
- Escala vigente (Categoria B): o system prompt usa placeholders e deve ser alimentado com a escala real de 2026 quando publicada.
- Poluição de Contexto: a pasta `Notebooklm` contém os arquivos originais unsegmentados do Drive que concorrem no retrieval com os novos POPs segmentados. É recomendável o saneamento (remoção ou exclusão do índice).

**Fase 3 - Órion - pendente:**
- Ainda não iniciada. Próxima fase após Fase 8.

---

## Dois notebooks

Ambos os notebooks estao sincronizados em 07/06/2026:

- `segredos.env` preenchido manualmente em cada maquina.
- `CORPUS_PATH` ajustado conforme a letra de unidade local.
- `google-genai` instalado.
- `corpus_index.json` sincronizado pelo git.
- Teste end-to-end da Despachadora executado com sucesso.

---

## Como manter este arquivo

Ao fim de cada sprint, atualizar: a data, **Onde estou**, **Ja feito**, **Proximo passo** e **Bloqueios**. Mantenha curto - e uma foto, nao um diario. O diario detalhado fica no ROADMAP.md (Historico).
