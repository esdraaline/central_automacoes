"""
nucleo/vpn.py — Gerenciamento da VPN Cisco Secure Client para PMESP.

Fluxo:
1. Verifica se o host da intranet já está acessível (VPN já conectada).
2. Se não, localiza o vpncli.exe e auto-detecta o servidor nos perfis XML.
3. Conecta via subprocess com credenciais piped.
4. Verifica novamente a acessibilidade após conexão.
"""

from __future__ import annotations

import os
import re
import socket
import subprocess
import time
import xml.etree.ElementTree as ET
from glob import glob
from logging import Logger
from typing import Dict, List, Optional


_DEFAULT_CLI_PATHS: List[str] = [
    r"C:\Program Files (x86)\Cisco\Cisco Secure Client\vpncli.exe",
    r"C:\Program Files\Cisco\Cisco Secure Client\vpncli.exe",
    r"C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exe",
    r"C:\Program Files\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exe",
]

_DEFAULT_PROFILE_PATHS: List[str] = [
    r"C:\ProgramData\Cisco\Cisco Secure Client\Profile",
    r"C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\Profile",
]


class VPNManager:
    """Controla conexão/desconexão com Cisco Secure Client."""

    def __init__(
        self,
        logger: Logger,
        creds: Dict[str, str],
        server: str = "",
        group: str = "",
        intranet_host: str = "",
        cli_paths: Optional[List[str]] = None,
        profile_paths: Optional[List[str]] = None,
        connect_timeout: int = 60,
        check_retries: int = 3,
    ) -> None:
        """
        Args:
            logger:          Logger da automação.
            creds:           Dict com "user" e "password" (de Segredos.get("vpn")).
            server:          Hostname/IP do servidor VPN (fallback se não detectado no XML).
            group:           Nome do grupo de conexão VPN.
            intranet_host:   Host usado para verificar conectividade da intranet.
            cli_paths:       Caminhos candidatos para o vpncli.exe.
            profile_paths:   Pastas com perfis XML do Cisco (auto-detecção do servidor).
            connect_timeout: Tempo máximo (s) para conectar.
            check_retries:   Tentativas de verificação de conectividade.
        """
        self.log = logger
        self._user = creds["user"]
        self._password = creds["password"]
        self._server_hint = server
        self._group = group
        self._intranet_host = intranet_host
        self._cli_paths = cli_paths or _DEFAULT_CLI_PATHS
        self._profile_paths = profile_paths or _DEFAULT_PROFILE_PATHS
        self._connect_timeout = connect_timeout
        self._check_retries = check_retries
        self._cli_path: Optional[str] = None
        self._server: Optional[str] = None
        self._connected_by_manager = False

    # ------------------------------------------------------------------
    # Pública: verificar conectividade
    # ------------------------------------------------------------------

    def is_intranet_reachable(self) -> bool:
        """Testa se o host da intranet PMESP é resolvível e acessível."""
        host = self._intranet_host
        for attempt in range(1, self._check_retries + 1):
            try:
                socket.setdefaulttimeout(5)
                socket.gethostbyname(host)
                self.log.debug(f"Intranet acessível: {host} (tentativa {attempt})")
                return True
            except OSError:
                self.log.debug(
                    f"Intranet inacessível (tentativa {attempt}/{self._check_retries})"
                )
                time.sleep(2)
        return False

    # ------------------------------------------------------------------
    # Pública: conectar
    # ------------------------------------------------------------------

    def connect(self) -> bool:
        """
        Conecta na VPN PMESP. Retorna True se bem-sucedido.
        Levanta RuntimeError em caso de falha crítica.
        """
        self._connected_by_manager = False
        if self.is_intranet_reachable():
            self.log.info("VPN já está conectada ou intranet acessível. Pulando conexão VPN.")
            return True

        self.log.info("Intranet não acessível. Iniciando conexão VPN...")

        cli = self._find_cli()
        if not cli:
            raise RuntimeError(
                "vpncli.exe não encontrado. Verifique se o Cisco Secure Client está instalado."
            )

        server = self._find_server()
        if not server:
            if self._server_hint:
                server = self._server_hint
                self.log.info(f"Usando servidor VPN da configuração: {server}")
            else:
                raise RuntimeError(
                    "Servidor VPN não encontrado nos perfis do Cisco e VPN_SERVER "
                    "não está definido em config.py. Preencha o campo VPN_SERVER."
                )

        return self._do_connect(cli, server)

    # ------------------------------------------------------------------
    # Pública: desconectar
    # ------------------------------------------------------------------

    def disconnect(self) -> None:
        """Desconecta a VPN de forma segura."""
        if not self._connected_by_manager:
            self.log.info("VPN não foi conectada por esta execução. Mantendo conexão ativa.")
            return

        cli = self._find_cli()
        if not cli:
            self.log.warning("CLI não encontrado — não foi possível desconectar a VPN.")
            return
        try:
            result = subprocess.run(
                [cli, "disconnect"],
                capture_output=True, text=True, timeout=15,
            )
            self.log.info(f"VPN desconectada: {result.stdout.strip()}")
        except Exception as exc:
            self.log.warning(f"Erro ao desconectar VPN: {exc}")

    # ------------------------------------------------------------------
    # Pública: garantir conexão durante a execução
    # ------------------------------------------------------------------

    def ensure_connected(self) -> None:
        """
        Verifica se a VPN está conectada durante a execução.
        Levanta RuntimeError se a conexão cair.
        """
        if not self.is_intranet_reachable():
            raise RuntimeError(
                "VPN CAIU durante a automação! Interrompendo para evitar dados inconsistentes."
            )

    # ------------------------------------------------------------------
    # Privados
    # ------------------------------------------------------------------

    def _find_cli(self) -> Optional[str]:
        if self._cli_path:
            return self._cli_path
        for path in self._cli_paths:
            if os.path.isfile(path):
                self._cli_path = path
                self.log.info(f"vpncli.exe encontrado: {path}")
                return path
        self.log.error("vpncli.exe não encontrado em nenhum dos caminhos padrão.")
        return None

    def _find_server(self) -> Optional[str]:
        """Auto-detecta o servidor VPN a partir dos perfis XML do Cisco."""
        if self._server:
            return self._server
        for profile_dir in self._profile_paths:
            if not os.path.isdir(profile_dir):
                continue
            for xml_file in glob(os.path.join(profile_dir, "*.xml")):
                try:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    ns_pattern = re.compile(r"\{.*\}")
                    for elem in root.iter():
                        tag = ns_pattern.sub("", elem.tag)
                        if tag in ("HostAddress", "HostEntry", "Address") and elem.text:
                            server = elem.text.strip()
                            self.log.info(
                                f"Servidor VPN detectado no perfil {xml_file}: {server}"
                            )
                            self._server = server
                            return server
                except ET.ParseError:
                    continue
        self.log.warning("Nenhum servidor VPN encontrado nos perfis do Cisco.")
        return None

    def _kill_vpn_processes(self) -> None:
        """Encerra processos Cisco que possam bloquear o CLI."""
        for proc in ["vpnui.exe", "csc_ui.exe", "vpncli.exe"]:
            try:
                result = subprocess.run(
                    ["taskkill", "/f", "/im", proc],
                    capture_output=True, text=True,
                )
                if "ÊXITO" in result.stdout or "SUCCESS" in result.stdout.upper():
                    self.log.info(f"Processo {proc} encerrado.")
            except Exception:
                pass
        time.sleep(2)

    def _do_connect(self, cli: str, server: str) -> bool:
        """Executa a conexão via CLI com credenciais piped."""
        self._kill_vpn_processes()

        stdin_input = "\n".join([
            "y",              # aceitar aviso de certificado
            self._group,      # seleção de grupo
            self._user,       # usuário
            self._password,   # senha
            "y",              # aceitar banner PMESP
            "",
        ]) + "\n"

        self.log.info(
            f"Conectando VPN: servidor={server}, grupo={self._group}, "
            f"usuário={self._user}"
        )

        try:
            proc = subprocess.Popen(
                [cli, "connect", server],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = proc.communicate(
                input=stdin_input, timeout=self._connect_timeout
            )

            self.log.debug(f"VPN stdout: {stdout.strip()[:500]}")
            if stderr:
                self.log.debug(f"VPN stderr: {stderr.strip()[:200]}")

            if re.search(r"error:", stdout, re.IGNORECASE):
                self.log.error(f"VPN reportou erro na saída:\n{stdout[:400]}")
                return False

            connected = bool(
                re.search(r"state:\s+Connect(?:ed|ado)\b", stdout, re.IGNORECASE)
            )
            if connected:
                self._connected_by_manager = True
                self.log.info("VPN conectada com sucesso!")
                time.sleep(4)
                if self.is_intranet_reachable():
                    return True
                else:
                    self.log.error("VPN reportou conexão mas intranet ainda inacessível.")
                    return False
            else:
                self.log.error(f"VPN não confirmou conexão. Saída:\n{stdout[:400]}")
                return False

        except subprocess.TimeoutExpired:
            self.log.error(f"Timeout ao conectar VPN ({self._connect_timeout}s).")
            proc.kill()
            return False
        except FileNotFoundError:
            self.log.error(f"Executável não encontrado: {cli}")
            return False
        except Exception as exc:
            self.log.error(f"Erro inesperado ao conectar VPN: {exc}")
            return False
