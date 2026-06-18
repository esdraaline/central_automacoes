# OCR Lote 1 — Sprint 8.8-b

## Estado inicial
- **Branch:** `main`
- **Commit:** `b3ca247 chore(despachadora): organiza testes de regressao`
- **Working Tree:** Limpo
- **Testes de Regressão:** OK (Validador, Normalizador e Sintaxe)
- **Status do Índice:** Estável, nenhum documento novo.

## PDFs pendentes avaliados
Foram avaliados os documentos listados com a classificação `PRECISA_OCR` na Varredura da Sprint 8.5, localizados em sua maioria no diretório `G:\Meu Drive\...\Skill despachadora de Docs\`. Havia 51 arquivos pendentes, majoritariamente PDFs não-pesquisáveis (apenas imagem).

## Critério de seleção
A seleção seguiu as diretrizes de **Alta Prioridade**: normas permanentes, instruções PM, POPs, NIs e orientações relacionadas a IPMs, acidentes com viaturas e condução de ocorrências, evitando B.O.s e materiais fáticos transitórios.

## PDFs selecionados para OCR
1. `JD/Arquivo/2020/Bol G 132 - 21JUL20 - Instruções IPM e Susp do PAE.pdf`
2. `Normas/NI PM3_004_03_13 ICC.pdf`
3. `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf`
4. `P3/Outros/Preleção/Desp Nº PM3 005 02 19 - Acesso a dados em celular.pdf`
5. `P3/OS/ODS/Resolução CONTRAN nº 432-13.pdf`

## Resultado do OCR

| arquivo | páginas | caracteres | qualidade | decisão |
|---|---:|---:|---|---|
| `Bol G 132 - 21JUL20 - Instruções IPM...` | 4 | 0 | OCR_RUIM | NAO_INDEXAR |
| `NI PM3_004_03_13 ICC.pdf` | 5 | 0 | OCR_RUIM | NAO_INDEXAR |
| `NI Nº PM3-002-02-17.pdf` | 11 | 0 | OCR_RUIM | NAO_INDEXAR |
| `Desp Nº PM3 005 02 19 - Acesso...` | 2 | 0 | OCR_RUIM | NAO_INDEXAR |
| `Resolução CONTRAN nº 432-13.pdf` | 10 | 0 | OCR_RUIM | NAO_INDEXAR |

> [!WARNING]
> **FALHA TÉCNICA (Falta de Dependências):** O ambiente atual (Windows do usuário) não possui o pacote executável do **Tesseract OCR**, nem as bibliotecas `pytesseract` ou `pdf2image` instaladas globalmente. As ferramentas internas nativas (PyMuPDF / pypdf) não conseguem ler PDFs de imagem, extraindo exatamente 0 caracteres legíveis. Em cumprimento rígido à regra *"NÃO indexar OCR ruim"*, o processo foi interrompido com segurança.

## Documentos integrados ao corpus
Nenhum.

## Documentos rejeitados e motivo
Todos os 5 arquivos foram temporariamente rejeitados do índice porque a extração resultou em `0` caracteres (ausência do motor OCR Tesseract). A indexação de conteúdos vazios ou corrompidos violaria as diretrizes de segurança da Despachadora.

## Impacto no índice
- **chunks antes:** 674 (Mantido igual ao final da 8.5)
- **chunks depois:** 674
- **diferença:** 0

## Teste de recuperação
Como nenhum texto útil foi extraído e o índice permaneceu inalterado (`corpus_index.json` intacto), os testes de recuperação antes/depois apresentaram 100% de isometria (mesmos resultados anteriores sem poluição).

## Testes de regressão
```powershell
>>> TESTE DO VALIDADOR
VALIDADOR: OK

>>> TESTE DO NORMALIZADOR
NORMALIZADOR: OK

>>> TESTE DE SINTAXE (PY_COMPILE)
PY_COMPILE: OK
```
**Resultado:** SUCESSO. Nenhuma regressão foi introduzida no núcleo da Despachadora.

## Riscos remanescentes
- A ausência de motor Tesseract impede a automação do OCR de todos os 51 PDFs prioritários.
- Esses documentos podem conter bases fundamentais não recuperadas pela IA.

## Próxima recomendação
Instalação oficial das dependências de OCR na máquina hospedeira (`pip install pytesseract pdf2image` + Instalação do Binário do Tesseract-OCR no Windows), seguida de OCR Lote 2; ou, se a infraestrutura for bloqueada, conversão assistida externa dos 51 PDFs e importação apenas do arquivo `.txt`.
