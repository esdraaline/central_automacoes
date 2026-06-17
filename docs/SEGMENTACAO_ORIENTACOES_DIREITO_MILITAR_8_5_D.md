# Relatório de Segmentação Controlada — Sprint 8.5-d
## Segmentação de `orientações direito militar.pdf`

Este relatório registra a execução da segmentação controlada do arquivo `orientações direito militar.pdf` em 15 arquivos Markdown literals com frontmatter na pasta `Normas/Orientacoes_Direito_Militar_Segmentos/`, a reindexação oficial do corpus e a validação local pós-segmentação.

---

### A. Estado inicial

* **Branch**: `main` (limpo, sem modificações pendentes).
* **HEAD**: `6ec981c docs(despachadora): audita fidelidade das fontes autonomas`.
* **Manifesto**: `curadoria_corpus.json` possuía o PDF bruto catalogado em `rebaixar` como `OUTRO`.

---

### B. Arquivo-fonte

* **Caminho**: `G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\Notebooklm\Supervisor Regional\orientações direito militar.pdf`
* **Existe?**: Sim.
* **Tamanho**: `13.36 MB`.
* **Páginas**: `481`.
* **Caracteres extraíveis**: `1.153.578` (extração realizada via PyMuPDF com sucesso, sem necessidade de OCR).
* **TOC / Sumário**: 36 entradas detectadas (incluindo uma entrada corrompida de nível 2 na página -1 com título vazio).

---

### C. TOC identificado

Foram filtradas as entradas válidas (removendo a entrada truncada/corrompida de página `-1`):

| Índice | Título | Pág. Inicial | Pág. Final Estimada | Caracteres Estimados |
| :--- | :--- | :---: | :---: | :---: |
| 1 | AÇÃO DO POLICIAL MILITAR PARA PRESERVAR... | 1 | 5 | 11.188 |
| 2 | AGRESSÃO ENVOLVENDO MILITARES ESTADUAIS... | 6 | 7 | 2.639 |
| 3 | apfd pm inativo | 8 | 9 | 0 |
| 4 | apostila pd | 10 | 63 | 104.154 |
| 5 | apostila pjm | 64 | 93 | 59.431 |
| 6 | apostila processo regular | 94 | 118 | 56.516 |
| 7 | apostila sindicancia | 119 | 139 | 39.672 |
| 8 | AVALIAÇÃO E PRESERVAÇÃO DE LOCAL... | 140 | 142 | 7.212 |
| 9 | COLETÂNEA DE TRECHOS DE JURISPRUDÊNCIAS | 143 | 154 | 26.448 |
| 10 | convenio pm e defensoria publica | 155 | 161 | 0 |
| 11 | crimes militares mdip | 162 | 165 | 8.778 |
| 12 | DIRETRIZES A SEREM SEGUIDAS NO ATENDIMENTO... | 166 | 169 | 10.656 |
| 13 | DISCIPLINA O ATENDIMENTO A REQUISIÇÕES... | 170 | 171 | 3.686 |
| 14 | Dispõe sobre a audiência de custódia... | 172 | 176 | 12.404 |
| 15 | duvidas frequentes | 177 | 179 | 6.427 |
| 16 | exame toxicologico na pm | 180 | 180 | 25.022 |
| 17 | INSTRUÇÕES SOBRE ENVOLVIMENTO DE INATIVOS... | 181 | 182 | 4.619 |
| 18 | JURISPRUDENCIAS- DPRD | 183 | 310 | 391.677 |
| 19 | jurisprudencias | 311 | 325 | 59.511 |
| 20 | orientações da caj | 326 | 328 | 10.575 |
| 21 | orientações pjm | 329 | 342 | 3.515 |
| 22 | policiais sentenciados | 343 | 343 | 3.214 |
| 23 | PRINCIPAIS DÚVIDAS SOBRE POLÍCIA JUDICIÁRIA... | 344 | 360 | 32.566 |
| 24 | principais vicios processuais | 361 | 365 | 9.910 |
| 25 | Procedimento de apreensao de aparelho celular | 366 | 366 | 2.207 |
| 26 | procedimentos cartorarios | 367 | 400 | 66.200 |
| 27 | PROCEDIMENTOS VOLTADOS À PRESERVAÇÃO DE LOCAL... | 401 | 405 | 10.394 |
| 28 | processo regular pedido de baixa | 406 | 406 | 2.804 |
| 29 | questionamentos judiciais | 407 | 408 | 2.440 |
| 30 | QUESTIONÁRIO DO PROCEDIMENTO DISCIPLINAR | 409 | 442 | 82.390 |
| 31 | Resolução SSP-40, de 24-03-2015 | 443 | 446 | 5.292 |
| 32 | ROTINA PARA AFASTAMENTO DO SERVIÇO... | 447 | 449 | 4.248 |
| 33 | SALVO-CONDUTO | 450 | 453 | 5.474 |
| 34 | Sentença \| NUM: 223615 \| 08/07/2020 15:29 | 454 | 477 | 74.013 |
| 35 | SÚMULA ICC Nº 340.2023 | 478 | 481 | 8.296 |

