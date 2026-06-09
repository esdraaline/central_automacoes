# PROMPT DE ABERTURA — FASE 8 · ENRIQUECIMENTO DA BASE DE CONHECIMENTO DA DESPACHADORA

## Quem você é neste projeto
Você é meu parceiro de engenharia no projeto Central de Automações
(C:\Projetos\central_automacoes). Antes de qualquer coisa, leia e absorva:
- README.md, docs/PLANO.md, docs/DECISOES.md, docs/ROADMAP.md, docs/STATUS.md,
  docs/APRENDIZADOS.md
- automacoes/despachadora/nucleo_despachadora/despachadora.py
- automacoes/despachadora/nucleo_despachadora/indexar_corpus.py
- automacoes/despachadora/nucleo_despachadora/ocr_pdfs_imagem.py

## Regras de trabalho (invioláveis)
1. Fluxo: entender → planejar → confirmar → executar. Apresente o plano e ESPERE
   meu OK explícito antes de modificar qualquer arquivo (inclusive os docs).
2. Nunca rode git commit/push nem deploy por conta própria.
3. Não toque na cópia de produção do BOPM fora de central_automacoes.
4. Segredos só via nucleo/segredos. CORPUS_PATH e GEMINI_API_KEY vêm de
   segredos.env. Se criar/alterar segredos.env, .gitignore ou segredos.env.exemplo,
   emita o alerta de SINCRONIZAÇÃO MANUAL (replicar no outro notebook; CORPUS_PATH
   pode ter letra de unidade diferente).
5. Um sprint por vez. Esta rodada executa SOMENTE o Sprint 8.1. Os sprints 8.2–8.4
   ficam registrados no ROADMAP como mapa, não são executados agora.

## Regra-mãe desta fase: ADITIVIDADE — não perca a riqueza que já existe
6. NUNCA remova, sobrescreva ou empobreça entradas do corpus_index.json atual.
   Todo enriquecimento é ADITIVO. Antes de qualquer reindexação futura, faça
   backup do corpus_index.json. O corpus físico (P1–P5, JD, Notebooklm) é a base
   real da 5ª Cia e é intocável: não renomeie, não mova, não delete.
7. Proveniência na ENTRADA, igual à da saída: nada entra na base sem origem
   rastreável e vigência atestável. Fonte oficial = pode virar FUNDAMENTO; sem
   isso, no máximo referência marcada [VERIFICAR]. NUNCA ingerir texto de fonte
   não-oficial como fundamento.

## Por que esta fase existe (contexto)
A Despachadora já funciona e é forte no que é da casa (precedentes e modelos da
5ª Cia). Mas a base é RASA em fundamento normativo e CEGA em metadados: o índice
não sabe a espécie do documento, o tema, a data, nem se a norma está VIGENTE ou
REVOGADA. Exemplo real: a Lei estadual nº 18.442/2026 reorganizou os quadros da
PMESP — qualquer documento antigo sobre quadros virou potencialmente obsoleto, e
hoje a busca por densidade recuperaria o texto velho com a mesma confiança.
Enriquecer sem antes dar à base metadados de vigência é encher balde furado.
Por isso a fase começa por DIAGNÓSTICO, não por ingestão.

## Objetivo da Fase 8 (mapa — não executar tudo agora)
Tornar a base de conhecimento da Despachadora mais rica e CONFIÁVEL, de forma
aditiva e curada, cobrindo as camadas que faltam sem perder o que já tem.

Sprints (registrar no ROADMAP; executar só o 8.1 agora):
- 8.1 — DIAGNÓSTICO do corpus (somente leitura; nenhum dado adicionado).
- 8.2 — METADADOS E VIGÊNCIA: estender o esquema do índice com espécie, tema,
        data, status (vigente/revogado), hierarquia normativa e fonte; adaptar
        indexar_corpus.py de forma retrocompatível.
- 8.3 — CURADORIA DE FONTES OFICIAIS (camadas 1–2): ingestão MANUAL e curada de
        legislação-base e normativos PMESP, só de fontes brancas, com proveniência.
- 8.4 — IA BUSCADORA ASSISTIDA: localiza e SUGERE fontes oficiais; humano confirma
        no portão de verificação antes de qualquer item entrar. Nunca ingestão direta.

### Camadas de cobertura que a fase visa preencher (referência para o diagnóstico)
- Camada 1 — Legislação-base: CP, CPP, CTB, Lei 11.343, Lei 11.340, ECA, CPM,
  CPPM; estaduais: RDPM (LC 893/2001), organização básica (Lei 616/1974),
  Lei 18.442/2026 (quadros).
- Camada 2 — Normativos internos PMESP: instruções I-NN-PM (incl. I-7-PM),
  NIs, DTZ, POPs, Diretrizes.
- Camada 3 — Modelos de redação por espécie: parte, ofício, despacho, sindicância,
  IPM, TC, relatório, escala, ata.
- Camada 4 — Jurisprudência operacional: busca pessoal, domicílio, flagrante,
  uso de força, abordagem.
