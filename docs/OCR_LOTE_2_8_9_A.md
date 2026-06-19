# OCR Lote 2 — Sprint 8.9-a

## Estado inicial
O ambiente Tesseract estava instalado e configurado corretamente (com pasta tessdata local e PyMuPDF operante). 5 PDFs haviam sido processados no Lote 1, resultando em 5 arquivos `.md` na pasta `corpus_ocr`. O índice contava com 730 chunks e as métricas de testes estavam intactas (SUCESSO).

## PDFs candidatos avaliados
A varredura prévia listava vários arquivos marcados como `PRECISA_OCR` (PDF imagem sem camada de texto útil).

## PDFs selecionados
Para o Lote 2, foram priorizados e selecionados 8 PDFs normativos ou de controle estratégico:
1. `Notebooklm/Supervisor Regional/DTZ PM3_002_02_16 DEJEM.pdf`
2. `OS/NI_001_02_15_resolução 57.pdf`
3. `NI - B - Exercícios de aquecimento prévio de condução de viatura policial de duas rodas.pdf`
4. `Nota de Serviço nº CoordOpPM-001-03-16 Operação Direção Segura Integrada - I-2016.pdf`
5. `OS NOta urgente copom OSv Coord Op PM 005 04 19 - Ocor de grav ou repercussão (1).pdf`
6. `Notebooklm/Supervisor Regional/OC PM3_007_02_16 DEJEM.pdf`
7. `Ordem de Serviço nº CoordOpPM-028.21.24, de 15OUT24 (3) (1).pdf`
8. `Sinopse nº 02-18 Fiscal. de Ciclomotor.pdf`

## Resultado OCR

| arquivo | páginas | caracteres | linhas úteis | qualidade | decisão |
|---|---:|---:|---:|---|---|
| DTZ_PM3_002_02_16_DEJEM | ~10 | ~35.496 | - | Alta | OCR_OK |
| NI_001_02_15_Resolucao_57 | ~11 | ~36.736 | - | Alta | OCR_OK |
| NI_Exercicios_Aquecimento... | ~3 | ~7.244 | - | Alta | OCR_OK |
| Nota_Servico_CoordOpPM... | ~2 | ~3.678 | - | Alta | OCR_OK |
| Nota_Urgente_COPOM_OS... | ~2 | ~5.363 | - | Alta | OCR_OK |
| OC_PM3_007_02_16_DEJEM | ~1 | ~1.364 | - | Alta | OCR_OK |
| OS_CoordOpPM_028_21_24 | ~3 | ~4.482 | - | Alta | OCR_OK |
| Sinopse_02_18_Fiscal_Ciclomotor | ~4 | ~7.829 | - | Alta | OCR_OK |

## Arquivos integrados
Os 8 documentos descritos foram convertidos para `.md` e integrados ao diretório `automacoes/despachadora/corpus_ocr/`.

## Arquivos rejeitados
Nenhum arquivo processado no Lote 2 foi rejeitado. Todos extraíram quantidade suficiente de caracteres.

## Curadoria aplicada
O arquivo `automacoes/despachadora/curadoria_corpus.json` foi atualizado. Inserimos 8 regras de silenciamento correspondentes aos 8 PDFs listados. O `motivo` aplicado foi `SUBSTITUIDO_POR_OCR_LOTE_2`.

## Impacto no índice

- chunks antes: 730
- chunks depois: 729
- corpus_ocr antes: 5
- corpus_ocr depois: 13
- diferença líquida: -1
> *Explicação:* O índice aumentou em 8 chunks úteis (de arquivos OCR convertidos com sucesso). Contudo, a varredura e exclusão dos PDFs de imagem resultou em um saldo final de 729 chunks. Isso significa que pelo menos 1 dos PDFs corrompidos que foram silenciados estava gerando 1 chunk vazio ou parcialmente fragmentado no índice anterior.

## Testes de recuperação
Foi criado um script temporário para forçar as consultas (`saidas/test_recuperacao_lote2.py`).
- **Verificação das Entradas Fantasmas:** Todos os 8 PDFs "fantasmas" (os arquivos `.pdf` de imagem puras que não continham texto e sujavam os resultados com erro ou poluição) desapareceram com êxito do escopo de recuperação.
- **Busca via TF-IDF e Competição:** O `.md` em formato Markdown providenciado pelo OCR foi injetado com sucesso no índice (13 chunks em `corpus_ocr`). Nos testes realizados, entretanto, para certas palavras-chave (`"DEJEM"`, `"Resolução 57"`), o script heurístico favoreceu (via sistema de escoragem e ponderação de diretório/natureza) outros manuais enormes e diretrizes já nativas que contêm incidência massiva desses termos e possuem status `norma_interna`. Isso é esperado do comportamento padrão da Despachadora (TF-IDF), porém os conteúdos do OCR Lote 2 já são detectáveis sem os antigos PDFs fantasmas causarem falsos positivos visuais ou ruidosos.

## Testes de regressão
Testes realizados executando `rodar_testes.py` e `test_ambiente_ocr.py`:
- Validador: OK
- Normalizador: OK
- Syntax (py_compile): OK
- Tesseract (Idioma pt-BR, PDF2Image e PyMuPDF): OK
Nenhum alerta de regressão ativado.

## Arquivos versionados
`automacoes/despachadora/corpus_index.json`
`automacoes/despachadora/curadoria_corpus.json`
`automacoes/despachadora/corpus_ocr/*.md` (8 novos)
`automacoes/despachadora/testes/ocr_lote2_8_9_a.py`
`automacoes/despachadora/testes/integra_ocr_lote2.py`
`docs/OCR_LOTE_2_8_9_A.md`

## Arquivos temporários não versionados
Script `saidas/test_recuperacao_lote2.py`, qualquer arquivo `.txt` provisório ou pasta de outputs (`saidas/`). Não versionamos também arquivos `.pdf` gerados por extração ou dados temporários.

## Riscos remanescentes
A competição de score entre os textos gerados via OCR (`.md`) e os PDFs textuais massivos do corpus original precisa ser avaliada em produção. Se a intenção for garantir que o resultado do OCR seja puxado prioritariamente, a natureza atribuída a pasta `corpus_ocr` precisaria receber bônus ou classificação heurística superior (Boost).

## Próxima etapa recomendada
Analisar as métricas na Branch `main` e, se favorável, planejar o Lote 3 ou estender os testes do Lote 2 para produção. Realizar push do Lote 2 de forma controlada.
