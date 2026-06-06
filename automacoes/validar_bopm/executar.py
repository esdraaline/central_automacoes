"""
executar.py — Contrato do validar_bopm para o painel.

Fluxo:
  1. Login no SIOPM Web (mesma rota do baixar_bopm).
  2. Navegar até a lista de BOPMs pendentes de validação.
  3. Para cada BOPM pendente:
     a. Abrir o BOPM clicando no ícone "Editar Ocorrência" (2º ícone da linha).
     b. Se "Validar BO-e" não estiver visível: clicar em "Visualiza PDF" primeiro.
     c. Marcar checkbox "Outros" em Providências Preliminares > Remessa ao.
     d. Registrar handler de dialog e clicar em "Validar BO-e".
     e. Dialog "Deseja validar o BO-e?" é aceito automaticamente.
     f. Clicar em "Retornar" para voltar à listagem.
  4. Retornar resumo no log e como dict de resultado.

Seletores mapeados pelos prints em 06/06/2026 (tela hsioocrwebtco.aspx).
Se falharem, o log registra URL e frames disponíveis para mapeamento manual.

Pré-condição: se manifesto.precisa_vpn, o painel já chamou ctx.vpn.connect().
"""

from __future__ import annotations

import sys
import time
import traceback
from pathlib import Path
from typing import Any, Dict, List

# Garante que nucleo/ e automacoes/baixar_bopm/ estejam no path,
# seja rodado diretamente ou carregado pelo painel via importlib.
_SELF = Path(__file__).resolve().parent          # automacoes/validar_bopm/
_ROOT = _SELF.parent.parent                      # raiz do projeto
_BOPM_DIR = _ROOT / "automacoes" / "baixar_bopm"

