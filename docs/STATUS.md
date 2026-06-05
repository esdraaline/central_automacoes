# 📍 Status Atual

> Foto do "onde estou agora". **Atualizado ao fim de cada sprint** (pelo Claude Code durante o build).
> **Última atualização:** 05/06/2026

---

## Onde estou
- **Fase:** 1 — Logins simples · ✅ **Concluída**
- **Sprint atual:** — (Fase 1 fechada, aguardando início da Fase 2)

## Já feito
- Scaffold, migração do BOPM, decisões A/B/C
- **Fase 0 · Sprint 1 ✅** — `nucleo/` criado (`segredos`, `log`, `vpn`, `browser`), credenciais migradas para `segredos.env`, BOPM testado pela linha de comando
- **Fase 0 · Sprint 2 ✅** — Contrato (`manifesto.py` + `executar.py`), `painel.py` com customtkinter; botão "Baixar BOPMs" roda o BOPM com log ao vivo na janela
- **Fase 1 · Sprint 1 ✅** — módulos `nucleo/login_mapa_forca.py` e `nucleo/login_dejem.py` criados; botões reais **Abrir Mapa Força** e **Abrir Dejem/Delegada** criados; `Teste de Logins` mantido como diagnóstico
- **Decisão D-06 ✅** — SEI removido do escopo de automação; acesso ao SEI será manual
- Aprendizados da validação registrados em `docs/APRENDIZADOS.md`

## Próximo passo
- Iniciar **Fase 2 — Validar BOPM (1.1)** quando autorizado

## Bloqueios / pendências
- Nenhum bloqueio técnico conhecido; dependências instaladas e painel abre.

---

## Como manter este arquivo
Ao fim de cada sprint, atualizar: a **data**, **Onde estou**, **Já feito**,
**Próximo passo** e **Bloqueios**. Mantenha curto — é uma foto, não um diário.
O diário detalhado fica no `ROADMAP.md` (Histórico).
