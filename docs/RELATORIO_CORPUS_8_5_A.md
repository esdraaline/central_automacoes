# Relatório de Auditoria e Curadoria do Corpus — Sprint 8.5-a

## A. Estado do repositório

O repositório está limpo e sincronizado localmente. O status do git foi validado e confirma que não há alterações pendentes no código de produção ou no corpus de dados:

* **Branch:** `main` (Ahead of `origin/main` by 1 commit)
* **Último Commit:** `2036f68` - *feat(despachadora): estabiliza recuperação híbrida e validador pós-Gemini*
* **Estado das alterações:** `nothing to commit, working tree clean`
* **Arquivos modificados/untracked:** Nenhum.

---

## B. Estrutura atual do corpus

O corpus da Despachadora está centralizado na pasta física no Google Drive de trabalho e mapeado localmente via o índice estruturado.

* **Localização do Índice:** [corpus_index.json](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_index.json)
* **Total de Entradas Válidas:** 674 chunks (sem erros e com tamanho `>= 150` caracteres).
* **Mecanismo de Indexação:** Baseado em partições por natureza física e procedimental do documento. Os arquivos brutos sofrem segmentação e enriquecimento de metadados retrocompatíveis que diferenciam os pools de recuperação.

---

## C. Inventário de naturezas

A distribuição de naturezas dos 674 chunks válidos no índice está assim estabelecida:

| Natureza | Quantidade | Descrição / Exemplos no Corpus |
|---|---|---|
| `NORMA` | 475 chunks | Leis, diretrizes, manuais e resoluções. Ex: `JD/Despacho para não instauração de Sindicância.docx` |
| `MODELO_PRECEDENTE` | 68 chunks | Minutas e relatórios reais com estrutura I-7-PM. Ex: `JD/Arquivo/2018/Relatório Sindicancia PT .40 - 19FEV18.docx` |
| `PROCEDIMENTAL` | 46 chunks | POPs operacionais brutos. Ex: `JD/Arquivo/2023/Croqui Cadavérico Cristiano Birigui.pdf` |
| `PRECEDENTE` | 39 chunks | Peças e expedientes reais de casos passados. Ex: `JD/Arquivo/2022/Croqui Diego.pdf` |
| `MODELO_DE_REDACAO` | 33 chunks | Esboços genéricos de peças e documentos. Ex: `JD/Arquivo/2024/Auto de exibição e apreensão.doc` |
| `OUTRO` | 8 chunks | Artigos e guias doutrinários auxiliares. Ex: `JD/PPJM/Orientações PJMD MDIP e LCDIP.pdf` |
| `JURISPRUDENCIA` | 5 chunks | Súmulas de tribunais superiores. Ex: `JD/PPJM/Súmulas do STJ Sobre Prisão/Súmula 171 STJ.doc` |

---

## D. Busca literal das lacunas prioritárias

A busca literal executada por termo no corpus revelou o seguinte mapeamento de presença e ausência:

### 1. Algemas / SV 11
* `"Súmula Vinculante nº 11"`: **SIM** (11 chunks) — Encontrado em sua maioria dentro dos arquivos compilados do `Notebooklm` e POPs procedimentais.
* `"Súmula Vinculante 11"`: **NÃO** (0 chunks)
* `"Súmula 11"`: **NÃO** (0 chunks)
* `"uso de algemas"`: **SIM** (68 chunks) — Ampla cobertura em modelos fáticos e POPs.
* `"algemas"`: **SIM** (98 chunks)
* `"fundado receio de fuga"`: **SIM** (9 chunks) — Presente em POPs (`Abordagem`, `Transporte/Guarda`) e no compilado de doutrinas.
* `"perigo à integridade física"`: **SIM** (12 chunks) — Coberto pelo RDPM e POPs.
* `"resistência"`: **SIM** (83 chunks)
* `"justificativa por escrito"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica* (requisito essencial da SV 11).

### 2. Autotutela / Súmula 473
* `"Súmula 473"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica*
* `"Súmula nº 473"`: **SIM** (1 chunk) — Encontrado apenas no compilado de `Notebooklm` (`orientações direito militar.pdf`).
* `"autotutela"`: **SIM** (2 chunks) — Apenas no compilado `Notebooklm` e em um precedente fático de retificação de BOPM.
* `"anular seus próprios atos"`: **SIM** (1 chunk) — Apenas no compilado `Notebooklm`.
* `"revogar seus próprios atos"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica*
* `"conveniência ou oportunidade"`: **SIM** (1 chunk) — Apenas no compilado `Notebooklm`.
* `"direitos adquiridos"`: **SIM** (5 chunks) — Encontrado no Código Civil e na Constituição Estadual.

### 3. IPM / Competência
* `"autoridade de polícia judiciária militar"`: **SIM** (11 chunks)
* `"Inquérito Policial Militar"`: **SIM** (29 chunks)
* `"IPM"`: **SIM** (102 chunks)
* `"competência para instaurar"`: **SIM** (4 chunks) — Localizado na I-16-PM e no compilado do `Notebooklm`.
* `"Comandante do Batalhão"`: **SIM** (10 chunks)
* `"Comandante de Companhia"`: **SIM** (16 chunks)
* `"delegação"`: **SIM** (52 chunks)
* `"CPPM"`: **SIM** (37 chunks)

### 4. Sindicância / Competência / Prazos
* `"Sindicância"`: **SIM** (43 chunks)
* `"competência para instaurar sindicância"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica*
* `"prazo de sindicância"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica*
* `"30 dias"`: **SIM** (27 chunks) — Disperso (CPP, I-16-PM).
* `"20 dias"`: **SIM** (10 chunks) — Apenas em compilado de `Notebooklm` e NI_001_02_15.
* `"prorrogação"`: **SIM** (36 chunks)

### 5. Acidente com viatura
* `"acidente de trânsito"`: **SIM** (45 chunks)
* `"viatura"`: **SIM** (303 chunks)
* `"vítima civil"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica*
* `"lesão corporal"`: **SIM** (49 chunks)
* `"perícia"`: **SIM** (89 chunks)
* `"preservação de local"`: **SIM** (34 chunks)
* `"sinistro"`: **SIM** (32 chunks)
* `"dano ao erário"`: **NÃO** (0 chunks) ⚠️ *Lacuna crítica*
* `"ressarcimento"`: **SIM** (29 chunks)

