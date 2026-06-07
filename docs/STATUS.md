# Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint.
**Ultima atualizacao: 07/06/2026**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execucao** | Fase 7 - Despachadora (em paralelo com Fase 2) |
| **Ultima fase concluida** | Fase 7 - Sprint 7.3 (integracao UI no painel em 07/06/2026) |
| **Sprint atual** | Sprint 7.4 - testes com casos reais e system prompt v1.3 |
| **Ultimo sprint concluido** | Sprint 7.3 - integracao UI da Despachadora no painel (07/06/2026) |
| **Proximo passo (trilha principal)** | Testar a Despachadora com expedientes reais; ajustar system prompt para v1.3 |
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

**Trilha principal:** Sprint 7.4 - testes com casos reais e system prompt v1.3.

Escopo imediato:

- Testar pelo menos 3 expedientes reais na Despachadora pelo painel.
- Conferir se os 6 blocos mantem formato, proveniencia e texto pronto.
- Promover `[VERIFICAR]` confirmados e corrigir desvios no system prompt v1.3.

**Trilha pendente:** Sprint 2.2 - relatorio `saidas/validacao_bopm_<data>.txt`, aguardando BO pendente real para validacao em campo.

---

## Bloqueios / pendencias

**Fase 7 - Sprint 7.4 - proximo:**
- Validar a Despachadora pelo painel com expedientes reais.
- Ajustar system prompt para v1.3 apos os testes.
- Confirmar que nenhum FUNDAMENTO inventado aparece nos casos reais.

**Fase 2 - Sprint 2.2 - pendente:**
- Validar fix double-Retornar com BO pendente real em campo.
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
