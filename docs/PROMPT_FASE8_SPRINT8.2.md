# PROMPT — FASE 8 · SPRINT 8.2 — METADADOS E CLASSIFICAÇÃO DA BASE (aditivo)

## Quem você é
Meu parceiro de engenharia no projeto Central de Automações
(C:\Projetos\central_automacoes). Antes de tudo, leia:
- docs/PLANO.md, docs/DECISOES.md, docs/ROADMAP.md, docs/STATUS.md,
  docs/APRENDIZADOS.md, docs/DIAGNOSTICO_CORPUS.md
- automacoes/despachadora/nucleo_despachadora/{despachadora.py, indexar_corpus.py,
  ocr_pdfs_imagem.py}

## Regras de trabalho (invioláveis)
1. Fluxo: entender → planejar → confirmar → executar. Apresente o plano e ESPERE
   meu OK explícito antes de modificar qualquer arquivo.
2. Nunca rode git commit/push nem deploy.
3. Segredos só via nucleo/segredos. Se tocar segredos.env/.gitignore/.env.exemplo,
   emita o alerta de SINCRONIZAÇÃO MANUAL.
4. Um sprint por vez: executa SOMENTE o 8.2. Não adianta 8.3/8.4.
5. py_compile em tudo que mexer antes de declarar pronto.

## Regra-mãe: ADITIVIDADE (esta é a que não se viola)
6. Este sprint MODIFICA o corpus_index.json — mas só ADICIONA campos. Nenhuma
   entrada existente pode ser removida, e NENHUM campo pré-existente
   (section, arquivo, tipo, texto, error) pode ter o valor alterado.
7. Antes de qualquer escrita, faça backup com timestamp:
   corpus_index.backup.AAAAMMDD-HHMMSS.json. Registre o caminho no relatório.
8. O corpus FÍSICO no Drive é intocável: não ler para escrever, não mover, não
   renomear, não deletar. A classificação trabalha a partir do que JÁ está no
   índice (campos texto/arquivo/section), sem reabrir os arquivos físicos.
9. Escrita do índice ATÔMICA (grava em arquivo temporário e troca), como faz o
   ocr_pdfs_imagem.py. Nunca grave por cima diretamente.
10. NÃO reindexe o corpus do zero. NÃO chame indexar_corpus.py em modo escrita.
    NÃO rode OCR. NÃO acesse a internet. NÃO chame nenhuma API de IA.

## Por que este sprint existe (achados do 8.1)
A base NÃO é pobre em fundamento — CP, CPP, CTB, CPM, CPPM, RDPM, ECA e Maria da
Penha estão presentes. O problema é que ela NÃO SABE O QUE SABE: 729 entradas sem
metadado de natureza, espécie ou vigência. Três achados guiam este sprint:
- A Camada 3 (436 sinais) MISTURA modelo de redação com precedente — são coisas
  diferentes e precisam de campos distintos.
- A Camada 4 (jurisprudência, 13 sinais) está sem fonte atestada — é o conteúdo
  mais perigoso da base e precisa de um campo de fonte (a ser preenchido só no 8.3).
- A pasta de origem é o melhor classificador disponível (foi o humano que
  organizou): use a seção como sinal PRIMÁRIO, o texto/nome só para refinar.

## Objetivo do 8.2
Dar à base um esquema de metadados e classificar as entradas existentes de forma
aditiva, HONESTA quanto à confiança: a máquina grava sozinha só o que é
inequívoco; o que é ambíguo vai para uma planilha de revisão humana.

### O QUE ENTRA
- Esquema de campos novos no corpus_index.json (todos opcionais, com default).
- Classificação automática por natureza e espécie, com score de confiança.
- Planilha dos ambíguos para eu revisar.
- Mecanismo de reimportar a planilha revisada de volta ao índice.

### O QUE NÃO ENTRA (escopo travado)
- NÃO avaliar vigência de norma: o campo vigencia nasce "nao_avaliado" para TODAS
  as entradas. Avaliar vigência é 8.3.
- NÃO ingerir nada novo: nem Lei 11.343, nem Lei 18.442/2026, nem jurisprudência.
  Isso é curadoria do 8.3.
- NÃO fazer a recuperação da Despachadora consumir os metadados ainda (não tocar
  na lógica dos dois pools do despachadora.py). Consumir é sprint posterior.
- NÃO construir tela: a revisão é por planilha (decisão tomada).
- NÃO incluir os 193 arquivos não indexados — apenas relatá-los (tarefa 6).

## Esquema de metadados (proponha o exato para meu OK)
Campos novos por entrada, todos aditivos e opcionais:
- natureza: NORMA | MODELO_DE_REDACAO | PRECEDENTE | JURISPRUDENCIA |
  PROCEDIMENTAL | OUTRO | NAO_CLASSIFICADO
