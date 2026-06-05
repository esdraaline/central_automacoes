"""
automacoes/teste_logins/executar.py - Smoke-test dos logins da Fase 1.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

_SELF = Path(__file__).resolve().parent
_ROOT = _SELF.parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from nucleo.browser import BrowserManager
from nucleo.contexto import Contexto
from nucleo.login_dejem import login as login_dejem
from nucleo.login_mapa_forca import login as login_mapa_forca


LoginFn = Callable[[Any], Any]


def run(ctx) -> Dict[str, str]:
    """Executa os tres logins em sequencia e continua mesmo se algum falhar."""
    log = ctx.log
    resultados: List[str] = []
    managers: List[BrowserManager] = []

    testes: List[Tuple[str, LoginFn]] = [
        ("Mapa Forca", login_mapa_forca),
        ("Dejem", login_dejem),
    ]

    for nome, login_fn in testes:
        log.info("")
        log.info(f"Iniciando teste de login: {nome}")
        browser = BrowserManager(log)
        managers.append(browser)
        login_ctx = Contexto(
            log=log,
            segredos=ctx.segredos,
            vpn=ctx.vpn,
            browser=browser,
            saidas=ctx.saidas,
        )

        try:
            login_fn(login_ctx)
            log.info(f"[OK] {nome}")
            resultados.append(f"{nome}: ok")
        except Exception as exc:
            log.error(f"[ERRO] {nome}: {exc}")
            resultados.append(f"{nome}: erro - {exc}")
        finally:
            browser.close()

    falhas = [r for r in resultados if ": erro" in r]
    status = "erro" if falhas else "ok"
    detalhes = "; ".join(resultados)

    log.info("")
    log.info(f"Resumo teste de logins: {detalhes}")
    return {"status": status, "detalhes": detalhes}
