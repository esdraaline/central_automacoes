# Ambiente OCR — Sprint 8.8-e

## Estado inicial
- Branch: main
- Working tree: limpo
- OCR estava bloqueado por falta de pacote de idioma português (por).
- `pdf2image`, `pytesseract`, `pymupdf` instalados, Tesseract instalado no PATH padrão.

## Instalação do idioma português
Arquivo `por.traineddata` (15MB) foi baixado da fonte oficial do Tesseract para a pasta ignorada local: `saidas/tessdata/por.traineddata`.

## TESSDATA_PREFIX local
Foi testado e configurado o uso da variável de ambiente `TESSDATA_PREFIX` apontando para a pasta local `C:\Projetos\central_automacoes\saidas\tessdata`. O Tesseract reconheceu a pasta corretamente e rodou sem exigir privilégios de administrador.

## Resultado do tesseract --list-langs
Com a variável configurada, o Tesseract retornou `por` como idioma disponível.

## Poppler / conversão PDF-imagem
`POPPLER_AUSENTE`
A conversão via `pdf2image` falhou acusando falta do Poppler no PATH do Windows. Como alternativa segura, utilizamos o `PyMuPDF` (fitz), que renderizou a página do PDF para imagem (PNG) com sucesso.

## Smoke test 1 página
O teste de OCR foi rodado sobre a 1ª página do arquivo piloto ("Bol G 132..."):
- Caracteres extraídos: 3560
- Linhas úteis: 51
- Qualidade do texto: Excelente, capturando corretamente todos os acentos, formatação de título e termos jurídicos esperados (ex: INQUÉRITOS POLICIAIS MILITARES, Portaria).

## Classificação do OCR
`OCR_OK`

## Decisão
`AMBIENTE_APTO_PARA_OCR_LOTE_1`

## Próxima etapa recomendada
- Integrar a configuração do `TESSDATA_PREFIX` local e o uso do `PyMuPDF` para conversão (no lugar de `pdf2image` ou ajustando o fluxo) no script final de OCR.
- Avançar para a execução do OCR no Lote 1 de PDFs.
