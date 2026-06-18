# Normalizador Determinístico da Resposta — Sprint 8.7-a

## A. Estado inicial

* Commit base: `9f74b02 fix(despachadora): destaca fontes autonomas no contexto normativo`
* Saliência de fontes ativada e funcional.
* O validador (Sprint 8.6-b) atuava diretamente sobre a resposta bruta do Gemini.
* No reteste 8.6-g, o Caso 3 foi bloqueado de forma legítima, pois o Gemini persistiu em usar terminologias como "autotutela", "vício insanável" e "não detém competência" fora do padrão esperado ou como conclusões fortes desancoradas.

## B. Problema resolvido

O Gemini exibe teimosia estrutural em casos de Processo Penal Militar/Direito Administrativo, formulando conclusões legais definitivas sem ancoragem normativa. A barreira do validador cumpriu seu papel e bloqueou, mas gerava uma experiência "tudo ou nada". O Normalizador Determinístico atua para tentar *sanear* ocorrências de menor risco (rebaixando o nível de certeza) antes da validação final, reduzindo bloqueios sem afrouxar a segurança.

## C. Regras de normalização

A nova função `normalizar_resposta_antes_validador` processa parágrafo a parágrafo sem invenção de contexto, aplicando regras de segurança:

1. **Regra N1 (`[PADRÃO]` sensível):** Substitui `[PADRÃO]` por `[VERIFICAR]` e modera a frase se houver termos como "crime militar", "prazo decadencial" ou "autotutela" que deveriam ser `[FUNDAMENTO]`.
2. **Regra N2 (`autotutela` isolada):** A presença da palavra "autotutela" sem referência documental é rebaixada para exigir confirmação da fonte.
3. **Regra N3 (`nulidade absoluta` / `vício insanável`):** Neutralizados e substituídos por determinação expressa de que não se deve decretar tais vícios sem amparo da autoridade.
4. **Regra N4 (`[VERIFICAR]` forte):** Desarma conclusões ativas que aparecem após `[VERIFICAR]`, como `configura`, `torna nulo`, substituindo-os por alertas de cautela.
5. **Regra N5 (Bloco 4 agressivo):** Ajusta o "Texto Pronto" mitigando afirmações diretas de "incompetência da autoridade", "competência originária" ou "não detém competência" para formulações avaliativas de encaminhamento.

## D. Integração no fluxo

O pipeline de verificação em `_aplicar_validacao` foi modificado para o seguinte fluxo seguro:

`Resposta Gemini -> normalizar_resposta_antes_validador -> validar_saida_despachadora`

A lista de `AJUSTES DE SEGURANÇA APLICADOS PELO NORMALIZADOR` é adicionada ao final do conteúdo validado como um alerta informativo extra se nenhuma violação final subsistir, não poluindo o Texto Pronto em si. O validador continuará barrando as alterações que fujam ao padrão normativo se o saneamento não der conta.

## E. Testes simulados

O script `saidas/testar_normalizador_8_7_a.py` submeteu frases cruas às funções de Regra N:
* `[PADRÃO] De acordo com o princípio da autotutela...` -> Saneado para `[VERIFICAR]` com suavização. Validador APROVOU.
* `Declarar a nulidade absoluta...` -> Saneado mitigando os termos "vício insanável". Validador APROVOU.
* `O fato configura peculato...` -> Ignorado pelo normalizador, mantido cru. Validador BLOQUEOU com segurança (frutos envenenados / peculato).
* `[FUNDAMENTO] ... [FONTE: corpus_manual/Sumula_473_Autotutela.md]` -> Mantido inalterado, pois a fonte constava.

## F. Teste com Caso 3 real ou snippets

Simulação usando as respostas problemáticas logadas no final da Sprint 8.6-g:
* **Snippet original:** `[PADRÃO] No caso em tela... padece de vício insanável.`
* **Ajuste N1 + N3 aplicado:** Transformado em verificação e termo forte extirpado.
* **Validador:** PASSOU (Saneado!).
* **Snippet original:** `...este Comando de Companhia não detém competência.`
* **Ajuste N5 aplicado:** `...submete-se a análise de competência.`
* **Validador:** PASSOU (Saneado!).

## G. Impacto nos Casos 1 e 2

O Caso 1 e o Caso 2 não sofrerão nenhum impacto destrutivo ou reescrita grosseira. Palavras lícitas, menções a Súmula 11 ou "acidente" passam ilesas pelas verificações do normalizador (pois as restrições são atreladas aos termos N). Nenhuma marcação legítima de `[FONTE:]` será afetada. Placeholders como `[nº]` ou `[RE não informado]` permanecem intocados.

## H. Riscos remanescentes

* O normalizador aplica RegEx pontual e pode tornar o linguajar da resposta artificialmente burocratizado ou muito extenso onde os "VERIFICAR" forem aplicados com frequência.
* O normalizador **não fabrica** fonte. Se faltar a `[FONTE:]`, o Bloco 2 continuará oco e com o texto meramente mitigado.
* Casos extremamente aberrantes de argumentação do modelo, repletos de "achismos", ainda encontrarão as amarras duras do Validador se não passarem na peneira do normalizador.

## I. Próxima etapa recomendada

`8.7-b — Reteste manual dos 3 casos no painel com normalizador ativo.`
