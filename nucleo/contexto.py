"""
nucleo/contexto.py — Objeto de contexto passado ao run() de cada automação.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class Contexto:
    """
    Agrupa os recursos do núcleo para uma execução de automação.

    Atributos:
        log:             Logger configurado para esta execução.
        segredos:        Instância de Segredos para obter credenciais.
        vpn:             VPNManager (já conectado se precisa_vpn=True); None caso contrário.
        browser:         BrowserManager pronto para ser lançado via .launch().
        saidas:          Pasta de saída central do projeto (saidas/).
        entrada_arquivo: Caminho de arquivo fornecido pelo usuário (opcional — Fase 7).
        entrada_texto:   Texto colado pelo usuário (opcional — Fase 7).
    """
    log: logging.Logger
    segredos: Any           # nucleo.segredos.Segredos
    vpn: Any                # nucleo.vpn.VPNManager | None
    browser: Any            # nucleo.browser.BrowserManager
    saidas: Path
    entrada_arquivo: Optional[Path] = field(default=None)
    entrada_texto: Optional[str]  = field(default=None)
