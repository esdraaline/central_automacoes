# Triagem Assistida 199

Gerado em: 09/06/2026. Atualizado apos auditoria de falsas `JURISPRUDENCIA`.

## Escopo

Triagem assistida, somente leitura, das entradas ainda `NAO_CLASSIFICADO` no indice canonico pos-patch cabeca+cauda.

- Indice analisado: `automacoes/despachadora/corpus_index.json`
- SHA-256 do indice: `3adf96695bcab1b080533ef049fb2c613ada822e1400d250ad3f0128045059e7`
- Saida sensivel local ignorada pelo git: `saidas/triagem_assistida_199.csv`
- Nenhuma alteracao foi feita em `corpus_index.json`.
- Nao houve reimportacao, segunda passada, OCR, reindexacao, internet ou API de IA.
- Correcao aplicada: as 26 sugestoes originais `JURISPRUDENCIA` foram reavaliadas; `JURISPRUDENCIA` ficou apenas quando o documento e decisao judicial, sumula ou acordao em si.

## Resultado Executivo

- Total triado: 199
- Alta confianca: 89
- Baixa confianca: 110
- Revisao obrigatoria: 143

## Contagem Por Natureza Sugerida

| Natureza | Quantidade |
|---|---:|
| OUTRO | 139 |
| NORMA | 26 |
| MODELO_PRECEDENTE | 20 |
| PROCEDIMENTAL | 8 |
| JURISPRUDENCIA | 6 |

## Contagem Por Confianca

| Confianca | Quantidade |
|---|---:|
| baixa | 110 |
| alta | 89 |

## Revisao Obrigatoria

| Revisar | Quantidade |
|---|---:|
| SIM | 143 |
| NAO | 56 |

## Quebra Por Pasta

| Pasta | Quantidade |
|---|---:|
| P3 | 59 |
| P1 | 54 |
| JD | 49 |
| P4 | 13 |
| P5 | 9 |
| P2 | 8 |
| [raiz] | 3 |
| Notebooklm | 2 |
| Normas | 1 |
| __pycache__ | 1 |

## Quebra Por Pasta E Natureza

| Pasta | Natureza sugerida | Quantidade |
|---|---|---:|
| P1 | OUTRO | 46 |
| P3 | OUTRO | 38 |
| JD | OUTRO | 32 |
| P3 | NORMA | 9 |
| JD | MODELO_PRECEDENTE | 8 |
| P3 | PROCEDIMENTAL | 8 |
| P4 | OUTRO | 8 |
| P5 | OUTRO | 7 |
| JD | NORMA | 5 |
| JD | JURISPRUDENCIA | 4 |
| P1 | MODELO_PRECEDENTE | 4 |
| P1 | NORMA | 4 |
| P2 | OUTRO | 4 |
| P2 | MODELO_PRECEDENTE | 3 |
| P4 | NORMA | 3 |
| P3 | JURISPRUDENCIA | 2 |
| P3 | MODELO_PRECEDENTE | 2 |
| P4 | MODELO_PRECEDENTE | 2 |
| P5 | NORMA | 2 |
| [raiz] | OUTRO | 2 |
| Normas | NORMA | 1 |
| Notebooklm | MODELO_PRECEDENTE | 1 |
| Notebooklm | OUTRO | 1 |
| P2 | NORMA | 1 |
| [raiz] | NORMA | 1 |
| __pycache__ | OUTRO | 1 |

## Criterios Aplicados

- `JURISPRUDENCIA` foi mantida apenas para decisao judicial, sumula ou acordao como documento principal.
- Documento que apenas cita tribunal, classe processual, sumula ou lei foi reclassificado pela natureza real.
- `JD` recebeu `revisar_obrigatorio=SIM` em todas as linhas.
- Baixa confianca recebeu `revisar_obrigatorio=SIM` em todas as linhas.
- Na duvida entre `MODELO_DE_REDACAO` e `PRECEDENTE`, a sugestao foi `MODELO_PRECEDENTE`, conforme D-11.
- Em `JD`, na duvida entre espelho util e peca sensivel, a sugestao foi `OUTRO`.
- `natureza_correta` e `especie_correta` ficaram vazias para preenchimento humano.
