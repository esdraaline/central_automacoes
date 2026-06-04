"""
gemini_submitter.py — Envia cada BOPM baixado para o Gem validador no Gemini.

Lança o Chrome real via subprocess com remote debugging, conecta via CDP,
navega para https://gemini.google.com/gem/5865dad897c5 em abas separadas,
anexa cada PDF e clica em Enviar. Todas as abas ficam abertas.
"""

import os
import socket
import subprocess
import time
from logging import Logger
from typing import List, Optional

from playwright.sync_api import sync_playwright, Browser


GEMINI_GEM_URL  = "https://gemini.google.com/gem/5865dad897c5"
CHROME_PATH     = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROME_ALT_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# IMPORTANTE: a partir do Chrome 136 a flag --remote-debugging-port é IGNORADA
# quando aponta para o perfil padrão do Chrome (User Data). Por isso usamos um
# diretório dedicado, não-padrão. Para não precisar logar de novo, na 1ª execução
# o script CLONA o seu perfil padrão (já logado) para este diretório dedicado.
CHROME_DEFAULT_USER_DATA = r"C:\Users\pc\AppData\Local\Google\Chrome\User Data"
CHROME_USER_DATA = r"C:\Users\pc\AppData\Local\Google\Chrome\BOPM_Automation"
CDP_PORT        = 9222


