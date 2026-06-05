# 🛣️ Roadmap

> **Como ler:** as **fases** são o mapa geral. Cada fase é quebrada em **sprints**
> com tarefas concretas — mas só detalhamos os sprints da fase **quando chegamos
> nela** (planejar os 6 em detalhe agora seria perder tempo que é pra construir).
> Marque `[x]` ao concluir. O "onde estou agora" fica no `STATUS.md`.

---

## ✅ Concluído antes das fases
- [x] Scaffold da central criado e salvo em `Projetos\central_automacoes`
- [x] Código do BOPM migrado para `automacoes/baixar_bopm/`
- [x] Decisões A/B/C registradas (`DECISOES.md`)

---

## Fase 0 — Fundação  *(próxima — detalhada)*

### Sprint 1 — Núcleo + segredos ✅
- [x] Criar `nucleo/segredos.py` (lê de `segredos.env`, interface `get("siopm")`)
- [x] Criar `segredos.env` a partir do `.exemplo` e preencher
- [x] Mover as senhas do `config.py` antigo para o `segredos.env`
- [x] Refatorar `vpn_manager.py` → `nucleo/vpn.py`
- [x] Refatorar parte de browser do `siopm_navigator.py` → `nucleo/browser.py`
- [x] Refatorar `logger_setup.py` → `nucleo/log.py`
- [x] Testar: BOPM ainda baixa rodando pelo código refatorado (linha de comando)

### Sprint 2 — Contrato + painel
- [x] Definir o contrato `manifesto.py` + `executar.py`
- [x] Adaptar `baixar_bopm/` ao contrato (manifesto + executar chamando o núcleo)
- [x] Criar `painel.py` (customtkinter): descobre automações, 1 botão, log ao vivo
- [x] Testar: clicar no botão "Baixar BOPMs" e baixar pela interface
- [x] Atualizar `STATUS.md` e marcar a Fase 0 como concluída

---

## Fase 1 — Logins simples  ✅

### Sprint 1 — Logins: Mapa Força · Dejem
- [x] Criar `nucleo/login_mapa_forca.py` reutilizando credenciais SIOPM e abrindo COMP MAPA FORÇA
- [x] Criar `nucleo/login_dejem.py` com credenciais do Portal MS
- [x] Criar `automacoes/abrir_mapa_forca/` para uso real, mantendo Edge aberto
- [x] Criar `automacoes/abrir_dejem/` para uso real, mantendo Edge aberto
- [x] Adicionar chaves Dejem em `segredos.env` e `segredos.env.exemplo`
- [x] Criar `automacoes/teste_logins/` como diagnóstico (`manifesto.py` + `executar.py`)
- [x] Confirmar descoberta pelo contrato sem alterar `painel.py`
- [x] Validar pelo painel em ambiente com `customtkinter`, VPN e Edge

### Itens da fase
- [x] 6 · Login Mapa Força 5ª Cia (SIOPM Web)
- [x] 7 · Login página Dejem/Delegada

## Fase 2 — Validar BOPM (1.1)
- [ ] Formalizar o que o `gemini_submitter.py` já faz como automação própria

## Fase 3 — Órion
- [ ] 2 · Consultar indicadores criminais (somente leitura)

## Fase 4 — Relatório de e-mails (só leitura)
- [ ] 4 · Gmail: relatório de não lidos (4 contas via API)
- [ ] 3 · Correio PM: relatório de não lidos (navegador)

## Fase 5 — Triagem/exclusão de e-mails ⚠ (ver D-02)
- [ ] 4.1 · Triagem + confirmação + lixeira (Gmail)
- [ ] 3.1 · Triagem + confirmação + lixeira (Correio PM)

## Fase 6 — Assinatura de PDF ⚠ (ver D-04)
- [ ] Confirmar formato do certificado local
- [ ] 8 · Botão "assinar" com certificado local (PIN na hora, por documento)

---

## Histórico (diário)
- **03/06/2026** — Scaffold criado, BOPM migrado, decisões A/B/C registradas, `STATUS.md` criado, Fase 0 detalhada em 2 sprints.
- **03/06/2026** — Fase 0 · Sprint 1 executado e testado: `nucleo/` criado com `segredos.py`, `log.py`, `vpn.py`, `browser.py`; credenciais migradas para `segredos.env`; `config.py` limpo; BOPM rodando pelo código refatorado.
- **03/06/2026** — Fase 0 · Sprint 2 concluído e testado: `painel.py` abre, botão "Baixar BOPMs" roda o BOPM com log ao vivo. **Fase 0 fechada.**
- **05/06/2026** — Decisão D-06 registrada: SEI removido do escopo de automação; acesso ao SEI ficará manual.
- **05/06/2026** — Fase 1 · Sprint 1 implementado: logins reutilizáveis Mapa Força/Dejem e smoke-test `Teste de Logins` criados. Pendente validação real pelo painel/VPN.
- **05/06/2026** — Fase 1 · Sprint 1 validado pelo painel: `[OK] Mapa Força` e `[OK] Dejem`. Aprendizados registrados em `docs/APRENDIZADOS.md`. **Fase 1 fechada.**
- **05/06/2026** — Ajuste pós-validação: criados botões reais **Abrir Mapa Força** e **Abrir Dejem/Delegada**; **Teste de Logins** mantido como diagnóstico.