---

## E. Fontes boas para fundamento

Representam a base sólida de dados normativos, manuais e legislações aplicáveis diretamente:
* **Vademecum Segmentado:** Os segmentos temáticos criados no Sprint 8.4 em `Normas/Vademecum_Segmentos/` (CTB, ECA, CP Militar, CPP flagrante, Maria da Penha e Drogas).
* **Doutrinas PM Segmentadas:** Os 31 arquivos em `Normas/Doutrinas_PM_Segmentos/`.
* **Regulamento Disciplinar da PMESP (RDPM):** As versões indexadas limpas (`RDPM atualizado 21MAR25.pdf` e `RDPM_LC915_out07.pdf`).
* **Instruções Operacionais e Administrativas:** I-16-PM, I-40-PM e providências em caso de óbito de policial.

---

## F. Fontes boas para modelo

Minutas, modelos formais estruturados e padrões de redação de referência que auxiliam a estruturar as saídas (especialmente Bloco 4):
* **Modelos Precedentes com I-7-PM:** Relatório de Sindicância, Portaria de IPM e Relatórios de Apuração Preliminar homologados.
* **Modelos de Redação Formais:** Minutas de Ofício para Apresentação em Juízo, Ofício de Busca e Apreensão e Minuta de Auto de Prisão em Flagrante (APFD).

---

## G. Fontes genéricas/Notebooklm

Documentos de compilação muito extensos que contêm material redundante ou genérico. Eles residem na pasta `Notebooklm/` e compreendem:
* `Notebooklm/Supervisor Regional/orientações direito militar.pdf` (1.15M caracteres)
* `Notebooklm/Supervisor Regional/Doutrinas pm_compressed (1).pdf` (3.09M caracteres)
* `Notebooklm/Supervisor Regional/POPs.pdf` (1.42M caracteres)
* `Notebooklm/Supervisor Regional/Vademecum.pdf` (7.37M caracteres)

*Nota:* Estes arquivos foram segmentados em capítulos menores no Sprint 8.4, tornando a permanência dos originais gigantes no indexador uma fonte de poluição do retrieval.

---

## H. Fontes problemáticas ou mal classificadas

A auditoria identificou **106 arquivos** que estão classificados erroneamente como `NORMA` (pelo indexador heurístico), mas que na verdade representam **documentos fáticos específicos de casos reais** (contaminações). 

### Exemplos críticos de falsos positivos (Fáticos marcados como NORMA):
1. **Peças de Casos Concretos (Contaminam a IA com nomes e datas reais):**
   * `JD/Despacho arquivamento de Manifestação Preliminar.docx` (FÁTICO: Termo BOPM / caso de arquivamento)
   * `JD/2025/RIOG Apreensão de Entorpecente.doc` (FÁTICO: Depoimento de testemunha)
   * `JD/2025/Dano vtr 504/Parte Dano vtr 504 (1).pdf` (FÁTICO: Boletim de dano a viatura)
   * `JD/Arquivo/2019/Parte Disparo de elastomero FT.doc` (FÁTICO: Relato de disparo de borracha em baile)
   * `JD/Arquivo/minhas ocorrências/Oitiva como testemunha acusacao sd garcia.pdf` (FÁTICO: Oitiva em audiência)
   * `P5/BOPC Flagrante Roubo Araçatuba Bilac.pdf` (FÁTICO: Boletim da Polícia Civil)
2. **Ofícios de Correspondência Simples (Poluição sem valor normativo):**
   * `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/` (Contém dezenas de minutas/ofícios direcionados a Prefeitos, Juízes e Promotores de cidades como Auriflama, Guzolândia, Gastão, etc., que apenas informam a assunção de comando).
   * `P1/Conseg/Oficios Convites Conseg/` (Ofícios de convite de reunião do Conseg para Rotary, Lions, OAB, etc.).

