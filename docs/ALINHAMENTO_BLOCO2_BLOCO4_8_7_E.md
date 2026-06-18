# Alinhamento Estrutural Bloco 2 → Bloco 4 e Refinamentos de Normalização (Sprint 8.7-e)

## A. Estado inicial
No estágio anterior, o normalizador aplicava heurísticas linha a linha. Ao tentar contornar a rigidez do validador (que exige `[FUNDAMENTO] + [FONTE:]` em conjunto no mesmo bloco), a lógica anexava forçadamente citações de fonte no final das linhas problemáticas. Adicionalmente, o validador interpretava quebras duplas de linha `\n\n` como blocos únicos, enquanto o normalizador avaliava quebras simples `\n`, gerando inconsistências no escopo analisado.

## B. Problemas da 8.7-d
- **Caso 1:** A Súmula Vinculante 11 foi citada perfeitamente no Bloco 2, e o Texto Pronto usou as terminologias derivadas do entendimento sumulado. O normalizador propagou a fonte para o Texto Pronto, mas não a tag `[FUNDAMENTO]`, resultando no bloqueio implacável da `[Regra D]`.
- **Caso 3:** A Regra N2 colocou um `[VERIFICAR]` no termo "autotutela". Porém, na linha imediatamente inferior (sem quebra de parágrafo dupla), havia a palavra `configura`. O normalizador `N4` (que remove conclusões fortes isoladas) não alcançou a segunda linha, mas o validador agrupou as duas linhas num mesmo parágrafo lógico, engatilhando a `[Regra F]` e bloqueando a resposta inteira.

## C. Ponte Bloco 2 → Bloco 4
Foi implementada uma função de leitura passiva do **Bloco 2 (Análise Jurídica)**, a `_extrair_termos_fundamentados_bloco2`.
- **Por que o Texto Pronto não deve conter `[FUNDAMENTO]`:** O Texto Pronto simula um documento administrativo real e final. Tags como `[FUNDAMENTO]` destroem a apresentação estética e quebram o fluxo de um expediente que será exportado e assinado pelo comandante.
- **Mecanismo:** Ao ler a resposta bruta, o validador agora guarda todos os termos sensíveis que **já constam amparados** pelo duo `[FUNDAMENTO] + [FONTE:]` restritamente no Bloco 2.
- **Tolerância Direcionada (Ponte):** Quando a `[Regra D]` escaneia o Bloco 4 (Texto Pronto) e encontra um desses termos, ela confere a "ponte". Se o termo já foi "carimbado" no Bloco 2, ele é poupado do bloqueio e gera apenas um alerta construtivo: *"Termo sensível usado sem fonte direta, mas já ancorado no Bloco 2"*.

## D. N4 por parágrafo lógico
O saneamento determinístico da **Regra N4** foi descolado do processamento linha a linha e transferido para uma etapa subsequente que processa o texto inteiramente subdividido em **parágrafos lógicos** (quebras por `\n\n`).
Isso alinhar o critério de visão da N4 com o do Validador. Assim, se o `[VERIFICAR]` brotar em uma frase e o termo de conclusão forte (ex.: `configura`) surgir no final do mesmo agrupamento, a N4 irá identificá-lo e substituí-lo por `[VERIFICAR: conclusão forte isolada neutralizada]`, imunizando o documento da `[Regra F]`.

## E. Limitação cautelosa do Texto Pronto em IPM/competência
Foi estabelecida a **Regra N8**. Quando detecta-se, no escopo de um parágrafo estrutural (típico do Bloco 4), múltiplos termos sugestivos de instrução correcional (ex: "ipm", "remessa", "autoridade instauradora") **somados** a termos perigosos absolutos sem fundamentação explícita (ex: "nulidade absoluta", "incompetência da autoridade"), o normalizador atua de ofício e substitui o bloco inteiro por um desfecho estritamente administrativo:
> *"Submeto os autos à apreciação da autoridade competente, para análise da competência administrativa, da regularidade da portaria instauradora e da providência cabível, evitando-se declaração automática de nulidade nesta minuta."*

## F. Testes simulados
O roteiro de testes em `testar_normalizador_8_7_e.py` ratificou os comportamentos almejados:
- **✅ PASSARAM/ALERTARAM:** Texto Pronto de SV11 fundamentada (ponte de termo); competência mitigada; cabeçalho N7; desativação de conclusões via N4 em parágrafos unificados.
- **✅ BLOQUEARAM:** "Nulidade absoluta" solta; "vício insanável" sem lastro.

## G. Testes com saídas reais da 8.7-d
Aplicadas as mesmas premissas aos cenários reais que fracassaram anteriormente:
- O **Caso 1**, valendo-se da ponte lógica, ignorou a falta de `[FUNDAMENTO]` e passaria ileso (entregue com alerta informativo).
- O **Caso 2**, imune aos bloqueios e perfeitamente equilibrado, permaneceu intacto.
- O **Caso 3**, com o nivelamento da N4 para o parágrafo lógico (captando o "configura" residual) associado à robustez da N8, conseguiria converter o trecho punitivo do "vício de competência" em linguagem submissa e remissiva, escapando das garras da Regra F.

## H. Riscos remanescentes
- Se o Gemini redigir uma conclusão de mérito forte e inusitada no Texto Pronto (com um termo que não estava no Bloco 2), o validador **continuará bloqueando** adequadamente a resposta.
- A herança semântica da ponte Bloco 2 -> Bloco 4 é rígida: o Bloco 2 precisa ter a estrutura tag-fonte perfeita para ceder a imunidade.
- Como o preâmbulo cauteloso de remessa (N8) é universal nos casos suspeitos, ofícios correcionais podem soar mais repetitivos ou defensivos.

## I. Próxima etapa recomendada
`8.7-f — Reteste final dos 3 casos.`
