# Priorização de Fontes Autônomas no Retrieval — Sprint 8.6-d

## A. Estado inicial

* Commit base: `19df43b fix(despachadora): reduz falsos positivos do validador`
* Working tree: limpo
* Corpus: 707 entradas válidas, sem alteração
* Pool fundamento (POOL_FUNDAMENTO_N): 12 slots

---

## B. Diagnóstico antes do ajuste

### Posição das fontes autônomas por caso

| Caso | Fonte autônoma | Score | Posição no pool | Status |
|------|----------------|------:|----------------:|--------|
| 1 — Algemas | `corpus_manual/Sumula_Vinculante_11_Algemas.md` | 5.27 | fora (mínimo: 8.77) | ❌ Ausente |
| 2 — Acidente | `corpus_manual/Acidente_Viatura_Providencias.md` | 7.25 | 4º | ✅ Presente |
| 3 — IPM | `corpus_manual/Sumula_473_Autotutela.md` | 0.09 | fora (mínimo: 8.90) | ❌ Ausente |
| 3 — IPM | `corpus_manual/Competencia_IPM.md` | 5.39 | fora (mínimo: 8.90) | ❌ Ausente |
| 3 — IPM | `corpus_manual/Competencia_Prazos_Sindicancia.md` | 5.61 | fora (mínimo: 8.90) | ❌ Ausente |

### Causa raiz

1. **Súmula 473** (0.09): os termos-gatilho do conteúdo da fonte (`autotutela`, `anular`) **não aparecem** no expediente do Caso 3. O usuário usa `invalidação` e `remessa` — palavras que não constam no texto da súmula. Score base mínimo. Nenhum literal boost aplicável.

2. **SV11, Competencia_IPM, Competencia_Prazos_Sindicancia**: arquivos pequenos (986–2416 chars) vs POPs grandes (>10.000 chars). Mesmo com boost literal de +5.0 por correspondência de termos, o score final (5.27–5.61) ficou ~3.3–3.5 pontos abaixo do limiar do pool (8.77–8.90).

3. **Raiz estrutural**: a normalização por tamanho `count / len(texto)**0.5` prejudica arquivos pequenos e precisos em relação a POPs grandes com muitos termos genéricos.

---

## C. Ajuste implementado

### Função `_boost_fontes_autonomas(scored, query_text)`

Aplica boost adicional de `+5.0` a fontes `corpus_manual/` quando **pelo menos um gatilho temático específico** está presente no texto do expediente.

Mapa de gatilhos:

| Arquivo | Gatilhos (must match ≥1 in query) |
|---------|----------------------------------|
| `Sumula_Vinculante_11_Algemas.md` | `algema`, `algemas`, `uso de algemas`, `receio de fuga`, `justificativa por escrito`, `compartimento de presos` |
| `Sumula_473_Autotutela.md` | `autotutela`, `anular`, `revogar`, `invalidação`, `invalidar`, `nulidade`, `vício`, `incompetência`, `anulação` |
| `Competencia_IPM.md` | `ipm`, `inquérito policial militar`, `autoridade instauradora`, `instauradora`, `incompetência da autoridade`, `instauração de ipm` |
| `Competencia_Prazos_Sindicancia.md` | `sindicância`, `prazo de sindicância`, `instauração de sindicância`, `prorrogação`, `competência para instaurar`, `instaurar sindicância` |
| `Acidente_Viatura_Providencias.md` | `acidente`, `colisão`, `vítima civil`, `dano ao erário`, `ressarcimento` |

**Regra de precisão**: gatilhos propositalmente específicos para evitar falsos positivos. `encarregado`, `portaria`, `competência` sozinhos foram excluídos porque aparecem em expedientes de outros temas.

### Função `_incluir_autonomas_garantidas(pool_f, scored_normas, query_text)`

Se após o boost uma fonte autônoma pertinente ainda ficar fora do `pool_f`, ela é **inserida por inclusão garantida**:

1. Identifica candidatas pertinentes ausentes do pool;
2. Remove o item de menor score **não-autônomo** do pool;
3. Insere a candidata e re-ordena;
4. Máximo de 3 fontes autônomas por caso.

### Onde na função `recover_chunks`

```
Passo 1: Pontuação base + literal boost (existente)
Passo 2: Boost das pistas dos modelos (existente)
Passo 3: Boost de fontes autônomas pertinentes  ← NOVO (8.6-d)
Passo 4: Partição dos pools
Passo 4.5: Inclusão garantida de autônomas      ← NOVO (8.6-d)
```

