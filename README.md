# 🗂️ Central de Automações — PMESP / 5ª Cia

> **Comece por aqui.** Este README é o mapa do projeto inteiro.
> Se você abriu esta pasta sem lembrar do que se trata, leia esta página e a `docs/`.

---

## O que é isto

Um painel único que dispara automações do serviço (baixar BOPM, consultar Órion,
relatório de e-mails, logins, assinatura de PDF, etc.). Cada automação é um módulo
plugável — adicionar uma nova = largar uma pasta em `automacoes/`.

**Estado atual:** scaffold montado + automação de BOPM já dentro (ainda no formato antigo).
**Próximo passo:** Fase 0 (ver `docs/ROADMAP.md`).

---

## Onde está cada coisa

| Pasta / arquivo            | O que é                                                        |
|----------------------------|----------------------------------------------------------------|
| `README.md` (este)         | Mapa do projeto. Ponto de partida.                             |
| `docs/PLANO.md`            | O plano completo de arquitetura e fases.                       |
| `docs/DECISOES.md`         | Registro das decisões tomadas (e por quê). **Não perca isto.** |
| `docs/ROADMAP.md`          | Fases e sprints. Checklist do progresso.                       |
| `docs/STATUS.md`           | "Onde estou agora" — foto viva, atualizada a cada sprint.      |
| `painel.py`                | (a criar na Fase 0) A interface com os botões.                 |
| `nucleo/`                  | Código compartilhado por todas as automações (VPN, browser…).  |
| `automacoes/`              | Uma pasta por automação. Ver `automacoes/README.md`.           |
| `automacoes/baixar_bopm/`  | A automação atual de BOPM (código original, a ser refatorado). |
| `saidas/`                  | TUDO que as automações produzem: PDFs, relatórios, listas.     |
| `logs/`                    | Logs de execução.                                              |
| `segredos.env.exemplo`     | Modelo de credenciais. Copie para `segredos.env` e preencha.   |
| `.gitignore`               | Garante que segredos e saídas nunca sejam versionados.         |

---

## Regra de ouro dos arquivos

> **Nada vive só no chat.** Todo plano, código ou decisão que sair de uma conversa
> com a IA vai para dentro desta pasta — em `docs/` se for documento, no lugar certo
> se for código. Esta pasta é a **única fonte da verdade**.

---

## Como evoluir o projeto (fluxo)

1. Olhe `docs/ROADMAP.md` e veja qual é a próxima fase.
2. Entenda → planeje → confirme → execute (seu fluxo de sempre).
3. Ao concluir uma fase, marque no ROADMAP e anote no DECISOES se algo mudou.
4. Cada automação nova entra como pasta em `automacoes/` (ver o contrato lá).

---

## Segurança (leia antes de pôr em qualquer git/backup/pendrive)

As credenciais ficam em `segredos.env`, que **nunca** deve ser versionado nem
sincronizado. O `.gitignore` já protege isso. O código antigo de BOPM
(`automacoes/baixar_bopm/config.py`) ainda tem senhas embutidas — isso será movido
para o cofre na Fase 0. Até lá, **não suba esta pasta para nenhum repositório.**