for _p in (str(_ROOT), str(_BOPM_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import config
from siopm_navigator import SiopmNavigator, BopmEntry


# ─────────────────────────────────────────────────────────────────────────────
# Ponto de entrada do contrato
# ─────────────────────────────────────────────────────────────────────────────

def run(ctx) -> Dict[str, Any]:
    """
    Executa o fluxo completo de validação de BOPMs no SIOPM Web.
    Retorna dict: {status, detalhes, validados, falhas}
    """
    log = ctx.log
    total_validados = 0
    total_falhas = 0
    falhas_ids: List[str] = []

    try:
        # ── Lançar Edge ──────────────────────────────────────────────────
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
            log.info("Nenhum BOPM pendente de validação. Automação concluída.")
            return {"status": "ok", "detalhes": "0 BOPMs pendentes", "validados": 0, "falhas": 0}

        # ── Validar cada BOPM ────────────────────────────────────────────
        _step(log, f"Validar {total_found} BOPM(s) pendente(s)")

        for i, entry in enumerate(pending, 1):
            # Verifica VPN a cada BOPM (detecta queda durante o processamento)
            if ctx.vpn is not None:
                try:
                    ctx.vpn.ensure_connected()
                except RuntimeError as exc:
                    log.critical(str(exc))
                    raise

            log.info(f"\n{'─' * 50}")
            log.info(f"Validando BOPM {i}/{total_found} — {entry.bopm_id}")
            log.info(f"{'─' * 50}")

            try:
                # Abre o BOPM (reutiliza método do SiopmNavigator)
                if not nav.open_bopm(entry):
                    raise RuntimeError("Falha ao abrir BOPM.")

                # Executa os 3 cliques de validação
                _validar_bopm(log, page)

                log.info(f"[{entry.bopm_id}] ✓ Validado.")
                total_validados += 1

            except Exception as exc:
                log.error(f"[{entry.bopm_id}] ✗ Falha: {exc}")
                log.debug(traceback.format_exc())
                total_falhas += 1
                falhas_ids.append(entry.bopm_id)

            finally:
                try:
                    nav.go_back_to_list()
                except Exception:
                    pass

            if i < total_found:
                time.sleep(1.5)

        detalhes = f"{total_validados}/{total_found} BOPM(s) validado(s)"
        if falhas_ids:
            detalhes += f" | Falhas: {', '.join(falhas_ids)}"

        return {
            "status": "ok" if total_falhas == 0 else "parcial",
            "detalhes": detalhes,
            "validados": total_validados,
            "falhas": total_falhas,
        }

    finally:
        try:
            if 'nav' in dir() and nav._bopm_list_url and 'page' in dir():
                page.goto(nav._bopm_list_url, wait_until="domcontentloaded", timeout=15_000)
                log.info(f"Edge mantido aberto na listagem: {nav._bopm_list_url}")
        except Exception:
            pass
        try:
            ctx.browser.close(keep_open=True)
        except Exception:
            pass

        log.info("\n" + "═" * 60)
        log.info("  RELATÓRIO FINAL — VALIDAR BOPM")
        log.info("═" * 60)
        log.info(f"  BOPMs validados : {total_validados}")
        log.info(f"  Falhas          : {total_falhas}")
        if falhas_ids:
            log.warning(f"  IDs com falha   : {', '.join(falhas_ids)}")
        log.info("═" * 60)


# ─────────────────────────────────────────────────────────────────────────────
# Lógica de validação (fluxo real mapeado em 06/06/2026)
# ─────────────────────────────────────────────────────────────────────────────

def _validar_bopm(log, page) -> None:
    """
    Fluxo real de validação (mapeado pelos prints em 06/06/2026):
      1. Se 'Validar BO-e' não estiver visível: clicar em 'Visualiza PDF' primeiro
         (BOs nunca visualizados não exibem o botão de validação).
      2. Marcar checkbox 'Outros' em Providências Preliminares > Remessa ao.
         Pula se já estiver marcado.
      3. Registrar handler de dialog ANTES do clique (window.confirm nativo).
      4. Clicar em 'Validar BO-e'.
      5. Dialog 'Deseja validar o BO-e?' é aceito automaticamente pelo handler.
      6. Clicar em 'Retornar' para voltar à listagem.
    """
    _wait_stable(page)

    # Log diagnóstico: frames disponíveis
    frames = page.frames
    log.info(f"Frames disponíveis após abrir BOPM ({len(frames)}):")
    for f in frames:
        log.info(f"  • {f.url}")

    # ── Passo 1: verificar se 'Validar BO-e' está visível ────────────────
    log.info("Passo 1: verificando presença de 'Validar BO-e'...")
    validar_presente = _find_in_frames(
        page,
        selectors=[
            "input[name='W0236BTNVALIDARTCO']",
            "input[value='Validar BO-e']",
            "input[type='submit'][value*='Validar' i]",
        ],
        has_text_fallback="Validar BO-e",
        label="Validar BO-e (verificação)",
        log=log,
    )

    if validar_presente is None:
        log.info("'Validar BO-e' não visível. Clicando em 'Visualiza PDF' primeiro...")
        visualizar_btn = _find_in_frames(
            page,
            selectors=[
                "input[name='W0236BTNVISUALIZARTCO']",
                "input[value*='Visualiza' i]",
                "input[type='submit'][value*='PDF' i]",
            ],
            has_text_fallback="Visualiza PDF",
            label="Visualiza PDF",
            log=log,
        )
        if visualizar_btn is None:
            _log_falha_diagnostico(log, page, "Visualiza PDF")
            raise RuntimeError(
                "Botão 'Visualiza PDF' não encontrado e 'Validar BO-e' também ausente. "
                "Verifique o log acima."
            )
        visualizar_btn.scroll_into_view_if_needed()

        # O PDF pode abrir em nova aba — registrar handler para fechar automaticamente
        def _handle_popup(popup):
            try:
                popup.wait_for_load_state("domcontentloaded", timeout=10_000)
                popup.close()
                log.info("Aba de PDF fechada.")
            except Exception:
                pass

        page.context.once("page", _handle_popup)
        visualizar_btn.click()
        _wait_stable(page)
        time.sleep(2)
        log.info("'Visualiza PDF' clicado. Verificando 'Validar BO-e' novamente...")
        _wait_stable(page)

    # ── Passo 2: marcar checkbox 'Outros' ────────────────────────────────
    log.info("Passo 2: localizando checkbox 'Outros'...")
    outros = _find_in_frames(
        page,
        selectors=[
            "input[type='checkbox'][name*='OUTROS' i]",
            "input[type='checkbox'][id*='outros' i]",
            "input[type='checkbox'][value*='outros' i]",
            "label:has-text('Outros') input[type='checkbox']",
        ],
        has_text_fallback="Outros",
        label="Outros (checkbox)",
        log=log,
    )
    if outros is None:
        _log_falha_diagnostico(log, page, "Outros")
        raise RuntimeError(
            "Checkbox 'Outros' não encontrado. "
            "Verifique o log acima para URL e frames disponíveis."
        )
    outros.scroll_into_view_if_needed()
    try:
        if not outros.is_checked():
            outros.click()
            log.info("Checkbox 'Outros' marcado.")
        else:
            log.info("Checkbox 'Outros' já estava marcado. Pulando.")
    except Exception:
        outros.click()
        log.info("Checkbox 'Outros' clicado.")
    time.sleep(0.5)

    # ── Passo 3: localizar botão 'Validar BO-e' ──────────────────────────
    log.info("Passo 3: localizando botão 'Validar BO-e'...")
    validar_btn = _find_in_frames(
        page,
        selectors=[
            "input[name='W0236BTNVALIDARTCO']",
            "input[value='Validar BO-e']",
            "input[type='submit'][value*='Validar' i]",
        ],
        has_text_fallback="Validar BO-e",
        label="Validar BO-e",
        log=log,
    )
    if validar_btn is None:
        _log_falha_diagnostico(log, page, "Validar BO-e")
        raise RuntimeError(
            "Botão 'Validar BO-e' não encontrado. "
            "Verifique o log acima para URL e frames disponíveis."
        )
    validar_btn.scroll_into_view_if_needed()

    # ── Passo 4: registrar handler de dialog e clicar ────────────────────
    log.info("Passo 4: registrando handler de dialog e clicando em 'Validar BO-e'...")

    def _accept_dialog(dialog):
        log.info(f"Dialog capturado: '{dialog.message}'. Aceitando...")
        dialog.accept()

    page.once("dialog", _accept_dialog)
    validar_btn.click()
    _wait_stable(page)
    log.info("'Validar BO-e' clicado e dialog aceito.")

    # ── Passo 5: clicar em 'Retornar' ────────────────────────────────────
    log.info("Passo 5: clicando em 'Retornar' para voltar à listagem...")
    time.sleep(1)
    retornar_btn = _find_in_frames(
        page,
        selectors=[
            "input[name='W0236BTNRETORNAR']",
            "input[value='Retornar']",
            "a:has-text('Retornar')",
        ],
        has_text_fallback="Retornar",
        label="Retornar",
        log=log,
    )
    if retornar_btn is None:
        log.warning("Botão 'Retornar' não encontrado. O go_back_to_list() do finally cobrirá.")
    else:
        retornar_btn.scroll_into_view_if_needed()
        retornar_btn.click()
        _wait_stable(page)
        log.info("'Retornar' clicado. De volta à listagem.")


# ─────────────────────────────────────────────────────────────────────────────
# Helpers internos
# ─────────────────────────────────────────────────────────────────────────────

def _find_in_frames(page, selectors: list, has_text_fallback: str, label: str, log):
    """
    Tenta localizar um elemento em todos os frames da página.
    Testa cada seletor em todos os frames antes de passar para o próximo.
    Retorna o primeiro elemento visível encontrado, ou None.
    """
    frames = page.frames or [page]

    for sel in selectors:
        for frame in frames:
            try:
                el = frame.query_selector(sel)
                if el and el.is_visible():
                    log.debug(f"[{label}] Encontrado com seletor '{sel}' em frame '{frame.url}'")
                    return el
            except Exception:
                continue

    # Fallback: has-text em todos os frames
    for frame in frames:
        for tag in ("input", "button", "a", "label"):
            try:
                el = frame.locator(f"{tag}:has-text('{has_text_fallback}')").first
                if el and el.is_visible():
                    log.debug(
                        f"[{label}] Encontrado via has-text '{has_text_fallback}' "
                        f"(tag={tag}) em frame '{frame.url}'"
                    )
                    return el.element_handle()
            except Exception:
                continue

    return None


def _log_falha_diagnostico(log, page, label: str) -> None:
    """Loga URL atual e todos os frames para diagnóstico de seletor não encontrado."""
    log.warning(f"{'─' * 50}")
    log.warning(f"DIAGNÓSTICO — '{label}' não encontrado")
    log.warning(f"URL da page principal: {page.url}")
    log.warning(f"Frames disponíveis ({len(page.frames)}):")
    for f in page.frames:
        log.warning(f"  • {f.url}")
    # Loga todos os inputs/botões/links visíveis para ajudar no mapeamento
    for frame in page.frames:
        try:
            elements = frame.evaluate("""
                () => {
                    const tags = ['input', 'button', 'a', 'label'];
                    const result = [];
                    for (const tag of tags) {
                        for (const el of document.querySelectorAll(tag)) {
                            const r = el.getBoundingClientRect();
                            if (r.width === 0 || r.height === 0) continue;
                            result.push({
                                tag: el.tagName,
                                type: el.type || '',
                                value: (el.value || '').slice(0, 60),
                                text: (el.innerText || '').trim().slice(0, 60),
                                id: el.id || '',
                                name: el.name || '',
                            });
                        }
                    }
                    return result;
                }
            """)
            if elements:
                log.warning(f"  Elementos interativos visíveis em '{frame.url}':")
                for el in elements:
                    log.warning(
                        f"    <{el['tag'].lower()} type={el['type']!r} "
                        f"id={el['id']!r} name={el['name']!r} "
                        f"value={el['value']!r} text={el['text']!r}>"
                    )
        except Exception:
            pass
    log.warning(f"{'─' * 50}")


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


def _wait_stable(page, timeout: int = None) -> None:
    t = timeout or config.TIMEOUT_PAGE_LOAD
    try:
        page.wait_for_load_state("networkidle", timeout=t)
    except Exception:
        try:
            page.wait_for_load_state("load", timeout=t // 2)
        except Exception:
            pass