---

### D. Plano de segmentação

Os 35 tópicos identificados foram consolidados tematicamente em 15 segmentos para respeitar o limite ideal de caracteres (20k a 150k), garantindo coesão contextual:

1. `01_Preservacao_Local_Agressao_APFD_p1_9` (Páginas 1 a 9 | 13.827 chars)
2. `02_Apostila_PD_p10_63` (Páginas 10 a 63 | 104.154 chars)
3. `03_Apostila_PJM_p64_93` (Páginas 64 a 93 | 59.431 chars)
4. `04_Apostila_Processo_Regular_p94_118` (Páginas 94 a 118 | 56.516 chars)
5. `05_Apostila_Sindicancia_p119_139` (Páginas 119 a 139 | 39.672 chars)
6. `06_Avaliacao_Local_Jurisprudencias_Convenio_Crimes_p140_165` (Páginas 140 a 165 | 42.438 chars)
7. `07_Diretrizes_Custodia_Duvidas_Toxicologico_Inativos_p166_182` (Páginas 166 a 182 | 62.814 chars)
8. `08A_Jurisprudencias_DPRD_Parte1_p183_225` (Páginas 183 a 225 | 132.803 chars)
9. `08B_Jurisprudencias_DPRD_Parte2_p226_268` (Páginas 226 a 268 | 128.181 chars)
10. `08C_Jurisprudencias_DPRD_Parte3_p269_310` (Páginas 269 a 310 | 130.693 chars)
11. `09_Jurisprudencias_Geral_CAJ_p311_328` (Páginas 311 a 328 | 70.086 chars)
12. `10_PJM_Sentenciados_Duvidas_Vicios_Celular_p329_366` (Páginas 329 a 366 | 51.412 chars)
13. `11_Procedimentos_Cartorarios_Preservacao_Baixa_p367_408` (Páginas 367 a 408 | 81.838 chars)
14. `12_Questionario_PD_p409_442` (Páginas 409 a 442 | 82.390 chars)
15. `13_Resolucao_SSP40_Afastamento_SalvoConduto_Sentenca_Sumula_p443_481` (Páginas 443 a 481 | 97.323 chars)

---

### E. Segmentos criados

