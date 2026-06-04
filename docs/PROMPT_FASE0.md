# PROMPT DE ABERTURA — FASE 0 (Fundação)

> Cole este conteúdo no Claude Code, ou simplesmente diga a ele:
> *"Leia `docs/PROMPT_FASE0.md` e toda a pasta `docs/`, depois siga as instruções."*

---

## Quem você é neste projeto

Você é meu parceiro de engenharia no projeto **Central de Automações** (pasta
`C:\Projetos\central_automacoes`). Antes de qualquer coisa, **leia e absorva**:

- `README.md` — o mapa do projeto
- `docs/PLANO.md` — arquitetura e fases
- `docs/DECISOES.md` — decisões já fechadas (A/B/C, segredos, assinatura)
- `docs/ROADMAP.md` — fases e sprints (estamos iniciando a **Fase 0**)
- `docs/STATUS.md` — estado atual

O código atual da automação de BOPM está em `automacoes/baixar_bopm/` (formato
antigo, monolítico). A Fase 0 vai reorganizá-lo sem perder funcionalidade.

---

## Regras de trabalho (invioláveis)

1. **Fluxo: entender → planejar → confirmar → executar.** Antes de escrever
   código, me apresente o plano do sprint e **espere meu OK explícito**.
2. **Nunca** rode `git commit`, `git push` ou deploy por conta própria. Você
   pode preparar, mas quem confirma sou eu.
3. **Segredos:** mover as senhas para o cofre é um passo sensível — **me avise
   antes**, me mostre exatamente o que vai sair do `config.py` e ir pro
   `segredos.env`. Nunca exiba as senhas em texto no chat sem necessidade.
4. **Não quebre a versão de produção.** Existe uma cópia funcionando em
   `C:\Users\pc\Documents\bopm_automation` que eu uso todo dia. Trabalhe **só**
   dentro de `central_automacoes`. Não toque na pasta de Documents.
5. **Ao fim de cada sprint:** atualize `docs/STATUS.md` (a foto) e marque os
   checkboxes + adicione linha no Histórico do `docs/ROADMAP.md` (o filme).
6. Execute com o modelo de execução (Sonnet). Quando eu pedir auditoria, eu
   troco para Opus — não se autoauditе.
7. Trabalhe **um sprint de cada vez**. Não adiante a Fase 1.

---

## Objetivo da Fase 0

Transformar o BOPM monolítico em **núcleo compartilhado + automação plugável**, e
subir um **painel com 1 botão** que roda o BOPM pela interface. Sem mudar o que a
automação faz — só *como* ela está organizada.

São **2 sprints**. Comece apresentando o plano do Sprint 1.

---

## Sprint 1 — Núcleo + segredos

**Refatorar, preservando 100% do comportamento atual do BOPM.**

- Criar `nucleo/segredos.py`: classe que lê de `segredos.env` (use `python-dotenv`)
  e expõe algo como `segredos.get("siopm")` → `{"user": ..., "password": ...}`,
  `segredos.get("vpn")` → idem. Interface abstrata, para depois trocar por
  `keyring` do Windows sem reescrever quem chama.
- Criar `segredos.env` a partir de `segredos.env.exemplo` e migrar para ele as
  credenciais que hoje estão em `automacoes/baixar_bopm/config.py`
  (VPN e SIOPM). **Me mostre antes de mover.**
- Mover `vpn_manager.py` → `nucleo/vpn.py` (passa a ler credenciais do `segredos`,
  mantém caminhos/host não-secretos como configuração).
- Extrair o `BrowserManager` (abrir Edge via Playwright) → `nucleo/browser.py`.
- Mover `logger_setup.py` → `nucleo/log.py`.
- `config.py` do BOPM permanece, mas **sem segredos** — só o específico do BOPM
  (URLs, código OPM, filtro, seletores, timeouts).

**Critério de aceite do Sprint 1:** rodar o BOPM pela linha de comando, já usando
o núcleo refatorado, e ele baixar normalmente (sem regressão). `segredos.env`
fora do git (confirme no `.gitignore`).

---

## Sprint 2 — Contrato + painel

- Definir o **contrato** que toda automação seguirá (ver `automacoes/README.md`):
  - `manifesto.py` com o dict `MANIFESTO` (id, nome, descricao, categoria,
    precisa_vpn, destrutivo, confirma_antes, ordem).
  - `executar.py` com `def run(ctx): ...`, onde `ctx` dá acesso ao núcleo
    (`ctx.log`, `ctx.vpn`, `ctx.browser`, `ctx.saidas`, `ctx.segredos`).
- Adaptar `automacoes/baixar_bopm/` ao contrato: criar o `manifesto.py` e um
  `executar.py` que executa o fluxo de BOPM usando o núcleo. Pode reaproveitar a
  orquestração que hoje está no `main.py`. **Preserve o envio ao Gemini que já
  funciona** (não refatore essa parte agora — só mantenha rodando).
- Criar `painel.py` com **customtkinter**:
  - Descobre sozinho todas as automações lendo `automacoes/*/manifesto.py`.
  - Desenha um cartão + botão por automação, ordenado por `ordem`.
  - Ao clicar: se `precisa_vpn`, garante VPN antes; roda `run(ctx)` numa thread
    (não travar a janela); transmite o log ao vivo num painel de texto; mostra
    status (rodando / ✓ / ✗).
  - Janela não-headless (Edge visível, como hoje).

**Critério de aceite do Sprint 2:** abrir `painel.py`, ver o botão
"Baixar BOPMs", clicar, e o BOPM baixar com o log aparecendo na janela. Atualizar
`STATUS.md` e fechar a Fase 0 no `ROADMAP.md`.

---

## Sua primeira ação agora

Não escreva código ainda. Leia os docs, depois me apresente:
1. Um resumo do que você entendeu da estrutura atual do BOPM.
2. O plano do **Sprint 1** (ordem das mudanças, arquivos afetados, riscos).
3. Qualquer dúvida que tenha antes de começar.

Aí eu te dou o OK.
