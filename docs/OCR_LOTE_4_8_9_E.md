# OCR Lote 4 (Sprint 8.9-e)

## Resumo Executivo
Neste lote, foram selecionados 5 PDFs identificados como `PRECISA_OCR` na varredura de pendências, com foco em normas e regulamentos municipais/institucionais.

## Arquivos Processados
1. `P1/1415-1993 código de postura valparaiso.PDF` (16 páginas) - Sucesso, 28k caracteres, status `NORMA`.
2. `P1/1870-1994 decreto regulamenta codigo de postura valparaiso.PDF` (2 páginas) - Sucesso, 2k caracteres, status `NORMA`.
3. `P1/número codigo sei do batalhão e cpi.pdf` (1 página) - Ruim, caracteres ilegíveis, descartado.
4. `P3/Outros/Projeto VIDA/OFÍCIO DA CPI 10 – 2º RAJ - Projeto V.I.D.A.pdf` (2 páginas) - Falha, arquivo não encontrado na pasta/caminho (possível erro de codificação de caractere).
5. `P3/Outros/Acidente de trânsito vtr - PAAVI/MSG17-152- Circular.pdf` (1 página) - Fático/Descartável. Apenas aponta para a `NI PM3-002-02-17`, que já consta íntegra no índice.

## Ações Realizadas
1. **OCR Lote 4:** Processamento via Tesseract (psm 6, idioma português).
2. **Integração `corpus_ocr`:** Inclusão de `Lei_1415_93_Codigo_Postura_Valparaiso.md` e `Decreto_1870_94_Codigo_Postura_Valparaiso.md` (`OCR_MEDIANO`).
3. **Curadoria Aplicada:** Registrados em `curadoria_corpus.json` sob a tag `SUBSTITUIDO_POR_OCR_LOTE_4` para silenciar os PDFs fantasmas.
4. **Reindexação:** O corpus manteve a quantidade total de 728 chunks. O `corpus_ocr` subiu de 19 para 21 documentos.
5. **Calibração/Testes:** Executado o `test_recuperacao_ocr.py`. Para os novos casos de postura municipal, outras referências normativas no acervo (como Convênios e Manuais Estaduais) dominaram o Top 5 da busca original. Conforme regra, **nenhuma alteração no modelo de recuperação (BM25) ou no peso foi feita**.

## Próximos Passos
* Push da Sprint 8.9-e para a `main`.
* Continuar varredura para o próximo Lote OCR, caso existam mais documentos de valor normativo e operacional na lista restante do relatório de Skill.
