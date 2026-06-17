# Relatório de Curadoria de Corpus — Sprint 8.5-b2

Este relatório documenta a primeira curadoria real, controlada e reversível aplicada ao corpus da **Despachadora do Comandante** no projeto `C:\Projetos\central_automacoes`, realizada em 17 de junho de 2026.

---

## A. Estado Inicial

Antes do início da sprint, o estado do repositório git foi verificado e confirmado como limpo:
* **Últimos commits:**
  * `2036f68 feat(despachadora): estabiliza recuperação híbrida e validador pós-Gemini`
  * `839cee8 docs(despachadora): registra auditoria e varredura do corpus`
* **Arquivos pendentes no git:** Nenhum (working tree limpa).
* **Diagnóstico base do corpus:** 674 chunks indexados anteriormente, contendo poluição de arquivos fáticos simples de casos concretos (oitivas, termos, dano de viaturas), arquivos de convites/ofícios simples e arquivos consolidadores duplicados do NotebookLM.

---

## B. Manifesto Criado

Criou-se o arquivo de manifesto de curadoria em [curadoria_corpus.json](file:///c:/projetos/central_automacoes/automacoes/despachadora/curadoria_corpus.json). Ele define de forma auditável e reversível as regras de exclusão, reclassificação e rebaixamento do indexador através de padrões de caminho e nome de arquivos.

```json
{
  "excluir_do_indice": [
    {
      "padrao_arquivo": "P1/Anos anteriores/2021/Ofícios apresentação 3 cia/",
      "motivo": "Ofícios simples de apresentação sem valor normativo ou de modelo"
    },
    {
      "padrao_arquivo": "P1/Conseg/Oficios Convites Conseg/",
      "motivo": "Ofícios de convites para reuniões do Conseg de baixo valor modelo e sem valor normativo"
    },
    ...
    {
      "padrao_arquivo": "Notebooklm/Supervisor Regional/Vademecum.pdf",
      "motivo": "Fonte original gigante já segmentada e indexada no corpus"
    }
  ],
  "reclassificar": [
    {
      "padrao_arquivo": "Relatório Sindicancia PT .40 -  19FEV18.docx",
      "natureza_nova": "MODELO_PRECEDENTE",
      "motivo": "Modelo estruturado de sindicância"
    },
    ...
  ],
  "rebaixar": [
    {
      "padrao_arquivo": "Notebooklm/Supervisor Regional/orientações direito militar.pdf",
      "natureza_nova": "OUTRO",
      "motivo": "Compilado de orientações amplo e ainda não segmentado"
    }
  ]
}
```

---

## C. Alterações no Indexador

A lógica do script [indexar_corpus.py](file:///c:/projetos/central_automacoes/automacoes/despachadora/nucleo_despachadora/indexar_corpus.py) foi alterada para dar suporte nativo ao manifesto:
1. **Carregamento:** Carrega o arquivo `curadoria_corpus.json` do diretório pai.
2. **Filtragem e Alteração:** Aplica as regras de exclusão, reclassificação e rebaixamento sobre a lista mesclada de chunks (`existing` + `new_entries`), garantindo que chunks legados também sofram a curadoria.
3. **Estatísticas:** Coleta estatísticas detalhadas de itens excluídos, reclassificados e rebaixados.
4. **UTF-8 no Console:** Força stdout/stderr a utilizarem UTF-8 para evitar falhas de decodificação de caracteres gráficos no Windows terminal (ex: `UnicodeEncodeError` no caractere `═`).

*Nenhuma modificação foi realizada em `despachadora.py` nesta sprint, preservando o código de produção intacto.*

---

## D. Curadoria Aplicada — Exclusões

Um total de **53 chunks** legados foram excluídos da base indexada, além de **57 arquivos novos** detectados no Google Drive que foram bloqueados antes de entrarem no índice.

### Principais arquivos excluídos da indexação (exemplos):
* **Ofícios simples/Convites:**
  * `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Aracanguá.docx` (e outros 21 arquivos semelhantes)
  * `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Associação Comercial...` (e outros 11 convites semelhantes)
* **Documentos Pessoais/Financeiros:**
  * Holerites e demonstrativos pessoais na pasta `P1/Holerites` e `P1/Holerites Bonus DEJEM`
* **Casos Fáticos Concretos / Peças Judiciais Específicas:**
  * `JD/2025/Dano vtr 504/Despacho Dano VTR 504.pdf`
  * `JD/2025/Dano vtr 504/Parte Dano vtr 504 (1).pdf`
  * `JD/Arquivo/2022/Croqui Diego.pdf`
  * `JD/Arquivo/2023/croqui cristiano.pdf`
  * `JD/Arquivo/2024/Inquirição Cb PM Gustavo.docx`
  * `JD/Arquivo/2024/Termo de Declaração Cb PM Ataídes.docx`
  * `JD/Arquivo/minhas ocorrências/Oitiva como testemunha acusacao sd garcia.pdf`
  * `JD/Despacho arquivamento de Manifestação Preliminar.docx`
* **Compilados originais redundantes (já segmentados):**
  * `Notebooklm/Supervisor Regional/Vademecum.pdf`
  * `Notebooklm/Supervisor Regional/Doutrinas pm_compressed (1).pdf`
  * `Notebooklm/Supervisor Regional/POPs.pdf`

---

## E. Curadoria Aplicada — Reclassificações

Foram reclassificados **6 chunks** de arquivos fáticos/históricos da base que estavam rotulados como `NORMA` para `PRECEDENTE` ou `MODELO_PRECEDENTE`:
* `JD/Arquivo/2022/RELATORIO CD N 2BPMI-001-12-22...doc` ➔ **PRECEDENTE**
* `JD/Arquivo/2024/RELATORIO CD N 2BPMI-001-12-23 Cb PM Everton Carlos (1).doc` ➔ **PRECEDENTE**
* `JD/Arquivo/2024/RELATORIO CD N 2BPMI-001-12-23 Cb PM Everton Carlos (5).doc` ➔ **PRECEDENTE**
* `JD/Arquivo/2024/Relatório IP 2BPMI 050-12.5-24.doc` ➔ **PRECEDENTE**
* `JD/PPJM/MODELO DE RIOG PARA PPJM.doc` ➔ **MODELO_PRECEDENTE**
* `Notebooklm/Supervisor Regional/Relatório Ronda do Oficial  Supervisor Regional 23ago25 -  Modelo.pdf` ➔ **MODELO_PRECEDENTE**

---

## F. Curadoria Aplicada — Rebaixamentos

* **Arquivo:** `Notebooklm/Supervisor Regional/orientações direito militar.pdf`
* **Natureza antiga:** `NORMA`
* **Natureza nova:** `OUTRO`
* **Motivo:** O arquivo é um compilado gigante e redundante de doutrinas militares que ainda não foi segmentado. Rebaixar para `OUTRO` remove sua influência dos pools de fundamentos (`NORMA`) e de redação (`MODELO_DE_REDACAO`), impedindo que domine os resultados da busca por densidade até que sua segmentação seja feita.

---

## G. Resultado da Reindexação

* **Comando executado:**
  ```powershell
  python automacoes/despachadora/nucleo_despachadora/indexar_corpus.py
  ```
* **chunks no índice base:** 674
* **chunks excluídos da base:** 53
* **chunks novos adicionados (POPs e outros):** 120
* **chunks finais no novo índice:** 741
* **Novos arquivos ignorados (excluídos antes de indexar):** 57

---

## H. Distribuição de Naturezas Antes/Depois

| Natureza | Antes (Base 16/06) | Depois (Novo Índice) | Diferença |
| :--- | :---: | :---: | :---: |
| **NORMA** | 473 | 422 | -51 |
| **MODELO_PRECEDENTE** | 68 | 71 | +3 |
| **MODELO_DE_REDACAO** | 33 | 31 | -2 |
| **PRECEDENTE** | 39 | 41 | +2 |
| **PROCEDIMENTAL** | 16 | 43 | +27 |
| **OUTRO** | 8 | 9 | +1 |
| **JURISPRUDENCIA** | 5 | 5 | 0 |
| **N/A (Erros / Pequenos)** | 32 | 119 | +87 |
| **Total** | **674** | **741** | **+67** |

*Nota: O aumento de "N/A" se deve à incorporação de novos PDFs do Drive que continham erros operacionais ou tamanho de extração textual insuficiente, que agora ficam devidamente mapeados.*

---

## I. Validação por Buscas Locais

Buscas no arquivo `corpus_index.json` confirmam que:
1. **Sumiram do pool normativo:** `holerite`, `ofício convite`, `Conseg`, `fotografias`, `receituário`, `defesa prévia` e `oitiva`. Não há ocorrências dessas chaves mapeadas com a natureza `NORMA`.
2. **Continuam existindo como modelo/precedente:** Os relatórios de sindicâncias anteriores, portarias de IPM, e relatórios de ronda de supervisor continuam no índice, porém associados estritamente às naturezas `MODELO_PRECEDENTE` ou `PRECEDENTE`.
3. **Preservados como norma/procedimento:** Temas como "algemas", "preservação de local", "CPPM", "RDPM", "I-16-PM" e os POPs segmentados continuam saudáveis como `NORMA` ou `PROCEDIMENTAL`.

---

## J. Recuperação Local dos 3 Casos

A execução do validador em `saidas/test_retrieval.py` exibiu os seguintes resultados de busca para os 3 cenários operacionais:

### 1. Caso 1: Algemas / condução / espera na DP
* **CONTEXTO NORMATIVO (Fundamentos):**
  1. `P3/POPs/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` (Score: 10.62 | Natureza: PROCEDIMENTAL)
  2. `Normas/POPs_Segmentos/POP_3_03_00_Transporte_Guarda_Presos.txt` (Score: 10.33 | Natureza: NORMA)
  3. `P3/POPs/Processo-5.03.00_Uso-de-algemas.pdf` (Score: 8.95 | Natureza: PROCEDIMENTAL)
  4. `Normas/POPs_Segmentos/POP_5_03_00_Uso_de_Algemas.txt` (Score: 8.90 | Natureza: NORMA)
* **MODELOS DE REDAÇÃO:**
  1. `JD/PPJM/Manuais, Leis, Regulamentos/Portaria dispoe sobre armas na PM.pdf` (Score: 5.54 | Natureza: MODELO_PRECEDENTE)
  2. `JD/2025/Dano vtr 504/BO2025-8-171326905.pdf` (Score: 5.37 | Natureza: MODELO_DE_REDACAO)
  3. `JD/Arquivo/2024/RELATÓRIO SINDICANCIA 009-12-14 161700JUL24.docx` (Score: 5.36 | Natureza: MODELO_PRECEDENTE)
* **Confirmação:** Documentos fáticos e arquivos obsoletos do Notebooklm não dominaram o topo normativo. O POP 5.03.00 (algemas) e o POP 3.03.00 (transporte de preso) foram recuperados com prioridade máxima.

### 2. Caso 2: Acidente com viatura e vítima
* **CONTEXTO NORMATIVO (Fundamentos):**
  1. `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf` (Score: 4.15 | Natureza: NORMA)
  2. `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI Nº PM3-002-02-17 - Acidente Vtr.pdf` (Score: 4.14 | Natureza: NORMA)
  3. `JD/PPJM/Manuais, Leis, Regulamentos/M-02-PM.pdf` (Score: 3.99 | Natureza: NORMA)
  4. `Normas/POPs_Segmentos/POP_3_01_00_Acidente_Transito.txt` (Score: 3.97 | Natureza: PROCEDIMENTAL)
* **MODELOS DE REDAÇÃO:**
  1. `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.docx` (Score: 0.68 | Natureza: MODELO_PRECEDENTE)
  2. `JD/Arquivo/2024/RELATÓRIO SINDICANCIA 009-12-14 161700JUL24.docx` (Score: 0.38 | Natureza: MODELO_PRECEDENTE)
* **Confirmação:** O manual de trânsito M-02-PM, as Instruções de Prevenção de Acidentes com Viatura (NI PM3-002-02-17) e o POP 3.01.00 dominam a fundamentação de trânsito de forma coerente.

### 3. Caso 3: IPM / competência / autotutela
* **CONTEXTO NORMATIVO (Fundamentos):**
  1. `Normas/Doutrinas_PM_Segmentos/Doutrinas_RDPM.txt` (Score: 10.01 | Natureza: NORMA)
  2. `JD/PPJM/Manuais, Leis, Regulamentos/RDPM atualizado 21MAR25.pdf` (Score: 9.95 | Natureza: NORMA)
  3. `JD/PPJM/Manuais, Leis, Regulamentos/I-16-PM.pdf` (Score: 9.70 | Natureza: NORMA)
* **MODELOS DE REDAÇÃO:**
  1. `JD/PPJM/Manuais, Leis, Regulamentos/Portaria dispoe sobre armas na PM.pdf` (Score: 6.63 | Natureza: MODELO_PRECEDENTE)
  2. `JD/Arquivo/2024/Relatório IP 2BPMI 050-12.5-24.doc` (Score: 5.58 | Natureza: PRECEDENTE)
  3. `JD/Arquivo/2024/RELATÓRIO SINDICANCIA 009-12-14 161700JUL24.docx` (Score: 5.17 | Natureza: MODELO_PRECEDENTE)
* **Confirmação:** O RDPM, a I-16-PM e as doutrinas normativas ocupam o topo dos fundamentos normativos. Os relatórios reais históricos (como o IP 050-12.5-24 e a Sindicância 009-12-14) aparecem estritamente no pool de modelos/precedentes, conforme reclassificado, garantindo a sua utilidade como modelos estruturais sem risco de inventar normas a partir deles.

---

## K. Pendências Mantidas

Ficam registradas as seguintes pendências para sprints posteriores:
1. **51 PDFs precisam de OCR:** PDFs identificados com `pdf_imagem_sem_ocr` (escaneados sem texto disponível).
2. **Segmentação de `orientações direito militar.pdf`:** O arquivo compilado gigante de 1,15M caracteres continua no corpus físico, marcado como `OUTRO` para evitar poluição do índice até que seus capítulos sejam segmentados e limpos.
3. **6 arquivos `PRONTO_SEM_SEGMENTACAO`:** Ingestão postergada para o próximo ciclo de curadoria e carga.
4. **Fontes Autônomas Normativas:** Criação e inclusão de fontes oficiais autônomas limpas para a Súmula Vinculante 11 e a Súmula 473.

---

## L. Riscos Reduzidos

* **Fator de Poluição Eliminado:** A exclusão dos arquivos consolidados do `Notebooklm` (Vademecum, Doutrinas, POPs) reduziu drasticamente o score de densidade falso, garantindo que o indexador aponte prioritariamente para os segmentos menores e limpos.
* **Segurança Jurídica:** Ao reclassificar expedientes fáticos reais (IPM, Sindicância) como `PRECEDENTE` ou `MODELO_PRECEDENTE`, elimina-se o risco de a IA interpretar relatos de transgressões ou fatos históricos como regras normativas vigentes.
* **Privacidade do Corpus:** O bloqueio absoluto de arquivos pessoais (holerites) e de convites assegura a integridade das informações e evita o desperdício de tokens com material de pouca relevância jurídica.

---

## M. Próxima Etapa Recomendada

* **Sprint 8.6:** Iniciar o processo de OCR sobre os 51 PDFs escaneados utilizando a suíte de ferramentas de imagem/OCR já estabelecida no repositório.
* **Sprint 8.7:** Efetuar a segmentação do arquivo `orientações direito militar.pdf` e restaurar sua indexação na categoria correta.
