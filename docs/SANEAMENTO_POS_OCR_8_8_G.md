# Saneamento pós-OCR — Sprint 8.8-g

## Estado inicial
- branch `main` limpo.
- último commit `6597d0b chore(despachadora): integra OCR lote 1 ao corpus`.
- índice contendo entradas fantasmas (PDFs vazios com o nome e metadados que ofuscam os novos `.md` com OCR real).

## Entradas fantasmas encontradas
Foram identificadas 6 entradas fantasmas que representavam os originais (sendo uma duplicada no sistema de pastas do corpus original):
1. `Arquivo/2020/Bol G 132 - 21JUL20 - Instruções IPM e Susp do PAE.pdf`
2. `OS/NI_002_02_17 acidente de trânsito com viatura/NI Nº PM3-002-02-17 - Acidente Vtr.pdf`
3. `OS/ODS/Resolução CONTRAN nº 432-13.pdf`
4. `Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf`
5. `Outros/Preleção/Desp Nº PM3 005 02 19 - Acesso a dados em celular.pdf`
6. `NI PM3_004_03_13 ICC.pdf`

## Curadoria aplicada
As 6 entradas identificadas foram adicionadas ao `automacoes/despachadora/curadoria_corpus.json` sob a chave `"excluir_do_indice"`.
- **motivo:** `SUBSTITUIDO_POR_OCR_LOTE_1`
- **substituido_por:** link para a respectiva versão processada em `corpus_ocr`.

*Nota: Os arquivos originais (PDFs físicos) foram preservados intactos no seu diretório original, e apenas bloqueados do banco.*

## Impacto no índice
- chunks antes: 736
- chunks depois: 730
- diferença: -6 exatos referentes aos 6 fantasmas ocultados via curadoria.

## OCRs preservados
A contagem confirma que os 5 arquivos convertidos em `.md` (`corpus_ocr/`) continuam ativamente sendo indexados, providenciando o conteúdo para o motor de busca sem as falsas "sombras".

## Testes de recuperação
- **instruções IPM suspensão PAE:** mantém as normas competentes.
- **acidente viatura PAAVI NI PM3 002 02 17:** os dois fantasmas da NI PM3-002 sumiram das primeiras posições. Documentos manuais apropriados e demais diretrizes de acidente dominaram o topo.
- **acesso a dados em celular PM3 005 02 19:** `Desp_PM3_005_02_19_Celular.md` (*** OCR ***) segue ranqueado no topo (Top 2) sem competir com a antiga folha em branco.
- **resolução contran 432 etilômetro alcoolemia:** `Res_CONTRAN_432_13.md` (*** OCR ***) subiu para o Top 5 no lugar exato do seu antigo fantasma vazio.
As poluições de metadados vazios foram eliminadas com sucesso.

## Testes de regressão
- VALIDADOR: OK
- NORMALIZADOR: OK
- PY_COMPILE: OK
Nenhum componente principal da Despachadora sofreu impacto negativo.

## Riscos remanescentes
Quase nenhum para o Lote 1. O pipeline de OCR com exclusão em curadoria demonstrou-se limpo, seguro e totalmente não destrutivo em relação ao repositório fonte.

## Próxima etapa recomendada
- Expandir a operação (com a dupla "geração de MD + silenciamento do Original") para os 46 PDFs restantes.
