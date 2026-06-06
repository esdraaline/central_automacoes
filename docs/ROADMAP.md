# 🛣️ Roadmap
Como ler: as fases são o mapa geral. Cada fase é quebrada em sprints com tarefas concretas — mas só detalhamos os sprints da fase quando chegamos nela (planejar os 6 em detalhe agora seria perder tempo que é pra construir). Marque [x] ao concluir. O "onde estou agora" fica no STATUS.md.

---

## ✅ Concluído antes das fases
- [x] Scaffold da central criado e salvo em `Projetos\central_automacoes`
- [x] Código do BOPM migrado para `automacoes/baixar_bopm/`
- [x] Decisões A/B/C registradas (DECISOES.md)

---

## Fase 0 — Fundação ✅

### Sprint 1 — Núcleo + segredos ✅
- [x] Criar `nucleo/segredos.py` (lê de `segredos.env`, interface `get("siopm")`)
- [x] Criar `segredos.env` a partir do `.exemplo` e preencher
- [x] Mover as senhas do `config.py` antigo para o `segredos.env`
- [x] Refatorar `vpn_manager.py` → `nucleo/vpn.py`
- [x] Refatorar parte de browser do `siopm_navigator.py` → `nucleo/browser.py`
- [x] Refatorar `logger_setup.py` → `nucleo/log.py`
- [x] Testar: BOPM ainda baixa rodando pelo código refatorado (linha de comando)

### Sprint 2 — Contrato + painel ✅
- [x] Definir o contrato `manifesto.py` + `executar.py`
- [x] Adaptar `baixar_bopm/` ao contrato (manifesto + executar chamando o núcleo)
- [x] Criar `painel.py` (customtkinter): descobre automações, 1 botão, log ao vivo
- [x] Testar: clicar no botão "Baixar BOPMs" e baixar pela interface
- [x] Atualizar STATUS.md e marcar a Fase 0 como concluída

---

## Fase 1 — Logins simples ✅

### Sprint 1 — Logins: Mapa Força · Dejem ✅
- [x] Criar `nucleo/login_mapa_forca.py` reutilizando credenciais SIOPM e abrindo COMP MAPA FORÇA
- [x] Criar `nucleo/login_dejem.py` com credenciais do Portal MS
- [x] Criar `automacoes/abrir_mapa_forca/` para uso real, mantendo Edge aberto
- [x] Criar `automacoes/abrir_dejem/` para uso real, mantendo Edge aberto
- [x] Adicionar chaves Dejem em `segredos.env` e `segredos.env.exemplo`
- [x] Criar `automacoes/teste_logins/` como diagnóstico (`manifesto.py` + `executar.py`)
- [x] Confirmar descoberta pelo contrato sem alterar `painel.py`
- [x] Validar pelo painel em ambiente com customtkinter, VPN e Edge

**Itens da fase:**
- [x] 6 · Login Mapa Força 5ª Cia (SIOPM Web)
- [x] 7 · Login página Dejem/Delegada

---

## Fase 2 — Validar BOPM (1.1)

**Objetivo:** validar os BOPMs pendentes no SIOPM Web (Enviar para Providências Complementares → Outros → Confirmar).

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 2.1 | Criar `automacoes/validar_bopm/` com contrato `manifesto.py` + `executar.py`. Fluxo: login SIOPM → filtro → detecta pendentes → abre cada BOPM → seleciona "Outros" → clica "Validar BOPM" → clica "Confirmar". | Botão "Validar BOPM" aparece no painel; executa com log ao vivo; seletores mapeados na primeira execução real. |
| 2.2 | Saída: relatório em `saidas/validacao_bopm_<data>.txt` com resultado por BOPM. | Arquivo gerado corretamente; log ao vivo durante execução. |

**Itens da fase:**
- [ ] 1.1 · Validar BOPMs pendentes no SIOPM Web (Sprint 2.1 implementado ⏳ aguardando validação)

---

## Fase 3 — Órion

**Objetivo:** consultar indicadores criminais no sistema Órion (só leitura, sem ação).

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 3.1 | Login no Órion via Playwright (Edge, não-headless). Credenciais via `nucleo/segredos`. | Login bem-sucedido; sessão disponível para os próximos sprints. |
| 3.2 | Consulta por município/período; extração dos indicadores da página. | Dados extraídos corretamente para pelo menos 1 município de teste. |
| 3.3 | Saída em `saidas/orion_<municipio>_<data>.txt`. Log ao vivo. | Arquivo gerado; painel não trava durante extração. |

**Itens da fase:**
- [ ] 2 · Consultar indicadores criminais (somente leitura)

