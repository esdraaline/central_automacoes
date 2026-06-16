# Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint.
**Ultima atualizacao: 09/06/2026**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execucao** | Fase 8 — Enriquecimento da Base |
| **Ultima fase concluida** | Fase 7 - Sprint 7.4 (testes reais em 08/06/2026); Fase 7 encerrada |
| **Sprint atual** | Revisão humana da classificação restante (triagem assistida pronta) |
| **Ultimo sprint concluido** | Triagem Assistida das 199 Entradas restante (09/06/2026) |
| **Proximo passo (trilha principal)** | revisar `saidas/triagem_assistida_199.csv` (com sugestões assistidas); depois reimportar com `python automacoes/despachadora/nucleo_despachadora/classificar_corpus.py --reimport saidas/triagem_assistida_199.csv` |
| **Trilha pendente (Fase 2)** | Sprint 2.2 - relatorio em `saidas/validacao_bopm_<data>.txt` apos BO pendente real |

---

## Ja feito

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

**Trilha principal:** revisar manualmente `saidas/triagem_assistida_199.csv` e depois reimportar.

Escopo imediato:

- Revisar as 199 linhas de sugestões de triagem em `saidas/triagem_assistida_199.csv`.
- Preencher `natureza_correta`, `especie_correta` e, se necessário, `observacao` baseando-se nas sugestões assistidas geradas.
- Reimportar com `python automacoes/despachadora/nucleo_despachadora/classificar_corpus.py --reimport saidas/triagem_assistida_199.csv`.

---

## Bloqueios / pendencias

**Fase 8 - revisão humana - atual:**
- Triagem assistida de 199 linhas concluída com sucesso e salva em `saidas/triagem_assistida_199.csv`.
- JD agrupado no final com atenção redobrada e `revisar_obrigatorio=SIM`.
- Pronto para revisão humana antes da reimportação no índice.

**Fase 2 - Sprint 2.2 - atual:**
- Aguardando BO pendente real no SIOPM para validacao em campo.
- Validar fix double-Retornar com BO pendente real.
- Gerar relatorio `saidas/validacao_bopm_<data>.txt`.

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
