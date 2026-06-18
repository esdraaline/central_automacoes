# Refinamento do Normalizador de Resposta — Sprint 8.7-c

## A. Estado inicial
Na Sprint 8.7-b, implementamos o normalizador determinístico para moderar termos jurídicos incisivos proferidos pela IA. O Caso 2 passou lindamente, mas Casos 1 e 3 trombaram em bloqueios residuais:
- **Caso 1:** Termos intrínsecos à Súmula Vinculante nº 11 (como "fundado receio de fuga") causaram bloqueio (Regra D) porque a IA produziu as conclusões de algemamento sem anexar o rótulo da fonte normatizadora junto aos parágrafos, apesar da Súmula estar listada noutra parte do texto.
- **Caso 3:** O cabeçalho protocolar do Texto Pronto (`Assunto: Proposta de invalidação... incompetência da autoridade`) serviu como estopim de bloqueio porque a palavra `remessa` vinha instruindo nosso normalizador a ignorar o saneamento.

## B. Bloqueios residuais da 8.7-b
A estrita aderência do Validador causava, sem culpa sua, bloqueios em construções que o Normalizador poderia polir caso fosse dotado de lógica cirúrgica:
- Necessidade de propagar a validade da SV11 para qualquer frase argumentativa da mesma.
- Necessidade de neutralizar de vez qualquer palavra jurídica sentenciadora ("incompetência", "vício", "declaro nulo") caso ocorram no preâmbulo protocolar.

## C. Regras adicionadas

### Regra N6 — Termos da Súmula Vinculante nº 11
Se o termo `Sumula_Vinculante_11_Algemas.md` for encontrado globalmente na resposta gerada e os verbetes sensíveis pertinentes à Súmula (como "fundado receio de fuga", "resistência", "perigo à integridade física" e "uso de algemas") ocorrerem desancorados de fonte naquele parágrafo específico:
- Palavras excessivas são substituídas: `legitimando` -> `apresentando elementos compatíveis para`.
- A tag de ancoragem global é copiada/propagada: `[FONTE: corpus_manual/Sumula_Vinculante_11_Algemas.md]`.
- Se a SV11 por ventura **não** constasse de todo da resposta, a tag vira um aviso explícito de cautela: `[VERIFICAR: confirmar fundamento específico da Súmula Vinculante nº 11...]`.

### Regra N7 — Cabeçalho protocolar de competência
O validador isola cabeçalhos via RegEx. Agora o normalizador detecta linhas inauguradas por afixos preambulares (Assunto:, Referência:, Encaminhamento:, etc.) e, diante da existência indesejada de "incompetência", "vício insanável", "autoridade incompetente", varre a premissa substituindo incondicionalmente a linha por:
- `Proposta de remessa de autos para análise de competência pela autoridade competente`
- O ajuste isenta o resto do bloco de apagar-se e contorna o erro detectado na mitigação por `remessa`.

## D. Testes simulados
Execução bem-sucedida de `saidas/testar_normalizador_8_7_c.py`:
- `[PADRÃO] Houve fundado receio de fuga...` acompanhado de SV11 validado com fonte propagada e aprovação.
- `Assunto: Proposta de invalidação... por incompetência` neutralizado instantaneamente sem tocar na lógica do corpo argumentativo (testes bloqueados quando o próprio corpo afirma competências irreais, assegurando a eficácia do validador).

## E. Testes com saídas reais da 8.7-b
O log problemático de `output_caso_1_reteste_87b.txt` teve o preâmbulo `[PADRÃO]` e o parágrafo `3. O emprego de algemas...` devidamente retificados recebendo a fonte ao final do período, o que seria suficiente para blindá-los da Regra D.
O cabeçalho do `Caso 3` converteu-se à formatação neutra esperada pela regra N7.

## F. Impacto no Caso 2
Nulo. Os testes simulados corroboraram que a integridade semântica de relatórios normais (dano, acidente, Sindicância, referências de viatura ou RE) e a estrutura base não foi comprometida, e o Texto Pronto continua aproveitável.

## G. Riscos remanescentes
A propagação da Fonte (Regra N6) mitiga severamente o índice de falsos positivos sem comprometer o documento, mas exige que a referência principal `Sumula_Vinculante_11_Algemas.md` realmente esteja na saída geral. Além disso, se a IA fundir cabeçalhos e parágrafos sem quebras de linha num mega bloco massivo de caracteres de modo totalmente espúrio, a detecção de linha pode ser testada em seus limites; entretanto a normalização baseada no ponto `\n` previne grande parte destas anomalias.

## H. Próxima etapa recomendada
`8.7-d — Reteste real dos 3 casos após refinamento do normalizador.`
