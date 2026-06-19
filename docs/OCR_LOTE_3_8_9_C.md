# OCR Lote 3 — Sprint 8.9-c

## Estado inicial
- **Branch:** `main`
- **Índice (antes):** 729 chunks (`corpus_ocr`: 13)
- **Recuperação e Ambiente OCR:** OK

## PDFs candidatos
Foram varridos os arquivos com classificação `PRECISA_OCR`, excluindo os processados no Lote 1 e 2.
- `P2/OS CPI10-002-30-16 regularização revista de armários.pdf`
- `P2/OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf`
- `P3/OS/ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf`
- `Notebooklm/Supervisor Regional/OC PM3_008_02_16 DEJEM.pdf`
- `P3/Outros/Preleção/Codigo para tipificação de ocorrências 1961_190416104118_001.pdf`
- `P3/Outros/Preleção/Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf`

## PDFs selecionados
Os 6 PDFs foram selecionados porque são documentações normativas e procedimentais duradouras, com tamanho enxuto (1 a 4 páginas) e alto valor informativo. Nenhum documento isolado ou efêmero foi incluído.

## Resultado OCR

| arquivo | páginas | caracteres | linhas úteis | qualidade | decisão |
|---|---:|---:|---:|---|---|
| OS CPI10-002-30-16 regularização revista de armários.pdf | 1 | 1398 | 24 | OCR_OK | OCR_LOTE_3 |
| OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf | 4 | 7635 | 126 | OCR_OK | OCR_LOTE_3 |
| ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf | 2 | 3985 | 60 | OCR_OK | OCR_LOTE_3 |
| OC PM3_008_02_16 DEJEM.pdf | 1 | 1147 | 26 | OCR_OK | OCR_LOTE_3 |
| Codigo para tipificação de ocorrências 1961_190416104118_001.pdf | 1 | 6098 | 63 | OCR_OK | OCR_LOTE_3 |
| Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf | 1 | 2086 | 65 | OCR_OK | OCR_LOTE_3 |

## Arquivos integrados
- `OS_CPI10_002_30_16_Revista_Armarios.md` (NORMA)
- `OS_CPI10_003_20_17.md` (NORMA)
- `OS_2BPMI_001_30_14.md` (NORMA)
- `OC_PM3_008_02_16_DEJEM.md` (NORMA)
- `Codigos_Tipificacao_Ocorrencias.md` (PROCEDIMENTAL)
- `Codigos_Encerramento_Ocorrencia.md` (PROCEDIMENTAL)

## Arquivos rejeitados
Nenhum dos 6 arquivos gerou leitura ruim/corrompida no PyMuPDF/Tesseract. Todos foram integrados sem rejeições.

## Curadoria aplicada
O JSON de `curadoria_corpus.json` foi atualizado emulando a exclusão do índice com flag `SUBSTITUIDO_POR_OCR_LOTE_3`, impedindo as versões antigas de colidirem durante busca, sem as apagar no Drive.

## Impacto no índice
- chunks antes: 729
- chunks depois: 728
- corpus_ocr antes: 13
- corpus_ocr depois: 19
- diferença líquida: -1 chunk (porque alguns antigos geravam múltiplos chunks inválidos)

## Testes de recuperação
- 5 dos 6 arquivos assumiram as posições `1` ou `2` diretamente com boost.
- `Codigos_Tipificacao_Ocorrencias.md` ranqueou `>10` legitimamente, pois foi vencido por fonte normativamente melhor (o I-40-PM II do Bol G).

## Testes de regressão
- **Validador:** OK
- **Normalizador:** OK
- **Syntax Check (py_compile):** OK
- **Recuperação OCR:** OK (Tudo com SUCESSO)

## Riscos remanescentes
A extração ainda depende da tolerância local de ambiente, mas a Despachadora se mostrou robusta a contornar limitações e manter a coesão sem causar anomalias ou inflacionar os chunks. O pipeline está maduro.

## Próxima etapa recomendada
Avançar com a curadoria de mais lotes `PRECISA_OCR` priorizando relatórios e portarias complexas que ficaram estagnados, ou seguir para Lotes 4 controlados.
