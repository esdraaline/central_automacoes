# Metadados 8.2

Sprint 8.2 executado em 09/06/2026 07:13:26.

## Resultado executivo

- Entradas no indice: 729
- Alta confianca: 479
- Baixa confianca: 250
- Linhas geradas para revisao humana: 250
- Vigencia: `nao_avaliado` em 100% das entradas
- Backup local: `C:\projetos\central_automacoes\automacoes\despachadora\corpus_index.backup.20260609-071320.json`
- Backup Drive: `G:\Meu Drive\Arquivos Josemar\Trabalho\backups_corpus_index_despachadora\corpus_index.backup.20260609-071320.json`

## Contagem por natureza

| Valor | Quantidade |
|---|---:|
| MODELO_DE_REDACAO | 20 |
| NAO_CLASSIFICADO | 250 |
| NORMA | 414 |
| PRECEDENTE | 38 |
| PROCEDIMENTAL | 7 |

## Contagem por especie

| Valor | Quantidade |
|---|---:|
| None | 339 |
| ata | 18 |
| despacho | 33 |
| escala | 43 |
| ipm | 26 |
| oficio | 101 |
| outro | 8 |
| parte | 59 |
| relatorio | 90 |
| sindicancia | 9 |
| tc | 3 |

## Contagem por confianca

| Valor | Quantidade |
|---|---:|
| alta | 479 |
| baixa | 250 |

## Contagem por origem

| Valor | Quantidade |
|---|---:|
| heuristica | 729 |

## Prova de aditividade

```
OK: entradas nao diminuiram: antes=729 depois=729
OK: todas as chaves section/arquivo originais permanecem.
OK: nenhum campo original section/arquivo/tipo/texto/error foi alterado.
OK: as unicas mudancas estruturais sao campos novos de metadados.
OK: vigencia='nao_avaliado' em 100% (729/729).
```

## Reimportador

Reimportador testado com `C:\projetos\central_automacoes\saidas\revisao_classificacao_exemplo.csv` em copia temporaria `C:\projetos\central_automacoes\saidas\reimport_teste_index.json`. Primeira execucao: {'aplicadas': 3}. Segunda execucao idempotente: {'ja_humana_preservada': 3}.

## Relatorio dos arquivos nao indexados

- Arquivo: `saidas/relatorio_193_nao_indexados.csv`
- Candidatos por nome/extensao: 0

| Motivo | Quantidade |
|---|---:|
| arquivo_excluido_nome | 3 |
| extensao_excluida:.cer | 1 |
| extensao_excluida:.jpeg | 18 |
| extensao_excluida:.jpg | 12 |
| extensao_excluida:.mp4 | 1 |
| extensao_excluida:.pfx | 1 |
| extensao_excluida:.png | 9 |
| extensao_excluida:.ppt | 2 |
| extensao_excluida:.pptx | 1 |
| extensao_excluida:.rar | 1 |
| pasta_excluida | 144 |

## Compilacao

```
OK py_compile C:\projetos\central_automacoes\automacoes\despachadora\nucleo_despachadora\classificar_corpus.py
```

## Observacoes

- Entradas de baixa confianca foram gravadas no indice como `natureza=NAO_CLASSIFICADO` e `especie=null`.
- As sugestoes da heuristica para baixa confianca foram preservadas apenas em `saidas/revisao_classificacao.csv`.
- O corpus fisico no Drive nao foi reindexado, movido, renomeado ou editado.
