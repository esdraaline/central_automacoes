# Automação BOPM/SIOPM — Guia Completo

## Stack Tecnológica

| Camada | Tecnologia | Motivo |
|--------|-----------|--------|
| Linguagem | Python 3.10+ | Ecossistema rico, legível, fácil manutenção |
| Automação web | **Playwright** (sync API) | Controla Edge nativamente, aguarda carregamentos automáticos, suporta downloads, popups e iframes |
| Browser | Microsoft Edge (msedge channel) | Compatibilidade total com sistema intranet da PMESP |
| VPN | subprocess + vpncli.exe | CLI oficial do Cisco Secure Client — mais estável que automação de GUI |
| Downloads | requests + cookies Playwright | Reutiliza sessão autenticada para baixar PDFs sem nova autenticação |
| Logging | logging padrão + RotatingFileHandler | Log em arquivo (DEBUG) + console (INFO), rotação de 5 MB |

---

## Pré-requisitos

- Windows 10/11
- Python 3.10 ou superior → https://www.python.org/downloads/
- Microsoft Edge instalado
- Cisco Secure Client instalado
- VPN configurada com o perfil "00 - PMESP"

---

## Instalação (apenas uma vez)

```
1. Copie a pasta bopm_automation para um local de sua escolha (ex: Desktop).
2. Abra o Prompt de Comando como Administrador.
3. Navegue até a pasta: cd Desktop\bopm_automation
4. Execute: instalar.bat
```

O script instala automaticamente:
- Playwright e seus drivers
- requests
- Cria a pasta de logs em Downloads\logs_bopm

### Configuração do VPN_SERVER

Abra `config.py` e preencha a variável `VPN_SERVER` com o endereço do servidor VPN da PMESP. Este endereço já deve estar salvo no Cisco Secure Client — você pode encontrá-lo abrindo o Cisco Secure Client e verificando o servidor configurado.

```python
VPN_SERVER = "vpn.intranet.policiamilitar.sp.gov.br"  # substitua pelo real
```

> Se você já está conectado à VPN antes de executar, use a opção `--no-vpn` e não precisa preencher VPN_SERVER.

---

## Como Executar

### Opção A — Interface simples (recomendada)

Dê duplo clique em `executar_bopm.bat` e escolha uma das opções do menu.

### Opção B — Linha de comando

```cmd
cd Desktop\bopm_automation
python main.py
```

#### Parâmetros disponíveis

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `--days N` | Filtrar últimos N dias (padrão: 4) | `--days 7` |
| `--no-vpn` | Pular conexão VPN (já conectado) | `--no-vpn` |
| `--keep-vpn` | Não desconectar VPN ao terminar | `--keep-vpn` |
| `--log-level` | DEBUG, INFO, WARNING, ERROR | `--log-level DEBUG` |

---

## Estrutura de Arquivos

```
bopm_automation/
├── main.py              → Ponto de entrada, orquestração do fluxo
├── config.py            → URLs, filtros e timeouts não-secretos (EDITE AQUI)
├── vpn_manager.py       → Conectar/verificar/desconectar VPN Cisco
├── siopm_navigator.py   → Toda a navegação no SIOPM Web
├── pdf_handler.py       → Download e salvamento dos PDFs
├── logger_setup.py      → Configuração de logging
├── requirements.txt     → Dependências Python
├── instalar.bat         → Instalação (executar uma vez)
├── executar_bopm.bat    → Launcher com menu
└── COMO_EXECUTAR.md     → Este arquivo
```

---

## Fluxo de Execução Detalhado

```
1. VPNManager.connect()
   ├── is_intranet_reachable()  → já conectado? → pula
   ├── _find_cli()              → localiza vpncli.exe
   ├── _find_server()           → lê perfis XML do Cisco
   └── _do_connect()            → subprocess com stdin piped

2. BrowserManager.launch()
   └── playwright.chromium.launch(channel="msedge", headless=False)

3. SiopmNavigator.login()
   ├── page.goto(SIOPM_URL)
   ├── fill(usuário, senha)
   └── click(botão Entrar)

4. select_cad_and_category()
   ├── _select_cad()            → dropdown ou link "Araçatuba"
   └── _select_category()       → link "Ocorrências"

5. apply_bopm_filter()
   ├── select BOPM/TC P/ Validação
   ├── select Por código da OPM
   ├── select Todos
   ├── fill OPM = 610025000
   ├── _set_date_range(4 dias)
   └── click Renovar

6. get_pending_bopms()
   └── Para cada <tr>:
       ├── _row_has_orange_indicator() — 5 estratégias de detecção
       └── BopmEntry(row_index, bopm_id, link_selector)

7. Para cada BopmEntry:
   ├── vpn.ensure_connected()
   ├── nav.open_bopm()          → clica seta laranja
   ├── page.scroll to bottom
   ├── pdf.save_bopm_pdf()
   │   ├── Estratégia 1: expect_download()
   │   ├── Estratégia 2: expect_popup() + download via URL
   │   └── Estratégia 3: iframe src download
   └── nav.go_back_to_list()
```