- especie: parte|oficio|despacho|sindicancia|ipm|tc|relatorio|escala|ata|outro|null
- vigencia: nao_avaliado (FIXO neste sprint para todas)
- hierarquia: lei_federal|lei_estadual|decreto|resolucao|norma_interna|null
  (só quando natureza=NORMA e identificável com segurança; senão null)
- fonte: null por ora (campo criado; preenchimento de jurisprudência é 8.3)
- classificacao_confianca: "alta" | "baixa"
- classificacao_origem: "heuristica" | "humana"
- classificacao_sinais: string curta dizendo o que motivou (ex.: "pasta=Normas;
  texto contém 'DESPACHO'") — para auditoria.

Respeite a regra da Despachadora: o que está na seção Notebooklm é fonte
NORMATIVA (natureza tende a NORMA), nunca MODELO_DE_REDACAO.

## Tarefas
1. REGISTRAR A FASE: proponha (para meu OK) a atualização de docs/STATUS.md
   (último concluído = 8.1; sprint atual = 8.2; "próximo passo" aponta para
   docs/PROMPT_FASE8_SPRINT8.2.md) e marque 8.1 como concluído no ROADMAP.
2. ESQUEMA: implemente os campos acima de forma aditiva e retrocompatível.
3. CLASSIFICAÇÃO AUTOMÁTICA: para cada entrada, decida natureza/espécie usando a
   pasta como sinal primário e nome+texto-já-indexado como refino. Atribua
   confianca="alta" quando pasta e texto concordam ou o sinal é inequívoco;
   "baixa" quando há divergência, ambiguidade ou pasta genérica. Grave no índice
   APENAS as de confiança alta (origem="heuristica"). As de baixa confiança
   recebem natureza="NAO_CLASSIFICADO" no índice e vão para a planilha.
4. PLANILHA DE REVISÃO: gere saidas/revisao_classificacao.csv com uma linha por
   entrada de baixa confiança. Colunas: chave (section/arquivo), nome, pasta,
   trecho_amostra (1ª ~300 chars do texto indexado), natureza_sugerida,
   especie_sugerida, confianca, sinais, e DUAS colunas vazias para eu preencher:
   natureza_correta, especie_correta, e uma observacao.
5. REIMPORTADOR: implemente um modo do script que lê a planilha PREENCHIDA e
   aplica as correções ao índice com origem="humana". Ele NUNCA sobrescreve uma
   entrada cuja origem já seja "humana" (idempotente; não reverte revisão minha).
   Teste-o com um CSV de exemplo de 2-3 linhas (não dependa de eu já ter
   preenchido a planilha real).
6. RELATÓRIO DOS 193: gere saidas/relatorio_193_nao_indexados.csv quebrando os
   arquivos físicos não indexados por MOTIVO de exclusão, e marcando como
   "candidato" qualquer um cujo nome/extensão sugira norma ou modelo. SOMENTE
   relatório — não inclua nenhum deles. Incluir é decisão futura minha.
7. RESUMO: gere docs/METADADOS_8_2.md com contagens por natureza, espécie e
   confiança; quantas entradas alta vs baixa; quantas foram para a planilha;
   e o caminho do backup.

## Critério de aceite (verificável)
- Backup corpus_index.backup.*.json criado; caminho registrado no resumo.
- PROVA DE ADITIVIDADE: um verificador confirma e imprime que, comparando backup
  vs índice final — (a) nº de entradas não diminuiu; (b) toda chave
  section/arquivo original ainda existe; (c) nenhum campo original
  (section/arquivo/tipo/texto/error) teve valor alterado; (d) as únicas mudanças
  são campos novos adicionados. Cole esse resultado no resumo.
- vigencia == "nao_avaliado" em 100% das entradas.
- Entradas de alta confiança classificadas no índice; baixa confiança na planilha.
- Reimportador implementado e testado com CSV de exemplo; não reverte origem
  "humana".
- saidas/relatorio_193_nao_indexados.csv e docs/METADADOS_8_2.md gerados.
- py_compile ok; corpus físico intacto; nenhum commit/push.

## Sua primeira ação agora
Não modifique nada ainda. Apresente:
1. O que entendeu do sprint e dos achados do 8.1.
2. O esquema EXATO de campos que vai adicionar (para meu OK).
3. Como vai decidir confiança alta vs baixa (a regra concreta: que combinações de
   pasta+texto viram "alta", quais viram "baixa").
4. O plano de execução (ordem, como gera a planilha, como funciona o reimportador,
   como prova a aditividade) e as dúvidas.
Aí eu dou o OK.