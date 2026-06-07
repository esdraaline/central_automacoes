"""
painel.py — Interface gráfica da Central de Automações — PMESP.

Descobre automações lendo automacoes/*/manifesto.py e cria um cartão + botão
por automação. Ao clicar: garante VPN (se preciso), roda run(ctx) numa thread
e transmite o log ao vivo.
"""

from __future__ import annotations

import importlib.util
import logging
import sys
import threading
from tkinter import filedialog
from pathlib import Path
from typing import Any, Dict, List, Optional

import customtkinter as ctk

# Raiz do projeto no sys.path para que nucleo.* seja importável
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from nucleo.segredos import Segredos
from nucleo.log import setup_logger
from nucleo.vpn import VPNManager
from nucleo.browser import BrowserManager
from nucleo.contexto import Contexto

_AUTOMACOES_DIR = _ROOT / "automacoes"
_SAIDAS_DIR = _ROOT / "saidas"

# Configuração não-secreta de VPN — infraestrutura compartilhada da PMESP.
# Quando houver uma segunda automação com VPN, mover para config central.
_VPN_CONFIG: Dict[str, Any] = {
    "server":          "extranet.policiamilitar.sp.gov.br",
    "group":           "00 - PMESP",
    "intranet_host":   "sistemasopr.intranet.policiamilitar.sp.gov.br",
    "connect_timeout": 60,
    "check_retries":   3,
}


# ─────────────────────────────────────────────────────────────────────────────
# Descoberta dinâmica de automações
# ─────────────────────────────────────────────────────────────────────────────

def _discover() -> List[Dict[str, Any]]:
    """Lê automacoes/*/manifesto.py e retorna lista ordenada por 'ordem'."""
    automacoes = []
    for path in _AUTOMACOES_DIR.glob("*/manifesto.py"):
        try:
            spec = importlib.util.spec_from_file_location("manifesto", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            automacoes.append({"manifesto": mod.MANIFESTO, "dir": path.parent})
        except Exception as exc:
            print(f"[painel] Erro ao carregar {path}: {exc}")
    return sorted(automacoes, key=lambda a: a["manifesto"].get("ordem", 99))


def _load_executar(auto_dir: Path):
    """Carrega dinamicamente executar.py de uma automação."""
    path = auto_dir / "executar.py"
    spec = importlib.util.spec_from_file_location("executar", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ─────────────────────────────────────────────────────────────────────────────
# Handler de log para a GUI (thread-safe via after())
# ─────────────────────────────────────────────────────────────────────────────

class _GuiLogHandler(logging.Handler):
    """Redireciona mensagens de log para o CTkTextbox da janela."""

    def __init__(self, textbox: ctk.CTkTextbox) -> None:
        super().__init__()
        self._tb = textbox
        self.setFormatter(logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S",
        ))

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record) + "\n"
            self._tb.after(0, self._append, msg)
        except Exception:
            pass

    def _append(self, msg: str) -> None:
        try:
            self._tb.configure(state="normal")
            self._tb.insert("end", msg)
            self._tb.see("end")
            self._tb.configure(state="disabled")
        except Exception:
            pass


# ─────────────────────────────────────────────────────────────────────────────
# Janela principal
# ─────────────────────────────────────────────────────────────────────────────

