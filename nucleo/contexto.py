"""
nucleo/contexto.py — Objeto de contexto passado ao run() de cada automação.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Contexto:
    """
    Agrupa os recursos do núcleo para uma execução de automação.

    Atributos:
        log:      Logger configurado para esta execução.
        segredos: Instância de Segredos para obter credenciais.
        vpn:      VPNManager (já conectado se precisa_vpn=True); None caso contrário.
        browser:  BrowserManager pronto para ser lançado via .launch().
        saidas:   Pasta de saída central do projeto (saidas/).
    """
    log: logging.Logger
    segredos: Any     # nucleo.segredos.Segredos
    vpn: Any          # nucleo.vpn.VPNManager | None
    browser: Any      # nucleo.browser.BrowserManager
    saidas: Path