---

## Fase 4 — Relatório de e-mails (só leitura)

**Objetivo:** ler e-mails não-lidos das 4 contas Gmail + 1 Hotmail + correio PM, gerar relatório.

Contas: josemardp@gmail.com · josemar.dp@hotmail.com · esdraaline@gmail.com · lojadares@gmail.com · correio PM (por navegador).

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 4.1 | Configurar OAuth Gmail API para as 3 contas Google. Armazenar tokens em `segredos/` (fora do git). | Autenticação funciona nas 3 contas sem erro. |
| 4.2 | Leitura de não-lidos das 3 contas Gmail; saída estruturada por conta. | Relatório em `saidas/emails_<data>.txt` com remetente, assunto, data, trecho. |
| 4.3 | Leitura Hotmail via Microsoft Graph API. | Mesma estrutura do relatório, incluindo conta Hotmail. |
| 4.4 | Correio PM por Playwright (atrás da VPN). Só leitura. | Não-lidos do correio PM incluídos no relatório; painel não trava. |

**Itens da fase:**
- [ ] 4 · Gmail: relatório de não lidos (4 contas via API)
- [ ] 3 · Correio PM: relatório de não lidos (navegador)

---

## Fase 5 — Triagem/exclusão de e-mails ⚠ (ver D-02)

**Objetivo:** após relatório (Fase 4), permitir exclusão com confirmação explícita do usuário.

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 5.1 | UI de triagem: listar e-mails do relatório mais recente; checkbox por item. | Lista renderizada corretamente; nenhuma ação é tomada sem confirmação. |
| 5.2 | Mover para Lixeira (não exclusão permanente) após confirmação explícita. Nunca esvaziar lixeira. | E-mail movido para Lixeira na conta correta; log registra a ação. |

**Itens da fase:**
- [ ] 4.1 · Triagem + confirmação + lixeira (Gmail)
- [ ] 3.1 · Triagem + confirmação + lixeira (Correio PM)

---

## Fase 6 — Assinatura de PDF ⚠ (ver D-04)

**Objetivo:** assinar PDFs localmente com certificado e-CPF/Adobe, PIN digitado na hora, por documento.

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 6.1 | Confirmar formato do certificado local (A1 .pfx / A3 em token / ID digital do Adobe). Integrar `pyhanko`. Abrir diálogo de seleção de arquivo PDF. | PDF selecionado carregado corretamente. |
| 6.2 | Solicitar PIN ao usuário na hora; assinar; salvar em `saidas/`. | PDF assinado gerado; assinatura válida verificável no Adobe Reader. |
| 6.3 | Validar que gov.br não é automatizado (máximo: preparar PDF e abrir assinador para o humano). | Nenhum fluxo automatizado de gov.br na Central. |

**Itens da fase:**
- [ ] Confirmar formato do certificado local
- [ ] 8 · Botão "assinar" com certificado local (PIN na hora, por documento)

---

## Fase 7 — Despachadora do Comandante

**Objetivo:** portar a skill standalone de redação assistida para dentro do painel como automação plugável de categoria `"Redação"` (sem VPN/browser). **Independente das Fases 2–6 — pode ser priorizada e executada em paralelo.**

A Despachadora recebe um expediente (parte, ofício, despacho, denúncia, BO, laudo — arquivo ou texto colado), busca contexto num corpus indexado da 5ª Cia e devolve 6 blocos fixos: Classificação, Análise Jurídica, Decisão, Texto Pronto (padrão I-7-PM), Levantamentos, Assessoria do Estado-Maior.

**Estrutura alvo (`automacoes/despachadora/`):**
```
automacoes/despachadora/
├── manifesto.py              # precisa_vpn=False, destrutivo=False, categoria="Redação"
├── executar.py               # run(ctx) — chama o núcleo; lê CORPUS_PATH de ctx.segredos
├── corpus_index.json         # versionado no git (~34 MB); gerado pelo indexar_corpus
└── nucleo_despachadora/
    ├── despachadora.py       # MOVIDO do Drive — vira função chamável (main() → def processar())
    └── indexar_corpus.py     # MOVIDO do Drive — mantido junto para reindexações
```

**Restrições técnicas a investigar no Sprint 7.1 (não bloqueiam hoje):**

