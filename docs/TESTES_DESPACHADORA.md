# Testes da Despachadora

## Como rodar

python automacoes/despachadora/testes/rodar_testes.py

## Testes incluídos

- Validador pós-Gemini
- Normalizador determinístico
- py_compile dos módulos principais

## O que estes testes não fazem

- Não chamam Gemini
- Não rodam OCR
- Não reindexam corpus
- Não testam deploy

## Quando rodar

- Antes de push
- Após alterações em despachadora.py
- Após alteração no normalizador ou validador
