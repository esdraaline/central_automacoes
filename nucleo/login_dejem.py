"""
nucleo/login_dejem.py - Login no Dejem/Delegada pelo Portal MS.

Seletores/indicadores documentados:
- URL: http://ms.policiamilitar.sp.gov.br/login.aspx
- Usuario: input de texto com id/name contendo usuario/user/login ou primeiro texto visivel
- Senha: input[type=password] ou id/name contendo senha/pass
- Confirmar: input/button com texto/value "Confirmar"
- Sessao ativa: URL home.aspx e texto visivel "Bem Vindo(a)"
"""

from __future__ import annotations

from typing import Any

from playwright.sync_api import TimeoutError as PWTimeout


DEJEM_URL = "http://ms.policiamilitar.sp.gov.br/login.aspx"


def login(ctx: Any):
    """Autentica no Portal MS e confirma a home do Dejem/Delegada."""
    log = ctx.log
    creds = ctx.segredos.get("dejem")

    log.info("Abrindo Portal MS / Dejem...")
    _browser_ctx, page = ctx.browser.launch(headless=False)

    page.goto(DEJEM_URL, wait_until="domcontentloaded")
    _wait_stable(page)

    _fill_first(
        page,
        ["input[id*='usuario' i]", "input[name*='usuario' i]",
         "input[id*='user' i]", "input[name*='user' i]",
         "input[id*='login' i]", "input[name*='login' i]",
         "input[type='text']", "input:not([type])"],
        creds["usuario"],
        "usuario Dejem",
    )
    _fill_first(
        page,
        ["input[type='password']", "input[id*='senha' i]",
         "input[name*='senha' i]", "input[id*='pass' i]",
         "input[name*='pass' i]"],
        creds["senha"],
        "senha Dejem",
    )
    _click_first(
        page,
        ["input[value*='Confirmar' i]", "button:has-text('Confirmar')",
         "input[type='submit']", "button[type='submit']"],
        "botao Confirmar",
    )
    _wait_stable(page)
    _assert_dejem_ativo(page)

    log.info("Sessao Dejem ativa detectada.")
    return page


def _assert_dejem_ativo(page) -> None:
    url = (page.url or "").lower()
    try:
        welcome = page.get_by_text("Bem Vindo(a)", exact=False).first.is_visible(timeout=5_000)
    except Exception:
        welcome = False

    if "home.aspx" not in url or not welcome:
        raise RuntimeError("Sessao Dejem nao detectada: home.aspx/Bem Vindo(a) ausente.")


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
    el = _find_clickable_first(page, selectors)
    if el is None:
        raise RuntimeError(f"Elemento nao encontrado: {label}")
    el.scroll_into_view_if_needed()
    el.click()


def _find_first(page, selectors: list[str]):
    for sel in selectors:
        try:
            candidates = page.query_selector_all(sel)
            for el in candidates:
                if el and el.is_visible() and _is_fillable(el):
                    return el
        except Exception:
            continue
    return None


def _is_fillable(el) -> bool:
    try:
        tag = (el.evaluate("e => e.tagName") or "").lower()
        if tag == "textarea":
            return True
        if tag != "input":
            return False
        input_type = (el.get_attribute("type") or "text").lower()
        return input_type in {"", "text", "password", "email", "number", "tel"}
    except Exception:
        return False


def _find_clickable_first(page, selectors: list[str]):
    for sel in selectors:
        try:
            candidates = page.query_selector_all(sel)
            for el in candidates:
                if el and el.is_visible():
                    return el
        except Exception:
            continue
    return None