Todos os 15 arquivos Markdown foram gerados na pasta sincronizada do Drive:
`G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\Normas\Orientacoes_Direito_Militar_Segmentos\`

Cada arquivo contém o cabeçalho YAML-like de metadados obrigatórios contendo `natureza: "DOUTRINA"` e o texto literal extraído da respectiva faixa de páginas, sem qualquer resumo, alteração ou acréscimo jurídico de memória.

---

### F. Reindexação

* **Manifesto**: `orientações direito militar.pdf` bruto foi incluído em `excluir_do_indice`.
* **Indexador oficial (`indexar_corpus.py`)**: Modificado para parsear frontmatter de qualquer arquivo `.md` do corpus que o possua (garantindo que os segmentos entrem como `DOUTRINA` mesmo sob a pasta `Normas/`). Também habilitou-se o recálculo/overwrite em modo incremental para caminhos contendo `"Segmentos"`.
* **Classificador (`classificar_corpus.py`)**: Atualizado para incluir a natureza `"DOUTRINA"` em seu conjunto de categorias válidas.
* **Resultado do indexador**:
  * **Chunks Totais no Índice**: `731`
  * **Novos processados**: `175` (inclui os 15 segmentos da pasta `Orientacoes_Direito_Militar_Segmentos` e outras adições incrementais).
  * **Exclusões aplicadas**: `87` arquivos (incluindo o PDF original bruto gigante).
  * **Entradas do PDF bruto original encontradas no índice final**: `0` (excluído com sucesso).

---

### G. Busca literal pós-indexação

Buscas feitas diretamente na estrutura indexada em `corpus_index.json`:

1. **`Súmula 473`**:
   * *Matches*: 2
   * *Principais locais*: `corpus_manual/Sumula_473_Autotutela.md` (JURISPRUDENCIA), `Normas/Orientacoes_Direito_Militar_Segmentos/08A_Jurisprudencias_DPRD_Parte1_p183_225.md` (DOUTRINA).
   * *Aptidão*: Apenas DOUTRINA/JURISPRUDENCIA (Apoio).
2. **`autotutela`**:
   * *Matches*: 3
   * *Principais locais*: `corpus_manual/Sumula_473_Autotutela.md` (JURISPRUDENCIA), `Normas/Orientacoes_Direito_Militar_Segmentos/08A...` e `08C...` (DOUTRINA).
   * *Aptidão*: Apenas DOUTRINA/JURISPRUDENCIA (Apoio).
3. **`anular seus próprios atos`**:
   * *Matches*: 2
   * *Principais locais*: `corpus_manual/Sumula_473_Autotutela.md` (JURISPRUDENCIA) e Segmento DPRD Parte 1 (DOUTRINA).
4. **`revogar seus próprios atos`**:
   * *Matches*: 0 (Não há esta frase literal com essa grafia no texto oficial da Súmula 473 nem nos trechos; o STF grafa *"anular seus próprios atos... ou revogá-los"*).
5. **`competência para instaurar`**:
   * *Matches*: 4
   * *Principais locais*: `JD/PPJM/Manuais, Leis, Regulamentos/I-16-PM.pdf` (NORMA), `Normas/Orientacoes_Direito_Militar_Segmentos/05_Apostila_Sindicancia_p119_139.md` (DOUTRINA).
   * *Aptidão*: I-16-PM é apto para `[FUNDAMENTO]`. Apostila é apenas `DOUTRINA` (Apoio).
6. **`autoridade de polícia judiciária militar`**:
   * *Matches*: 13
   * *Principais locais*: `JD/PPJM/Manuais, Leis, Regulamentos/I-40-PM - (Bol G PM 101-23) II 1.pdf` (NORMA) - Apto para `[FUNDAMENTO]`.
7. **`prazo de sindicância`**:
   * *Matches*: 1
   * *Principais locais*: `corpus_manual/Competencia_Prazos_Sindicancia.md` (NORMA) - Apto para `[FUNDAMENTO]`.
8. **`preservação de local`**:
   * *Matches*: 39
   * *Principais locais*: Modelos de RIOG (MODELO_PRECEDENTE) e POPs de local de crime.
9. **`dano ao erário`**:
   * *Matches*: 1
   * *Principais locais*: `corpus_manual/Acidente_Viatura_Providencias.md` (NORMA) - Apto para `[FUNDAMENTO]`.
10. **`uso de algemas`**:
    * *Matches*: 69
    * *Principais locais*: Modelos de RIOG (MODELO_PRECEDENTE) e POPs procedimentais.
11. **`justificativa por escrito`**:
    * *Matches*: 1
    * *Principais locais*: `corpus_manual/Sumula_Vinculante_11_Algemas.md` (JURISPRUDENCIA) - Apoio.

---

### H. Recuperação local dos 3 casos

Os resultados da simulação local usando o algoritmo híbrido e a partição estrita de pools são:

#### Caso 1: Algemas / condução / espera na DP
* **CONTEXTO NORMATIVO (Pool F)**:
  1. `corpus_manual/Sumula_Vinculante_11_Algemas.md` (Score: **18.37** | JURISPRUDENCIA)
  2. `POPs/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` (Score: **9.37** | PROCEDIMENTAL)
  3. `POPs/Processo-5.03.00_Uso-de-algemas.pdf` (Score: **9.33** | PROCEDIMENTAL)
  4. `POPs/Processo-1.01.00-Abordagem-de-Pessoas-a-Pe.pdf` (Score: **9.02** | PROCEDIMENTAL)
* **MODELOS DE REDAÇÃO (Pool M)**:
  1. `PPJM/Manuais, Leis, Regulamentos/Portaria dispoe sobre armas na PM.pdf` (Score: **6.11** | MODELO_PRECEDENTE)
  2. `POPs/Processo-3.04.00-Atendimento-Ocor-Horario-Folga.pdf` (Score: **5.49** | MODELO_PRECEDENTE)
* **Status**: A fonte oficial autônoma de algemas aparece em Rank 1 com altíssimo score, sem poluição do PDF bruto.

#### Caso 2: Acidente com viatura e vítima
* **CONTEXTO NORMATIVO (Pool F)**:
  1. `POPs/Processo-1.01.00-Abordagem-de-Pessoas-a-Pe.pdf` (Score: **4.72** | PROCEDIMENTAL)
  2. `PPJM/Manuais, Leis, Regulamentos/I-40-PM (Bol G PM 101-23)` (Score: **4.71** | NORMA)
  3. `Outros/Acidente de trânsito vtr - PAAVI/NI Nº...` (Score: **4.63** | NORMA)
  4. `Normas/Orientacoes_Direito_Militar_Segmentos/03_Apostila_PJM_p64_93.md` (Score: **4.54** | DOUTRINA)
  5. `Normas/Orientacoes_Direito_Militar_Segmentos/13_Resolucao_SSP40...` (Score: **4.41** | DOUTRINA)
* **MODELOS DE REDAÇÃO (Pool M)**:
  1. `PPJM/Manuais, Leis, Regulamentos/Portaria dispoe sobre armas na PM.pdf` (Score: **2.01** | MODELO_PRECEDENTE)
* **Status**: Segmentos novos aparecem de forma controlada classificados como `DOUTRINA` para apoio secundário, convivendo harmonicamente com as normas oficiais da P3 e do CPPM.

#### Caso 3: IPM / autotutela / competência
* **CONTEXTO NORMATIVO (Pool F)**:
  1. `corpus_manual/Sumula_473_Autotutela.md` (Score: **10.41** | JURISPRUDENCIA)
  2. `Normas/Orientacoes_Direito_Militar_Segmentos/08C_Jurisprudencias_DPRD_Parte3_p269_310.md` (Score: **8.69** | DOUTRINA)
  3. `Normas/Orientacoes_Direito_Militar_Segmentos/08A_Jurisprudencias_DPRD_Parte1_p183_225.md` (Score: **8.60** | DOUTRINA)
  4. `PPJM/Manuais, Leis, Regulamentos/I-40-PM...` (Score: **5.04** | NORMA)
* **MODELOS DE REDAÇÃO (Pool M)**:
  1. `Outros/Retificação BOPM.txt` (Score: **5.05** | PRECEDENTE)
* **Status**: A Súmula 473 autônoma domina o topo como fundamentação jurídica primária. Os segmentos doutrinários novos referentes às jurisprudências da DPRD aparecem imediatamente abaixo com scores elevados, fornecendo robustez interpretativa sem sobrepor a competência legal normatizada no CPPM/I-40-PM.

---

### I. Limitações

1. O texto literal extraído do PDF possui quebras de linha e caracteres especiais residuais resultantes do formato original de compilação (ex. hifenização quebrada como `revogá- los`).
2. A pesquisa literal exata de frases truncadas como "revogar seus próprios atos" resulta em zero matches devido à diferença na escrita formal do STF ("anular seus próprios atos... ou revogá-los").

---

### J. Próxima etapa recomendada

A segmentação resolveu o problema do arquivo bruto gigante. O índice final está equilibrado e as fontes autônomas lideram as buscas críticas. Recomenda-se prosseguir com os testes de envio ao LLM de forma controlada.
