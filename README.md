# Central de Automações — 5ª Cia / 2º BPM-I / CPI-10

Painel desktop único (Python + customtkinter) que descobre e executa automações do serviço. Cada automação vive numa pasta plugável — adicionar uma nova = largar uma pasta nova; o botão aparece sozinho.

---

## Estado atual

| Fase | Status |
|---|---|
| Fase 0 — Fundação (nucleo/ + painel + BOPM) | ✅ Concluída |
| Fase 1 — Logins (Mapa Força + Dejem/Delegada) | ✅ Concluída |
| Fase 2 — Validar BOPM | ✅ Concluída |
| Fase 3 — Órion | 🚧 Sprint 3.1 implementada; validação em campo pendente |
| Fase 7/8 — Despachadora do Comandante | ✅ Operacional e endurecida |
| Fases 4–6 | ⏳ Planejadas |

Para o estado detalhado, consulte `docs/STATUS.md`.
Para o roadmap completo com sprints e critérios de aceite, consulte `docs/ROADMAP.md`.

---

## Como rodar

```bash
cd C:\Projetos\central_automacoes
python painel.py
```

Requisito: `segredos.env` preenchido (copiar de `segredos.env.exemplo`). Para o Órion, preencher também `ORION_URL` com o endereço interno exato.

---

## Adicionar uma automação nova

1. Criar `automacoes/<id>/manifesto.py` com o dict `MANIFESTO`.
2. Criar `automacoes/<id>/executar.py` com `def run(ctx)`.
3. Abrir o painel — o botão aparece automaticamente.

Detalhes do contrato em `docs/PLANO.md`.
