"""
executar.py — Contrato do baixar_bopm para o painel.

Pré-condição: se manifesto.precisa_vpn, o painel já chamou ctx.vpn.connect().
"""

from __future__ import annotations

import sys
import time
import traceback
from pathlib import Path
from typing import Any, Dict, List

# Garante que nucleo/ e o próprio diretório estejam acessíveis, seja rodado
# diretamente ou carregado pelo painel via importlib.
_SELF = Path(__file__).resolve().parent   # automacoes/baixar_bopm/
_ROOT = _SELF.parent.parent               # raiz do projeto
for _p in (str(_ROOT), str(_SELF)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import config
from siopm_navigator import SiopmNavigator, BopmEntry
from gemini_submitter import GeminiSubmitter


# ─────────────────────────────────────────────────────────────────────────────
# Ponto de entrada do contrato
# ─────────────────────────────────────────────────────────────────────────────

def run(ctx) -> Dict[str, Any]:
    """
    Executa o fluxo completo de baixar BOPMs.
    Retorna dict: {encontrados, salvos, falhas, arquivos}
    """
    log = ctx.log
    total_found = total_saved = total_failed = 0
    failed_ids: List[str] = []
    saved_paths: List[str] = []

    try:
        # ── Lançar browser ───────────────────────────────────────────────
        _step(log, "Iniciar Microsoft Edge")
        browser_ctx, page = ctx.browser.launch(
            headless=config.HEADLESS,
            timeout_element=config.TIMEOUT_ELEMENT,
            timeout_navigation=config.TIMEOUT_NAVIGATION,
        )
        nav = SiopmNavigator(
            log, ctx.vpn, browser_ctx, page,
            siopm_creds=ctx.segredos.get("siopm"),
        )

        # ── Login ────────────────────────────────────────────────────────
        _step(log, "Login no SIOPM Web")
        _with_retry(log, nav.login, "Login SIOPM")

        # ── CAD + Categoria ──────────────────────────────────────────────
        _step(log, f"Selecionar CAD '{config.SIOPM_CAD}' e Ocorrências")
        _with_retry(log, nav.select_cad_and_category, "Seleção CAD/Categoria")

        # ── Filtro ───────────────────────────────────────────────────────
        _step(log, f"Aplicar filtro BOPM — últimos {config.FILTER_DAYS} dias")
        _with_retry(log, nav.apply_bopm_filter, "Filtro BOPM")

        # ── Detectar pendentes ───────────────────────────────────────────
        _step(log, "Detectar BOPMs pendentes")
        pending: List[BopmEntry] = nav.get_pending_bopms()
        total_found = len(pending)

        if not pending:
            log.info("Nenhum BOPM pendente. Automação concluída.")
            _save_no_bopm_notice(log)
            return {"encontrados": 0, "salvos": 0, "falhas": 0, "arquivos": []}

        # ── Processar cada BOPM ──────────────────────────────────────────
        _step(log, f"Processar {total_found} BOPM(s) pendente(s)")

        for i, entry in enumerate(pending, 1):
            # Verifica VPN a cada BOPM (detecta queda durante o processamento)
            if ctx.vpn is not None:
                try:
                    ctx.vpn.ensure_connected()
                except RuntimeError as exc:
                    log.critical(str(exc))
                    raise

            log.info(f"\n{'─' * 50}")
            log.info(f"Processando BOPM {i}/{total_found} — {entry.bopm_id}")
            log.info(f"{'─' * 50}")

            try:
                if not nav.open_bopm(entry):
                    raise RuntimeError("Falha ao abrir BOPM.")
                filepath = nav.scroll_to_bottom_and_get_pdf(entry)
                if filepath:
                    saved_paths.append(filepath)
                    log.info(f"[{entry.bopm_id}] ✓ PDF salvo: {filepath}")
                    total_saved += 1
                else:
                    log.error(f"[{entry.bopm_id}] ✗ PDF não salvo.")
                    total_failed += 1
                    failed_ids.append(entry.bopm_id)
            except Exception as exc:
                log.error(f"[{entry.bopm_id}] Erro: {exc}")
                log.debug(traceback.format_exc())
                total_failed += 1
                failed_ids.append(entry.bopm_id)
            finally:
                try:
                    nav.go_back_to_list()
                except Exception:
                    pass

            if i < total_found:
                time.sleep(1.5)

        return {
            "encontrados": total_found,
            "salvos": total_saved,
            "falhas": total_failed,
            "arquivos": saved_paths,
        }

    finally:
        # Gemini: enquanto o Edge ainda está aberto
        if saved_paths:
            log.info(f"\n{len(saved_paths)} PDF(s) prontos para envio ao Gemini.")
            try:
                GeminiSubmitter(log).submit_pdfs(
                    saved_paths, playwright=ctx.browser.playwright
                )
            except Exception as exc:
                log.warning(f"Erro ao enviar ao Gemini: {exc}")

        try:
            if 'nav' in dir() and nav._bopm_list_url and 'page' in dir():
                page.goto(nav._bopm_list_url, wait_until="domcontentloaded", timeout=15_000)
                log.info(f"Edge mantido aberto na listagem: {nav._bopm_list_url}")
        except Exception:
            pass
        ctx.browser.close(keep_open=True)

        log.info("\n" + "═" * 60)
        log.info("  RELATÓRIO FINAL")
        log.info("═" * 60)
        log.info(f"  BOPMs encontrados : {total_found}")
        log.info(f"  PDFs salvos       : {total_saved}")
        log.info(f"  Falhas            : {total_failed}")
        if saved_paths:
            log.info("  Arquivos salvos:")
            for p in saved_paths:
                log.info(f"    • {p}")
        if failed_ids:
            log.warning(f"  Falhas: {', '.join(failed_ids)}")
        log.info("═" * 60)


# ─────────────────────────────────────────────────────────────────────────────
# Helpers internos
# ─────────────────────────────────────────────────────────────────────────────

def _step(log, description: str) -> None:
    log.info(f"\n{'═' * 60}")
    log.info(f"  {description}")
    log.info(f"{'═' * 60}")


def _with_retry(log, func, label: str, retries: int = None) -> None:
    max_r = (retries or config.MAX_RETRY) + 1
    for attempt in range(1, max_r + 1):
        try:
            func()
            return
        except RuntimeError:
            raise
        except Exception as exc:
            if attempt < max_r:
                log.warning(
                    f"'{label}' falhou ({attempt}/{max_r}): {exc} — retentando..."
                )
                time.sleep(3)
            else:
                raise RuntimeError(
                    f"'{label}' falhou após {max_r} tentativa(s): {exc}"
                )


def _save_no_bopm_notice(log) -> None:
    import os
    from datetime import datetime
    filepath = os.path.join(
        config.DOWNLOADS_DIR,
        f"BOPM_sem_pendencias_{datetime.now().strftime('%Y%m%d')}.txt",
    )
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            f.write("Resultado: Nenhum BOPM pendente de validação encontrado.\n")
            f.write(f"Filtro: {config.FILTER_TYPE} — últimos {config.FILTER_DAYS} dias\n")
            f.write(f"OPM: {config.SIOPM_OPM_CODE} ({config.SIOPM_OPM_NAME})\n")
        log.info(f"Aviso salvo: {filepath}")
    except Exception as exc:
        log.warning(f"Não foi possível salvar aviso: {exc}")
