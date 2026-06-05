"""
automacoes/abrir_dejem/executar.py - Abre Dejem/Delegada para uso real.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

_SELF = Path(__file__).resolve().parent
_ROOT = _SELF.parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from nucleo.login_dejem import login as login_dejem


def run(ctx) -> Dict[str, str]:
    """Abre o Dejem/Delegada e deixa o navegador aberto para o operador usar."""
    ctx.log.info("Abrindo Dejem/Delegada para uso...")
    login_dejem(ctx)
    ctx.log.info("[OK] Dejem/Delegada aberto. Navegador mantido aberto para uso.")
    return {"status": "ok", "detalhes": "Dejem/Delegada aberto para uso."}
