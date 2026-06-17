# Ajuste do Validador Pós-Gemini — Sprint 8.6-b

## A. Estado inicial

* Commit: `4ecaa04 docs(despachadora): fecha sprint 8.5 do corpus`
* Working tree: limpo
* Corpus: 707 entradas válidas, 731 chunks total
* Validador: 7 regras (A–G) ativas, sem ajustes desde Sprint 8.4-quater

---

## B. Diagnóstico dos bloqueios

### Caso 2 — Acidente com viatura (Regra E)

**Trecho bloqueador:**
```
[PADRÃO] **Situação da vítima civil (falta de CNH compatível):** A suspeita de falta de CNH compatível por parte do civi...
```

**Causa:** A Regra E detectou `[PADRÃO]` + termo jurídico `CTB` + termo de conclusão forte no mesmo parágrafo. O parágrafo era descritivo/factual (descrevia uma suspeita a verificar), não mascarava fundamento jurídico. Falso positivo.

### Caso 3 — IPM / competência (Regras D + G)

**Trecho bloqueador:**
```
Do Cmt 5ª Cia PM. Ao Sr. Subcmt 2º BPM/I. Assunto: Remessa de autos de IPM por incompetência da autoridade instauradora...
```

**Causa:** As Regras D e G detectaram `incompetência da autoridade` como conclusão definitiva no Bloco 4, mas o trecho era um **cabeçalho protocolar** (campo Assunto do ofício), não uma conclusão argumentativa. Bloqueio excessivo.

### Caso 1 — Algemas (fonte autônoma não citada)

**Causa:** A `Sumula_Vinculante_11_Algemas.md` está no corpus (1.688 chars, `JURISPRUDENCIA`) mas obteve score 5.27 (0.27 base + 5.0 literal boost por "algemas"). Os POPs de abordagem obtiveram ~9.5-9.87 por terem muitos mais termos coincidentes com a query. A SV11 ficou fora do top 12 do `pool_f`.

Mesmo assim, quando a fonte **está** presente no contexto, o Gemini rebaixou a referência para `[VERIFICAR]` em vez de citar como `[FUNDAMENTO]+[FONTE:]`. O prompt não tinha instrução explícita para priorizar fontes autônomas do `corpus_manual/`.

---

## C. Ajustes feitos

### 1. MASTER_SYSTEM_PROMPT — Fontes autônomas (Tarefa 3)

Adicionada seção `FONTES AUTÔNOMAS DO CORPUS_MANUAL` instruindo o modelo a citar fontes autônomas presentes no contexto como `[FUNDAMENTO]+[FONTE:]` antes de rebaixar para `[VERIFICAR]`.

### 2. MASTER_SYSTEM_PROMPT — Anti-RE fictício (Tarefa 4)

Adicionada seção `DADOS IDENTIFICADORES — NUNCA INVENTAR` proibindo fabricação de RE, matrícula, placa, portaria, BOPM, data ou nome não presentes no expediente. Instrui uso de placeholders como `[RE não informado]`.

### 3. Regra E — Tolerância para [PADRÃO] cauteloso (Tarefa 5)

Antes: qualquer `[PADRÃO]` + termo jurídico + conclusão forte → bloqueio.
Depois: se o parágrafo contém expressão cautelosa (`possível`, `eventual`, `consta`, `a verificar`, `[VERIFICAR]`, etc.) → **alerta** (não bloqueio). Se é cabeçalho protocolar → **alerta**. Conclusão forte sem cautela → continua bloqueando.

### 4. Regra D — Tolerância para cabeçalhos (Tarefa 6)

Adicionado `Caso 0` antes dos demais: se o parágrafo é cabeçalho protocolar (detectado por `_eh_cabecalho_protocolar`), gera **alerta** em vez de bloqueio.

### 5. Regra G — Tolerância para cabeçalhos no Bloco 4/6 (Tarefa 7)

Adicionada verificação `_eh_cabecalho_protocolar` no loop de parágrafos com termo novo: se o termo sensível aparece em cabeçalho protocolar, gera **alerta** em vez de bloqueio.