---

## Plano de Testes

### Teste 1 — Conectividade VPN
**Objetivo:** Confirmar que a automação detecta VPN desconectada e conecta corretamente.
```
1. Desconecte a VPN manualmente.
2. Execute: python main.py --log-level DEBUG
3. Esperado: log "Intranet não acessível. Iniciando conexão VPN..."
4. Esperado: Edge abre e acessa o SIOPM corretamente.
```

### Teste 2 — VPN já conectada
**Objetivo:** Confirmar que a etapa VPN é pulada quando já conectado.
```
1. Conecte a VPN manualmente.
2. Execute: python main.py --no-vpn
3. Esperado: log "VPN já está conectada ou intranet acessível."
4. Esperado: automação inicia sem tentar conectar VPN.
```

### Teste 3 — Login SIOPM
**Objetivo:** Confirmar login correto com as credenciais.
```
1. Execute com --no-vpn (já conectado na VPN).
2. Observe o Edge abrindo e preenchendo usuário/senha.
3. Esperado: página principal do SIOPM carregada.
4. Esperado: log "Login realizado."
```

### Teste 4 — Seleção de CAD e Categoria
**Objetivo:** Confirmar que Araçatuba e Ocorrências são selecionados.
```
1. Acompanhe visualmente o Edge após login.
2. Esperado: dropdown/link "Araçatuba" selecionado.
3. Esperado: menu "Ocorrências" clicado.
4. Esperado: tela de filtro carregada.
```

### Teste 5 — Filtro de BOPMs
**Objetivo:** Confirmar preenchimento correto do formulário de filtro.
```
1. Observe os dropdowns e campos sendo preenchidos.
2. Esperado: tipo = "BOPM/TC - P/ Validação"
3. Esperado: OPM = 610025000
4. Esperado: período = últimos 4 dias (datas corretas)
5. Esperado: clique em Renovar e listagem atualizada.
```

### Teste 6 — Detecção de seta laranja
**Objetivo:** Confirmar que apenas pendentes são processados.
```
1. Execute com --log-level DEBUG.
2. Verifique no log: "BOPM pendente encontrado: ID=..."
3. Compare visualmente com a tabela no Edge.
4. Esperado: nenhum BOPM não-pendente é processado.
```

### Teste 7 — Download de PDF
**Objetivo:** Confirmar que o PDF é salvo com nome original.
```
1. Execute a automação completa.
2. Verifique a pasta Downloads.
3. Esperado: arquivo PDF presente com nome original do servidor.
4. Esperado: log "PDF salvo: C:\...\Downloads\XXXXX.pdf"
5. Abra o PDF e confirme que é válido.
```

### Teste 8 — Queda de VPN simulada
**Objetivo:** Confirmar interrupção segura em caso de queda.
```
1. Durante execução (entre BOPMs), desconecte a VPN manualmente.
2. Esperado: log "VPN CAIU durante a automação! Interrompendo..."
3. Esperado: automação para sem corromper dados.
4. Esperado: relatório mostra BOPMs processados até o momento.
```

### Teste 9 — Zero BOPMs pendentes
**Objetivo:** Confirmar comportamento quando não há pendências.
```
1. Execute em dia sem BOPMs pendentes (ou use --days 1 em dia sem ocorrências).
2. Esperado: log "Nenhum BOPM pendente encontrado."
3. Esperado: código de saída 0 (sucesso).
```

### Teste 10 — Relatório final
**Objetivo:** Confirmar geração correta do relatório.
```
1. Execute com ao menos 1 BOPM pendente.
2. Ao final, verifique o log em Downloads\logs_bopm\.
3. Esperado: "BOPMs encontrados: N", "PDFs salvos: N", "Falhas: 0"
```

---

## Tratamento de Erros

| Situação | Comportamento | Código de Saída |
|----------|--------------|-----------------|
| VPN não conecta | Log crítico, interrompe | 2 |
| VPN cai durante execução | Log crítico, interrompe imediatamente | 2 |
| Login falha | RuntimeError, interrompe | 2 |
| Seleção de CAD falha | Aviso + tenta prosseguir | — |
| Filtro falha | RuntimeError, interrompe | 2 |
| BOPM não abre | Log erro, pula para próximo | 1 |
| PDF não baixa (3 estratégias) | Log erro, pula para próximo | 1 |
| Timeout de página | Retry único, depois RuntimeError | 2 |
| Ctrl+C pelo usuário | Log aviso, relatório parcial | 2 |
| Erro inesperado | Log + traceback, relatório parcial | 2 |

