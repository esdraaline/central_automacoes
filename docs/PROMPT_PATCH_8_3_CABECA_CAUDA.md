# PROMPT — PATCH DO SPRINT 8.3 · DETECTOR CABEÇA+CAUDA

## Quem você é

Meu parceiro de engenharia no projeto Central de Automações (`C:\Projetos\central_automacoes`).

Antes de modificar qualquer arquivo, leia:

- `docs/CONTEXTO_RETORNO_2026-06-10.md`
- `docs/DECISOES.md`
- `docs/STATUS.md`
- `docs/SEGUNDA_PASSADA_8_3.md`
- `automacoes/despachadora/nucleo_despachadora/classificar_corpus.py`

## Contexto

O Sprint 8.3 promoveu 36 entradas para `MODELO_PRECEDENTE` e deixou 214 na planilha. Ao analisar as 39 "quase promovidas", foi encontrado um bug no detector: ele avaliou `texto[:12000]`, mas fecho e assinatura normalmente ficam no final do documento.

Em 38/39 quase promovidas havia sinal de fecho ou assinatura em algum lugar do texto indexado; em 31/39 o sinal estava no final; em 9 casos o fecho estava só no fim, fora da janela analisada.

## Objetivo

Corrigir a miopia do detector I-7-PM sem afrouxar a régua.

Reprocessar as entradas ainda em baixa confiança com `natureza_sugerida=MODELO_DE_REDACAO`, usando cabeça + cauda do texto já indexado, e promover apenas as que passarem na mesma régua do 8.3.

## Regras Invioláveis

1. Não reindexar.
2. Não rodar OCR.
3. Não acessar internet nem API de IA.
4. Não tocar no corpus físico.
5. Não alterar campos originais: `section`, `arquivo`, `tipo`, `texto`, `error`.
6. Não tocar em entradas já em alta confiança, inclusive:
   - 20 `MODELO_DE_REDACAO`
   - 38 `PRECEDENTE`
   - 36 `MODELO_PRECEDENTE`
7. Não sobrescrever entrada com `classificacao_origem="humana"`.
8. Não baixar limiar.
9. Não relaxar obrigatórios.
10. Criar backup local + Drive antes de escrever.
11. Escrita atômica.
12. `vigencia` continua `nao_avaliado`.

## Mudança Permitida

Somente corrigir onde o detector olha e os marcadores de fecho/assinatura que ele já deveria reconhecer.

Use janela explícita:

- cabeça: primeiros `12000` caracteres.
- cauda: últimos `6000` caracteres.
- documento curto: unir os intervalos sem duplicar categorias, porque cada categoria é booleana.

Justificativa:

- Cabeçalho, tipo e corpo formal tendem a estar no início.
- Fecho, assinatura, posto e função tendem a estar no fim.
- `6000` caracteres de cauda absorvem ruído de OCR/PDF sem transformar o detector em busca irrestrita.

## Marcadores A Ajustar

Além dos marcadores já existentes, reconhecer na categoria de fecho/assinatura:

- lema PM: `Nós, Policiais Militares, sob a proteção de Deus...`
- `Assinado no original`
- `Certifico que o presente arquivo eletrônico confere`
- nome + posto/função no fim
- funções: `Encarregado`, `Presidente`, `Oficial PPJM`, `Chefe P/3`, `Cmt`, `Cmt Pel`, `Cmt Cia`
- postos já existentes: `Cap PM`, `Ten PM`, `Maj PM`, `Cel PM`, `Sgt PM`, `Sd PM`

## Régua Mantida

P1-P5:

- Promover com `4 de 6` categorias.
- Obrigatório: pelo menos uma de `tipo` ou `corpo`.
- Obrigatório: pelo menos uma de `fecho` ou `assinatura`.

JD:

- Promover com `5 de 6` categorias.
- Obrigatórios: `tipo`, `corpo`, `assinatura`.
- Na dúvida, fica na planilha.
- Peça de JD sem endereçamento claro deve continuar barrada se não atingir o limiar.

## Tarefas

1. Atualizar `classificar_corpus.py` para o detector usar cabeça + cauda.
2. Manter o modo `--segunda-passada`.
3. Reprocessar apenas as baixas ainda presentes em `saidas/revisao_classificacao.csv` com `natureza_sugerida=MODELO_DE_REDACAO`.
4. Criar backup local + Drive.
5. Promover somente baixa→alta como `MODELO_PRECEDENTE`.
6. Regenerar `saidas/revisao_classificacao.csv`.
7. Atualizar `docs/SEGUNDA_PASSADA_8_3.md` com uma seção "Patch cabeça+cauda", contendo:
   - quantas novas promoções o patch fez;
   - quantas linhas sobraram na planilha;
   - quantas quase promovidas sobraram;
   - prova de aditividade;
   - caminhos dos backups.
8. Rodar `py_compile`.

## Prova De Aceite

O relatório deve confirmar:

- Total segue `729`.
- Campos originais intactos.
- Nenhuma entrada humana sobrescrita.
- Altas antigas preservadas:
  - 20 `MODELO_DE_REDACAO`
  - 38 `PRECEDENTE`
  - 36 `MODELO_PRECEDENTE` pré-patch
- Únicas mudanças: entradas baixa→alta como `MODELO_PRECEDENTE`.
- `vigencia=nao_avaliado` em 100%.
- `corpus_index.json` e backups continuam fora do git.
- Sem commit/push, salvo se o usuário pedir explicitamente.