class GeminiSubmitter:
    """Abre Chrome real via CDP e envia os PDFs para o Gem do Gemini."""

    def __init__(self, logger: Logger) -> None:
        self.log = logger
        self._chrome_proc: Optional[subprocess.Popen] = None

    def submit_pdfs(self, pdf_paths: List[str], playwright=None) -> None:
        if not pdf_paths:
            self.log.info("Nenhum PDF para enviar ao Gemini.")
            return

        self.log.info(f"Preparando envio de {len(pdf_paths)} PDF(s) ao Gemini...")
        self.log.info("Encerrando instâncias do Chrome automaticamente...")

        chrome_exe = self._find_chrome()
        if not chrome_exe:
            self.log.error("Chrome não encontrado. Verifique a instalação.")
            return

        # Encerra qualquer instância de Chrome em background
        self._kill_chrome()

        # Garante o perfil dedicado já logado (clona do perfil padrão na 1ª vez)
        self._ensure_profile()

        # Lança Chrome com remote debugging
        self.log.info(f"Abrindo Chrome com remote debugging na porta {CDP_PORT}...")
        self._chrome_proc = subprocess.Popen([
            chrome_exe,
            f"--remote-debugging-port={CDP_PORT}",
            f"--user-data-dir={CHROME_USER_DATA}",
            "--profile-directory=Default",
            "--start-maximized",
            "--no-first-run",
            "--no-default-browser-check",
        ])
        time.sleep(8)  # Aguarda Chrome inicializar

        # Verifica se a porta está respondendo
        if not self._wait_for_cdp(timeout=20):
            self.log.error(f"Chrome não respondeu na porta {CDP_PORT}. Abortando.")
            return

        # Reaproveita a instância do Playwright já existente (ex.: a do Edge), se
        # fornecida, para NÃO abrir uma segunda instância síncrona simultânea —
        # duas instâncias ao mesmo tempo conflitam. Se nada for passado, cria a sua.
        own_pw = playwright is None
        _pw_cm = sync_playwright() if own_pw else None
        p = _pw_cm.__enter__() if own_pw else playwright
        try:
            try:
                browser = p.chromium.connect_over_cdp(f"http://localhost:{CDP_PORT}")
                self.log.info("Conectado ao Chrome via CDP.")
            except Exception as exc:
                self.log.error(f"Falha ao conectar via CDP: {exc}")
                return

            # Usa o contexto existente (já tem cookies/login do Google)
            if browser.contexts:
                context = browser.contexts[0]
            else:
                context = browser.new_context()

            # Testa acesso ao Gemini
            self.log.info("Verificando acesso ao Gemini...")
            test_page = context.new_page()
            try:
                test_page.goto(GEMINI_GEM_URL, wait_until="domcontentloaded", timeout=30_000)
                time.sleep(4)
                current_url = test_page.url
                self.log.info(f"URL após navegação de teste: {current_url}")
                if "accounts.google.com" in current_url or "signin" in current_url.lower():
                    # Leva direto à tela de login do Google
                    try:
                        test_page.goto("https://accounts.google.com/",
                                       wait_until="domcontentloaded", timeout=30_000)
                    except Exception:
                        pass
                    self.log.warning("=" * 70)
                    self.log.warning("LOGIN NECESSÁRIO (apenas nesta primeira vez)")
                    self.log.warning(
                        "Na janela do Chrome que abriu, faça login na sua conta Google "
                        "(josemardp@gmail.com). O login fica SALVO neste perfil e NÃO "
                        "será pedido novamente nas próximas execuções."
                    )
                    self.log.warning("Depois de logar, volte aqui e pressione Enter...")
                    self.log.warning("=" * 70)
                    try:
                        input()
                    except Exception:
                        pass
                    # Reabre o Gem após o login manual
                    test_page.goto(GEMINI_GEM_URL, wait_until="domcontentloaded", timeout=30_000)
                    time.sleep(4)
                    current_url = test_page.url
                    if "accounts.google.com" in current_url or "signin" in current_url.lower():
                        self.log.error("Login não concluído. Abortando.")
                        test_page.close()
                        return
                self.log.info("Gemini acessível. Iniciando envio dos PDFs...")
            except Exception as exc:
                self.log.error(f"Falha ao acessar Gemini: {exc}")
                test_page.close()
                return
            test_page.close()

            # Envia cada PDF em aba separada
            submitted = 0
            for i, pdf_path in enumerate(pdf_paths, 1):
                if not os.path.isfile(pdf_path):
                    self.log.warning(f"PDF não encontrado, pulando: {pdf_path}")
                    continue

                self.log.info(f"[{i}/{len(pdf_paths)}] Enviando: {os.path.basename(pdf_path)}")
                page = context.new_page()

                try:
                    page.goto(GEMINI_GEM_URL, wait_until="domcontentloaded", timeout=30_000)
                    time.sleep(5)

                    attached = self._attach_file(page, pdf_path)
                    if not attached:
                        self.log.warning(f"[{i}] Anexo falhou.")
                        continue

                    time.sleep(3)

                    sent = self._click_send(page)
                    if sent:
                        self.log.info(f"[{i}] Enviado: {os.path.basename(pdf_path)}")
                        submitted += 1
                    else:
                        self.log.warning(f"[{i}] Botão Enviar não encontrado.")

                    time.sleep(3)

                except Exception as exc:
                    self.log.error(f"[{i}] Erro: {exc}")

            self.log.info(f"\n{submitted}/{len(pdf_paths)} BOPMs enviados ao Gemini.")
            self.log.info("Concluído. Abas do Gemini deixadas abertas para revisão.")
        finally:
            # Só encerra o Playwright se foi criado aqui; se reaproveitado (Edge),
            # deixa vivo para o chamador encerrar.
            if own_pw and _pw_cm is not None:
                try:
                    _pw_cm.__exit__(None, None, None)
                except Exception:
                    pass

        # Mantém o Chrome aberto com as abas do Gemini para revisão.
        # (não encerramos self._chrome_proc de propósito)

    # ------------------------------------------------------------------

    def _kill_chrome(self) -> None:
        """Encerra todos os processos chrome.exe e aguarda até que não reste nenhum."""
        # Mata via taskkill (inclui processos filhos)
        subprocess.run(
            ["taskkill", "/F", "/IM", "chrome.exe", "/T"],
            capture_output=True, text=True
        )

        # Espera até que nenhum chrome.exe apareça no tasklist
        deadline = time.time() + 20
        while time.time() < deadline:
            result = subprocess.run(
                ["tasklist", "/FI", "IMAGENAME eq chrome.exe", "/NH"],
                capture_output=True, text=True
            )
            if "chrome.exe" not in result.stdout.lower():
                self.log.info("Todos os processos Chrome encerrados.")
                break
            self.log.debug("Aguardando Chrome encerrar completamente...")
            # Segunda força-bruta caso ainda haja processos
            subprocess.run(
                ["taskkill", "/F", "/IM", "chrome.exe", "/T"],
                capture_output=True, text=True
            )
            time.sleep(1)

        # Remove lockfiles do perfil
        for lf in [
            os.path.join(CHROME_USER_DATA, "lockfile"),
            os.path.join(CHROME_USER_DATA, "SingletonLock"),
            os.path.join(CHROME_USER_DATA, "SingletonSocket"),
            os.path.join(CHROME_USER_DATA, "Default", "lockfile"),
        ]:
            try:
                if os.path.exists(lf):
                    os.remove(lf)
                    self.log.debug(f"Lockfile removido: {lf}")
            except Exception:
                pass

        time.sleep(2)

    def _ensure_profile(self) -> None:
        """
        Garante que o perfil dedicado exista já com o login do Google.

        Na 1ª execução o diretório dedicado não existe: clonamos o perfil padrão
        do Chrome (que já está logado) usando robocopy, pulando caches pesados
        para ser rápido. Assim o Chrome dedicado abre já logado, sem aba "limpa".
        Nas próximas execuções o perfil já existe e nada é copiado.
        """
        cookies_marker = os.path.join(CHROME_USER_DATA, "Default", "Network", "Cookies")
        if os.path.exists(cookies_marker):
            self.log.debug("Perfil dedicado já existe; pulando clonagem.")
            return

        if not os.path.isdir(CHROME_DEFAULT_USER_DATA):
            self.log.warning(
                "Perfil padrão do Chrome não encontrado para clonar. "
                "Será necessário logar manualmente no perfil dedicado."
            )
            return

        self.log.info("Primeira execução: clonando seu perfil logado do Chrome...")
        os.makedirs(CHROME_USER_DATA, exist_ok=True)

        # Diretórios de cache/temporários que não precisam ser copiados (ganho de tempo)
        excl_dirs = [
            "Cache", "Code Cache", "GPUCache", "ShaderCache", "GraphiteDawnCache",
            "Service Worker", "Crashpad", "Crash Reports", "Greaselion",
            "component_crx_cache", "extensions_crx_cache", "DawnGraphiteCache",
            "DawnWebGPUCache", "optimization_guide_model_store",
        ]
        try:
            cmd = ["robocopy", CHROME_DEFAULT_USER_DATA, CHROME_USER_DATA,
                   "/E", "/XJ", "/R:1", "/W:1", "/NFL", "/NDL", "/NJH", "/NJS", "/NP",
                   "/XD"] + excl_dirs
            # robocopy retorna 0-7 em sucesso (>=8 é erro)
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode >= 8:
                self.log.warning(f"robocopy retornou {res.returncode}; tentando xcopy...")
                subprocess.run(
                    ["xcopy", CHROME_DEFAULT_USER_DATA, CHROME_USER_DATA,
                     "/E", "/I", "/H", "/Y", "/Q"],
                    capture_output=True, text=True,
                )
            self.log.info("Perfil clonado. O Chrome dedicado deve abrir já logado.")
        except Exception as exc:
            self.log.warning(
                f"Falha ao clonar perfil ({exc}). "
                "Será necessário logar manualmente no perfil dedicado."
            )

    def _find_chrome(self) -> Optional[str]:
        for path in [CHROME_PATH, CHROME_ALT_PATH]:
            if os.path.isfile(path):
                return path
        self.log.error(f"Chrome não encontrado em {CHROME_PATH}")
        return None

    def _wait_for_cdp(self, timeout: int = 15) -> bool:
        """Aguarda a porta CDP ficar disponível."""
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                s = socket.create_connection(("localhost", CDP_PORT), timeout=1)
                s.close()
                return True
            except OSError:
                time.sleep(1)
        return False

    # Termos que NUNCA devem ser clicados (evita acertar o microfone, etc.)
    _BLOCK_TERMS = ("microfone", "microphone", "voz", "voice", "fala", "speech")

    # --- Filtros JS (executados na página, atravessam shadow DOM) ------------

    # Botão '+' que abre o menu de upload.
    # No Gemini pt-BR esse botão tem aria-label = "Envio e ferramentas".
    # Cuidado: NÃO usar termos genéricos como "mais"/"more", pois casam com os
    # botões "Mais opções de ..." da barra lateral.
    _FILTER_PLUS = r"""
    (n) => {
      const role = n.getAttribute && n.getAttribute('role');
      if (!(n.tagName === 'BUTTON' || role === 'button')) return false;
      const r = n.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return false;
      const al = (n.getAttribute('aria-label')||'').toLowerCase();
      if (al.startsWith('mais opções')) return false;
      if (/microfone|microphone|voz|voice|enviar mensagem/.test(al)) return false;
      return al.includes('envio e ferramentas')
             || al.includes('fazer upload')
             || al.includes('upload')
             || al.includes('anexar')
             || (al.includes('adicionar') && al.includes('arquivo'));
    }
    """

    # Item de menu 'Enviar arquivos' (evita 'Adicionar do Drive')
    _FILTER_UPLOAD_ITEM = r"""
    (n) => {
      if (!/^(BUTTON|A|LI|DIV|SPAN)$/.test(n.tagName) && !/^MAT-/.test(n.tagName)) return false;
      const t = (n.innerText||'').trim().toLowerCase();
      if (!t || t.length > 28) return false;
      if (t.includes('drive')) return false;
      return t.startsWith('enviar arquivo') || t.startsWith('fazer upload') ||
             t.startsWith('upload de arquivo') || t.startsWith('upload files') ||
             t.startsWith('add files') || t.startsWith('carregar arquivo');
    }
    """

    # Botão de enviar a mensagem (flecha), habilitado
    _FILTER_SEND = r"""
    (n) => {
      const role = n.getAttribute && n.getAttribute('role');
      if (!(n.tagName === 'BUTTON' || role === 'button')) return false;
      const r = n.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return false;
      if (n.disabled || n.getAttribute('aria-disabled') === 'true') return false;
      const s = ((n.getAttribute('aria-label')||'') + ' ' +
                 (n.getAttribute('title')||'') + ' ' +
                 (n.getAttribute('mattooltip')||'')).toLowerCase();
      if (/microfone|microphone|voz|voice/.test(s)) return false;
      return /enviar|send|submit/.test(s);
    }
    """

    def _deep_query(self, page, filter_src):
        """Procura no DOM (incl. shadow DOM) o 1º elemento que casa com o filtro.
        Guarda a referência em window.__bopmTarget e devolve um resumo."""
        js = r"""(filterSrc) => {
          const filter = eval('(' + filterSrc + ')');
          const all = [];
          const walk = (root) => {
            let nodes;
            try { nodes = root.querySelectorAll('*'); } catch (e) { return; }
            for (const n of nodes) { all.push(n); if (n.shadowRoot) walk(n.shadowRoot); }
          };
          walk(document);
          let t = null;
          for (const n of all) { try { if (filter(n)) { t = n; break; } } catch (e) {} }
          window.__bopmTarget = t;
          if (!t) return null;
          return { al: t.getAttribute('aria-label'), tx: (t.innerText||'').trim().slice(0,40), tag: t.tagName };
        }"""
        try:
            return page.evaluate(js, filter_src)
        except Exception as exc:
            self.log.debug(f"_deep_query erro: {exc}")
            return None

    def _deep_click(self, page) -> bool:
        """Clica no elemento guardado em window.__bopmTarget (ou no ancestral clicável)."""
        js = r"""() => {
          const el = window.__bopmTarget;
          if (!el) return false;
          const a = el.closest('button,[role=menuitem],[role=option],a,li') || el;
          try { a.scrollIntoView({block:'center'}); } catch (e) {}
          a.click();
          return true;
        }"""
        try:
            return bool(page.evaluate(js))
        except Exception as exc:
            self.log.debug(f"_deep_click erro: {exc}")
            return False

    def _dump_buttons(self, page, context: str = "") -> None:
        """Lista no log (DEBUG) todos os botões visíveis — para diagnosticar seletores."""
        js = r"""() => {
          const out = [];
          const walk = (root) => {
            for (const n of root.querySelectorAll('button,[role=button],[role=menuitem]')) {
              const r = n.getBoundingClientRect();
              if (r.width === 0 || r.height === 0) continue;
              const al = n.getAttribute('aria-label') || '';
              if (al.toLowerCase().startsWith('mais opções')) continue;  // ruído da barra lateral
              out.push({
                al: al,
                ti: n.getAttribute('title'),
                tt: n.getAttribute('mattooltip'),
                tx: (n.innerText||'').trim().slice(0,25)
              });
            }
            for (const e of root.querySelectorAll('*')) { if (e.shadowRoot) walk(e.shadowRoot); }
          };
          walk(document);
          return out;
        }"""
        try:
            items = page.evaluate(js)
            self.log.debug(f"[DOM {context}] {len(items)} botões visíveis:")
            for it in items:
                self.log.debug(
                    f"   btn al={it.get('al')!r} ti={it.get('ti')!r} "
                    f"tt={it.get('tt')!r} tx={it.get('tx')!r}"
                )
        except Exception as exc:
            self.log.debug(f"_dump_buttons erro: {exc}")

    def _attach_file(self, page, pdf_path: str) -> bool:
        """
        Anexa o PDF seguindo o fluxo real do Gemini:
        '+'  ->  'Enviar arquivos'  ->  seleciona o PDF.
        Usa busca profunda no DOM (atravessa shadow DOM) e registra diagnóstico.
        """
        self._dump_buttons(page, "antes do '+'")

        # 1) Abrir o menu '+'
        plus = self._deep_query(page, self._FILTER_PLUS)
        if plus:
            self.log.debug(f"Botão '+' encontrado: {plus}")
            self._deep_click(page)
            time.sleep(1.5)  # aguarda o menu abrir
            self._dump_buttons(page, "menu aberto")
        else:
            self.log.debug("Botão '+' NÃO encontrado no DOM.")

        # 2) input[type=file] (pode ter surgido após abrir o menu)
        try:
            page.wait_for_selector('input[type="file"]', state="attached", timeout=3_000)
        except Exception:
            pass
        try:
            for fi in page.query_selector_all('input[type="file"]'):
                try:
                    fi.set_input_files(pdf_path)
                    self.log.debug("Arquivo anexado via input[type=file].")
                    if self._wait_for_attachment(page):
                        return True
                except Exception:
                    continue
        except Exception:
            pass

        # 3) Clicar em 'Enviar arquivos' capturando o seletor de arquivos
        item = self._deep_query(page, self._FILTER_UPLOAD_ITEM)
        if item:
            self.log.debug(f"Item de menu de upload: {item}")
            try:
                with page.expect_file_chooser(timeout=8_000) as fc_info:
                    self._deep_click(page)
                fc_info.value.set_files(pdf_path)
                self.log.debug("Arquivo anexado via 'Enviar arquivos'.")
                if self._wait_for_attachment(page):
                    return True
            except Exception as exc:
                self.log.debug(f"Falha no file chooser: {exc}")
        else:
            self.log.debug("Item 'Enviar arquivos' NÃO encontrado no menu.")

        self.log.debug("Todas as estratégias de anexo falharam.")
        return False

    def _wait_for_attachment(self, page, timeout: int = 25) -> bool:
        """Aguarda o PDF terminar de subir (chip do arquivo aparece)."""
        chip_selectors = (
            '[data-test-id*="file" i]',
            '[class*="attachment" i]',
            '[class*="file-preview" i]',
            '[class*="uploaded" i]',
        )
        deadline = time.time() + timeout
        while time.time() < deadline:
            for sel in chip_selectors:
                try:
                    el = page.query_selector(sel)
                    if el and el.is_visible():
                        self.log.debug("Anexo confirmado (chip do arquivo visível).")
                        return True
                except Exception:
                    continue
            time.sleep(1)
        # Mesmo sem detectar o chip, segue (o envio valida o estado do botão)
        self.log.debug("Chip não detectado; prosseguindo mesmo assim.")
        return True

    def _click_send(self, page) -> bool:
        """Clica na flecha de Enviar, esperando o botão ficar habilitado."""
        selectors = [
            'button[aria-label*="Enviar" i]',
            'button[aria-label*="Send" i]',
            'button[mattooltip*="Enviar" i]',
            'button[mattooltip*="Send" i]',
            'button[jsname="Qx7uuf"]',
            'button[data-test-id*="send" i]',
            'button.send-button',
        ]
        # Espera o upload concluir: o botão só habilita quando o PDF está pronto
        deadline = time.time() + 30
        while time.time() < deadline:
            for sel in selectors:
                try:
                    for btn in page.query_selector_all(sel):
                        lbl = (btn.get_attribute("aria-label") or "").lower()
                        if any(b in lbl for b in self._BLOCK_TERMS):
                            continue
                        if btn.is_visible() and btn.is_enabled():
                            btn.click()
                            self.log.debug(f"Enviar clicado: {sel}")
                            return True
                except Exception:
                    continue
            # Fallback por busca profunda (atravessa shadow DOM)
            send = self._deep_query(page, self._FILTER_SEND)
            if send:
                if self._deep_click(page):
                    self.log.debug(f"Enviar clicado (deep): {send}")
                    return True
            time.sleep(1)

        # Fallback: Enter no campo de texto
        try:
            el = page.query_selector('div[contenteditable="true"], rich-textarea')
            if el and el.is_visible():
                el.press("Enter")
                self.log.debug("Enviado via Enter no campo de texto.")
                return True
        except Exception:
            pass
        return False
