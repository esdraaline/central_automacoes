# 📍 Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint (pelo Claude Code durante o build).
**Última atualização: 06/06/2026 (tarde)**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execução** | Fase 2 — Validar BOPM ✅ |
| **Última fase concluída** | Fase 2 — Validar BOPM ✅ |
| **Sprint atual** | Sprint 2.1 ✅ — validado em campo: 1/1 BOPMs validados, zero falhas |
| **Próximo passo (trilha principal)** | Sprint 2.2 — relatório em `saidas/validacao_bopm_<data>.txt` |
| **Trilha paralela disponível** | Fase 7 — Despachadora (Sprint 7.1 de investigação) — pode ser iniciada a qualquer momento |

---

## Já feito

- Scaffold, migração do BOPM, decisões A/B/C
- **Fase 0 · Sprint 1 ✅** — `nucleo/` criado (segredos, log, vpn, browser), credenciais migradas para `segredos.env`, BOPM testado pela linha de comando
- **Fase 0 · Sprint 2 ✅** — Contrato (`manifesto.py` + `executar.py`), `painel.py` com customtkinter; botão "Baixar BOPMs" roda o BOPM com log ao vivo na janela
- **Fase 1 · Sprint 1 ✅** — módulos `nucleo/login_mapa_forca.py` e `nucleo/login_dejem.py` criados; botões reais Abrir Mapa Força e Abrir Dejem/Delegada criados; Teste de Logins mantido como diagnóstico
- **Decisão D-06 ✅** — SEI removido do escopo de automação; acesso ao SEI será manual
- **Decisão D-07 ✅** — Despachadora: código na Central, corpus no Drive; `GEMINI_API_KEY` e `CORPUS_PATH` via `segredos.env`
- **Fase 2 · Sprint 2.1 ✅** — validado em campo em 06/06/2026: fluxo completo (2º ícone → Visualiza PDF se necessário → Outros → Validar BO-e → dialog → Retornar). "Outros" é `<img id='W0236CHK_OUT'>` GeneXus, não checkbox HTML. Edge mantido aberto na listagem ao fim.
- Aprendizados da validação registrados em `docs/APRENDIZADOS.md`
- **Fix Baixar BOPM ✅** — `siopm_navigator.py` corrigido para detectar também BOPMs com status "BO Informal" (antes só detectava "Não Formalizado"); validado com sucesso em execução real

---

## ⚠️ PRÓXIMO PASSO IMEDIATO (retomada em outra máquina)

1. `git pull` para puxar fix do double-Retornar.
2. **Validar em campo (a partir de 08/06/2026):** rodar "Validar BOPM" com um BO pendente real e confirmar que o Edge fica aberto na listagem filtrada (não no formulário vazio). Commit `9a24716` corrige o bug — pendente confirmação em campo por falta de BO pendente no dia 06/06.
3. Após confirmação: Sprint 2.2 — relatório em `saidas/validacao_bopm_<data>.txt` com resultado por BOPM.

> Sprint 2.1 validado em campo. Fase 2 pode ser considerada 50% concluída (Sprint 2.2 pendente).

---

## Próximo passo

**Trilha principal:** Validar pelo painel — clicar em "Validar BOPM" com VPN ativa e um BOPM pendente real. O log mostrará onde os seletores falharam (se falharem) com URL e elementos visíveis para mapeamento.

**Trilha paralela (pode iniciar a qualquer momento):** Fase 7 — Despachadora · Sprint 7.1 (investigação — Claude Code lê a Central e propõe plano de port, sem escrever código).

---

## Bloqueios / pendências

**Fase 2 · Sprint 2.2 — próxima entrega:**
- Gerar relatório em `saidas/validacao_bopm_<data>.txt` com resultado por BOPM (critério de aceite da fase).

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
