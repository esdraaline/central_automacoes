# Ambiente OCR — Sprint 8.8-d

## Estado inicial
- Branch: main
- Working tree: limpo
- Testes iniciais OK.
- Tesseract e dependências de Python estavam ausentes.

## Instalação do Tesseract
Tesseract foi instalado via `winget` (ID `tesseract-ocr.tesseract`). 

## Caminho detectado
`C:\Program Files\Tesseract-OCR\tesseract.exe`

## Idiomas disponíveis
`eng`, `osd`.
O pacote de idioma `por.traineddata` (português) está **AUSENTE** e a cópia exigiria elevação de privilégio de administrador, portanto não foi instalada nesta sprint.

## Dependências Python
- `pytesseract`: OK
- `pdf2image`: OK
- `pillow`: OK
- `pymupdf`: OK

## Poppler
Como `pdf2image` importou com sucesso, mas OCR não foi rodado, não houve erro em tempo de importação relacionado ao Poppler. Porém, no Windows, o Poppler costuma ser exigido durante a execução de conversão de PDFs. O teste final sobre o Poppler será feito futuramente quando o idioma português for instalado.

## Resultado do test_ambiente_ocr.py
O script detectou o Tesseract no caminho explícito `C:\Program Files\Tesseract-OCR\tesseract.exe`.
Detectou a ausência do idioma 'por'.
Confirmou que todas as bibliotecas Python (pytesseract, pdf2image, pymupdf) estão OK.

## Smoke test de 1 página
Não executado (depende do idioma português disponível).

## Classificação
OCR_BLOQUEADO_POR_AMBIENTE

## Próxima etapa recomendada
- Instalar manualmente o arquivo `por.traineddata` na pasta `C:\Program Files\Tesseract-OCR\tessdata` (requer permissão de administrador).
- Avaliar e possivelmente instalar o `Poppler` for Windows e adicioná-lo ao PATH, caso o `pdf2image` falhe na etapa de conversão de PDF.
