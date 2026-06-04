"""
nucleo/log.py — Logging padronizado para todas as automações.
"""

from __future__ import annotations

import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_LOG_DIR = _PROJECT_ROOT / "logs"


def setup_logger(
    name: str = "automacao",
    level: str = "INFO",
    log_dir: Optional[Path] = None,
    log_file: Optional[Path] = None,
) -> logging.Logger:
    """
    Configura e retorna o logger principal de uma automação.

    Handlers:
    - Console: INFO+   — saída resumida com cores ANSI
    - Arquivo:  DEBUG+ — registro completo com rotação de 5 MB

    Args:
        name:     Nome do logger (aparece nos logs e define o nome do arquivo).
        level:    Nível mínimo para o console ("DEBUG", "INFO", etc.).
        log_dir:  Pasta para o arquivo de log. Padrão: <raiz>/logs/.
        log_file: Caminho completo do arquivo de log. Sobrescreve log_dir se passado.
    """
    if log_dir is None:
        log_dir = _DEFAULT_LOG_DIR
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    if log_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"{name}_{timestamp}.log"
    log_file = Path(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    fmt_detailed = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(module)-20s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt_detailed)
    logger.addHandler(fh)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(getattr(logging, level.upper(), logging.INFO))
    ch.setFormatter(_ColorFormatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%H:%M:%S",
    ))
    logger.addHandler(ch)

    logger.info("=" * 70)
    logger.info(f"Automação '{name}' iniciada")
    logger.info(f"Log salvo em: {log_file}")
    logger.info("=" * 70)

    return logger


_COLORS = {
    "DEBUG":    "\033[36m",
    "INFO":     "\033[32m",
    "WARNING":  "\033[33m",
    "ERROR":    "\033[31m",
    "CRITICAL": "\033[35m",
}
_RESET = "\033[0m"


class _ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:  # noqa: A003
        color = _COLORS.get(record.levelname, "")
        record.levelname = f"{color}{record.levelname}{_RESET}"
        return super().format(record)
