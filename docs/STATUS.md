# 📍 Status Atual
Foto do "onde estou agora". Atualizado ao fim de cada sprint (pelo Claude Code durante o build).
**Última atualização: 06/06/2026**

---

## Onde estou

| Campo | Valor |
|---|---|
| **Fase em execução** | Fase 2 — Validar BOPM |
| **Última fase concluída** | Fase 1 — Logins simples ✅ |
| **Sprint atual** | Sprint 2.1 — hotfix aplicado, aguardando re-teste em campo |
| **Próximo passo (trilha principal)** | Re-testar pelo painel com VPN + BOPM pendente real — fluxo real mapeado e corrigido em 06/06/2026 |
| **Trilha paralela disponível** | Fase 7 — Despachadora (Sprint 7.1 de investigação) — pode ser iniciada a qualquer momento |

---

## Já feito

- Scaffold, migração do BOPM, decisões A/B/C
- **Fase 0 · Sprint 1 ✅** — `nucleo/` criado (segredos, log, vpn, browser), credenciais migradas para `segredos.env`, BOPM testado pela linha de comando
- **Fase 0 · Sprint 2 ✅** — Contrato (`manifesto.py` + `executar.py`), `painel.py` com customtkinter; botão "Baixar BOPMs" roda o BOPM com log ao vivo na janela
- **Fase 1 · Sprint 1 ✅** — módulos `nucleo/login_mapa_forca.py` e `nucleo/login_dejem.py` criados; botões reais Abrir Mapa Força e Abrir Dejem/Delegada criados; Teste de Logins mantido como diagnóstico
- **Decisão D-06 ✅** — SEI removido do escopo de automação; acesso ao SEI será manual
- **Decisão D-07 ✅** — Despachadora: código na Central, corpus no Drive; `GEMINI_API_KEY` e `CORPUS_PATH` via `segredos.env`
- **Fase 2 · Sprint 2.1 ⏳ (hotfix aplicado — re-teste pendente)** — primeiro teste em campo (06/06/2026) revelou fluxo real: ícone correto é o 2º ("Editar Ocorrência"), botão é "Validar BO-e" (não "Validar BOPM"), confirmação via `window.confirm` nativo (não elemento HTML), e BOs não visualizados precisam de "Visualiza PDF" antes. Hotfix aplicado em `executar.py` e `siopm_navigator.py`.
- Aprendizados da validação registrados em `docs/APRENDIZADOS.md`
- **Fix Baixar BOPM ✅** — `siopm_navigator.py` corrigido para detectar também BOPMs com status "BO Informal" (antes só detectava "Não Formalizado"); validado com sucesso em execução real

---

## ⚠️ PRÓXIMO PASSO IMEDIATO (retomada em outra máquina)

1. `git pull` para puxar o hotfix.
2. Abrir o painel (`python painel.py`) com **VPN ativa**.
3. Clicar no botão **"Validar BOPM"** com pelo menos um BOPM pendente real no SIOPM.
4. Observar se o fluxo completo roda: Editar Ocorrência → (Visualiza PDF se necessário) → checkbox Outros → Validar BO-e → dialog aceito → Retornar.
5. Se ainda falhar: copiar o log e abrir nova sessão com o Claude Code.

> O fluxo real foi mapeado pelos prints de 06/06/2026 e o hotfix está aplicado. O re-teste confirma se todos os seletores batem.

---

## Próximo passo

**Trilha principal:** Validar pelo painel — clicar em "Validar BOPM" com VPN ativa e um BOPM pendente real. O log mostrará onde os seletores falharam (se falharem) com URL e elementos visíveis para mapeamento.

**Trilha paralela (pode iniciar a qualquer momento):** Fase 7 — Despachadora · Sprint 7.1 (investigação — Claude Code lê a Central e propõe plano de port, sem escrever código).

---

## Bloqueios / pendências

**Fase 2 · Sprint 2.1 — pendência remanescente após hotfix:**
- Comportamento pós-"Retornar" — confirmar no re-teste se a página volta corretamente à listagem e o próximo BOPM é processado sem erro.

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