---

## Estratégia Anti-Travamento

A automação implementa múltiplas camadas para evitar que o script fique preso:

**1. Timeouts em cascata**
- Cada ação tem timeout próprio (15s para elementos, 30s para páginas, 60s para PDFs).
- Playwright lança `TimeoutError` automaticamente — nunca trava esperando infinitamente.

**2. Retry único (MAX_RETRY = 1)**
- Em timeout ou falha transitória, tenta exatamente uma vez a mais.
- Nunca entra em loop de tentativas.

**3. Verificação de VPN por BOPM**
- Antes de processar cada ocorrência, verifica se a intranet está acessível.
- Se a VPN caiu, para imediatamente (evita sessão inválida gerando erros em cascata).

**4. wait_for_load_state em cascata**
- Primeiro tenta `networkidle` (melhor), depois `load` (fallback), depois prossegue mesmo assim.
- Nunca trava em páginas que não emitem `networkidle`.

**5. slow_mo = 300ms**
- Adiciona 300ms entre cada ação do Playwright, prevenindo cliques antes do carregamento.

**6. try/finally no loop principal**
- Mesmo se um BOPM falha, o bloco `finally` sempre executa `go_back_to_list()`.
- A automação continua processando os demais BOPMs.

**7. Seleção defensiva de elementos**
- Cada elemento crítico tem 5-10 seletores alternativos.
- Usa `query_selector` (não lança exceção se não encontrar) + verificação de visibilidade.

**8. Fechamento garantido do browser**
- O `browser_mgr.close()` fica no bloco `finally` do `run()`.
- O Edge é sempre fechado, mesmo em caso de exceção.

---

## Logs

Os logs ficam em: `C:\Users\<seu_usuario>\Downloads\logs_bopm\`

Formato do arquivo: `bopm_YYYYMMDD_HHMMSS.log`

Exemplo de log saudável:
```
2026-05-27 08:00:01 | INFO     | ETAPA 1: Conectar VPN Cisco Secure Client
2026-05-27 08:00:05 | INFO     | VPN conectada com sucesso!
2026-05-27 08:00:06 | INFO     | ETAPA 2: Iniciar Microsoft Edge
2026-05-27 08:00:08 | INFO     | Edge lançado com sucesso.
2026-05-27 08:00:15 | INFO     | ETAPA 3: Login no SIOPM Web
2026-05-27 08:00:22 | INFO     | Login realizado.
2026-05-27 08:00:30 | INFO     | ETAPA 6: Detectar BOPMs pendentes (seta laranja)
2026-05-27 08:00:31 | INFO       → BOPM pendente encontrado: ID=123456 | linha=3
2026-05-27 08:00:31 | INFO     Total de BOPMs pendentes: 1
2026-05-27 08:00:45 | INFO     [123456] PDF salvo: C:\Users\...\Downloads\BOPM_123456.pdf
2026-05-27 08:00:46 | INFO     PDFs salvos: 1 | Falhas: 0
```

---

## Perguntas Frequentes

**P: O Edge abre mas fica em branco.**
R: A VPN pode não estar conectada corretamente. Execute com `--log-level DEBUG` e verifique os logs.

**P: O login falha com "campo usuário não encontrado".**
R: A estrutura do formulário do SIOPM pode ter mudado. Abra manualmente o SIOPM, inspecione o HTML do campo usuário (F12) e atualize os seletores em `siopm_navigator.py`.

**P: Nenhum BOPM pendente é detectado mas existem setas laranjas visualmente.**
R: Execute com `--log-level DEBUG` e verifique qual cor/classe CSS as setas laranjas usam. Adicione o valor correspondente em `config.py` nas listas `ORANGE_HEX_VALUES` ou `ORANGE_CSS_CLASSES`.

**P: O PDF não está sendo salvo.**
R: Verifique o log para ver qual estratégia de download foi tentada. O botão "Visualiza PDF" pode ter um seletor diferente — abra a ocorrência manualmente, inspecione o HTML do botão e adicione o seletor em `pdf_handler.py` na lista `selectors`.

**P: A automação para com "VPN CAIU".**
R: A VPN desconectou durante a execução. Reconecte a VPN e execute novamente. Os BOPMs já processados não serão duplicados (os PDFs já estão salvos).
