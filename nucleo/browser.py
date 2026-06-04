"""
nucleo/browser.py — Inicialização do Microsoft Edge via Playwright.
"""

from __future__ import annotations

from logging import Logger
from typing import Optional, Tuple

from playwright.sync_api import (
    Browser, BrowserContext, Page, Playwright, sync_playwright,
)


class BrowserManager:
    """Inicializa o Microsoft Edge via Playwright."""

    def __init__(self, logger: Logger) -> None:
        self.log = logger
        self._playwright: Optional[Playwright] = None
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None

    def launch(
        self,
        headless: bool = False,
        timeout_element: int = 15_000,
        timeout_navigation: int = 45_000,
    ) -> Tuple[BrowserContext, Page]:
        """
        Lança o Edge e retorna (contexto, página inicial).

        Args:
            headless:           True para rodar sem janela visível.
            timeout_element:    Timeout padrão (ms) para localizar elementos.
            timeout_navigation: Timeout padrão (ms) para navegação entre páginas.
        """
        self.log.info("Iniciando Microsoft Edge...")
        self._playwright = sync_playwright().start()

        launch_kwargs = dict(
            headless=headless,
            slow_mo=300,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--start-maximized",
            ],
        )

        try:
            self._browser = self._playwright.chromium.launch(
                channel="msedge", **launch_kwargs
            )
            self.log.info("Edge lançado com sucesso.")
        except Exception:
            self.log.warning("Edge não encontrado, usando Chromium embutido.")
            self._browser = self._playwright.chromium.launch(**launch_kwargs)

        self._context = self._browser.new_context(
            viewport={"width": 1366, "height": 768},
            accept_downloads=True,
            ignore_https_errors=True,
        )
        self._context.set_default_timeout(timeout_element)
        self._context.set_default_navigation_timeout(timeout_navigation)

        page = self._context.new_page()
        self.log.info("Navegador pronto.")
        return self._context, page

    @property
    def playwright(self) -> Optional[Playwright]:
        """Instância do Playwright em uso — para reaproveitar em outras conexões."""
        return self._playwright

    def close(self) -> None:
        """Fecha browser e libera recursos do Playwright."""
        try:
            if self._context:
                self._context.close()
            if self._browser:
                self._browser.close()
            if self._playwright:
                self._playwright.stop()
            self.log.info("Navegador encerrado.")
        except Exception as exc:
            self.log.warning(f"Erro ao fechar navegador: {exc}")
