# Aprendizados da Central de Automações

> Registro curto de erros, acertos e cuidados técnicos para orientar sprints futuros.

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