### 6. EXPRESSOES_CAUTELOSAS — Expandidas

Adicionados: `possível`, `suposta`, `consta`, `relatado`, `a verificar`, `eventual`, `ponto de apuração`, `submeter à análise`.

### 7. Função auxiliar `_eh_cabecalho_protocolar`

Detecta parágrafos que começam com prefixos administrativos (`Assunto:`, `Referência:`, `Do `, `Ao `, etc.) e são curtos (< 200 chars). Usada pelas Regras D, E e G.

---

## D. Testes simulados

12 cenários testados com `saidas/testar_validador_8_6_b.py`:

### Deve passar (não bloquear)

| # | Cenário | Resultado |
|---|---------|-----------|
| 1 | `[PADRÃO]` factual com CTB e "possível" | ✅ ALERTA |
| 2 | Cabeçalho protocolar com "incompetência" | ✅ ALERTA |
| 3 | `Referência: IPM instaurado para apuração` | ✅ OK |
| 4 | Cabeçalho + corpo cauteloso com `[VERIFICAR]` | ✅ ALERTA |

### Deve bloquear

| # | Cenário | Resultado |
|---|---------|-----------|
| 5 | `[PADRÃO]` + competência + "configura" | ✅ BLOQUEADO |
| 6 | `[PADRÃO]` + crime militar + conclusão forte | ✅ BLOQUEADO |
| 7 | Peculato sem fonte | ✅ BLOQUEADO |
| 8 | Frutos da árvore envenenada sem fonte | ✅ BLOQUEADO |
| 9 | `[FUNDAMENTO]` sem `[FONTE:]` | ✅ BLOQUEADO |
| 10 | `[VERIFICAR]` + conclusão forte "nulo" | ✅ BLOQUEADO |
| 11 | `Bloco 4.1` (termo proibido absoluto) | ✅ BLOQUEADO |
| 12 | Fundamento novo no Bloco 4 como conclusão | ✅ BLOQUEADO |

**Resultado: 12/12 passaram.**

---

## E. Resultado com saídas reais

As saídas brutas do Gemini para os Casos 2 e 3 não foram capturadas (o validador as substituiu pelo bloqueio antes de salvar). Os testes simulados usam snippets baseados nos logs reais capturados em `task-1064.log`.

O snippet do Caso 2 simulado (com "possível" adicionado para representar o cenário factual real) agora gera ALERTA em vez de BLOQUEIO.

O snippet do Caso 3 simulado (cabeçalho `Assunto: Remessa por incompetência...`) agora gera ALERTA em vez de BLOQUEIO.

---

## F. Riscos remanescentes

1. **SV11 fora do top 12:** A fonte autônoma `Sumula_Vinculante_11_Algemas.md` obtém score 5.27 contra POPs que obtêm ~9.5. Pode continuar ficando fora do pool de fundamento se houver muitos POPs relevantes. Uma futura melhoria seria dar boost adicional a fontes do `corpus_manual/` quando keywords da query coincidem com o nome do arquivo.

2. **Cabeçalhos longos:** A heurística de 200 chars pode falhar em cabeçalhos incomumente longos. Risco baixo — cabeçalhos protocolares reais são curtos.

3. **Falsos negativos cautelosos:** A expansão de `EXPRESSOES_CAUTELOSAS` com "possível" e "eventual" pode tolerar parágrafos que deveriam bloquear se o Gemini combinar termo cauteloso com conclusão forte na mesma frase. Risco mitigado: a Regra F (`[VERIFICAR]` + conclusão forte) continua ativa.

---

## G. Próxima etapa recomendada

1. **Sprint 8.6-b.1** — Re-rodar os 3 casos de teste com as correções aplicadas e verificar se os bloqueios foram eliminados e as respostas são úteis.

2. **Sprint 8.6-c** — Avaliar boost adicional para fontes `corpus_manual/` no recuperador, caso a SV11 continue fora do pool.

3. **Sprint 8.6-d** — Revisão de push/deploy.
