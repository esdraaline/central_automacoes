# nucleo/

Código compartilhado por todas as automações. Será preenchido na Fase 0,
refatorando o que hoje está dentro de `automacoes/baixar_bopm/`.

- `vpn.py` — conectar/verificar/desconectar VPN Cisco (de `vpn_manager.py`)
- `browser.py` — abrir o Edge via Playwright (de `siopm_navigator.py`)
- `log.py` — logging padronizado (de `logger_setup.py`)
- `segredos.py` — acesso a credenciais (lê de `segredos.env`)
- `assinatura.py` — assinar PDF com certificado local (Fase 6)
- `relatorio.py` — relatórios padronizados em `saidas/`
