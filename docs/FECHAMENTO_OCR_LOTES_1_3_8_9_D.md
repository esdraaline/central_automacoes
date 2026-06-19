# Fechamento OCR — Lotes 1 a 3 — Sprint 8.9-d

## Estado inicial do ciclo OCR
O pipeline da Despachadora enfrentava dificuldades com PDFs normativos escaneados sem camada de texto (imagem pura), resultando em ausência no índice BM25 ou lixo na recuperação. A infraestrutura baseou-se na instalação do Tesseract OCR (`v5`), uso de `fitz` (PyMuPDF) para renderizar a 150 DPI, e o modelo de idioma `por.traineddata` configurado externamente na raiz do repositório para evitar inchaço no versionamento (arquivos grandes ignorados pelo `.gitignore`).

## Ambiente OCR
- Motor: Tesseract-OCR (v5.5.0, Windows)
- Wrapper Python: `pytesseract`
- Renderização: `pymupdf` (fitz)
- Idioma: `por` (via `TESSDATA_PREFIX` em `saidas/tessdata`)
- Tratamento: Imagens renderizadas convertidas nativamente para strings em RAM, evitando I/O de disco excessivo e arquivos PNG residuais.

## Lote 1
- PDFs processados: 5 (Alta prioridade normativa)
- OCRs integrados: 5
- Curadoria aplicada: 6 entradas físicas suprimidas (`SUBSTITUIDO_POR_OCR_LOTE_1`)
- Impacto: Primeiras integrações limpas, resolvendo o bug do fantasma no índice através da flag de curadoria. Chunks normalizados.

## Lote 2
- PDFs processados: 8 (Prioridade intermediária e complementar)
- OCRs integrados: 8
- Curadoria aplicada: 8 entradas físicas suprimidas (`SUBSTITUIDO_POR_OCR_LOTE_2`)
- Impacto: Calibração fina no motor de BM25 (`test_recuperacao_ocr.py` e `despachadora.py`) com injeção de boost dinâmico focado em siglas curtas, assegurando o ranqueamento top 5 de OCRs normativos.

## Lote 3
- PDFs processados: 6 (Foco em normativas curtas de alto valor)
- OCRs integrados: 6
- Curadoria aplicada: 6 entradas físicas suprimidas (`SUBSTITUIDO_POR_OCR_LOTE_3`)
- Impacto: Homologação definitiva do ciclo. Pipeline rodando sem falhas sistêmicas. Extração precisa de códigos de encerramento e diretrizes operacionais.

## Estado consolidado
- Chunks atuais: 728
- `corpus_ocr` atual: 19
- PDFs físicos substituídos/suprimidos por curadoria: 20
- Recuperação OCR: Totalmente funcional, automatizada e auditável via `test_recuperacao_ocr.py`.
- Testes: BM25/Recuperação (100% Top 5), Normalizador/Validador impecáveis.

## Arquivos principais criados/alterados
- `automacoes/despachadora/nucleo_despachadora/ocr_pdfs_imagem.py`
- `automacoes/despachadora/testes/test_ambiente_ocr.py`
- `automacoes/despachadora/testes/test_recuperacao_ocr.py`
- `automacoes/despachadora/curadoria_corpus.json`
- `automacoes/despachadora/corpus_ocr/*.md` (19 documentos)
- Boost calibrado em `automacoes/despachadora/nucleo_despachadora/despachadora.py`.

## Riscos remanescentes
A recuperação ainda é fortemente baseada em siglas literais. Textos com OCR muito sujo podem sofrer perda de correspondência exata de metadados se não mitigados pelo frontmatter. O limite estrito de 5 a 8 PDFs é salutar para controle humano desse viés.

## PDFs PRECISA_OCR ainda pendentes
Existem ainda pastas com OS/Preleções mais complexas, atas antigas ou escalas. Muitas podem não justificar o esforço, devendo ser priorizadas normas de impacto real e não de histórico fático efêmero.

## Próxima recomendação
Prosseguir com OCR Lote 4, mantendo o limite cirúrgico de 5 a 8 PDFs. Avaliar varredura de pendências para descarte das obsoletas ou efêmeras do backlog.
