"""
siopm_navigator.py — Automação completa da navegação no SIOPM Web.

Módulo:
- SiopmNavigator : toda a lógica de negócio do SIOPM
    - login()
    - select_cad_and_category()
    - apply_bopm_filter()
    - get_pending_bopms()
    - open_bopm()
    - go_back_to_list()

BrowserManager foi movido para nucleo/browser.py na Fase 0 · Sprint 1.
"""

import os
import re
import time
from dataclasses import dataclass, field
from logging import Logger
from typing import Dict, List, Optional

from playwright.sync_api import (
    BrowserContext, Page, TimeoutError as PWTimeout,
)

import config
from pdf_handler import PDFHandler


# ─────────────────────────────────────────────────────────────────────────────
# Estrutura de dados para cada BOPM pendente
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class BopmEntry:
    row_index: int
    bopm_id: str = ""
    link_selector: str = ""
    extra_info: dict = field(default_factory=dict)


# ─────────────────────────────────────────────────────────────────────────────
# SiopmNavigator
# ─────────────────────────────────────────────────────────────────────────────

class SiopmNavigator:
    """
    Lógica de negócio para operar o SIOPM Web.
    Todos os métodos públicos registram ações no log e lançam exceções
    com mensagens descritivas em caso de falha.
    """

    def __init__(
        self,
        logger: Logger,
        vpn,
        context: BrowserContext,
        page: Page,
        siopm_creds: Optional[Dict[str, str]] = None,
    ) -> None:
        self.log = logger
        self.vpn = vpn
        self.ctx = context
        self.page = page
        self.pdf = PDFHandler(logger, context)
        self._bopm_list_url: Optional[str] = None
        creds = siopm_creds or {}
        self._siopm_user = creds.get("user", "")
        self._siopm_password = creds.get("password", "")

    # ------------------------------------------------------------------
    # 1. Login
    # ------------------------------------------------------------------

    def login(self) -> None:
        """Navega para o SIOPM e realiza login com as credenciais configuradas."""
        self.log.info(f"Acessando SIOPM: {config.SIOPM_URL}")
        self._navigate(config.SIOPM_URL)
        self._wait_for_stable_page()

        # Preenche usuário
        user_field = self._smart_find(
            ["#txtUsuario", "input[name*='usu' i]", "input[name*='user' i]",
             "input[id*='user' i]", "input[type='text']:first-of-type"]
        )
        self._fill(user_field, self._siopm_user, "campo usuário")

        # Preenche senha
        pass_field = self._smart_find(
            ["#txtSenha", "input[type='password']",
             "input[name*='senha' i]", "input[name*='pass' i]",
             "input[id*='senha' i]"]
        )
        self._fill(pass_field, self._siopm_password, "campo senha")

        # Clica em entrar
        login_btn = self._smart_find(
            ["input[type='submit']", "input[value*='Entra' i]",
             "button[type='submit']", "input[value*='Login' i]",
             "input[value*='OK' i]", "input[name*='btn' i]"]
        )
        self.log.info("Clicando em Entrar...")
        self._click(login_btn, "botão login")
        self._wait_for_stable_page(timeout=config.TIMEOUT_NAVIGATION)
        self.log.info("Login realizado.")

    # ------------------------------------------------------------------
    # 2. Selecionar CAD e Categoria
    # ------------------------------------------------------------------

    def select_cad_and_category(self) -> None:
        """Seleciona o CAD Araçatuba e a categoria Ocorrências."""
        self._select_cad()
        self._select_category()

    def _select_cad(self) -> None:
        """Escolhe o CAD 'Araçatuba' (dropdown, link ou radio button)."""
        self.log.info(f"Selecionando CAD: {config.SIOPM_CAD}")
        cad_name = config.SIOPM_CAD

        # Tenta como dropdown primeiro
        selects = self.page.query_selector_all("select")
        for sel in selects:
            try:
                options = sel.query_selector_all("option")
                for opt in options:
                    text = (opt.inner_text() or "").strip()
                    if cad_name.lower() in text.lower():
                        sel.select_option(label=text)
                        self.log.info(f"CAD selecionado no dropdown: '{text}'")
                        self._wait_for_stable_page(timeout=5000)
                        # Clica no botão de confirmação para navegar ao menu principal
                        self._click_if_exists(
                            [
                                "input[type='submit']",
                                "input[value*='OK' i]",
                                "input[value*='Entra' i]",
                                "input[value*='Confirma' i]",
                                "button[type='submit']",
                            ],
                            "botão confirmação CAD"
                        )
                        self._wait_for_stable_page()
                        return
            except Exception:
                continue

        # Tenta como link/texto
        try:
            link = self.page.get_by_text(cad_name, exact=False).first
            if link:
                link.click()
                self._wait_for_stable_page()
                self.log.info(f"CAD selecionado via link: {cad_name}")
                return
        except Exception:
            pass

        # Aceita qualquer botão de confirmação na tela do CAD
        self._click_if_exists(
            ["input[type='submit']", "input[value*='OK' i]", "input[value*='Entra' i]"],
            "botão confirmação CAD"
        )
        self.log.warning(f"CAD '{cad_name}' não localizado explicitamente; prosseguindo.")

    def _select_category(self) -> None:
        """Seleciona OCORRENCIAS no dropdown de Categoria e clica Confirmar."""
        self.log.info(f"Selecionando categoria: {config.BOPM_CATEGORY}")

        try:
            # Categoria é um <select> dropdown na página hsiopmcat.aspx
            selects = self.page.query_selector_all("select")
            selected = False
            for sel in selects:
                options = sel.query_selector_all("option")
                for opt in options:
                    text = (opt.inner_text() or "").strip()
                    if "OCORR" in text.upper():
                        sel.select_option(label=text)
                        self.log.info(f"Categoria selecionada no dropdown: '{text}'")
                        selected = True
                        break
                if selected:
                    break

            if not selected:
                raise RuntimeError("Opção OCORRENCIAS não encontrada nos dropdowns da página")

            # Clica no botão Confirmar para prosseguir
            self._click_if_exists(
                [
                    "input[value*='Confirmar' i]",
                    "input[value*='Confirm' i]",
                    "input[type='submit']",
                    "button:has-text('Confirmar')",
                ],
                "botão Confirmar categoria"
            )
            self._wait_for_stable_page()
            self.log.info("Categoria confirmada.")
        except Exception as exc:
            raise RuntimeError(f"Não foi possível selecionar a categoria: {exc}")

    # ------------------------------------------------------------------
    # 3. Aplicar filtro de BOPMs
    # ------------------------------------------------------------------

    def apply_bopm_filter(self) -> None:
        """
        Configura e executa o filtro de BOPMs pendentes de validação
        dos últimos N dias.
        """
        self.log.info("Aplicando filtro BOPM/TC - P/ Validação...")

        # Tipo de consulta
        self._select_option_containing(
            config.FILTER_TYPE,
            context_label="tipo de consulta"
        )
        time.sleep(0.5)

        # Por código da OPM
        self._select_option_containing(
            config.FILTER_BY,
            context_label="filtro por"
        )
        time.sleep(0.5)

        # Todos
        self._select_option_containing(
            config.FILTER_SELECTION,
            context_label="seleção"
        )
        time.sleep(0.5)

        # OPM Code
        self._fill_field_containing(
            ["opm", "cod", "codigo"],
            config.SIOPM_OPM_CODE,
            "código OPM"
        )
        time.sleep(0.5)

        # Período — últimos N dias
        self._set_date_range(config.FILTER_DAYS)

        # Clicar em Renovar
        self.log.info("Clicando em Renovar...")
        renovar = self._smart_find([
            f"input[value*='{config.RENOVAR_BTN_TEXT}' i]",
            f"button:has-text('{config.RENOVAR_BTN_TEXT}')",
            f"a:has-text('{config.RENOVAR_BTN_TEXT}')",
            "input[type='submit']",
        ])
        self._click(renovar, "botão Renovar")
        self._wait_for_stable_page(timeout=config.TIMEOUT_NAVIGATION)

        # Salva URL da listagem para retorno
        self._bopm_list_url = self.page.url
        self.log.info(f"Filtro aplicado. URL da listagem: {self._bopm_list_url}")

    # ------------------------------------------------------------------
    # 4. Detectar BOPMs pendentes (seta laranja)
    # ------------------------------------------------------------------

    def get_pending_bopms(self) -> List[BopmEntry]:
        """
        Detecta BOPMs com status "Não Formalizado" usando JavaScript diretamente
        no browser — contorna problemas de seletor CSS, encoding e frameset.
        """
        self.log.info("Detectando BOPMs pendentes (Não Formalizado)...")
        pending: List[BopmEntry] = []

        frames = self.page.frames or [self.page]
        self.log.debug(f"Frames disponíveis: {len(frames)}")

        for frame in frames:
            try:
                frame.wait_for_load_state("domcontentloaded", timeout=10_000)
            except Exception:
                pass

            try:
                row_count = len(frame.query_selector_all("table tr"))
                self.log.debug(f"  Frame '{frame.url}': {row_count} <tr> encontradas")
            except Exception as exc:
                self.log.debug(f"  Frame inacessível: {exc}")
                continue

            # JavaScript roda dentro do browser — vê o DOM real, sem problemas de encoding
            try:
                js_candidates = frame.evaluate(r"""
                    () => {
                        const results = [];
                        const rows = Array.from(document.querySelectorAll('table tr'));

                        rows.forEach((row, idx) => {
                            if (row.querySelector('th') || row.querySelector('select')) return;

                            const cells = Array.from(row.querySelectorAll('td'));
                            if (cells.length < 2) return;

                            const lastCell = cells[cells.length - 1];
                            const rowText = (row.innerText || '').trim();
                            if (!rowText) return;

                            // Normaliza: remove acentos, caixa baixa
                            const norm = rowText.normalize('NFD')
                                .replace(/[̀-ͯ]/g, '')
                                .toLowerCase();

                            const clickables = lastCell.querySelectorAll(
                                'a, input[type="image"], input[type="submit"], button'
                            );

                            const byText  = norm.includes('nao formalizado');
                            const byIcons = clickables.length >= 2;

                            if (!byText && !byIcons) return;

                            const ocrMatch  = rowText.match(/\b(\d{4,})\b/);
                            const dateMatch = rowText.match(/\d{2}\/\d{2}\/\d{2,4}/);

                            results.push({
                                idx:            idx,
                                byText:         byText,
                                byIcons:        byIcons,
                                clickableCount: clickables.length,
                                ocr:            ocrMatch  ? ocrMatch[1]  : '',
                                date:           dateMatch ? dateMatch[0] : '',
                                lastCellHTML:   lastCell.innerHTML.substring(0, 400),
                                rowText:        rowText.substring(0, 200),
                            });
                        });

                        return results;
                    }
                """)
            except Exception as exc:
                self.log.warning(f"  JavaScript evaluation falhou: {exc}")
                js_candidates = []

            for item in js_candidates:
                self.log.debug(
                    f"  Candidato linha {item['idx']}: byText={item['byText']}, "
                    f"byIcons={item['byIcons']}, clicáveis={item['clickableCount']}, "
                    f"OCR='{item['ocr']}', data='{item['date']}'"
                )
                self.log.debug(f"    HTML última célula: {item['lastCellHTML'][:300]}")

                # Rejeita linhas sem OCR numérico (rodapé, paginação, etc.)
                if not item['ocr']:
                    self.log.debug(f"  Linha {item['idx']} ignorada: sem OCR numérico")
                    continue

                ocr      = item['ocr']
                date_text = item['date']
                date_raw  = re.sub(r'[^\d]', '', date_text)
                if len(date_raw) == 6:          # DD/MM/YY → DDMMYYYY
                    date_raw = date_raw[:4] + "20" + date_raw[4:]

                entry = BopmEntry(row_index=item['idx'])
                entry.link_selector   = f"table tr:nth-child({item['idx'] + 1})"
                entry.extra_info['frame'] = frame
                entry.bopm_id = f"OCR_{ocr}_{date_raw}" if date_raw else f"OCR_{ocr}"

                self.log.info(f"  → BOPM pendente: Data={date_text} OCR={ocr}")
                pending.append(entry)

        # Screenshot de debug
        try:
            os.makedirs(config.LOG_DIR, exist_ok=True)
            suffix = "pendentes" if pending else "sem_resultados"
            shot = os.path.join(config.LOG_DIR, f"debug_{suffix}.png")
            self.page.screenshot(path=shot, full_page=True)
            self.log.info(f"Screenshot de debug: {shot}")
        except Exception:
            pass

        self.log.info(f"Total de BOPMs pendentes: {len(pending)}")
        return pending

    # ------------------------------------------------------------------
    # 5. Abrir BOPM
    # ------------------------------------------------------------------

    def open_bopm(self, entry: BopmEntry) -> bool:
        """
        Clica na seta ou lupa da linha — o SIOPM abre o BO num popup via window.open().
        Captura o popup e guarda em entry.extra_info['pdf_popup'] para download posterior.
        self.page permanece na listagem (não muda).
        """
        self.log.info(f"[{entry.bopm_id}] Abrindo BOPM (linha {entry.row_index})...")

        try:
            frame = entry.extra_info.get('frame', self.page)
            m = re.search(r'\d{4,}', entry.bopm_id)
            ocr_num = m.group(0) if m else ""

            # Re-localiza a linha pelo OCR no texto completo da linha.
            # Prefere linhas com >= 2 células diretas (linhas de dados, não wrappers colspan).
            rows = frame.query_selector_all("table tr")
            row = None
            row_fallback = None
            for r in rows:
                try:
                    if ocr_num and re.search(rf'\b{re.escape(ocr_num)}\b', r.inner_text() or ""):
                        if row_fallback is None:
                            row_fallback = r
                        r_cells = r.query_selector_all(":scope > td")
                        if len(r_cells) >= 2:
                            row = r
                            break
                except Exception:
                    continue
            if row is None:
                row = row_fallback
            if row is None:
                row = rows[entry.row_index] if entry.row_index < len(rows) else None
            if row is None:
                self.log.error(f"[{entry.bopm_id}] Linha não encontrada.")
                return False

            cells = row.query_selector_all(":scope > td")
            self.log.debug(f"[{entry.bopm_id}] {len(cells)} células diretas na linha")

            # Se linha tem apenas 1 td (colspan wrapper do GeneXus), drilla na tabela aninhada
            if len(cells) < 2:
                for nested_row in row.query_selector_all("table tr"):
                    try:
                        nc = nested_row.query_selector_all(":scope > td")
                        if len(nc) < 2:
                            continue
                        nc_icons = nc[-2].query_selector_all(
                            "a, input[type='image'], input[type='submit']"
                        )
                        if any(i.is_visible() for i in nc_icons):
                            row = nested_row
                            cells = nc
                            self.log.debug(
                                f"[{entry.bopm_id}] Linha aninhada com ícones: {len(cells)} células"
                            )
                            break
                    except Exception:
                        continue

            if len(cells) >= 2:
                # Procura de trás para frente (pula cells[-1] = hidden GeneXus) até achar ícone visível
                target = None
                for rev_idx, cell in enumerate(reversed(cells)):
                    if rev_idx == 0:
                        continue  # pula cells[-1] (hidden input GeneXus)
                    try:
                        icons = cell.query_selector_all(
                            "a, input[type='image'], input[type='submit'], img[onclick], span[onclick]"
                        )
                        visible = [i for i in icons if i.is_visible()]
                        if visible:
                            target = visible[0]
                            self.log.debug(
                                f"[{entry.bopm_id}] Ícone em cells[-{rev_idx + 1}] "
                                f"({len(visible)} visível(is))"
                            )
                            break
                    except Exception:
                        continue
                if target:
                    target.scroll_into_view_if_needed()
                    # GeneXus usa gxSubmit() — navega na mesma aba. NÃO usar expect_popup().
                    frame = entry.extra_info.get('frame', self.page)
                    url_antes = frame.url
                    target.click()
                    self._wait_for_stable_page(timeout=config.TIMEOUT_NAVIGATION)
                    # Loga TODOS os frames para identificar onde o BO carregou
                    all_frame_urls = [f.url for f in self.page.frames]
                    self.log.info(f"[{entry.bopm_id}] Frames após clique: {all_frame_urls}")
                    # Identifica o frame que recebeu hsiopdftco
                    bo_frame = next(
                        (f for f in self.page.frames if 'hsiopdftco' in f.url.lower()),
                        None
                    )
                    if bo_frame:
                        entry.extra_info['nav_frame'] = bo_frame
                        self.log.info(f"[{entry.bopm_id}] Frame do BO: {bo_frame.url}")
                    else:
                        # Fallback: usa o frame original ou a page
                        entry.extra_info['nav_frame'] = frame
                        self.log.warning(f"[{entry.bopm_id}] hsiopdftco não encontrado nos frames. Usando frame original: {frame.url}")
                    nav_frame = entry.extra_info.get('nav_frame', self.page)
                    self.log.info(f"[{entry.bopm_id}] Ocorrência aberta — frame: {nav_frame.url} | page: {self.page.url}")
                    return True
                else:
                    try:
                        self.log.info(
                            f"[{entry.bopm_id}] HTML da linha: {(row.inner_html() or '')[:600]}"
                        )
                    except Exception:
                        pass
                    self.log.error(f"[{entry.bopm_id}] Nenhum ícone clicável.")
                    return False
            else:
                try:
                    self.log.info(
                        f"[{entry.bopm_id}] HTML da linha: {(row.inner_html() or '')[:600]}"
                    )
                except Exception:
                    pass
                self.log.error(f"[{entry.bopm_id}] Nenhum ícone clicável (células insuficientes).")
                return False

        except Exception as exc:
            self.log.error(f"[{entry.bopm_id}] Falha ao abrir BOPM: {exc}")
            return False

    # ------------------------------------------------------------------
    # 6. Scroll + PDF
    # ------------------------------------------------------------------

    def scroll_to_bottom_and_get_pdf(self, entry: BopmEntry) -> Optional[str]:
        self.log.info(f"[{entry.bopm_id}] Baixando PDF do BO...")
        nav_frame = entry.extra_info.get('nav_frame', self.page)
        self.log.info(f"[{entry.bopm_id}] Frame do BO: {nav_frame.url}")
        try:
            nav_frame.wait_for_load_state("load", timeout=15_000)
        except Exception:
            pass
        try:
            nav_frame.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        except Exception:
            pass
        time.sleep(1)
        return self.pdf.save_bopm_pdf(self.page, entry.bopm_id, nav_frame=nav_frame)

    def _is_valid_pdf(self, filepath: str) -> bool:
        """Verifica se o arquivo é um PDF real (assinatura %PDF no início)."""
        try:
            with open(filepath, 'rb') as f:
                return f.read(4) == b'%PDF'
        except Exception:
            return False

    # ------------------------------------------------------------------
    # 7. Voltar para a listagem
    # ------------------------------------------------------------------

    def go_back_to_list(self) -> None:
        """Retorna à lista de BOPMs para processar a próxima ocorrência."""
        self.log.info("Voltando para a listagem de BOPMs...")
        try:
            back_btn = self.page.query_selector(
                "input[value*='Voltar' i], button:has-text('Voltar'), a:has-text('Voltar')"
            )
            if back_btn:
                back_btn.click()
                self._wait_for_stable_page()
                return
        except Exception:
            pass

        if self._bopm_list_url:
            self._navigate(self._bopm_list_url)
            self._wait_for_stable_page()
        else:
            self.page.go_back()
            self._wait_for_stable_page()

    # ══════════════════════════════════════════════════════════════════
    # Métodos privados — detecção da seta laranja
    # ══════════════════════════════════════════════════════════════════

    def _row_has_orange_indicator(self, row) -> bool:
        """
        Verifica se uma linha da tabela tem o indicador laranja de pendência.
        Usa 5 estratégias em cascata.
        """
        # Exclui linhas de formulário/filtro (contêm <select> ou inputs de filtro)
        try:
            if row.query_selector("select"):
                return False
        except Exception:
            pass

        # 1. Imagens com palavras-chave no src
        for img in row.query_selector_all("img"):
            src = (img.get_attribute("src") or "").lower()
            alt = (img.get_attribute("alt") or "").lower()
            title = (img.get_attribute("title") or "").lower()
            if any(kw in src for kw in config.ORANGE_IMG_KEYWORDS):
                return True
            if any(kw in alt for kw in config.ORANGE_ALT_TEXTS):
                return True
            if any(kw in title for kw in config.ORANGE_ALT_TEXTS):
                return True

        # 2. Classes CSS suspeitas em qualquer elemento filho
        all_elements = row.query_selector_all("*")
        for el in all_elements:
            cls = (el.get_attribute("class") or "").lower()
            if any(kw in cls for kw in config.ORANGE_CSS_CLASSES):
                return True

        # 3. Cor inline (style="color:orange" ou "background:orange")
        for el in all_elements:
            style = (el.get_attribute("style") or "").lower().replace(" ", "")
            for hex_val in config.ORANGE_HEX_VALUES:
                if hex_val in style:
                    return True
            if "orange" in style:
                return True

        # 4. Cor computada via JavaScript — usa row.evaluate() para funcionar em qualquer frame
        try:
            result = row.evaluate("""
                (row) => {
                    const els = row.querySelectorAll('*');
                    for (const el of els) {
                        const s = window.getComputedStyle(el);
                        const props = [s.color, s.backgroundColor, s.borderColor];
                        for (const p of props) {
                            if (!p) continue;
                            const rgb = p.match(/\\d+/g);
                            if (!rgb || rgb.length < 3) continue;
                            const [r, g, b] = rgb.map(Number);
                            if (r > 180 && g > 80 && g < 200 && b < 80) return true;
                        }
                    }
                    return false;
                }
            """)
            if result:
                return True
        except Exception:
            pass

        # 5. Texto da linha indica pendência — inclui "Não Formalizado" (status real do SIOPM)
        try:
            row_text = (row.inner_text() or "").lower()
            keywords = ["pendente", "aguardando", "p/ valid",
                        "não formalizado", "nao formalizado", "não formalizado"]
            if any(kw in row_text for kw in keywords):
                return True
        except Exception:
            pass

        # 6. Dois ícones clicáveis na última célula = "Não Formalizado" (seta + lupa)
        try:
            cells = row.query_selector_all("td")
            if cells:
                last_td = cells[-1]
                icons = last_td.query_selector_all(
                    "a, input[type='image'], input[type='submit'], img[onclick], span[onclick]"
                )
                if len(icons) >= 2:
                    return True
        except Exception:
            pass

        return False

    def _find_orange_element_in_row(self, row):
        """
        Retorna o elemento clicável de validação dentro da linha.

        No SIOPM, linhas "Não Formalizado" têm dois ícones na última célula:
        1º = seta para cima (abre o BO para validar) ← queremos este
        2º = lupa (apenas visualizar)
        """
        # Estratégia principal: coluna Status (última célula)
        # Formalizado   → 1 ícone (círculo)
        # Não Formalizado → 2 ícones: [0]=círculo  [1]=seta p/ cima (abre o BO)
        try:
            cells = row.query_selector_all("td")
            if cells:
                last_td = cells[-1]
                icons = last_td.query_selector_all("a, input[type='image'], input[type='submit']")
                if len(icons) >= 2:
                    # Seta para cima = segundo ícone = abre o BO para validar
                    target = icons[1]
                elif len(icons) == 1:
                    target = icons[0]
                else:
                    target = None

                if target:
                    parent = target.evaluate_handle(
                        "el => el.closest('a') || el.closest('input') || el"
                    )
                    return parent
        except Exception:
            pass

        # Fallback: imagem cujo src/alt bate com palavras-chave de pendência
        for img in row.query_selector_all("img"):
            src = (img.get_attribute("src") or "").lower()
            alt = (img.get_attribute("alt") or "").lower()
            if any(kw in src for kw in config.ORANGE_IMG_KEYWORDS):
                parent = img.evaluate_handle("el => el.closest('a') || el.closest('input') || el")
                return parent
            if any(kw in alt for kw in config.ORANGE_ALT_TEXTS):
                parent = img.evaluate_handle("el => el.closest('a') || el.closest('input') || el")
                return parent

        # Fallback: links/botões com classes de pendência
        for el in row.query_selector_all("a, input[type='image'], input[type='submit'], button"):
            cls = (el.get_attribute("class") or "").lower()
            if any(kw in cls for kw in config.ORANGE_CSS_CLASSES):
                return el

        return None

    # ══════════════════════════════════════════════════════════════════
    # Métodos privados — extração de informações
    # ══════════════════════════════════════════════════════════════════

    def _extract_bopm_id(self, row, fallback_index: int) -> str:
        """Extrai o número/ID do BOPM da linha da tabela."""
        try:
            text = row.inner_text()
            # Procura padrão de BOPM: sequência de dígitos
            match = re.search(r'\b(\d{4,})\b', text)
            if match:
                return match.group(1)
        except Exception:
            pass
        return f"idx_{fallback_index}"

    def _build_row_selector(self, row, index: int) -> str:
        """Constrói um seletor CSS para referenciar a linha após recarregamento."""
        try:
            row_id = row.get_attribute("id")
            if row_id:
                return f"#{row_id}"
        except Exception:
            pass
        return f"table tr:nth-child({index + 1})"

    # ══════════════════════════════════════════════════════════════════
    # Métodos privados — interação com formulário
    # ══════════════════════════════════════════════════════════════════

    def _select_option_containing(self, text: str, context_label: str = "") -> None:
        """Seleciona opção em qualquer <select> da página que contenha 'text'."""
        selects = self.page.query_selector_all("select")
        for sel in selects:
            try:
                options = sel.query_selector_all("option")
                for opt in options:
                    opt_text = (opt.inner_text() or "").strip()
                    if text.lower() in opt_text.lower():
                        sel.select_option(label=opt_text)
                        self.log.debug(f"[{context_label}] Selecionado: '{opt_text}'")
                        return
            except Exception:
                continue
        self.log.warning(f"[{context_label}] Opção '{text}' não encontrada nos dropdowns.")

    def _fill_field_containing(self, keywords: list, value: str, label: str) -> None:
        """Preenche um input cujo id/name contenha um dos keywords."""
        inputs = self.page.query_selector_all("input[type='text'], input:not([type])")
        for inp in inputs:
            name = (inp.get_attribute("name") or "").lower()
            id_ = (inp.get_attribute("id") or "").lower()
            combined = name + " " + id_
            if any(kw in combined for kw in keywords):
                self._fill(inp, value, label)
                return
        self.log.warning(f"Campo '{label}' não encontrado com keywords {keywords}.")

    def _set_date_range(self, days: int) -> None:
        """Preenche os campos de data para os últimos N dias."""
        from datetime import date, timedelta
        today = date.today()
        start = today - timedelta(days=days)

        fmt = "%d/%m/%Y"
        start_str = start.strftime(fmt)
        end_str = today.strftime(fmt)

        self.log.info(f"Período: {start_str} até {end_str}")

        date_inputs = self.page.query_selector_all(
            "input[id*='data' i], input[name*='data' i], "
            "input[id*='date' i], input[name*='date' i], "
            "input[id*='dt' i], input[name*='dt' i]"
        )

        date_fields = [d for d in date_inputs if d.is_visible()]
        if len(date_fields) >= 2:
            self._fill(date_fields[0], start_str, "data início")
            self._fill(date_fields[1], end_str, "data fim")
        elif len(date_fields) == 1:
            self._fill(date_fields[0], start_str, "data início")
        else:
            self.log.warning("Campos de data não encontrados — verifique o filtro manualmente.")

    # ══════════════════════════════════════════════════════════════════
    # Métodos privados — helpers de Playwright
    # ══════════════════════════════════════════════════════════════════

    def _navigate(self, url: str) -> None:
        """Navega para URL com retry único em caso de timeout."""
        try:
            self.page.goto(url, wait_until="domcontentloaded",
                           timeout=config.TIMEOUT_NAVIGATION)
        except PWTimeout:
            self.log.warning(f"Timeout na navegação para {url}. Tentando novamente...")
            time.sleep(3)
            self.page.goto(url, wait_until="domcontentloaded",
                           timeout=config.TIMEOUT_NAVIGATION)

    def _wait_for_stable_page(self, timeout: int = None) -> None:
        """Espera a página estabilizar (networkidle ou load event)."""
        t = timeout or config.TIMEOUT_PAGE_LOAD
        try:
            self.page.wait_for_load_state("networkidle", timeout=t)
        except PWTimeout:
            try:
                self.page.wait_for_load_state("load", timeout=t // 2)
            except PWTimeout:
                self.log.debug("Timeout em wait_for_load_state — continuando mesmo assim.")

    def _smart_find(self, selectors: list):
        """
        Tenta múltiplos seletores em sequência e retorna o primeiro visível.
        Levanta RuntimeError se nenhum for encontrado.
        """
        for sel in selectors:
            try:
                el = self.page.query_selector(sel)
                if el and el.is_visible():
                    return el
            except Exception:
                continue
        raise RuntimeError(
            f"Nenhum dos seletores foi encontrado na página: {selectors}\n"
            f"URL atual: {self.page.url}"
        )

    def _fill(self, element, value: str, label: str) -> None:
        """Limpa e preenche um campo de forma segura."""
        try:
            element.scroll_into_view_if_needed()
            element.click(click_count=3)
            element.fill(value)
            self.log.debug(f"Campo '{label}' preenchido com '{value}'")
        except Exception as exc:
            raise RuntimeError(f"Falha ao preencher campo '{label}': {exc}")

    def _click(self, element, label: str) -> None:
        """Clica em um elemento de forma segura."""
        try:
            element.scroll_into_view_if_needed()
            element.click()
            self.log.debug(f"Clique em '{label}'")
        except Exception as exc:
            raise RuntimeError(f"Falha ao clicar em '{label}': {exc}")

    def _click_if_exists(self, selectors: list, label: str) -> None:
        """Clica no elemento se existir; ignora silenciosamente se não encontrado."""
        for sel in selectors:
            try:
                el = self.page.query_selector(sel)
                if el and el.is_visible():
                    el.click()
                    self.log.debug(f"Clique opcional em '{label}': {sel}")
                    return
            except Exception:
                continue