---

## I. Lacunas críticas

A Despachadora possui ausências documentais sérias sobre temas cruciais que forçam o Gemini a recorrer ao seu conhecimento próprio (e, por consequência, a ser bloqueado ou alertado pelo validador pós-Gemini):

1. **Súmulas Fundamentais de Forma Limpa:** Ausência do texto literal e interpretação autônoma da **Súmula Vinculante 11** (uso de algemas) e da **Súmula 473** (autotutela administrativa).
2. **Providências de SV 11:** O requisito explícito de *"justificativa por escrito"* do uso de algemas não aparece como regra expressa fundamentada (0 ocorrências).
3. **Prazos e Competência de Sindicância:** As normas da I-16-PM estão dispersas; não há uma folha normativa simplificada definindo as competências de instauração (ex: Comandante, Subcomandante) e o prazo regulamentar (30 dias prorrogáveis).
4. **Instruções para Acidentes de Viatura:** Falta normatização isolada cobrindo sinistros com **vítima civil** e **dano ao erário** (ressarcimento, perícia imediata do IC, preservação de local).

---

## J. Fontes existentes, mas não indexadas

* **Súmula Vinculante 11 e Súmula 473:** Existem de forma dispersa em relatórios e no arquivo compilado de orientações militares do Notebooklm, mas não de forma autônoma e limpa no pool normativo.
* **Regulamentos Completos de Sindicância e IPM (I-16-PM e I-40-PM):** Arquivos físicos parciais estão indexados na pasta `JD/`, mas capítulos chaves de regras operacionais de prazos e competência estão incompletos ou representados apenas por modelos fáticos em vez de folhas normativas dedicadas.
* **Lei 18.442/2026 (Quadros PMESP):** Ausente no corpus. Qualquer citação de estruturas anteriores de pessoal nos relatórios gerados pode estar desatualizada.

---

## K. Plano recomendado para Sprint 8.5-b

Para resolver o diagnóstico acima, a execução do Sprint 8.5-b deverá seguir os seguintes passos:

1. **Saneamento e Reclassificação (106 arquivos do Grupo D):**
   * Criar ou atualizar a tabela de classificação para alterar os documentos fáticos e ofícios do Grupo D.
   * Documentos de casos específicos (BOs, depoimentos, partes reais) devem ser alterados de `NORMA` para `PRECEDENTE` ou `EXCLUIR`.
   * Ofícios de apresentação/convite irrelevantes (como os convites do Conseg e ofícios de apresentação da 3ª Cia) devem ser marcados como `EXCLUIR` para limpar o indexador.
2. **Criação de Fontes Autônomas (Markdown):**
   * Criar `Normas/Sumula_Vinculante_11.md` contendo a transcrição da SV 11 e suas 3 condicionais estritas + exigência de justificativa por escrito.
   * Criar `Normas/Sumula_473_Autotutela.md` contendo a transcrição da súmula de autotutela.
   * Criar `Normas/Competencia_Prazos_Sindicancia_IPM.md` contendo tabela limpa extraída da I-16-PM com autoridades competentes e prazos de conclusão e prorrogação.
   * Criar `Normas/Acidente_Viatura_Providencias.md` com as diretrizes da I-40-PM sobre perícia, preservação, ressarcimento e tratamento em caso de vítima civil.
3. **Exclusão de Poluição do Notebooklm:**
   * Alterar a classificação dos 4 arquivos compilados de `Notebooklm/` para `EXCLUIR` no índice, já que seus fragmentos segmentados e limpos agora estão ativos no corpus.
4. **Reindexação:**
   * Executar o reimportador/indexador para atualizar o `corpus_index.json`.
5. **Validação:**
   * Rodar o script de validação de regras [testar_validador_saida.py](file:///c:/projetos/central_automacoes/saidas/testar_validador_saida.py).
   * Testar a geração com os 3 expedientes de campo para verificar se as fontes novas são recuperadas no `pool_f` e citadas com sucesso em `[FONTE:]`, eliminando alertas do validador.

---

## L. Riscos se nada for corrigido

* **Bloqueio Sistemático de Respostas:** O rigoroso validador pós-Gemini (implementado na Sprint 8.4-quater) **bloqueará** e substituirá as respostas da Despachadora por uma tela de erro se ela tentar propor súmulas ou fundamentar conclusões jurídicas importantes sem que o corpus as forneça como `[FONTE:]` normativa no pool de retrieval.
* **Diluição Crítica de Contexto:** Os 106 arquivos fáticos (declarações, ofícios, danos antigos de viatura) continuarão disputando espaço no pool de 12 chunks normativos, expulsando regras jurídicas verdadeiras do prompt final enviado ao Gemini.
* **Alucinação de Fatos Concretos:** A presença de oitivas de testemunhas e dados reais de 2019/2021 marcados como `NORMA` pode fazer a IA citar nomes, locais e placas de viaturas de casos passados como se fossem regras gerais a serem aplicadas no caso novo.
