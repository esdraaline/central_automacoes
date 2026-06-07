"""
executar.py — Contrato da Despachadora para o painel.

Pré-condições:
  - manifesto.precisa_vpn = False  →  ctx.vpn é None
  - ctx.entrada_arquivo ou ctx.entrada_texto deve estar preenchido (Sprint 7.3
    garante isso via UI; em testes pode ser injetado diretamente no ctx)
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

_SELF = Path(__file__).resolve().parent       # automacoes/despachadora/
_ROOT = _SELF.parent.parent                   # raiz do projeto
_NUCLEO_DESP = _SELF / "nucleo_despachadora"

for _p in (str(_ROOT), str(_SELF), str(_NUCLEO_DESP)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from nucleo_despachadora.despachadora import processar


def run(ctx) -> Dict[str, Any]:
    """
    Ponto de entrada do contrato.

    ctx.entrada_arquivo : Path | None  — expediente como arquivo
    ctx.entrada_texto   : str  | None  — expediente colado como texto

    Retorna:
        status_txt  : string curta para o label de status do card
        saida_longa : string com os 6 blocos do despacho (Sprint 7.3 exibe em janela)
    """
    resultado = processar(ctx)
    return {
        "status_txt": "✓ Despacho gerado",
        "saida_longa": resultado,
    }


# ─── Execução direta para testes (sem painel) ────────────────────────────────
if __name__ == "__main__":
    import argparse
    from nucleo.segredos import Segredos
    from nucleo.log import setup_logger
    from nucleo.browser import BrowserManager
    from nucleo.contexto import Contexto

    parser = argparse.ArgumentParser(description="Teste local da Despachadora")
    grp = parser.add_mutually_exclusive_group(required=True)
    grp.add_argument("--arquivo", metavar="PATH", help="Caminho do expediente")
    grp.add_argument("--texto",   metavar="TEXTO", help="Expediente como texto direto")
    args = parser.parse_args()

    _log = setup_logger(name="despachadora_teste", level="INFO")
    _ctx = Contexto(
        log=_log,
        segredos=Segredos(),
        vpn=None,
        browser=BrowserManager(_log),
        saidas=_ROOT / "saidas",
        entrada_arquivo=Path(args.arquivo) if args.arquivo else None,
        entrada_texto=args.texto,
    )

    r = run(_ctx)
    print("\n" + "═" * 60)
    print(r.get("saida_longa", ""))
    print("═" * 60)
