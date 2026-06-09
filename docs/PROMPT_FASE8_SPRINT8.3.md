# PROMPT — FASE 8 · SPRINT 8.3 — SEGUNDA PASSADA DE CLASSIFICAÇÃO (aditiva pura)

## Quem você é
Meu parceiro de engenharia no projeto Central de Automações
(C:\Projetos\central_automacoes). Antes de tudo, leia:
- docs/PLANO.md, docs/DECISOES.md, docs/ROADMAP.md, docs/STATUS.md,
  docs/METADADOS_8_2.md
- automacoes/despachadora/nucleo_despachadora/classificar_corpus.py

## Regras de trabalho (invioláveis)
1. Fluxo: entender → planejar → confirmar → executar. Apresente o plano e ESPERE
   meu OK explícito antes de modificar qualquer arquivo.
2. Nunca rode git commit/push nem deploy.
3. Um sprint por vez: executa SOMENTE o 8.3.
4. py_compile em tudo que tocar antes de declarar pronto.
5. Não acesse internet, não chame API de IA, não rode OCR, não reindexe.

## Regra-mãe: ADITIVIDADE PURA (esta é a que define o sprint)
6. Este sprint só PROMOVE entradas hoje de baixa confiança para alta confiança.
   Ele NÃO toca em nenhuma entrada que já esteja em alta confiança.
7. PROIBIDO migrar, renomear ou colapsar rótulos existentes. As naturezas
   MODELO_DE_REDACAO (20 entradas) e PRECEDENTE (38) de alta confiança ficam
   EXATAMENTE como estão. Quem mexer nelas reprovou o sprint.
8. Backup com timestamp antes de escrever (local + Drive em
   backups_corpus_index_despachadora, fora do CORPUS_PATH), escrita atômica,
   prova de aditividade ao final.
9. Não tocar no corpus físico. Trabalhar só a partir do texto já indexado.
10. NUNCA sobrescrever entrada com classificacao_origem="humana".

## Doutrina desta fase (REGISTRAR como decisão nova no DECISOES.md, para meu OK)
Na base da 5ª Cia, modelos de redação são despachos REAIS antigos reusados como
espelho — modelo e precedente são, no arquivo físico, a mesma coisa. A distinção
só existe quando há SINAL claro. Portanto define-se uma TERCEIRA natureza:

- MODELO_PRECEDENTE = "documento-espelho da casa, com forma I-7-PM reconhecível,
  cujo tipo (molde vs caso) NÃO pôde ser cravado por sinal."

Isto é categoria NOVA, não substituição. MODELO_DE_REDACAO (sinal de molde) e
PRECEDENTE (sinal de caso real) continuam existindo e válidas para quando o sinal
for claro. Adicione MODELO_PRECEDENTE à lista de naturezas válidas do
classificar_corpus.py, sem remover as outras.

## Contexto (achados do 8.2)
Baixa confiança hoje: 250 entradas. Destas, 145 têm sugestão MODELO_DE_REDACAO,
concentradas em P3/JD/P1. Elas caíram em baixa confiança porque a regra do 8.2
exigia marcador explícito de "Modelo/Minuta/Template" no nome — que os documentos
reais da casa não têm (chamam-se pelo assunto). O sinal mais forte e ainda não
usado é a ESTRUTURA documental I-7-PM no texto já indexado.

## Objetivo do 8.3
Reduzir a planilha de revisão manual promovendo, para MODELO_PRECEDENTE em alta
confiança, as entradas de baixa confiança que tenham estrutura I-7-PM INEQUÍVOCA —
sem chutar, mantendo JD em régua mais alta, e deixando todo o resto na planilha
para meu olho.

### O QUE ENTRA
- Nova natureza MODELO_PRECEDENTE registrada (DECISOES.md + lista de válidas).
- Modo novo no classificar_corpus.py (ex.: --segunda-passada) que relê SOMENTE as
  entradas de baixa confiança com natureza_sugerida=MODELO_DE_REDACAO.
- Promoção a alta confiança (MODELO_PRECEDENTE, origem="heuristica") só das que
  têm forma I-7-PM inequívoca.
- Planilha de revisão regerada, menor.

### O QUE NÃO ENTRA (escopo travado)
- NÃO mexer nas 20 MODELO_DE_REDACAO nem nas 38 PRECEDENTE de alta confiança.
- NÃO avaliar vigência (segue nao_avaliado).
- NÃO ingerir conteúdo novo, NÃO tapar Lei 11.343/Lei 18.442 (isso é sprint
  posterior de curadoria).
- NÃO promover as sugestões OUTRO (85), NORMA (19) nem a única PRECEDENTE da
  planilha — só as MODELO_DE_REDACAO. As demais ficam para revisão manual.
- NÃO tocar na recuperação/dois pools do despachadora.py.

## Critério de estrutura I-7-PM inequívoca (proponha o detalhado para meu OK)
Promover a alta confiança SOMENTE quando o texto indexado exibir forma documental
clara de expediente da casa — p.ex. combinação de: cabeçalho/timbre de OPM,
fórmula de tratamento/endereçamento, corpo com fecho protocolar, bloco de
assinatura/posto-função. Defina um limiar concreto (quantos marcadores) e seja
CONSERVADOR: na ausência de combinação clara, NÃO promova — deixe na planilha.

## Régua especial para JD (inviolável)
JD é justiça e disciplina: contém peça sensível (sindicância, IPM, disciplinar com
nome de pessoa). Em JD a régua é mais alta — só promova com estrutura ainda mais
clara; na menor dúvida, mantenha na planilha. Erro de expor peça de JD como
espelho de redação é mais caro que em P1–P5.

## Tarefas
1. Registrar a nova natureza no DECISOES.md (decisão nova, numeração que segue) e
   atualizar STATUS.md (sprint atual 8.3; próximo passo) e ROADMAP.md.
2. Implementar o modo segunda-passada (aditivo) no classificar_corpus.py.
3. Aplicar o critério I-7-PM; promover as inequívocas a MODELO_PRECEDENTE/alta;
   registrar em classificacao_sinais o que motivou cada promoção.
4. Regerar saidas/revisao_classificacao.csv com o que SOBROU em baixa confiança.
5. Gerar docs/SEGUNDA_PASSADA_8_3.md: quantas foram promovidas (por pasta),
   quantas sobraram na planilha (por pasta e sugestão), e o tamanho final da
   revisão manual.

## Critério de aceite (verificável)
- Backup local + Drive criados; caminhos no relatório.
- Prova de aditividade: nº de entradas igual; nenhum campo original alterado; as
  ÚNICAS mudanças são entradas que saíram de baixa→alta confiança como
  MODELO_PRECEDENTE. Verificador imprime e confirma que as 20 MODELO_DE_REDACAO e
  as 38 PRECEDENTE de alta confiança permaneceram idênticas.
- vigencia=nao_avaliado em 100%.
- Nenhuma entrada origem="humana" sobrescrita.
- Planilha regerada e menor; tamanho final relatado.
- py_compile ok; corpus físico intacto; sem commit/push.

## Sua primeira ação agora
Não modifique nada ainda. Apresente:
1. O que entendeu (incluindo por que NÃO há migração e por que os 58 ficam intactos).
2. O critério I-7-PM EXATO (marcadores e limiar) que vai usar, e a régua reforçada
   de JD.
3. O texto da decisão nova para o DECISOES.md.
4. Plano de execução e como prova a aditividade.
Aí eu dou o OK.