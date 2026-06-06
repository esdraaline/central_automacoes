# 📍 Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint (pelo Claude Code durante o build).
**Última atualização: 05/06/2026**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execução** | Nenhuma (entre sprints — documentação em dia) |
| **Última fase concluída** | Fase 1 — Logins simples ✅ |
| **Próximo passo (trilha principal)** | Fase 2 — Validar BOPM (Sprint 2.1) |
| **Trilha paralela disponível** | Fase 7 — Despachadora (Sprint 7.1 de investigação) — pode ser iniciada a qualquer momento |

---

## Já feito

- Scaffold, migração do BOPM, decisões A/B/C
- **Fase 0 · Sprint 1 ✅** — `nucleo/` criado (segredos, log, vpn, browser), credenciais migradas para `segredos.env`, BOPM testado pela linha de comando
- **Fase 0 · Sprint 2 ✅** — Contrato (`manifesto.py` + `executar.py`), `painel.py` com customtkinter; botão "Baixar BOPMs" roda o BOPM com log ao vivo na janela
- **Fase 1 · Sprint 1 ✅** — módulos `nucleo/login_mapa_forca.py` e `nucleo/login_dejem.py` criados; botões reais Abrir Mapa Força e Abrir Dejem/Delegada criados; Teste de Logins mantido como diagnóstico
- **Decisão D-06 ✅** — SEI removido do escopo de automação; acesso ao SEI será manual
- **Decisão D-07 ✅** — Despachadora: código na Central, corpus no Drive; `GEMINI_API_KEY` e `CORPUS_PATH` via `segredos.env`
- Aprendizados da validação registrados em `docs/APRENDIZADOS.md`

---

## Próximo passo

**Trilha principal:** Iniciar Fase 2 — Validar BOPM (Sprint 2.1) quando autorizado.

**Trilha paralela (pode iniciar a qualquer momento):** Fase 7 — Despachadora · Sprint 7.1 (investigação — Claude Code lê a Central e propõe plano de port, sem escrever código).

---

## Bloqueios / pendências

Nenhum bloqueio técnico. Dependências instaladas e painel abre.

**Restrições técnicas identificadas para a Fase 7 (não bloqueiam hoje — investigar no Sprint 7.1):**
- Input de arquivo: painel atual não tem campo para receber arquivo(s) — extensão necessária.
- Saída longa: mecanismo de exibição dos 6 blocos ainda a definir.
- `indexar_corpus.py`: `SKILL_ROOT` hardcoded na linha 38 — adaptar para `CORPUS_PATH` de `segredos.env`.
- `despachadora.py`: `CORPUS_FILE` relativo ao script — ajuste de path ao mover para `nucleo_despachadora/`.
- `.gitignore`: cobrir pastas do corpus (P1–P5, JD, Notebooklm) antes do Sprint 7.2.
- `segredos.env.exemplo`: atualizado com `GEMINI_API_KEY` e `CORPUS_PATH` ✅

---

## Como manter este arquivo

Ao fim de cada sprint, atualizar: a data, **Onde estou**, **Já feito**, **Próximo passo** e **Bloqueios**. Mantenha curto — é uma foto, não um diário. O diário detalhado fica no ROADMAP.md (Histórico).
