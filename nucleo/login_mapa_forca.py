"""
nucleo/login_mapa_forca.py - Login e abertura do Mapa Forca no SIOPM Web.

Seletores/indicadores documentados:
- Login: http://sistemasopr.intranet.policiamilitar.sp.gov.br/siopmweb/HSiopm.aspx
- Usuario: #txtUsuario ou inputs cujo id/name contenham usu/user
- Senha: #txtSenha ou input[type=password]
- Categoria: select da tela HSIOPMCat.aspx, opcao "COMP MAPA FORÇA"
- Destino: hsioptrsel.aspx
- Campo OPM: input de texto proximo ao rotulo "OPM" ou primeiro input visivel
- Procurar: input/button/link com texto/value "Procurar"
- Sessao ativa: tabela com colunas "US", "Status" e "Componente"
"""

from __future__ import annotations

import time
from typing import Any

from playwright.sync_api import TimeoutError as PWTimeout


SIOPM_URL = "http://sistemasopr.intranet.policiamilitar.sp.gov.br/siopmweb/HSiopm.aspx"
CATEGORIA_MAPA_FORCA = "COMP MAPA FORÇA"
OPM_5_CIA = "610025000"


def login(ctx: Any):
    """Autentica no SIOPM Web e abre a composicao do Mapa Forca."""
    log = ctx.log
    creds = ctx.segredos.get("siopm")

    log.info("Abrindo SIOPM Web para Mapa Forca...")
    _browser_ctx, page = ctx.browser.launch(headless=False)

    _goto(page, SIOPM_URL)
    _fill_first(
        page,
        ["#txtUsuario", "input[name*='usu' i]", "input[name*='user' i]",
         "input[id*='user' i]", "input[type='text']"],
        creds["user"],
        "usuario SIOPM",
    )
    _fill_first(
        page,
        ["#txtSenha", "input[type='password']", "input[name*='senha' i]",
         "input[name*='pass' i]", "input[id*='senha' i]"],
        creds["password"],
        "senha SIOPM",
    )
    _click_first(
        page,
        ["input[type='submit']", "input[value*='Entra' i]",
         "button[type='submit']", "input[value*='Login' i]",
         "input[value*='OK' i]", "input[name*='btn' i]"],
        "botao login SIOPM",
    )
    _wait_stable(page)
    log.info("Login SIOPM realizado.")

    _selecionar_cad_se_necessario(page, log)
    _selecionar_categoria_mapa_forca(page, log)
    _preencher_opm_e_procurar(page, log)
    _assert_mapa_forca_ativo(page)

    log.info("Mapa Forca carregado com tabela de resultados.")
    return page


def _selecionar_cad_se_necessario(page, log) -> None:
    """Seleciona CAD Aracatuba quando a tela intermediaria aparece apos o login."""
    selects = page.query_selector_all("select")
    for sel in selects:
        try:
            for opt in sel.query_selector_all("option"):
                text = (opt.inner_text() or "").strip()
                if "ARACATUBA" in _normalizar(text):
                    log.info("Selecionando CAD Aracatuba...")
                    sel.select_option(label=text)
                    _click_first(
                        page,
                        ["input[value*='Confirmar' i]", "input[value*='Confirma' i]",
                         "input[value*='OK' i]", "input[value*='Entra' i]",
                         "input[type='submit']", "button[type='submit']"],
                        "botao confirmacao CAD",
                    )
                    _wait_stable(page)
                    return
        except Exception:
            continue


def _selecionar_categoria_mapa_forca(page, log) -> None:
    log.info("Selecionando categoria COMP MAPA FORÇA...")
    selects = page.query_selector_all("select")
    for sel in selects:
        try:
            for opt in sel.query_selector_all("option"):
                text = (opt.inner_text() or "").strip()
                if _normalizar(CATEGORIA_MAPA_FORCA) in _normalizar(text):
                    sel.select_option(label=text)
                    _click_first(
                        page,
                        ["input[value*='Confirmar' i]", "input[value*='Confirm' i]",
                         "input[type='submit']", "button:has-text('Confirmar')"],
                        "botao Confirmar categoria",
                    )
                    _wait_stable(page)
                    return
        except Exception:
            continue
    raise RuntimeError(
        "Categoria COMP MAPA FORÇA nao encontrada. "
        f"URL atual: {page.url}. Opcoes visiveis: {_select_options_debug(page)}"
    )


