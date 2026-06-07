# 📍 Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint (pelo Claude Code durante o build).
**Última atualização: 06/06/2026 (noite)**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execução** | Fase 7 — Despachadora (em paralelo com Fase 2) |
| **Última fase concluída** | Fase 2 · Sprint 2.1 ✅ (validado em campo 06/06/2026) |
| **Sprint atual** | Sprint 7.2 — port do núcleo da Despachadora |
| **Próximo passo (trilha principal)** | Sprint 7.2: colar implementação do Drive em `nucleo_despachadora/`, rodar caso de teste end-to-end |
| **Trilha pendente (Fase 2)** | Sprint 2.2 — relatório em `saidas/validacao_bopm_<data>.txt` (após validar fix double-Retornar em 08/06) |

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
- **Fase 7 · Sprint 7.1 ✅** — Diagnóstico completo: mecanismo de descoberta/contrato mapeado; lacunas de input e saída longa identificadas; adaptações mínimas de `despachadora.py` descritas; .gitignore e `segredos.env.exemplo` verificados. Decisões aprovadas: Input=A (Contexto opcional), Saída=A (CTkToplevel), corpus_index=git direto.

---

## ⚠️ PRÓXIMO PASSO IMEDIATO (retomada em outra máquina)

1. `git pull` para puxar todos os commits recentes (fix double-Retornar + scaffold Sprint 7.2).
2. **Sprint 7.2 — completar port do núcleo:**
   - Copiar `despachadora.py` e `indexar_corpus.py` do Drive para `automacoes/despachadora/nucleo_despachadora/`
   - Colar a implementação do Drive nas seções marcadas com `# COLE AQUI` de cada arquivo
   - Rodar caso de teste end-to-end com um expediente real
3. **Validar fix double-Retornar (a partir de 08/06/2026):** rodar "Validar BOPM" com um BO pendente real e confirmar Edge na listagem. Após confirmação: Sprint 2.2.

> Sprint 7.1 concluído. Sprint 7.2 scaffold criado — pendente cola da implementação do Drive.

---

## Próximo passo

**Trilha principal:** Sprint 7.2 — colar implementação do Drive nos scaffolds de `nucleo_despachadora/` e rodar caso de teste end-to-end.

**Trilha pendente:** Sprint 2.2 — relatório `saidas/validacao_bopm_<data>.txt` (aguarda validação do fix double-Retornar em 08/06/2026).

---

## Bloqueios / pendências

**Fase 7 · Sprint 7.2 — em andamento:**
- Scaffold criado: `automacoes/despachadora/`, `nucleo_despachadora/despachadora.py`, `nucleo_despachadora/indexar_corpus.py`
- Pendente: colar implementação do Drive nas seções `# COLE AQUI` e validar end-to-end

**Fase 2 · Sprint 2.2 — pendente (aguarda 08/06/2026):**
- Validar fix double-Retornar em campo, então gerar relatório `saidas/validacao_bopm_<data>.txt`

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