- Camada 5 — Procedimental: prazos, fluxos, checklists.

### Fontes (valem para 8.3/8.4; não agora)
- BRANCAS (podem virar FUNDAMENTO): Planalto, al.sp.gov.br, policiamilitar.sp.gov.br,
  Diário Oficial SP, CONTRAN/DENATRAN, STJ, STF. Sempre com URL e data de captura.
- PRETAS (jamais como fundamento): Jusbrasil, qconcursos, blogs, resumos de IA,
  PDF solto sem origem. Servem no máximo para localizar a norma oficial.

## PRIMEIRA TAREFA: registrar a fase no projeto
Antes de executar o diagnóstico, proponha (para meu OK) os textos exatos a inserir:
- docs/ROADMAP.md: adicionar a Fase 8 como a PRÓXIMA fase livre na numeração (leia
  o ROADMAP atual e confirme o número; se não for 8, ajuste). Independente das
  Fases 3–6 (pode rodar em paralelo, como a 7 foi). Incluir os sprints 8.1–8.4 em
  alto nível, com 8.1 detalhado.
- docs/STATUS.md: definir "Fase em execução: Fase 8 — Enriquecimento da Base";
  "Sprint atual: 8.1 — Diagnóstico"; e em "Próximo passo" escrever explicitamente:
  "seguir docs/PROMPT_FASE8.md (Sprint 8.1 — diagnóstico do corpus, somente leitura)".
  Esse apontamento é proposital: quando eu abrir o projeto e perguntar a próxima
  tarefa, o STATUS.md deve me mandar para este prompt.

## SPRINT 8.1 — DIAGNÓSTICO DO CORPUS (executar após o OK; SOMENTE LEITURA)
Restrição absoluta do 8.1: não modifique corpus_index.json, não baixe/mova/edite
arquivos, não chame nenhuma API de IA, não acesse a internet. Reaproveite os
extratores de indexar_corpus.py — não reescreva. Disciplina de proveniência na
investigação: quando não conseguir ler ou classificar, registre ILEGÍVEL /
NAO_CLASSIFICADO; nunca presuma conteúdo.

Tarefas:
1. INVENTÁRIO FÍSICO: varra CORPUS_PATH. Por seção (P1–P5, JD, Notebooklm e
   quaisquer outras que existam de fato), conte arquivos por tipo, tamanho e datas.
   Liste seções que existem no Drive e não conhecíamos.
2. CRUZAMENTO COM O ÍNDICE: compare Drive × corpus_index.json. Reporte: arquivos
   não indexados; entradas órfãs (no índice, sem arquivo); entradas com error;
   entradas com texto abaixo do mínimo; prováveis duplicatas (nome/tamanho/hash).
3. CLASSIFICAÇÃO POR NATUREZA (heurística nome+amostra): NORMA | MODELO_DE_REDACAO
   | PRECEDENTE | JURISPRUDENCIA | PROCEDIMENTAL | OUTRO | NAO_CLASSIFICADO. Some.
4. CLASSIFICAÇÃO POR ESPÉCIE (documentos da casa): parte, ofício, despacho,
   sindicância, IPM, TC, relatório, escala, ata, outro. Conte.
5. NORMAS PRESENTES: por busca textual, liste quais normas aparecem citadas/contidas
   (ex.: "LC 893", "Lei 616", "CTB", "I-7-PM", "Lei 18.442"). Só PRESENÇA; não
   afirme vigência.
6. LACUNAS contra as 5 camadas acima: para cada item, PRESENTE / PARCIAL / AUSENTE,
   com base apenas no que encontrou.

Entregáveis do 8.1:
- docs/DIAGNOSTICO_CORPUS.md — relatório legível com as tabelas dos itens 1–6 e
  um resumo executivo de ~10 linhas no topo (o que a base tem de forte, o que falta).
- saidas/inventario_corpus.csv — uma linha por arquivo: seção, arquivo, tipo,
  tamanho, indexado(s/n), erro, natureza, especie, normas_citadas.
- Lista de suposições de classificação e do que ficou NAO_CLASSIFICADO.

Critério de aceite do 8.1: ROADMAP e STATUS atualizados; DIAGNOSTICO_CORPUS.md e
inventario_corpus.csv gerados; nenhuma alteração no corpus_index.json nem no corpus
físico; nenhuma chamada de rede/IA. Eu consigo ler o diagnóstico e decidir o 8.2.

## Sua primeira ação agora
Não modifique nada ainda. Leia os arquivos indicados, confirme o CORPUS_PATH e os
extratores disponíveis, e me apresente:
1. O que entendeu da fase e do estado atual do projeto.
2. Os textos exatos que vai inserir em ROADMAP.md e STATUS.md (para meu OK).
3. O plano de varredura do Sprint 8.1 (ordem, como vai classificar, riscos).
4. Dúvidas.
Aí eu dou o OK para você registrar a fase e executar o diagnóstico.