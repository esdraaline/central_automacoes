# Fechamento Sprint 8.7 — Despachadora

## Resultado

Sprint 8.7 tecnicamente estabilizada.

## Arquitetura consolidada

Gemini bruto
→ normalizador determinístico
→ validador final
→ resposta entregue ou bloqueada

## Melhorias principais

- priorização de fontes autônomas;
- destaque de fontes autônomas no contexto normativo;
- exemplos obrigatórios de [FUNDAMENTO] + [FONTE:];
- normalizador determinístico antes do validador;
- ponte Bloco 2 → Bloco 4;
- alinhamento da N4 com Regra F;
- tratamento de bullets/listas;
- preservação de bloqueios críticos.

## Reteste final 8.7-h

### Caso 1 — Algemas
Entregue sem alertas.

### Caso 2 — Acidente com viatura
Entregue com alertas leves.

### Caso 3 — IPM / competência
Entregue com alertas protetivos.

## Limitações remanescentes

- sistema ainda depende de revisão humana para assinatura;
- temas IPM/competência devem permanecer cautelosos;
- OCR dos 51 PDFs pendente;
- scripts de teste em `saidas/` devem ser reorganizados futuramente para pasta própria de testes.

## Próxima sprint recomendada

Após push controlado:

1. OCR por lote dos PDFs pendentes; ou
2. organização dos scripts de teste; ou
3. teste ampliado com novos expedientes reais.