| Ponto | Detalhe | Impacto |
|---|---|---|
| Input de arquivo no painel | `_on_run` passa apenas `ctx` sem argumento de arquivo. Extensão necessária. | ⚠ investigar no Sprint 7.1 |
| Exibição de saída longa | `_run_thread` exibe resultado como string curta hardcoded. Os 6 blocos precisam de mecanismo próprio. | ⚠ investigar no Sprint 7.1 |
| `SKILL_ROOT` hardcoded | `indexar_corpus.py` linha 38: `Path("G:/Meu Drive/...")`. Ao portar, ler `CORPUS_PATH` de `segredos.env`. | Adaptação mínima |
| `CORPUS_FILE` relativo ao script | `despachadora.py`: `CORPUS_FILE = SCRIPT_DIR / "corpus_index.json"`. Ao mover para `nucleo_despachadora/`, apontar um nível acima. | Adaptação mínima |
| `.gitignore` e corpus | Quando `automacoes/despachadora/` existir, garantir que P1–P5, JD, Notebooklm não entrem por acidente. | Corrigir antes do Sprint 7.2 |

| Sprint | Escopo | Critério de aceite |
|---|---|---|
| 7.1 | **Investigação:** Claude Code lê a Central e propõe plano de port (input de arquivo, exibição de saída longa, adaptações mínimas). **Nenhum código escrito.** | Plano aprovado por Josemar com mapeamento das restrições técnicas acima. |
| 7.2 | Port do núcleo: mover `despachadora.py` e `indexar_corpus.py` para `nucleo_despachadora/`. Adaptar `main()` → função chamável. Corrigir `SKILL_ROOT` e `CORPUS_FILE`. Atualizar `.gitignore`. | `run(ctx)` executa end-to-end sem erro com caso de teste. |
| 7.3 | Integração UI: extensão do painel para input por arquivo e por texto colado; área de saída longa para os 6 blocos com botões Copiar e Salvar. | Dois modos funcionando no painel; saída dos 6 blocos legível sem truncamento. |
| 7.4 | Testes com casos reais; ajuste system prompt → v1.3 (promover `[VERIFICAR]` confirmados; corrigir desvios de formato). | Pelo menos 3 casos reais testados; nenhum FUNDAMENTO inventado detectado. |

**Itens da fase:**
- [ ] Sprint 7.1 — Investigação e plano de port
- [ ] Sprint 7.2 — Port do núcleo
- [ ] Sprint 7.3 — Integração UI
- [ ] Sprint 7.4 — Testes e system prompt v1.3

---

## Histórico (diário)

**03/06/2026** — Scaffold criado, BOPM migrado, decisões A/B/C registradas, STATUS.md criado, Fase 0 detalhada em 2 sprints.

**03/06/2026** — Fase 0 · Sprint 1 executado e testado: `nucleo/` criado com `segredos.py`, `log.py`, `vpn.py`, `browser.py`; credenciais migradas para `segredos.env`; `config.py` limpo; BOPM rodando pelo código refatorado.

**03/06/2026** — Fase 0 · Sprint 2 concluído e testado: `painel.py` abre, botão "Baixar BOPMs" roda o BOPM com log ao vivo. Fase 0 fechada.

**05/06/2026** — Decisão D-06 registrada: SEI removido do escopo de automação; acesso ao SEI ficará manual.

**05/06/2026** — Fase 1 · Sprint 1 implementado: logins reutilizáveis Mapa Força/Dejem e smoke-test Teste de Logins criados. Pendente validação real pelo painel/VPN.

**05/06/2026** — Fase 1 · Sprint 1 validado pelo painel: [OK] Mapa Força e [OK] Dejem. Aprendizados registrados em `docs/APRENDIZADOS.md`. Fase 1 fechada.

**05/06/2026** — Ajuste pós-validação: criados botões reais Abrir Mapa Força e Abrir Dejem/Delegada; Teste de Logins mantido como diagnóstico.

**05/06/2026** — Diagnóstico de consistência (sprint de documentação): D-07 registrada em DECISOES.md; Fases 2–7 detalhadas com sprints e critérios de aceite; Fase 7 (Despachadora) adicionada ao ROADMAP, PLANO e STATUS; `segredos.env.exemplo` atualizado com `GEMINI_API_KEY` e `CORPUS_PATH`; README atualizado.

**05/06/2026** — Fase 2 · Sprint 2.1 implementado: `automacoes/validar_bopm/manifesto.py` e `automacoes/validar_bopm/executar.py` criados. Botão "Validar BOPM" aparece no painel automaticamente (descoberta pelo contrato). Fluxo: login SIOPM → filtro → detecta pendentes → abre cada BOPM → tenta 3 cliques (Outros / Validar BOPM / Confirmar). Seletores dos 3 cliques a mapear na primeira execução real com VPN — log diagnostica URL e elementos visíveis em caso de falha. Pendente validação pelo painel.