def _preencher_opm_e_procurar(page, log) -> None:
    log.info("Preenchendo OPM do Mapa Forca...")
    opm = _find_opm_input(page)
    if opm is None:
        raise RuntimeError("Campo OPM nao encontrado no Mapa Forca.")
    opm.click(click_count=3)
    opm.fill(OPM_5_CIA)
    time.sleep(0.5)

    log.info("Clicando em Procurar...")
    _click_first(
        page,
        ["input[value*='Procurar' i]", "button:has-text('Procurar')",
         "a:has-text('Procurar')", "input[type='submit']"],
        "botao Procurar",
    )
    _wait_stable(page)


def _find_opm_input(page):
    candidates = page.query_selector_all("input[type='text'], input:not([type])")
    visible = []
    for inp in candidates:
        try:
            if inp.is_visible():
                visible.append(inp)
                combined = (
                    (inp.get_attribute("id") or "") + " " +
                    (inp.get_attribute("name") or "") + " " +
                    (inp.get_attribute("title") or "")
                ).lower()
                if "opm" in combined:
                    return inp
        except Exception:
            continue

    for inp in visible:
        try:
            label_text = inp.evaluate(
                """el => {
                    const tr = el.closest('tr');
                    return tr ? (tr.innerText || '') : '';
                }"""
            )
            if "OPM" in (label_text or "").upper():
                return inp
        except Exception:
            continue

    return visible[0] if visible else None


def _assert_mapa_forca_ativo(page) -> None:
    try:
        page.wait_for_load_state("domcontentloaded", timeout=10_000)
    except PWTimeout:
        pass

    text = _page_text(page).upper()
    required = ["US", "STATUS", "COMPONENTE"]
    if not all(item in text for item in required):
        raise RuntimeError("Tabela do Mapa Forca nao detectada.")


def _goto(page, url: str) -> None:
    page.goto(url, wait_until="domcontentloaded")
    _wait_stable(page)


def _wait_stable(page, timeout: int = 45_000) -> None:
    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
    except PWTimeout:
        try:
            page.wait_for_load_state("load", timeout=10_000)
        except PWTimeout:
            pass


def _fill_first(page, selectors: list[str], value: str, label: str) -> None:
    el = _find_first(page, selectors)
    if el is None:
        raise RuntimeError(f"Campo nao encontrado: {label}")
    el.scroll_into_view_if_needed()
    el.click(click_count=3)
    el.fill(value)


def _click_first(page, selectors: list[str], label: str) -> None:
    el = _find_first(page, selectors)
    if el is None:
        raise RuntimeError(f"Elemento nao encontrado: {label}")
    el.scroll_into_view_if_needed()
    el.click()


def _find_first(page, selectors: list[str]):
    for sel in selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                return el
        except Exception:
            continue
    return None


def _page_text(page) -> str:
    try:
        return page.locator("body").inner_text(timeout=5_000)
    except Exception:
        return ""


def _select_options_debug(page) -> str:
    options = []
    for sel in page.query_selector_all("select"):
        try:
            texts = [
                (opt.inner_text() or "").strip()
                for opt in sel.query_selector_all("option")
            ]
            options.extend([t for t in texts if t])
        except Exception:
            continue
    return " | ".join(options[:30])


def _normalizar(text: str) -> str:
    return (
        text.upper()
        .replace("Ç", "C")
        .replace("Á", "A")
        .replace("À", "A")
        .replace("Â", "A")
        .replace("Ã", "A")
        .replace("É", "E")
        .replace("Ê", "E")
        .replace("Í", "I")
        .replace("Ó", "O")
        .replace("Ô", "O")
        .replace("Õ", "O")
        .replace("Ú", "U")
    )
