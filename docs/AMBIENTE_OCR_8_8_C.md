# Ambiente OCR — Sprint 8.8-c

## Estado inicial
- Branch: main
- Working tree: limpo
- Último commit: 54e98b9 chore(despachadora): executa OCR piloto do corpus
- Testes: OK (Validador, Normalizador, Sintaxe)

## Dependências verificadas
- **Tesseract**: Não encontrado no PATH.
- **pytesseract**: Não instalado.
- **pdf2image**: Não instalado.
- **pymupdf**: Instalado (OK).

## Resultado do Tesseract
Tesseract não está instalado/configurado.

## Smoke test
Não executado.

## Qualidade do OCR
Não avaliada.

## Decisão
- OCR_BLOQUEADO_POR_AMBIENTE

Motivo: Tesseract não instalado/configurado.

## Próximo passo
Instalar Tesseract OCR para Windows.
Adicionar o executável ao PATH.
Confirmar idioma português `por.traineddata`.
Reabrir terminal/IDE.
Rodar `tesseract --version`.