---

## D. Resultado após ajuste

| Caso | Fonte autônoma | Posição antes | Posição depois | Status |
|------|----------------|:-------------:|:--------------:|--------|
| 1 | `Sumula_Vinculante_11_Algemas.md` | Ausente | **1º** (13.27) | ✅ |
| 2 | `Acidente_Viatura_Providencias.md` | 4º (7.25) | **1º** (12.25) | ✅ |
| 3 | `Competencia_Prazos_Sindicancia.md` | Ausente | **1º** (13.61) | ✅ |
| 3 | `Competencia_IPM.md` | Ausente | **11º** (8.39) | ✅ |
| 3 | `Sumula_473_Autotutela.md` | Ausente | **12º** (5.10)* | ✅ |

*Score 5.10 via inclusão garantida (base muito baixo porque os termos do expediente não coincidem com o texto da súmula).

---

## E. Recuperação dos 3 casos (top chunks relevantes)

### Caso 1 — Algemas
1. `corpus_manual/Sumula_Vinculante_11_Algemas.md` (13.27) ← **SV 11 agora em 1º**
2. `P3/POPs/Processo-1.01.00-Abordagem-de-Pessoas-a-Pe.pdf` (9.87)
3. `P3/POPs/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` (9.83)
4. `P3/POPs/Processo-1.02.00-AbordagemPolVtr4Rodas.pdf` (9.67)
5. `P3/POPs/Processo-5.03.00_Uso-de-algemas.pdf` (9.50)

### Caso 2 — Acidente
1. `corpus_manual/Acidente_Viatura_Providencias.md` (12.25) ← **Posição melhorada (era 4º)**
2. `P3/POPs/Processo-3.01.00-Acidente-de-Transito.pdf` (8.12)
3. `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf` (7.78)
4. `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI Nº PM3-002-02-17 - Acidente Vtr.pdf` (7.76)

### Caso 3 — IPM/autotutela
1. `corpus_manual/Competencia_Prazos_Sindicancia.md` (13.61) ← **nova entrada em 1º**
2. `JD/PPJM/Manuais, Leis, Regulamentos/I-16-PM.pdf` (9.82)
3. `JD/PPJM/Manuais, Leis, Regulamentos/RDPM atualizado 21MAR25.pdf` (9.35)
4. `Normas/Orientacoes_Direito_Militar_Segmentos/...` (doutrina)
11. `corpus_manual/Competencia_IPM.md` (8.39) ← **nova entrada**
12. `corpus_manual/Sumula_473_Autotutela.md` (5.10) ← **nova entrada via inclusão garantida**

---

## F. Testes do validador

```
testar_validador_8_6_b.py: 12/12 testes passaram ✅
```

Validador inalterado. Nenhuma regressão.

---

## G. Riscos remanescentes

1. **Gemini ainda pode não citar a fonte**: mesmo presente no contexto, o Gemini pode usar os conceitos sem citar as fontes autônomas como `[FUNDAMENTO]+[FONTE:]`. O prompt reforçado na Sprint 8.6-b instrui explicitamente, mas não há garantia absoluta sem teste real.

2. **Súmula 473 com score baixo (5.10)**: entrou via inclusão garantida, mas aparece em 12º lugar, após 11 fontes com scores mais altos. O Gemini pode não ponderar adequadamente uma fonte no final do contexto. Se necessário, a Sprint 8.6-e poderá reordenar o contexto para colocar fontes autônomas primeiro.

3. **Competencia_Prazos_Sindicancia em 1º no Caso 3**: é uma fonte pertinente, mas o Caso 3 menciona especificamente IPM. A fonte de prazos de sindicância pode fazer o Gemini focar em sindicância quando a dúvida real é sobre competência de IPM. Monitorar no reteste.

4. **Nenhum teste real com Gemini nesta sprint**: toda validação foi local (scoring, sem API). O reteste real é a Sprint 8.6-e.

---

## H. Próxima etapa recomendada

**Sprint 8.6-e** — Reteste manual dos 3 casos no painel com fontes autônomas priorizadas.

Objetivo: verificar se o Gemini agora cita as fontes autônomas como `[FUNDAMENTO]+[FONTE:]` e se os bloqueios do validador foram eliminados nos Casos 1 e 3.
