"""
main.py — Ponto de entrada da Automação BOPM/SIOPM PMESP.

Uso:
    python main.py                  # modo supervisionado padrão
    python main.py --days 4         # filtrar últimos N dias
    python main.py --no-vpn         # pular etapa VPN (já conectado)
    python main.py --log-level DEBUG

Fluxo completo:
    1. Verificar/Conectar VPN
    2. Lançar Edge
    3. Login no SIOPM
    4. Selecionar CAD + Categoria Ocorrências
    5. Aplicar filtro BOPM/TC P/ Validação (últimos 4 dias)
    6. Detectar pendentes (seta laranja)
    7. Para cada pendente:
       a. Abrir ocorrência
       b. Rolar até o fim
       c. Clicar em Visualiza PDF
       d. Salvar PDF na pasta Downloads
       e. Voltar para lista
    8. Gerar relatório final
"""

import argparse
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import List

# Adiciona a raiz do projeto ao sys.path para que 'nucleo' seja importável
_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from nucleo.segredos import Segredos
from nucleo.log import setup_logger
from nucleo.vpn import VPNManager
from nucleo.browser import BrowserManager

import config
from siopm_navigator import SiopmNavigator, BopmEntry
from gemini_submitter import GeminiSubmitter


# ─────────────────────────────────────────────────────────────────────────────
# Executor principal
# ─────────────────────────────────────────────────────────────────────────────

