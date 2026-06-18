# Microcorreção N4 x Regra F (Sprint 8.7-g)

## A. Estado inicial
No final da Sprint 8.7-f, os Casos 1 e 3 retestados foram bloqueados no validador. A investigação comprovou que a matriz legal e a estrutura do Texto Pronto estavam corretas e respeitavam as novas pontes lógicas. O bloqueio ocorreu por uma limitação sintática: o validador estava unindo listas de bullets como um único "parágrafo lógico". Dentro dessa lista, um item possuía o marcador cauteloso `[VERIFICAR]`, e outro item (ou o mesmo) possuía uma palavra que configurava "conclusão forte", como `configurando` ou `configurar`. 
A Regra N4, desenhada para neutralizar parágrafos contendo essa exata colisão, não atuava porque buscava a palavra exata (`\bconfigura\b`), enquanto o validador aceitava variações flexionais como substrings (`configurando` contém `configura`).

## B. Bloqueios residuais da 8.7-f
- **Caso 1:** A lista de análise jurídica (Bloco 2) agrupada continha `[VERIFICAR]` (sobre a permanência na delegacia) e `configurando` (sobre a ausência de lesões na condução). O Validador interpretou como a Regra F (conclusão definitiva misturada com dúvida estrutural).
- **Caso 3:** Apresentava dinâmica similar, contendo `[VERIFICAR]` gerado pela Regra N2 (autotutela) e palavras flexionais fortes em bullets adjacentes.

## C. Correção implementada
Para homogeneizar o comportamento do normalizador e do validador, adotou-se as seguintes medidas seguras:
- **Detector único de conclusão forte:** Foi criada a função `_tem_conclusao_forte(texto)` que utiliza `TERMOS_CONCLUSAO_FORTE` para verificação de substring, exatamente da mesma forma como operava a Regra F isoladamente.
- **N4 por parágrafo lógico agrupado:** A Regra N4 foi ajustada para consumir a mesma varredura de quebra lógica e utilizar o detector recém-criado.
- **Tratamento de variações `configur*`:** O `_tem_conclusao_forte` resolveu automaticamente a assimetria das substrings sem necessitar de novas expressões regulares complexas.
- **Tratamento de bullets/listas:** Em respeito ao padrão de segurança máxima ("Preferência B"), constatado um parágrafo lógico unificado contendo o perigoso combo de `[VERIFICAR]` nativo + `conclusão forte`, o bloco inteiro é transformado num remetimento seguro: `[VERIFICAR: fundamento não localizado para emitir declaração jurídica de mérito. Requer análise técnica por autoridade competente.]`. Isso blinda a peça sem risco de falha.
- **Defesa do N1 Trap:** Implementou-se salvaguarda para impedir que a N4 desativasse parágrafos que foram deliberadamente neutralizados pela Regra N1 do próprio normalizador (ex: detecção direta de crime militar).

## D. Testes simulados
- **Testes de saneamento (Passaram perfeitamente):** Casos simulados com `[VERIFICAR]` + "configurando", "configurar", ou "legitimando" no mesmo bloco foram limpos pelo normalizador e aprovados no validador.
- **Testes de segurança (Continuaram Bloqueando):** Expressões flagrantes sem `[VERIFICAR]`, como peculato-desvio, teoria dos frutos e vício insanável continuaram reprovando as defesas corretamente. Invenções brutas disfarçadas de `[PADRÃO] O fato configura crime militar` seguiram a armadilha do N1 e também bloquearam.
- **Testes de integridade:** Constantes como `[RE não informado]`, SV11 explícitas e despachos não sofreram adulterações destrutivas.

## E. Testes com saídas reais da 8.7-f
- Ao submeter a saída bruta que reprovou a 8.7-f do **Caso 1**, o normalizador detectou o conflito de lista com `configurando` e a substituiu corretamente. A Regra F parou de bloquear o documento (a saída só bloqueou de fato na simulação local avulsa por uma Regra B isolada onde o LLM ocasionalmente esqueceu de colocar o `[FONTE:]` nativo).
- A saída real isolada do **Caso 3** foi processada, ativando corretamente a Regra N2 na autotutela. Ela não colidiu em falsos positivos da N4 e foi aprovada integralmente (com alertas didáticos).

## F. Impacto no Caso 2
Nulo. O normalizador não foi sensibilizado pelo vocabulário contido no Acidente de Viatura.

## G. Riscos remanescentes
A Preferência B de neutralização apaga o bloco inteiro se ele juntar indevidamente o alerta com uma conclusão forte. Se o modelo redigir um Bloco 2 gigantesco agrupando quase todos os fundamentos numa única super-lista sem `\n\n`, o normalizador neutralizará essa análise jurídica como um todo.

## H. Próxima etapa recomendada
`8.7-h — Reteste finalíssimo dos 3 casos, sem nova alteração prévia.`
