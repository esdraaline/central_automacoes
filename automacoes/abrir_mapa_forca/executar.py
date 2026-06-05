"""
automacoes/abrir_mapa_forca/executar.py - Abre Mapa Forca para uso real.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

_SELF = Path(__file__).resolve().parent
_ROOT = _SELF.parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from nucleo.login_mapa_forca import login as login_mapa_forca


def run(ctx) -> Dict[str, str]:
    """Abre o Mapa Forca e deixa o navegador aberto para o operador usar."""
    ctx.log.info("Abrindo Mapa Forca para uso...")
    login_mapa_forca(ctx)
    ctx.log.info("[OK] Mapa Forca aberto. Navegador mantido aberto para uso.")
    return {"status": "ok", "detalhes": "Mapa Forca aberto para uso."}