class BopMAutomation:
    """Orquestra todas as etapas da automação."""

    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args

        segredos = Segredos()
        self.log = setup_logger(name="bopm", level=args.log_level)
        self.vpn = VPNManager(
            logger=self.log,
            creds=segredos.get("vpn"),
            server=config.VPN_SERVER,
            group=config.VPN_GROUP,
            intranet_host=config.INTRANET_PING_HOST,
            cli_paths=config.VPN_CLI_PATHS,
            profile_paths=config.VPN_PROFILE_PATHS,
            connect_timeout=config.VPN_CONNECT_TIMEOUT,
            check_retries=config.VPN_CHECK_RETRIES,
        )
        self.browser_mgr = BrowserManager(self.log)
        self._siopm_creds = segredos.get("siopm")

        # Contadores para relatório final
        self._total_found = 0
        self._total_saved = 0
        self._total_failed = 0
        self._failed_ids: List[str] = []
        self._saved_paths: List[str] = []

    def run(self) -> int:
        """
        Executa a automação completa.
        Retorna 0 em sucesso, 1 em erro parcial, 2 em erro crítico.
        """
        start_time = datetime.now()
        context = None
        page = None

        try:
            # ── Etapa 1: VPN ────────────────────────────────────────────
            if not self.args.no_vpn:
                self._step("ETAPA 1", "Conectar VPN Cisco Secure Client")
                if not self.vpn.connect():
                    self.log.critical("Falha ao conectar VPN. Automação interrompida.")
                    return 2
            else:
                self.log.info("ETAPA 1 — VPN ignorada por --no-vpn.")

            # ── Etapa 2: Browser ─────────────────────────────────────────
            self._step("ETAPA 2", "Iniciar Microsoft Edge")
            context, page = self.browser_mgr.launch(
                headless=config.HEADLESS,
                timeout_element=config.TIMEOUT_ELEMENT,
                timeout_navigation=config.TIMEOUT_NAVIGATION,
            )
            nav = SiopmNavigator(
                self.log, self.vpn, context, page,
                siopm_creds=self._siopm_creds,
            )

            # ── Etapa 3: Login ───────────────────────────────────────────
            self._step("ETAPA 3", "Login no SIOPM Web")
            self._with_retry(nav.login, "Login SIOPM")

            # ── Etapa 4: CAD + Categoria ──────────────────────────────────
            self._step("ETAPA 4", f"Selecionar CAD '{config.SIOPM_CAD}' e Ocorrências")
            self._with_retry(nav.select_cad_and_category, "Seleção CAD/Categoria")

            # ── Etapa 5: Filtro ───────────────────────────────────────────
            days = self.args.days or config.FILTER_DAYS
            config.FILTER_DAYS = days
            self._step("ETAPA 5", f"Aplicar filtro BOPM — últimos {days} dias")
            self._with_retry(nav.apply_bopm_filter, "Filtro BOPM")

            # ── Etapa 6: Detectar pendentes ───────────────────────────────
            self._step("ETAPA 6", "Detectar BOPMs pendentes (seta laranja)")
            pending: List[BopmEntry] = nav.get_pending_bopms()
            self._total_found = len(pending)

            if not pending:
                self.log.info("Nenhum BOPM pendente encontrado. Automação concluída.")
                self._save_no_bopm_notice()
                self._print_report(start_time)
                return 0

            # ── Etapa 7: Processar cada BOPM ─────────────────────────────
            self._step("ETAPA 7", f"Processar {len(pending)} BOPM(s) pendente(s)")

            for i, entry in enumerate(pending, 1):
                if not self.args.no_vpn:
                    try:
                        self.vpn.ensure_connected()
                    except RuntimeError as vpn_err:
                        self.log.critical(str(vpn_err))
                        return 2

                self.log.info(f"\n{'─' * 50}")
                self.log.info(f"Processando BOPM {i}/{len(pending)} — ID: {entry.bopm_id}")
                self.log.info(f"{'─' * 50}")

                success = self._process_single_bopm(nav, entry)
                if success:
                    self._total_saved += 1
                else:
                    self._total_failed += 1
                    self._failed_ids.append(entry.bopm_id)

                if i < len(pending):
                    time.sleep(1.5)

            self._print_report(start_time)
            return 0 if self._total_failed == 0 else 1

        except RuntimeError as exc:
            self.log.critical(f"ERRO CRÍTICO: {exc}")
            self._print_report(start_time)
            return 2
        except KeyboardInterrupt:
            self.log.warning("Automação interrompida pelo usuário (Ctrl+C).")
            self._print_report(start_time)
            return 2
        except Exception as exc:
            self.log.critical(f"Erro inesperado: {exc}")
            self.log.debug(traceback.format_exc())
            self._print_report(start_time)
            return 2
        finally:
            self.log.info("\nAutomação SIOPM finalizada. Edge mantido aberto.")
            # Envia PDFs para o Gemini com o Edge ainda ABERTO, reaproveitando a
            # mesma instância do Playwright (evita conflito de instâncias).
            if self._saved_paths:
                self.log.info(f"\n{len(self._saved_paths)} PDF(s) prontos para envio ao Gemini.")
                submitter = GeminiSubmitter(self.log)
                submitter.submit_pdfs(
                    self._saved_paths,
                    playwright=self.browser_mgr.playwright,
                )
            # Fecha o Edge e desconecta a VPN.
            self.browser_mgr.close()
            if not self.args.no_vpn and not self.args.keep_vpn:
                self.log.info("Desconectando VPN...")
                self.vpn.disconnect()

    # ------------------------------------------------------------------
    # Processar um único BOPM
    # ------------------------------------------------------------------

    def _process_single_bopm(self, nav: SiopmNavigator, entry: BopmEntry) -> bool:
        try:
            opened = nav.open_bopm(entry)
            if not opened:
                self.log.error(f"[{entry.bopm_id}] Falha ao abrir BOPM.")
                return False

            filepath = nav.scroll_to_bottom_and_get_pdf(entry)
            if filepath:
                self._saved_paths.append(filepath)
                self.log.info(f"[{entry.bopm_id}] ✓ PDF salvo: {filepath}")
                result = True
            else:
                self.log.error(f"[{entry.bopm_id}] ✗ PDF não foi salvo.")
                result = False

        except Exception as exc:
            self.log.error(f"[{entry.bopm_id}] Erro ao processar: {exc}")
            self.log.debug(traceback.format_exc())
            result = False

        finally:
            try:
                nav.go_back_to_list()
            except Exception as back_exc:
                self.log.warning(f"[{entry.bopm_id}] Erro ao voltar para lista: {back_exc}")

        return result

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _with_retry(self, func, label: str, retries: int = None) -> None:
        max_r = (retries or config.MAX_RETRY) + 1
        for attempt in range(1, max_r + 1):
            try:
                func()
                return
            except RuntimeError:
                raise
            except Exception as exc:
                if attempt < max_r:
                    self.log.warning(
                        f"'{label}' falhou (tentativa {attempt}/{max_r}): {exc} — retentando..."
                    )
                    time.sleep(3)
                else:
                    raise RuntimeError(
                        f"'{label}' falhou após {max_r} tentativa(s): {exc}"
                    )

    def _save_no_bopm_notice(self) -> None:
        import os
        today = datetime.now().strftime("%Y%m%d")
        filename = f"BOPM_sem_pendencias_{today}.txt"
        filepath = os.path.join(config.DOWNLOADS_DIR, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
                f.write("Resultado: Nenhum BOPM pendente de validação encontrado.\n")
                f.write(f"Filtro: {config.FILTER_TYPE} — últimos {config.FILTER_DAYS} dias\n")
                f.write(f"OPM: {config.SIOPM_OPM_CODE} ({config.SIOPM_OPM_NAME})\n")
            self.log.info(f"Aviso de sem pendências salvo: {filepath}")
        except Exception as exc:
            self.log.warning(f"Não foi possível salvar aviso: {exc}")

    def _step(self, tag: str, description: str) -> None:
        self.log.info(f"\n{'═' * 60}")
        self.log.info(f"  {tag}: {description}")
        self.log.info(f"{'═' * 60}")

    def _print_report(self, start_time: datetime) -> None:
        elapsed = datetime.now() - start_time
        self.log.info("\n" + "═" * 60)
        self.log.info("  RELATÓRIO FINAL DA AUTOMAÇÃO BOPM")
        self.log.info("═" * 60)
        self.log.info(f"  BOPMs encontrados : {self._total_found}")
        self.log.info(f"  PDFs salvos       : {self._total_saved}")
        self.log.info(f"  Falhas            : {self._total_failed}")
        self.log.info(f"  Tempo total       : {elapsed}")
        self.log.info(f"  Pasta Downloads   : {config.DOWNLOADS_DIR}")
        if self._saved_paths:
            self.log.info("  Arquivos salvos:")
            for p in self._saved_paths:
                self.log.info(f"    • {p}")
        if self._failed_ids:
            self.log.warning(f"  BOPMs com falha: {', '.join(self._failed_ids)}")
        self.log.info("═" * 60)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Automação BOPM/SIOPM — PMESP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python main.py                   # execução padrão (últimos 4 dias)
  python main.py --days 7          # últimos 7 dias
  python main.py --no-vpn          # VPN já conectada manualmente
  python main.py --keep-vpn        # não desconecta VPN ao terminar
  python main.py --log-level DEBUG # log completo para diagnóstico
        """,
    )
    p.add_argument("--days", type=int, default=None,
                   help="Número de dias para filtro (padrão: 4)")
    p.add_argument("--no-vpn", action="store_true",
                   help="Pular etapa de conexão VPN")
    p.add_argument("--keep-vpn", action="store_true",
                   help="Manter VPN conectada ao terminar")
    p.add_argument("--log-level", default="INFO",
                   choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                   help="Nível de detalhe dos logs (padrão: INFO)")
    p.add_argument("--headless", action="store_true",
                   help="Executar sem janela visível (modo agendado/automático)")
    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    if args.headless:
        config.HEADLESS = True
        config.SUPERVISED_MODE = False
    automation = BopMAutomation(args)
    sys.exit(automation.run())
