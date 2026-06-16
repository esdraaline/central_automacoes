# Contexto de Retorno — 10/06/2026

Este arquivo é a fotografia para retomar a Fase 8 em outra máquina/conversa sem perder o fio.

## Estado Atual

- Projeto: Central de Automações — Despachadora do Comandante.
- Branch: `main`.
- Sprint 8.1 concluído: diagnóstico somente leitura do corpus.
- Sprint 8.2 concluído: metadados adicionados ao `corpus_index.json` de forma aditiva.
- Sprint 8.3 concluído: segunda passada promoveu documentos com estrutura I-7-PM inequívoca para `MODELO_PRECEDENTE`.
- Patch 8.3 cabeça+cauda concluído: detector passou a analisar cabeça de 12.000 caracteres + cauda de 6.000 caracteres, sem afrouxar a régua.
- Não houve commit/push dos arquivos sigilosos/derivados ignorados: `corpus_index.json`, backups e arquivos em `saidas/`.

## Números Atuais Do Índice

- Total de entradas: `729`.
- Alta confiança: `530`.
- Baixa confiança: `199`.
- `vigencia=nao_avaliado`: `729/729`.
- SHA-256 canônico do índice final: `3adf96695bcab1b080533ef049fb2c613ada822e1400d250ad3f0128045059e7`.

Naturezas:

| Natureza | Quantidade |
|---|---:|
| NORMA | 414 |
| PRECEDENTE | 38 |
| MODELO_PRECEDENTE | 51 |
| MODELO_DE_REDACAO | 20 |
| PROCEDIMENTAL | 7 |
| NAO_CLASSIFICADO | 199 |

Planilha de revisão atual (`saidas/revisao_classificacao.csv`):

| Sugestão | Quantidade |
|---|---:|
| MODELO_DE_REDACAO | 94 |
| OUTRO | 85 |
| NORMA | 19 |
| PRECEDENTE | 1 |

## Decisões Importantes

- `D-11` registrada: `MODELO_PRECEDENTE` é uma terceira natureza, sem substituir `MODELO_DE_REDACAO` nem `PRECEDENTE`.
- As 20 entradas `MODELO_DE_REDACAO` e as 38 `PRECEDENTE` já classificadas em alta confiança são protegidas e não devem ser migradas.
- O patch cabeça+cauda do 8.3 foi executado e promoveu mais 15 entradas para `MODELO_PRECEDENTE`.
- A correção manteve a régua original: `4 de 6` nas pastas P1-P5 e `5 de 6` em JD, com os mesmos obrigatórios.

## Arquivos Principais

- Código do classificador: `automacoes/despachadora/nucleo_despachadora/classificar_corpus.py`.
- Relatório do 8.2: `docs/METADADOS_8_2.md`.
- Relatório do 8.3: `docs/SEGUNDA_PASSADA_8_3.md`.
- Prompt do patch executado: `docs/PROMPT_PATCH_8_3_CABECA_CAUDA.md`.
- Planilha para revisão humana: `saidas/revisao_classificacao.csv`.
- Índice atualizado: `automacoes/despachadora/corpus_index.json`.

## Próximo Movimento

Revisar manualmente a planilha restante `saidas/revisao_classificacao.csv`.

Objetivo da revisão:

- Preencher `natureza_correta`, `especie_correta` e `observacao` quando necessário.
- Reimportar a planilha humana com `--reimport`.
- Manter `vigencia=nao_avaliado`; avaliação de vigência fica para sprint posterior.

## Travas Para Amanhã

- Não reindexar.
- Não rodar OCR.
- Não acessar internet nem API de IA.
- Não tocar no corpus físico.
- Não sobrescrever `classificacao_origem=humana`.
- Criar backup local + Drive antes de escrever.
- Provar aditividade após escrever.

## Sincronização Entre Máquinas

Vai pelo GitHub:

- Código.
- Documentação.
- Prompts.
- `.gitignore`.

Vai pelo Google Drive, fora do git:

- `corpus_index.json` atualizado no corpus: `G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs\corpus_index.json`.
- Pacote de artefatos ignorados em: `G:\Meu Drive\Arquivos Josemar\Trabalho\central_automacoes_sync\fase8_20260609\`.
- Backups do índice em: `G:\Meu Drive\Arquivos Josemar\Trabalho\backups_corpus_index_despachadora\`.

## Comandos Úteis Amanhã

```powershell
git pull origin main
Get-Content docs\CONTEXTO_RETORNO_2026-06-10.md
Get-Content docs\PROMPT_PATCH_8_3_CABECA_CAUDA.md
```

Para conferir o índice canônico no Drive:

```powershell
Get-FileHash -Algorithm SHA256 "G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs\corpus_index.json"
```

Para reimportar a planilha humana depois:

```powershell
python automacoes\despachadora\nucleo_despachadora\classificar_corpus.py --reimport saidas\revisao_classificacao.csv
```