class Painel(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.title("Central de Automações — PMESP")
        self.geometry("860x720")
        self.minsize(640, 500)

        self._segredos = Segredos()
        self._running = False
        self._automacoes = _discover()
        self._btn_refs: Dict[str, ctk.CTkButton] = {}
        self._status_refs: Dict[str, ctk.CTkLabel] = {}
        self._entrada_texto_refs: Dict[str, ctk.CTkEntry] = {}
        self._entrada_arquivo_refs: Dict[str, ctk.CTkLabel] = {}
        self._entrada_arquivo_path_refs: Dict[str, Optional[Path]] = {}

        self._build_ui()

    # ------------------------------------------------------------------
    # Construção da UI
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)   # cards expandem verticalmente
        self.grid_rowconfigure(3, weight=2)   # log expande mais

        # Cabeçalho
        ctk.CTkLabel(
            self,
            text="Central de Automações — PMESP",
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w",
        ).grid(row=0, column=0, padx=20, pady=(16, 4), sticky="w")

        # Frame rolável com cards
        cards = ctk.CTkScrollableFrame(self, label_text="Automações disponíveis")
        cards.grid(row=1, column=0, padx=16, pady=(0, 8), sticky="nsew")
        cards.grid_columnconfigure(0, weight=1)

        if self._automacoes:
            for i, auto in enumerate(self._automacoes):
                self._build_card(cards, i, auto["manifesto"], auto["dir"])
        else:
            ctk.CTkLabel(
                cards,
                text="Nenhuma automação encontrada em automacoes/",
                text_color="gray",
            ).grid(row=0, column=0, pady=20)

        # Label do log
        ctk.CTkLabel(
            self, text="Log de execução", anchor="w",
            font=ctk.CTkFont(size=12),
        ).grid(row=2, column=0, padx=20, pady=(0, 2), sticky="w")

        # Caixa de log
        self._log_box = ctk.CTkTextbox(
            self,
            state="disabled",
            font=("Courier New", 11),
            wrap="none",
        )
        self._log_box.grid(row=3, column=0, padx=16, pady=(0, 4), sticky="nsew")

        # Botão limpar log
        ctk.CTkButton(
            self, text="Limpar log", width=120, height=28,
            fg_color="gray40", hover_color="gray30",
            command=self._clear_log,
        ).grid(row=4, column=0, padx=16, pady=(0, 12), sticky="e")

    def _build_card(
        self,
        parent: ctk.CTkScrollableFrame,
        row: int,
        m: dict,
        auto_dir: Path,
    ) -> None:
        card = ctk.CTkFrame(parent, corner_radius=8)
        card.grid(row=row, column=0, padx=8, pady=6, sticky="ew")
        card.grid_columnconfigure(1, weight=1)
        aid = m["id"]

        # Linha 0: badges (categoria + VPN)
        badges = ctk.CTkFrame(card, fg_color="transparent")
        badges.grid(row=0, column=0, columnspan=2, padx=12, pady=(10, 0), sticky="w")

        ctk.CTkLabel(
            badges,
            text=m.get("categoria", "—"),
            font=ctk.CTkFont(size=10),
            fg_color=("gray75", "gray30"),
            corner_radius=4,
            padx=6, pady=2,
        ).pack(side="left", padx=(0, 4))

        if m.get("precisa_vpn"):
            ctk.CTkLabel(
                badges,
                text="VPN",
                font=ctk.CTkFont(size=10, weight="bold"),
                fg_color=("darkorange3", "darkorange4"),
                text_color="white",
                corner_radius=4,
                padx=6, pady=2,
            ).pack(side="left")

        # Linha 1: nome
        ctk.CTkLabel(
            card,
            text=m["nome"],
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w",
        ).grid(row=1, column=0, columnspan=2, padx=12, pady=(4, 0), sticky="w")

        # Linha 2: descrição
        ctk.CTkLabel(
            card,
            text=m.get("descricao", ""),
            font=ctk.CTkFont(size=11),
            text_color=("gray40", "gray70"),
            anchor="w",
        ).grid(row=2, column=0, columnspan=2, padx=12, pady=(2, 6), sticky="w")

        # Linha 3: botão + status
        btn = ctk.CTkButton(
            card,
            text=f"▶  {m['nome']}",
            width=200,
            command=lambda d=auto_dir, mf=m: self._on_run(d, mf),
        )
        btn.grid(row=3, column=0, padx=12, pady=(0, 12), sticky="w")

        status = ctk.CTkLabel(
            card, text="● Aguardando", font=ctk.CTkFont(size=11),
        )
        status.grid(row=3, column=1, padx=8, pady=(0, 12), sticky="w")

        self._btn_refs[aid] = btn
        self._status_refs[aid] = status

        if m.get("requer_texto") or m.get("requer_arquivo"):
            inputs = ctk.CTkFrame(card, fg_color="transparent")
            inputs.grid(row=4, column=0, columnspan=2, padx=12, pady=(0, 12), sticky="ew")
            inputs.grid_columnconfigure(1, weight=1)

            input_row = 0
            if m.get("requer_texto"):
                entrada = ctk.CTkEntry(
                    inputs,
                    placeholder_text="Cole o texto do expediente...",
                )
                entrada.grid(row=input_row, column=0, columnspan=2, pady=(0, 6), sticky="ew")
                self._entrada_texto_refs[aid] = entrada
                input_row += 1

            if m.get("requer_arquivo"):
                escolher = ctk.CTkButton(
                    inputs,
                    text="Selecionar arquivo",
                    width=150,
                    command=lambda auto_id=aid: self._selecionar_arquivo(auto_id),
                )
                escolher.grid(row=input_row, column=0, padx=(0, 8), sticky="w")

                arquivo_lbl = ctk.CTkLabel(
                    inputs,
                    text="Nenhum arquivo selecionado",
                    font=ctk.CTkFont(size=11),
                    text_color=("gray40", "gray70"),
                    anchor="w",
                )
                arquivo_lbl.grid(row=input_row, column=1, sticky="ew")
                self._entrada_arquivo_refs[aid] = arquivo_lbl
                self._entrada_arquivo_path_refs[aid] = None

    # ------------------------------------------------------------------
    # Execução da automação
    # ------------------------------------------------------------------

    def _on_run(self, auto_dir: Path, manifesto: dict) -> None:
        aid = manifesto["id"]
        if self._running:
            self._gui_log("⚠ Já há uma automação em execução. Aguarde o término.")
            return

        entrada_texto = None
        entrada_texto_ref = self._entrada_texto_refs.get(aid)
        if entrada_texto_ref is not None:
            valor = entrada_texto_ref.get().strip()
            entrada_texto = valor or None

        entrada_arquivo = self._entrada_arquivo_path_refs.get(aid)

        self._running = True
        self._set_status(aid, "▶ Iniciando…", "orange")
        self._btn_refs[aid].configure(state="disabled")
        threading.Thread(
            target=self._run_thread,
            args=(auto_dir, manifesto, entrada_texto, entrada_arquivo),
            daemon=True,
        ).start()

    def _run_thread(
        self,
        auto_dir: Path,
        manifesto: dict,
        entrada_texto: Optional[str],
        entrada_arquivo: Optional[Path],
    ) -> None:
        aid = manifesto["id"]
        log = setup_logger(name=aid, level="INFO")

        gui_handler = _GuiLogHandler(self._log_box)
        gui_handler.setLevel(logging.INFO)
        log.addHandler(gui_handler)

        vpn: Optional[VPNManager] = None

        try:
            # VPN: o painel conecta antes de chamar run()
            if manifesto.get("precisa_vpn"):
                self._set_status(aid, "▶ Conectando VPN…", "orange")
                vpn = VPNManager(
                    logger=log,
                    creds=self._segredos.get("vpn"),
                    **_VPN_CONFIG,
                )
                if not vpn.connect():
                    raise RuntimeError("Falha ao conectar VPN.")

            self._set_status(aid, "▶ Rodando…", "orange")

            ctx = Contexto(
                log=log,
                segredos=self._segredos,
                vpn=vpn,
                browser=BrowserManager(log),
                saidas=_SAIDAS_DIR,
                entrada_arquivo=entrada_arquivo,
                entrada_texto=entrada_texto,
            )

            mod = _load_executar(auto_dir)
            result = mod.run(ctx)

            if result.get("status_txt"):
                txt = result["status_txt"]
            elif "salvos" in result or "encontrados" in result:
                s = result.get("salvos", 0)
                e = result.get("encontrados", 0)
                txt = f"✓ {s}/{e} BOPMs" if e > 0 else "✓ Concluído (sem pendentes)"
            else:
                txt = "✓ Concluído"
            self._set_status(aid, txt, "green")
            if result.get("saida_longa"):
                self.after(0, self._abrir_saida_longa, result["saida_longa"], manifesto["nome"])

        except Exception as exc:
            log.error(f"Erro fatal: {exc}")
            self._set_status(aid, f"✗ {exc}", "red")

        finally:
            if vpn is not None:
                try:
                    vpn.disconnect()
                except Exception:
                    pass
            log.removeHandler(gui_handler)
            self._btn_refs[aid].after(
                0, lambda: self._btn_refs[aid].configure(state="normal")
            )
            self._running = False

    # ------------------------------------------------------------------
    # Helpers de UI (todos thread-safe via after())
    # ------------------------------------------------------------------

    _COLOR_MAP = {
        "orange": ("orange3",  "darkorange"),
        "green":  ("green4",   "green3"),
        "red":    ("red3",     "red2"),
        "gray":   ("gray50",   "gray60"),
    }

    def _set_status(self, aid: str, text: str, color: str) -> None:
        lbl = self._status_refs.get(aid)
        if lbl is None:
            return
        tc = self._COLOR_MAP.get(color, ("white", "white"))
        lbl.after(0, lambda: lbl.configure(text=text, text_color=tc))

    def _selecionar_arquivo(self, aid: str) -> None:
        caminho = filedialog.askopenfilename(title="Selecionar expediente")
        if not caminho:
            return

        path = Path(caminho)
        self._entrada_arquivo_path_refs[aid] = path
        lbl = self._entrada_arquivo_refs.get(aid)
        if lbl is not None:
            lbl.configure(text=str(path))

    def _abrir_saida_longa(self, texto: str, titulo: str) -> None:
        janela = ctk.CTkToplevel(self)
        janela.title(f"Resultado — {titulo}")
        janela.geometry("800x600")
        janela.minsize(700, 500)
        janela.grid_columnconfigure(0, weight=1)
        janela.grid_rowconfigure(0, weight=1)

        caixa = ctk.CTkTextbox(janela, wrap="word")
        caixa.grid(row=0, column=0, padx=12, pady=(12, 8), sticky="nsew")
        caixa.insert("1.0", texto)
        caixa.configure(state="disabled")

        botoes = ctk.CTkFrame(janela, fg_color="transparent")
        botoes.grid(row=1, column=0, padx=12, pady=(0, 12), sticky="e")

        def copiar() -> None:
            self.clipboard_clear()
            self.clipboard_append(texto)

        def salvar() -> None:
            caminho = filedialog.asksaveasfilename(
                title="Salvar resultado",
                initialdir=_SAIDAS_DIR,
                defaultextension=".txt",
                filetypes=[("Texto", "*.txt")],
            )
            if caminho:
                Path(caminho).write_text(texto, encoding="utf-8")

        ctk.CTkButton(botoes, text="Copiar", width=90, command=copiar).pack(side="left", padx=(0, 8))
        ctk.CTkButton(botoes, text="Salvar", width=90, command=salvar).pack(side="left", padx=(0, 8))
        ctk.CTkButton(botoes, text="Fechar", width=90, command=janela.destroy).pack(side="left")

    def _gui_log(self, msg: str) -> None:
        self._log_box.configure(state="normal")
        self._log_box.insert("end", msg + "\n")
        self._log_box.see("end")
        self._log_box.configure(state="disabled")

    def _clear_log(self) -> None:
        self._log_box.configure(state="normal")
        self._log_box.delete("1.0", "end")
        self._log_box.configure(state="disabled")


# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = Painel()
    app.mainloop()
