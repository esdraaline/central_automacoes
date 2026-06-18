# Saliência de Fontes Autônomas e Prompt Reforçado — Sprint 8.6-f

## A. Estado inicial

* Commit base: `2494116 fix(despachadora): prioriza fontes autonomas no retrieval`
* Working tree limpo, nenhum corpus alterado.
* Problema residual (Sprint 8.6-e): Fontes autônomas entraram no pool normativo (priorização técnica funcionou), mas Gemini não as formatou adequadamente, combinando `[VERIFICAR]` com "configura" (Caso 1) e usando memória jurídica para "autotutela" sem `[FONTE:]` porque a fonte ficou no fim do contexto (Caso 3).

## B. Diagnóstico da montagem anterior do contexto

Na montagem anterior, todas as fontes do `pool_f` eram iteradas sequencialmente em um bloco genérico `CONTEXTO NORMATIVO (corpus 5ª Cia)`.
* No Caso 1, SV11 apareceu no início. No Caso 3, a Súmula 473 caiu para o 12º slot do prompt, ficando muito distante das instruções iniciais.
* O `MASTER_SYSTEM_PROMPT` não trazia exemplo concreto de como ancorar uma referência a JURISPRUDENCIA do corpus_manual.

## C. Ajuste implementado

1. **Bloco de Fontes Prioritárias:** A função `build_user_prompt` foi modificada para interceptar as fontes com prefixo `corpus_manual/` presentes no `pool_f`. Elas agora são extraídas e formatadas num bloco distinto no início do contexto, chamado `FONTES AUTÔNOMAS PRIORITÁRIAS`.
2. **Campos Enriquecidos:** Cada fonte autônoma no novo bloco informa explicitamente a sua `Natureza` e a regra de `Uso` (mapeada pelos gatilhos temáticos).
3. **Ordenação Lógica:** As fontes autônomas recebem uma ordenação primária que favorece a linha mestra de raciocínio. No Caso 3, a ordem forçada é: `Sumula_473_Autotutela` -> `Competencia_IPM` -> `Competencia_Prazos_Sindicancia`.
4. **Exemplo Obrigatório:** O `MASTER_SYSTEM_PROMPT` recebeu seção explícita mostrando o que fazer:
   `[FUNDAMENTO] A Súmula Vinculante nº 11... [FONTE: corpus_manual/...]`
   `[FUNDAMENTO] A Súmula 473... [FONTE: corpus_manual/...]`
   E também o que *não* fazer (e.g. `[VERIFICAR] ... configura ...`).
5. **Proteção contra Termos Jurídicos Sem Fonte:** Adicionada orientação explícita que proíbe o uso isolado de conclusões como "nulidade absoluta", "vício insanável" ou "autotutela" a não ser que haja um `[FUNDAMENTO] + [FONTE:]` amparando ou que a frase seja formulada de maneira estritamente cautelosa.

## D. Prompt dos Casos 1 e 3 sem Gemini (Testes Locais)

Validação realizada via script local `scratch/audit_context_86f.py`.

* **Caso 1:**
  * Bloco `FONTES AUTÔNOMAS PRIORITÁRIAS` está presente.
  * `Sumula_Vinculante_11_Algemas.md` aparece neste bloco (index 757, no topo da lista normativo).
* **Caso 3:**
  * Bloco `FONTES AUTÔNOMAS PRIORITÁRIAS` está presente.
  * Ordem forçada conferida: Súmula 473 (index 706) -> Competencia_IPM (index 1920) -> Competencia_Prazos_Sindicancia (index 4159). Todas antes das `DEMAIS FONTES NORMATIVAS / PROCEDIMENTAIS`.
* **Prompt Geral:**
  * O bloco `EXEMPLO OBRIGATÓRIO — FONTES AUTÔNOMAS DO CORPUS_MANUAL` foi inserido no `MASTER_SYSTEM_PROMPT`.
  * Regras contra `[VERIFICAR] ... configura` e `nulidade absoluta` confirmadas.

## E. Testes

* Validador local: `12/12` testes passaram (nenhuma regressão).
* Compilação (`py_compile`): `despachadora.py`, `indexar_corpus.py` e `classificar_corpus.py` compilados sem erro de sintaxe.

## F. Riscos remanescentes

* O LLM (Gemini) ainda tem livre arbítrio durante a geração e pode não seguir à risca os exemplos ou as formatações, mesmo com as instruções explícitas.
* Se a formatação incorreta persistir (violando a estrutura `[FUNDAMENTO]+[FONTE:]`), a próxima etapa exigiria um pós-processamento de reescrita/normalização da resposta (um agente auxiliar) antes da passagem pelo validador.
* Não foi chamado o Gemini nesta sprint; logo, o comportamento em produção será aferido no reteste.

## G. Próxima etapa recomendada

`8.6-g — Reteste manual dos 3 casos no painel após saliência das fontes autônomas.`
