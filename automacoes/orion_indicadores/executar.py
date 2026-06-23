"""Abre o Órion autenticado e mantém o Edge disponível ao operador."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from nucleo.login_orion import login as login_orion


def run(ctx) -> Dict[str, str]:
    ctx.log.info("Abrindo Órion para uso...")
    login_orion(ctx)
    ctx.log.info("[OK] Órion autenticado. Navegador mantido aberto.")
    return {"status": "ok", "detalhes": "Órion autenticado e aberto para uso."}
