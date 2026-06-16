# Curadoria 8.4 — Fontes Oficiais

Data de abertura: 16/06/2026

---

## Passo 0 — Sincronização Drive (16/06/2026)

O índice do Drive estava na versão pré-triagem (729 entradas, SHA-256 `3ADF96...`).
O reimport da triagem humana (16/06) havia atualizado apenas o índice local.

**Ação:** índice local pós-triagem (605 entradas) copiado para o Drive antes de qualquer operação do Sprint 8.4.

- SHA-256 Drive após cópia: `7f5982f3c4acf763d8f7b09848317c949a599d96cb00ad04b12d9aeecf5f4ebf`
- SHA-256 local: idêntico — `OK`

---

## Passo 1 — Quick wins (reclassificação)

### Achado
As 3 entradas alvo já estavam classificadas como `natureza=NORMA` e `classificacao_origem=humana`
no índice local pós-triagem — foram cobertas pela triagem assistida de 16/06/2026.
O Drive não as refletia porque o índice do Drive estava desatualizado (resolvido no Passo 0).

### Entradas confirmadas no Drive

| Chave | Natureza | Origem | Texto |
|---|---|---|---|
| `JD/PPJM/Manuais, Leis, Regulamentos/I-7-PM_7ª ed. Atual.pdf` | NORMA | humana | 95.443 chars |
| `JD/PPJM/Manuais, Leis, Regulamentos/RDPM atualizado 21MAR25.pdf` | NORMA | humana | 134.871 chars |
| `JD/PPJM/Manuais, Leis, Regulamentos/RDPM_LC915_out07.pdf` | NORMA | humana | 140.343 chars |

### Prova de aditividade

```
Total entradas: 605
Chaves únicas: 605
OK: sem duplicatas

Naturezas:
  NORMA: 436
  MODELO_PRECEDENTE: 68
  PRECEDENTE: 39
  MODELO_DE_REDACAO: 33
  PROCEDIMENTAL: 16
  OUTRO: 8
  JURISPRUDENCIA: 5

Origens:
  heuristica: 530
  humana: 75

SHA-256 Drive: 7f5982f3c4acf763d8f7b09848317c949a599d96cb00ad04b12d9aeecf5f4ebf
```

---

## Passo 2 — Ingestão de normas ausentes

### 2.1 Lei 18.442/2026
- **Status:** AUSENTE no corpus (0 entradas)
- **Fonte branca:** `al.sp.gov.br` ou Diário Oficial SP
- **Aguardando:** arquivo trazido pelo operador

### 2.2 CTB — artigos operacionais
- **Status:** aguardando operador
- **Artigos alvo:** Art. 165–165-B (alcoolemia), Art. 269 (abordagem), Art. 302–304 (acidente com vítima)
- **Fonte branca:** Planalto

### 2.3 ECA — artigos operacionais
- **Status:** aguardando operador
- **Artigos alvo:** Art. 106, 171–174 (apreensão), Art. 98–101 (medidas protetivas)
- **Fonte branca:** Planalto

---

## O que ficou de fora e por quê

- **Jurisprudência:** risco jurídico sem URL atestada e data de captura verificável. Sprint posterior.
- **CP/CPP completos:** textos muito longos; busca por densidade se perde sem recorte temático.

---

## SHA-256 final do índice (Drive)

`7f5982f3c4acf763d8f7b09848317c949a599d96cb00ad04b12d9aeecf5f4ebf`

*(Atualizar ao concluir o Passo 2)*
