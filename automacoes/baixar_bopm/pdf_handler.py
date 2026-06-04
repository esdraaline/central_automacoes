"""
pdf_handler.py — Tratamento de download e salvamento de PDFs do SIOPM.

Estratégias em ordem de prioridade:
1. Playwright expect_download() — o servidor envia Content-Disposition: attachment
2. Popup/nova aba com PDF — captura URL e baixa com as cookies da sessão
3. Iframe com PDF embutido — extrai a URL do iframe e baixa
4. Fallback: print-to-PDF via Playwright (somente para páginas HTML)
"""

import os
import re
import time
from logging import Logger
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from playwright.sync_api import BrowserContext, Page

import config


class PDFHandler:
    """Gerencia o download e armazenamento dos PDFs de BOPM."""

    def __init__(self, logger: Logger, context: BrowserContext) -> None:
        self.log = logger
        self.ctx = context
        os.makedirs(config.DOWNLOADS_DIR, exist_ok=True)

    # ------------------------------------------------------------------
    # Pública: salvar PDF a partir da página de ocorrência aberta
    # ------------------------------------------------------------------

    def save_bopm_pdf(self, page: Page, bopm_id: str, nav_frame=None) -> Optional[str]:
        """
        Clica em 'Visualizar PDF' e salva o arquivo em Downloads.
        nav_frame: frame onde o BO foi carregado (pode diferir da page principal).
        """
        self.log.info(f"[{bopm_id}] Tentando salvar PDF...")
        frame = nav_frame or page

        # Estratégia 1: popup com timeout curto (10s)
        # Funciona se o PDF abre em nova aba (comportamento não-GeneXus)
        filepath = self._try_popup_download(page, bopm_id, frame, popup_timeout=10_000)
        if filepath:
            return filepath

        # Estratégia 2: same-tab (gxSubmit)
        # Comportamento padrão do SIOPM — GeneXus navega na mesma aba
        filepath = self._try_same_tab_download(page, bopm_id, frame)
        if filepath:
            return filepath

        # Estratégia 3: iframe
        filepath = self._try_iframe_download(page, bopm_id, frame)
        if filepath:
            return filepath

        self.log.error(f"[{bopm_id}] Nenhuma estratégia de download funcionou.")
        return None

    # ------------------------------------------------------------------
    # Estratégia 1: download direto (Content-Disposition: attachment)
    # ------------------------------------------------------------------

    def _try_direct_download(self, page: Page, bopm_id: str) -> Optional[str]:
        btn = self._find_pdf_button(page)
        if not btn:
            return None

        try:
            with page.expect_download(timeout=config.TIMEOUT_PDF_DOWNLOAD) as dl_info:
                btn.click()
            download = dl_info.value

            suggested = download.suggested_filename or f"BOPM_{bopm_id}.pdf"
            dest = os.path.join(config.DOWNLOADS_DIR, suggested)
            download.save_as(dest)
            self.log.info(f"[{bopm_id}] PDF salvo (download direto): {dest}")
            return dest
        except Exception as exc:
            self.log.debug(f"[{bopm_id}] Estratégia 1 falhou: {exc}")
            return None

    # ------------------------------------------------------------------
    # Estratégia 2: popup / nova aba
    # ------------------------------------------------------------------

    def _try_popup_download(self, page: Page, bopm_id: str, frame=None, popup_timeout: int = 10_000) -> Optional[str]:
        btn = self._find_pdf_button(page)
        if not btn:
            return None

        try:
            with page.expect_popup(timeout=popup_timeout) as popup_info:
                btn.click()
            popup: Page = popup_info.value
            popup.wait_for_load_state("domcontentloaded", timeout=config.TIMEOUT_PAGE_LOAD)
            time.sleep(3)  # aguarda iframe interno carregar

            # SIOPM: hsiopdftco.aspx é wrapper HTML com <IFRAME> apontando para o PDF real.
            # Tenta obter a URL do iframe (child frame ou atributo src).
            pdf_url = None
            try:
                for f in popup.frames:
                    furl = getattr(f, 'url', '') or ""
                    if furl and not furl.startswith("about:") and furl != popup.url:
                        pdf_url = furl
                        self.log.debug(f"[{bopm_id}] Popup iframe frame: {pdf_url}")
                        break
            except Exception:
                pass

            if not pdf_url:
                try:
                    iframe_el = popup.query_selector("iframe[src]")
                    if iframe_el:
                        src = iframe_el.get_attribute("src") or ""
                        if src and not src.startswith("about:"):
                            pdf_url = src if src.startswith("http") else urljoin(popup.url, src)
                            self.log.debug(f"[{bopm_id}] Popup iframe src: {pdf_url}")
                except Exception:
                    pass

            if not pdf_url:
                pdf_url = popup.url

            self.log.debug(f"[{bopm_id}] Popup URL: {pdf_url}")
            filepath = self._download_url(pdf_url, bopm_id, popup)
            popup.close()
            return filepath

        except Exception as exc:
            self.log.debug(f"[{bopm_id}] Estratégia popup falhou: {exc}")
            return None

    # ------------------------------------------------------------------
    # Estratégia 2b: same-tab (gxSubmit)
    # ------------------------------------------------------------------

    def _try_same_tab_download(self, page: Page, bopm_id: str, frame=None) -> Optional[str]:
        """
        Estratégia para quando 'Visualizar PDF' usa gxSubmit() (same-tab).
        Clica no botão, detecta mudança de URL no frame ou na page, e baixa.
        """
        target = frame or page
        btn = self._find_pdf_button(target)
        if not btn and frame and frame != page:
            btn = self._find_pdf_button(page)
        if not btn:
            self.log.debug(f"[{bopm_id}] Estratégia same-tab: botão não encontrado.")
            return None

        try:
            url_antes_frame = target.url if hasattr(target, 'url') else ""
            url_antes_page = page.url
            btn.click()
            time.sleep(4)  # aguarda gxSubmit completar

            url_depois_frame = target.url if hasattr(target, 'url') else ""
            url_depois_page = page.url

            self.log.debug(f"[{bopm_id}] Same-tab frame: {url_antes_frame} → {url_depois_frame}")
            self.log.debug(f"[{bopm_id}] Same-tab page:  {url_antes_page} → {url_depois_page}")

            for candidate_url in [url_depois_frame, url_depois_page]:
                if (candidate_url and
                        candidate_url not in (url_antes_frame, url_antes_page) and
                        not candidate_url.startswith("about:")):
                    filepath = self._download_url(candidate_url, bopm_id, page)
                    if filepath:
                        return filepath

            # Fallback: verifica se a page atual já é um PDF inline
            try:
                content_type = page.evaluate(
                    "() => document.contentType || document.mimeType || ''"
                ) or ""
                if "pdf" in content_type.lower():
                    filepath = self._download_url(page.url, bopm_id, page)
                    if filepath:
                        return filepath
            except Exception:
                pass

            return None

        except Exception as exc:
            self.log.debug(f"[{bopm_id}] Estratégia same-tab falhou: {exc}")
            return None

    # ------------------------------------------------------------------
    # Estratégia 3: iframe com PDF embutido
    # ------------------------------------------------------------------

    def _try_iframe_download(self, page: Page, bopm_id: str, frame=None) -> Optional[str]:
        target = frame or page
        btn = self._find_pdf_button(target)
        if not btn and frame and frame != page:
            btn = self._find_pdf_button(page)
        if not btn:
            return None

        try:
            btn.click()
            time.sleep(3)  # aguarda carregamento do iframe

            # Procura iframes com src de PDF
            iframes = page.query_selector_all("iframe")
            for iframe in iframes:
                src = iframe.get_attribute("src") or ""
                if ".pdf" in src.lower() or "relatorio" in src.lower() or "bopm" in src.lower():
                    full_url = src if src.startswith("http") else urljoin(page.url, src)
                    self.log.debug(f"[{bopm_id}] Iframe PDF URL: {full_url}")
                    filepath = self._download_url(full_url, bopm_id, page)
                    if filepath:
                        return filepath

            return None

        except Exception as exc:
            self.log.debug(f"[{bopm_id}] Estratégia 3 falhou: {exc}")
            return None

    # ------------------------------------------------------------------
    # Utilitário: baixar URL com cookies da sessão Playwright
    # ------------------------------------------------------------------

    def _download_url(self, url: str, bopm_id: str, page: Page) -> Optional[str]:
        """Baixa um PDF por URL reutilizando os cookies do contexto Playwright."""
        if not url or url.startswith("about:"):
            return None
        try:
            cookies = {c["name"]: c["value"] for c in self.ctx.cookies()}
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
                "Referer": page.url,
            }

            session = requests.Session()
            response = session.get(
                url, cookies=cookies, headers=headers, timeout=30, stream=True
            )
            response.raise_for_status()

            # Determina nome do arquivo
            filename = self._extract_filename(response, url, bopm_id)
            dest = os.path.join(config.DOWNLOADS_DIR, filename)

            with open(dest, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            size_kb = os.path.getsize(dest) / 1024
            self.log.info(f"[{bopm_id}] PDF salvo: {dest} ({size_kb:.1f} KB)")
            return dest

        except Exception as exc:
            self.log.debug(f"[{bopm_id}] _download_url falhou: {exc}")
            return None

    # ------------------------------------------------------------------
    # Utilitários
    # ------------------------------------------------------------------

    def _find_pdf_button(self, page_or_frame):
        """
        Localiza o botão 'Visualiza PDF' por vários seletores possíveis.
        Retorna o elemento ou None.
        """
        # Seletores ordenados do mais específico ao mais genérico.
        # NÃO incluir "a:has-text('Visualiza')" — bate em "Visualizar Impressão" da listagem.
        selectors = [
            "text=Visualizar PDF",
            "text=Visualiza PDF",
            "input[value='Visualizar PDF']",
            "input[value='Visualiza PDF']",
            "input[value*='Visualizar PDF']",
            "button:has-text('Visualizar PDF')",
            "a:has-text('Visualizar PDF')",
            "a:has-text('Visualiza PDF')",
            "input[value*='PDF']",
            "button:has-text('PDF')",
            "a:has-text('PDF')",
            "[id*='pdf' i]",
            "[name*='pdf' i]",
            "input[type='submit'][value*='PDF' i]",
            "input[type='button'][value*='PDF' i]",
        ]
        for sel in selectors:
            try:
                el = page_or_frame.query_selector(sel)
                if el and el.is_visible():
                    self.log.debug(f"Botão PDF encontrado: {sel}")
                    return el
            except Exception:
                continue
        self.log.warning("Botão 'Visualiza PDF' não encontrado na página.")
        return None

    @staticmethod
    def _extract_filename(response: requests.Response, url: str, bopm_id: str) -> str:
        """
        Extrai o nome do arquivo do header Content-Disposition.
        Garante extensão .pdf e nome único por BOPM_ID + timestamp.
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        cd = response.headers.get("Content-Disposition", "")
        # RFC 5987 / RFC 6266
        match = re.search(r"filename\*=(?:UTF-8'')?(.+?)(?:;|$)", cd, re.IGNORECASE)
        if not match:
            match = re.search(r'filename=["\']?([^"\';\n]+)', cd, re.IGNORECASE)
        if match:
            name = requests.utils.unquote(match.group(1).strip().strip('"\''))
            if name and name.lower().endswith(".pdf"):
                return f"BOPM_{bopm_id}_{name}"

        # Tenta extrair da URL — somente se for realmente um PDF
        parsed = urlparse(url)
        path_part = parsed.path.split("/")[-1]
        if path_part and path_part.lower().endswith(".pdf"):
            return f"BOPM_{bopm_id}_{path_part}"

        # Bug2 fix: bopm_id já contém OCR+data (ex: OCR_15502_26052026), timestamp removido
        return f"BOPM_{bopm_id}.pdf"
