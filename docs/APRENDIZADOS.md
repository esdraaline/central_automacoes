# Aprendizados da Central de Automações

> Registro curto de erros, acertos e cuidados técnicos para orientar sprints futuros.

---

## 06/06/2026 — Fase 2 · Sprint 2.1 · Validar BOPM — fluxo real mapeado em campo

### Acertos
- O contrato `manifesto.py` + `executar.py` funcionou: botão "Validar BOPM" apareceu no painel sem editar `painel.py`.
- Diagnóstico automático (log de frames + elementos visíveis) foi decisivo para mapear cada seletor sem acesso ao código-fonte do SIOPM.
- `page.once("dialog", ...)` registrado antes do clique capturou o `window.confirm` nativo sem race condition.
- `keep_open=True` no `BrowserManager` manteve o Edge aberto na listagem filtrada após a automação — útil para inspeção.

### Erros encontrados
- **Ícone errado:** o código clicava no 1º ícone da linha (visualizar). O ícone correto é o 2º (Editar Ocorrência).
- **"Validar BOPM" vs "Validar BO-e":** o botão real tem `value='Validar BO-e'` e `name='W0236BTNVALIDARTCO'` — nome diferente do planejado.
- **Confirmação não é HTML:** após clicar em "Validar BO-e" o SIOPM dispara `window.confirm` nativo do browser, não um elemento HTML. Seletor CSS nunca funcionaria.
- **"Outros" não é checkbox:** o GeneXus implementa o checkbox "Outros" como `<img id='W0236CHK_OUT'>` clicável. `input[type='checkbox']` nunca o encontraria. Estado (marcado/desmarcado) verificado pelo `src` da imagem: `UnChecked` = desmarcado.
- **Scroll necessário:** a seção "Providências Preliminares" fica abaixo do fold. `window.scrollTo(0, document.body.scrollHeight)` antes do Passo 2 garante que o elemento esteja no viewport.
- **BOs nunca visualizados:** se o BO nunca foi aberto em PDF, o botão "Validar BO-e" não aparece. Solução: clicar em "Visualiza PDF" primeiro e fechar a aba que abre.

### Regras para próximas automações no SIOPM/GeneXus
- **Nunca assumir que checkboxes são `<input type='checkbox'>`** — o GeneXus usa `<img>` clicável com `id` padronizado. Inspecionar pelo diagnóstico antes de escrever seletores.
- **Confirmar tipo de dialog antes de escrever seletor:** dialogs nativos do browser (`alert`, `confirm`, `prompt`) exigem `page.once("dialog", ...)` — não são elementos HTML.
- **Usar o diagnóstico ampliado** (tags `img`, `span`, `td`; campos `onclick`, `src`, `checked`) para revelar elementos GeneXus não-padrão.
- **Sempre verificar o número de ícones na linha** antes de assumir qual clicar.
- **`keep_open=True`** no `BrowserManager.close()` desvincula o Playwright sem fechar o browser — sessão e cookies intactos, janela permanece aberta.
- **Filtro GeneXus é POST-based:** `page.goto(url)` após filtro aplicado faz GET e exibe formulário vazio. Nunca navegar de volta via goto — usar apenas o botão "Retornar" que o SIOPM fornece na tela.
- **Double-Retornar bug:** se `_validar_bopm` clicar "Retornar" (Passo 5) E o `go_back_to_list()` do finally também clicar, o Edge fica 2 níveis acima do esperado. Delegue o retorno a um único ponto (o finally do loop).

---

## 06/06/2026 — Fix Baixar BOPM · Detecção de "BO Informal"

### Erro encontrado
`get_pending_bopms` não detectava BOPMs com status **"BO Informal"** — só reconhecia "Não Formalizado". BOPMs com esse status eram silenciosamente ignorados na listagem.

### Causa raiz
A detecção opera em 3 camadas independentes (JavaScript na listagem, método `_row_has_orange_indicator` e log de abertura), e todas usavam apenas a string `'nao formalizado'` como critério de texto.

### Correção aplicada
Três pontos em `siopm_navigator.py`:
1. Filtro JavaScript (`byText`): adicionado `|| norm.includes('bo informal')`.
2. Keywords de `_row_has_orange_indicator`: adicionados `"bo informal"` e `"b.o. informal"`.
3. Log de abertura: atualizado para refletir os dois status detectados.

### Regra para próximas automações
Ao listar BOPMs por status textual, nunca assumir que existe um único valor possível — o SIOPM usa ao menos dois: "Não Formalizado" e "BO Informal". Qualquer futura automação que filtre por status deve cobrir ambos.

---

## 05/06/2026 — Fase 1 · Sprint 1 · Logins Mapa Força e Dejem

### Acertos
- O contrato `manifesto.py` + `executar.py` funcionou: o botão **Teste de Logins** apareceu no painel sem editar `painel.py`.
- Depois da validação, o uso real ficou separado do diagnóstico: **Abrir Mapa Força** e **Abrir Dejem/Delegada** deixam o navegador aberto; **Teste de Logins** apenas valida e fecha.
- `ctx.segredos` centralizou credenciais sem hardcode nos módulos de login.
- `ctx.browser.launch(headless=False)` abriu Edge visível, adequado para validação assistida.
- O Mapa Força ficou estável ao reproduzir o fluxo real: login SIOPM → CAD Araçatuba → categoria `COMP MAPA FORÇA` → OPM `610025000` → `Procurar`.
- SEI foi removido do escopo por decisão D-06; melhor manter gov.br/2FA manual.

### Erros Encontrados
- A VPN foi desconectada ao fim do teste mesmo já estando conectada manualmente.
  Correção: `VPNManager` agora só desconecta quando a própria execução abriu a conexão.
- O Mapa Força não encontrou a categoria de primeira porque faltava selecionar o CAD intermediário.
  Correção: `login_mapa_forca.py` seleciona CAD Araçatuba antes de procurar `COMP MAPA FORÇA`.
- Abrir um segundo Playwright sem fechar o primeiro causou erro de Sync API.
  Correção: o smoke-test fecha o navegador do Mapa Força antes de iniciar o Dejem.
- O Dejem tentou preencher um `input type="button"` como usuário.
  Correção: `login_dejem.py` separa busca de campos preenchíveis da busca de botões clicáveis.
- Um erro de indentação em `login_dejem.py` foi detectado por `py_compile`.
  Regra prática: rodar `python -m py_compile` antes de reabrir o painel.

### Regras Para Próximas Automações
- Separar botões de uso real de botões de diagnóstico. Testes podem fechar navegador; automações de uso devem manter a tela aberta quando o operador precisa continuar manualmente.
- Não assumir que VPN conectada pelo operador pode ser encerrada pela automação.
- Em sistemas antigos com muitos `input`, separar claramente seletores de campos e seletores de botões.
- Fechar cada instância de Playwright antes de iniciar outra dentro da mesma automação sequencial.
- Registrar no log a URL atual e opções visíveis quando um dropdown esperado não for encontrado.
- Validar pelo painel, não só por linha de comando, quando o critério envolve thread, VPN e Edge visível.
