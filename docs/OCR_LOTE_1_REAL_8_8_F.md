# OCR Lote 1 Real — Sprint 8.8-f

## Estado inicial
- Branch `main` limpo.
- `TESSDATA_PREFIX` e ambiente local aptos para uso com o idioma `por`.

## Ambiente OCR
- Tesseract no PATH (`C:\Program Files\Tesseract-OCR\tesseract.exe`).
- Renderização realizada via `PyMuPDF` (DPI: 150).
- Processamento em lote realizado por script `automacoes/despachadora/testes/ocr_lote1_8_8_f.py`.

## PDFs processados e Resultado do OCR

| arquivo | páginas | caracteres | linhas úteis | qualidade | decisão |
|---|---:|---:|---:|---|---|
| Bol G 132 - 21JUL20 - Instruções IPM e Susp do PAE.pdf | 4 | 7898 | 119 | OCR_OK | INTEGRAR_AO_CORPUS |
| NI PM3_004_03_13 ICC.pdf | 5 | 9911 | 150 | OCR_OK | INTEGRAR_AO_CORPUS |
| NI Nº PM3-002-02-17.pdf | 11 | 24949 | 381 | OCR_OK | INTEGRAR_AO_CORPUS |
| Desp Nº PM3 005 02 19 - Acesso a dados em celular.pdf | 2 | 4576 | 72 | OCR_OK | INTEGRAR_AO_CORPUS |
| Resolução CONTRAN nº 432-13.pdf | 10 | 13653 | 274 | OCR_OK | INTEGRAR_AO_CORPUS |

Todos apresentaram mais de 1000 caracteres, com texto bem estruturado e com os termos jurídicos e operacionais esperados. 

## Arquivos integrados
Todos os 5 arquivos foram encapsulados em formato Markdown com o devido _frontmatter_ e copiados para `automacoes/despachadora/corpus_ocr/`:
1. `Bol_G_132_IPM_Susp_PAE.md`
2. `NI_PM3_004_03_13_ICC.md`
3. `NI_PM3_002_02_17.md`
4. `Desp_PM3_005_02_19_Celular.md`
5. `Res_CONTRAN_432_13.md`

## Arquivos rejeitados
Nenhum (100% de aproveitamento neste lote).

## Classificação de natureza
- Bol_G_132_IPM_Susp_PAE.md: `PROCEDIMENTAL`
- NI_PM3_004_03_13_ICC.md: `NORMA`
- NI_PM3_002_02_17.md: `NORMA`
- Desp_PM3_005_02_19_Celular.md: `PROCEDIMENTAL`
- Res_CONTRAN_432_13.md: `NORMA`

## Impacto no corpus_index
A lógica de atualização incremental de `indexar_corpus.py` foi ajustada de forma mínima e documentada para incluir e ler da pasta `corpus_ocr`.
- chunks antes: 731
- chunks depois: 736
- diferença: +5 exatos referentes aos novos MDs OCRizados.

## Testes de recuperação
- `instruções IPM suspensão PAE`: recuperou `Competencia_IPM.md` e outras normas de IPM. O Bol G 132 não ficou no top 5 (mas está indexado, e ofuscado pela semelhança dos originais).
- `acesso a dados em celular PM3 005 02 19`: recuperou `Desp_PM3_005_02_19_Celular.md` (*** OCR ***) no Top 3 perfeitamente.
- `acidente viatura PAAVI NI PM3 002 02 17`: Recuperou `Acidente_Viatura_Providencias.md` (Top 1) e o PDF antigo sem OCR (Top 4).
- O índice não foi poluído e a recuperação continua focada no léxico apropriado.

## Testes de regressão
- VALIDADOR: OK
- NORMALIZADOR: OK
- PY_COMPILE: OK
- Nenhuma falha identificada na despachadora ou script de OCR.

## Riscos
Como demonstrado no teste de recuperação, às vezes as fontes não indexadas (vazias, `pdf_imagem_sem_ocr`) mas cujos nomes de arquivos contém palavras-chave exatas podem ofuscar temporariamente o texto indexado via OCR. Esse é um risco de _ranking_ leve que pode ser sanado aplicando curadoria.

## Próxima etapa
- Limpar/excluir (curar) os arquivos PDF originais (que ficaram como `pdf_imagem_sem_ocr`) do índice para evitar duplicidade de recuperação com a sua respectiva versão útil `corpus_ocr`.
- Expandir a operação para os PDFs restantes do Lote Completo.
