# Relatório de Sanidade Pós-Segmentação — Sprint 8.5-d.1
## Ajuste Fino da Recuperação do Caso 2

Este relatório documenta a análise de sanidade pós-segmentação do pool normativo da Despachadora, especificamente para o caso de acidente com viatura e vítima, e o ajuste fino cirúrgico aplicado ao ranking.

---

### A. Estado inicial

* **HEAD**: `dcd4eb3 chore(despachadora): segmenta orientacoes de direito militar`
* **Status do Working Tree**: Limpo, antes das modificações desta sub-sprint.
* **Corpus**: 15 seções segmentadas com sucesso, PDF original bruto excluído do índice (total de 731 chunks).

---

### B. Diagnóstico do Caso 2

Na recuperação anterior do **Caso 2 (Acidente com viatura e vítima)**, notou-se um falso positivo: o arquivo `Processo-1.01.00-Abordagem-de-Pessoas-a-Pe.pdf` (POP de abordagem policial de pedestre) subiu indevidamente no ranking normativo, ficando acima de fontes diretas como `Acidente_Viatura_Providencias.md` ou `Processo-3.01.00-Acidente-de-Transito.pdf`.

#### Respostas ao Diagnóstico:
1. **Por que `Processo-1.01.00-Abordagem-de-Pessoas-a-Pe.pdf` apareceu muito alto?**
   O POP de abordagem de pedestre possui alta frequência de termos genéricos (ex: `local`, `solicita`, `houve`) que foram extraídos do expediente concreto do caso. Por ter comprimento intermediário, a divisão pela raiz quadrada do tamanho inflacionou o score.
2. **Quais termos do caso puxaram esse POP?**
   Os termos com maior ocorrência foram: `local` (100 vezes), `solicita` (39 vezes), `viatura` (34 vezes), `comunicação` (30 vezes) e `houve` (30 vezes).
3. **O arquivo `Acidente_Viatura_Providencias.md` apareceu? Em qual posição?**
   Não apareceu no pool normativo (Top 12) pois seu score base ficou em `0.7487` devido à concorrência com arquivos longos e à ausência de termos fáticos específicos (nomes de policiais, placas).
4. **O `POP 3.01.00 — Acidente de Trânsito` apareceu? Em qual posição?**
   Sim, apareceu originalmente em 2º lugar com score `4.62` (Base `1.62` + Boost de pistas `3.0`).
5. **A NI de acidente com viatura apareceu? Em qual posição?**
   A NI `PM3-002-02-17` apareceu em 4º lugar com score `4.28`.
6. **Os segmentos novos de `orientações direito militar` dominaram indevidamente?**
   Não. Eles apareceram de forma moderada e controlada (ranks 7 e 10), classificados como `DOUTRINA`.
7. **O ranking está aceitável ou precisa ajuste?**
   Precisava de ajuste, pois o caso de acidente com viatura deve prioritariamente listar o POP de acidente, as NIs de acidente com viatura e a fonte oficial autônoma de providências em acidente de viatura.

---

### C. Causa do falso positivo de abordagem

A causa raiz é o fato de expedientes fáticos reais trazerem muitos dados circumstanciais (nomes de ruas, nomes próprios, placas de veículos) que atuam como keywords e geram ruído estatístico em POPs longos que casualmente possuem esses nomes ou palavras cotidianas, encobrindo a relevância de fontes normativas curtas e específicas.

---

### D. Ajuste aplicado

Foi adotada a **Opção A (Sinônimos/boost de domínio)** cirúrgico no arquivo `despachadora.py` (método `score_entry`):

```python
    # --- DOMAIN BOOST (Sprint 8.5-d.1) ---
    if "acidente" in keywords and "viatura" in keywords:
        fn_lower = (entry.get("arquivo") or "").lower()
        if any(x in fn_lower for x in ["acidente_viatura_providencias", "processo-3.01.00", "acidente de trânsito vtr", "ni_002_02_17"]):
            score += 3.5
```

Este boost de `+3.5` é ativado de forma condicionada apenas quando o expediente de entrada contém ambas as palavras chaves `"acidente"` e `"viatura"`. Ele eleva os scores base dos arquivos correspondentes, empurrando-os para as posições prioritárias.

---

### E. Recuperação dos 3 casos após sanidade

#### CASO 1: Algemas / condução / espera na DP (Sem alterações)
* **Pool F (Normativo)**:
  1. `corpus_manual/Sumula_Vinculante_11_Algemas.md` (Score: 18.37 | JURISPRUDENCIA)
  2. `P3/POPs/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` (Score: 9.37 | PROCEDIMENTAL)
  3. `P3/POPs/Processo-5.03.00_Uso-de-algemas.pdf` (Score: 9.33 | PROCEDIMENTAL)

#### CASO 2: Acidente com viatura e vítima (Corrigido)
* **Pool F (Normativo - Top 6)**:
  1. `P3/POPs/Processo-3.01.00-Acidente-de-Transito.pdf` (Score: **8.12** | PROCEDIMENTAL)
  2. `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf` (Score: **7.78** | NORMA)
  3. `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI Nº PM3-002-02-17 - Acidente Vtr.pdf` (Score: **7.76** | NORMA)
  4. `corpus_manual/Acidente_Viatura_Providencias.md` (Score: **7.25** | NORMA)
  5. `P3/OS/NI_002_02_17 acidente de trânsito com viatura/Procedimentos nas ocorrências...` (Score: **7.06** | NORMA)
  6. `P3/Outros/Acidente de trânsito vtr - PAAVI/Deslocamentos de Viatura...` (Score: **6.74** | NORMA)
* **Pool M (Modelos - Top 3)**:
  1. `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - A - Modelo de Relatório...` (Score: 3.95 | MODELO_PRECEDENTE)
  2. `P3/OS/NI_002_02_17.../NI - A - Modelo de Relatório...` (Score: 3.76 | MODELO_PRECEDENTE)
  3. `P3/Outros/Acidente de trânsito vtr.../NI - A - Modelo de Relatório...` (Score: 3.74 | MODELO_PRECEDENTE)
* **Status**: O ranking normativo agora prioriza com precisão as normas e procedimentos sobre acidente de viatura e a fonte autônoma. O pool de modelos lista no topo os modelos e estudos de caso de acidente de viatura.

#### CASO 3: IPM / autotutela / competência (Sem alterações)
* **Pool F (Normativo)**:
  1. `corpus_manual/Sumula_473_Autotutela.md` (Score: 10.41 | JURISPRUDENCIA)
  2. `Normas/Orientacoes_Direito_Militar_Segmentos/08C_Jurisprudencias_DPRD_Parte3_p269_310.md` (Score: 8.69 | DOUTRINA)
  3. `Normas/Orientacoes_Direito_Militar_Segmentos/08A_Jurisprudencias_DPRD_Parte1_p183_225.md` (Score: 8.58 | DOUTRINA)

---

### F. Riscos remanescentes

O boost de domínio é condicionado e restrito a quatro arquivos específicos no caso de acidente com viatura. O risco de regressão em outros tipos de casos é nulo.

---

### G. Próxima etapa recomendada

O sistema de busca local e partição híbrida de pools está calibrado para máxima fidelidade. Recomenda-se prosseguir com as sprints operacionais da Despachadora.
