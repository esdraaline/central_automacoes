"""Login no Órion para consulta de indicadores criminais (somente leitura)."""

from __future__ import annotations

from typing import Any, Iterable

from playwright.sync_api import TimeoutError as PWTimeout


USER_SELECTORS = (
    "input[id*='usuario' i]", "input[name*='usuario' i]",
    "input[id*='user' i]", "input[name*='user' i]",
    "input[id*='login' i]", "input[name*='login' i]",
    "input[type='email']", "input[type='text']",
)
PASSWORD_SELECTORS = (
    "input[type='password']", "input[id*='senha' i]",
    "input[name*='senha' i]", "input[id*='pass' i]",
    "input[name*='pass' i]",
)
SUBMIT_SELECTORS = (
    "button[type='submit']", "input[type='submit']",
    "button:has-text('Entrar')", "button:has-text('Acessar')",
    "button:has-text('Login')", "input[value*='Entrar' i]",
    "input[value*='Acessar' i]", "input[value*='Login' i]",
)
SUCCESS_TERMS = (
    "indicadores", "painel", "dashboard", "consultas", "município",
    "municipio", "estatística", "estatistica", "sair", "logout",
)
ERROR_TERMS = (
    "usuário ou senha inválid", "usuario ou senha invalid",
    "credenciais inválid", "acesso negado", "login inválido",
    "login invalido", "senha incorreta",
)


def login(ctx: Any):
    """Abre o Órion, autentica e devolve a página com a sessão ativa."""
    log = ctx.log
    creds = ctx.segredos.get("orion")
    url = creds["url"].strip()
    if not url.lower().startswith(("http://", "https://")):
        raise ValueError("ORION_URL deve começar com http:// ou https://.")

    log.info("Abrindo Órion...")
    _browser_ctx, page = ctx.browser.launch(headless=False)
    page.goto(url, wait_until="domcontentloaded")
    _wait_stable(page)

    if _sessao_ativa(page, url):
        log.info("Sessão Órion já estava ativa.")
        return page

    user = _find_first_in_frames(page, USER_SELECTORS, fillable=True)
    password = _find_first_in_frames(page, PASSWORD_SELECTORS, fillable=True)
    if user is None or password is None:
        _log_diagnostico(page, log)
        raise RuntimeError("Campos de usuário/senha do Órion não encontrados.")

    user.click(click_count=3)
    user.fill(creds["user"])
    password.click(click_count=3)
    password.fill(creds["password"])

    submit = _find_first_in_frames(page, SUBMIT_SELECTORS)
    if submit is None:
        _log_diagnostico(page, log)
        raise RuntimeError("Botão de entrada do Órion não encontrado.")

    log.info("Enviando credenciais ao Órion...")
    submit.click()
    _wait_stable(page)
    _assert_sessao_ativa(page, url)
    log.info("Sessão Órion ativa. Tela inicial pronta para consulta.")
    return page


def _frames(page) -> Iterable:
    return page.frames or [page]


def _find_first_in_frames(page, selectors, fillable: bool = False):
    for selector in selectors:
        for frame in _frames(page):
            try:
                for element in frame.query_selector_all(selector):
                    if not element.is_visible():
                        continue
                    if fillable and not _is_fillable(element):
                        continue
                    return element
            except Exception:
                continue
    return None


def _is_fillable(element) -> bool:
    try:
        tag = (element.evaluate("e => e.tagName") or "").lower()
        if tag == "textarea":
            return True
        if tag != "input":
            return False
        return (element.get_attribute("type") or "text").lower() in {
            "", "text", "password", "email", "number", "tel",
        }
    except Exception:
        return False


def _sessao_ativa(page, login_url: str) -> bool:
    password = _find_first_in_frames(page, PASSWORD_SELECTORS, fillable=True)
    if password is not None:
        return False
    text = _page_text(page).lower()
    url_changed = (page.url or "").rstrip("/") != login_url.rstrip("/")
    return url_changed or any(term in text for term in SUCCESS_TERMS)


def _assert_sessao_ativa(page, login_url: str) -> None:
    text = _page_text(page).lower()
    erro = next((term for term in ERROR_TERMS if term in text), None)
    if erro:
        raise RuntimeError("Login Órion recusado; verifique usuário e senha.")
    if not _sessao_ativa(page, login_url):
        raise RuntimeError(
            f"Sessão Órion não confirmada. URL atual: {page.url}. "
            "O formulário de senha permaneceu visível."
        )


def _page_text(page) -> str:
    partes = []
    for frame in _frames(page):
        try:
            partes.append(frame.locator("body").inner_text(timeout=3_000))
        except Exception:
            continue
    return "\n".join(partes)


def _wait_stable(page, timeout: int = 45_000) -> None:
    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
    except PWTimeout:
        try:
            page.wait_for_load_state("load", timeout=10_000)
        except PWTimeout:
            pass


def _log_diagnostico(page, log) -> None:
    """Registra estrutura útil, sem valores digitados ou credenciais."""
    log.warning(f"Diagnóstico Órion — URL atual: {page.url}")
    for frame in _frames(page):
        log.warning(f"Frame: {frame.url}")
        try:
            elementos = frame.evaluate("""() => Array.from(
                document.querySelectorAll('input, button, a')
            ).filter(e => e.offsetParent !== null).slice(0, 40).map(e => ({
                tag: e.tagName, type: e.type || '', id: e.id || '',
                name: e.name || '', text: (e.innerText || '').trim().slice(0, 50)
            }))""")
            for item in elementos:
                log.warning(
                    f"  <{item['tag'].lower()} type={item['type']!r} "
                    f"id={item['id']!r} name={item['name']!r} text={item['text']!r}>"
                )
        except Exception:
            continue
