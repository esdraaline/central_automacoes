# Contexto de Retorno — 16/06/2026

Fotografia para retomar o trabalho em outra máquina ou conversa sem perder o fio.

## Estado Atual

- Projeto: Central de Automações — Despachadora do Comandante.
- Branch: `main`.
- Fase 2 encerrada: Sprint 2.2 validado em campo (relatório validacao_bopm OK).
- Fase 7 encerrada: Despachadora integrada ao painel, testada com expedientes reais.
- Fase 8 em andamento: Sprints 8.1–8.3 + Patch + Revisão humana concluídos. Sprint 8.4 é o próximo passo.

## Números Atuais do Índice (pós-triagem 16/06/2026)

- Total de entradas: `605`
- `classificacao_origem=humana`: entradas revisadas na triagem das 199
- SHA-256 do índice pré-triagem: `3adf96695bcab1b080533ef049fb2c613ada822e1400d250ad3f0128045059e7`

Naturezas após triagem:

| Natureza | Situação |
|---|---|
| `NORMA` | Forte — mas RDPM e I-7-PM JD ainda NAO_CLASSIFICADO (ver Passo 1 abaixo) |
| `MODELO_DE_REDACAO` | Forte |
| `MODELO_PRECEDENTE` | Forte |
| `PRECEDENTE` | OK |
| `PROCEDIMENTAL` | POPs presentes |
| `NAO_CLASSIFICADO` | Resíduo de entradas não cobertas pela triagem das 199 |

## Próximo Passo — Sprint 8.4

**Problema:** Bloco 2 (Análise Jurídica) da Despachadora cita `[VERIFICAR]` onde deveria citar artigo de lei com confiança. O corpus é forte em modelos da casa mas fraco em fundamento normativo.

### Passo 0 — Teste de campo (FAZER PRIMEIRO, sem Claude Code)
Rodar 3 expedientes reais pelo painel (parte, ofício, despacho de IPM/sindicância). Anotar:
- Quantos `[VERIFICAR]` no Bloco 2?
- Fundamento rastreável `[FONTE: section/arquivo]` ou genérico?
- Artigo de lei citado sem fonte?

### Passo 1 — Quick wins (reclassificar sem ingestão nova)
Entradas já no corpus com texto volumoso mas `NAO_CLASSIFICADO`:
- `JD/PPJM/Manuais, Leis, Regulamentos/I-7-PM_7ª ed. Atual.pdf` → `NORMA` (95k chars)
- `JD/PPJM/Manuais, Leis, Regulamentos/RDPM atualizado 21MAR25.pdf` → `NORMA` (134k chars)
- `JD/PPJM/Manuais, Leis, Regulamentos/RDPM_LC915_out07.pdf` → `NORMA` (140k chars)

Reclassificar via CSV de reimport (3 linhas, `natureza_correta=NORMA`).

### Passo 2 — Ingestão de alta prioridade
- **Lei 18.442/2026** — AUSENTE no corpus (0 entradas). Reorganiza quadros PMESP. Urgente.
- **CTB** — artigos operacionais (alcoolemia, abordagem de veículo, acidente com vítima)
- **ECA** — artigos da 5ª Cia (apreensão de menor, medidas protetivas)

Deixar para depois: jurisprudência (risco sem URL atestada), CP/CPP completos (muito longos).

## Decisões Relevantes

- **D-11:** `MODELO_PRECEDENTE` é terceira natureza — não substituir `MODELO_DE_REDACAO` nem `PRECEDENTE`.
- **D-12:** `corpus_index.json` sincroniza pelo Drive, não pelo git.
- **D-13:** `natureza_correta=EXCLUIR` remove entrada do índice — operação humana via planilha, não automática.

## Arquivos Principais

- Classificador/reimportador: `automacoes/despachadora/nucleo_despachadora/classificar_corpus.py`
- Roadmap detalhado do Sprint 8.4: `docs/ROADMAP.md` (seção Sprint 8.4)
- Índice canônico: `G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs\corpus_index.json`
- Backups: `G:\Meu Drive\Arquivos Josemar\Trabalho\backups_corpus_index_despachadora\`

## Comandos Úteis

```powershell
git pull origin main

# Verificar SHA-256 do índice no Drive
Get-FileHash -Algorithm SHA256 "G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs\corpus_index.json"

# Reclassificar quick wins (Passo 1) — criar CSV com 3 linhas e rodar:
python automacoes\despachadora\nucleo_despachadora\classificar_corpus.py --reimport saidas\quick_wins_8_4.csv

# Indexar novos documentos ingeridos (Passo 2):
python automacoes\despachadora\nucleo_despachadora\indexar_corpus.py
```

## Sincronização Entre Máquinas

Via GitHub: código, documentação, prompts, `.gitignore`.

Via Google Drive (fora do git):
- Índice: `G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs\corpus_index.json`
- Backups: `G:\Meu Drive\Arquivos Josemar\Trabalho\backups_corpus_index_despachadora\`
