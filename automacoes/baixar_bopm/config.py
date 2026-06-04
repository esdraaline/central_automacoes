"""
config.py — Configurações não-secretas da automação BOPM/SIOPM.

Credenciais (VPN e SIOPM) foram movidas para segredos.env na Fase 0 · Sprint 1.
"""

import os
from pathlib import Path

# Raiz do projeto: automacoes/baixar_bopm/ -> automacoes/ -> raiz
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# =============================================================================
# VPN — Cisco Secure Client  (credenciais em segredos.env)
# =============================================================================
VPN_SERVER       = "extranet.policiamilitar.sp.gov.br"
VPN_GROUP        = "00 - PMESP"

VPN_CLI_PATHS = [
    r"C:\Program Files (x86)\Cisco\Cisco Secure Client\vpncli.exe",
    r"C:\Program Files\Cisco\Cisco Secure Client\vpncli.exe",
    r"C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exe",
    r"C:\Program Files\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exe",
]

VPN_PROFILE_PATHS = [
    r"C:\ProgramData\Cisco\Cisco Secure Client\Profile",
    r"C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\Profile",
]

# =============================================================================
# SIOPM Web  (credenciais em segredos.env)
# =============================================================================
SIOPM_URL        = "http://sistemasopr.intranet.policiamilitar.sp.gov.br/siopmweb/HSiopm.aspx"
SIOPM_CAD        = "Araçatuba"
SIOPM_OPM_CODE   = "610025000"
SIOPM_OPM_NAME   = "2.BPM/I 5.CIA PM"

# =============================================================================
# Filtro de BOPMs
# =============================================================================
FILTER_TYPE      = "BOPM/TC - P/ Validação"
FILTER_BY        = "Por código da OPM"
FILTER_SELECTION = "Todos"
FILTER_DAYS      = 4
BOPM_CATEGORY    = "Ocorrências"
RENOVAR_BTN_TEXT = "Renovar"

# =============================================================================
# Caminhos de saída
# =============================================================================
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
LOG_DIR       = str(_PROJECT_ROOT / "logs")

# =============================================================================
# Timeouts e tentativas (ms / s)
# =============================================================================
TIMEOUT_PAGE_LOAD    = 30_000
TIMEOUT_ELEMENT      = 15_000
TIMEOUT_NAVIGATION   = 45_000
TIMEOUT_PDF_DOWNLOAD = 60_000
VPN_CONNECT_TIMEOUT  = 60
VPN_CHECK_RETRIES    = 3
INTRANET_PING_HOST   = "sistemasopr.intranet.policiamilitar.sp.gov.br"

# =============================================================================
# Modo de execução
# =============================================================================
SUPERVISED_MODE  = True
HEADLESS         = False
MAX_RETRY        = 1

# =============================================================================
# Detecção da seta laranja (múltiplas estratégias)
# =============================================================================
ORANGE_HEX_VALUES = [
    "ff6600", "ff8c00", "ffa500", "ff4500",
    "ff7700", "f07000", "e06000", "ffa000",
    "ff9900", "ff6a00",
]
ORANGE_IMG_KEYWORDS = ["seta", "arrow", "pend", "laranja", "orange", "atencao", "alerta"]
ORANGE_CSS_CLASSES  = ["pendente", "pend", "seta", "laranja", "orange", "aguard", "atencao"]
ORANGE_ALT_TEXTS    = ["pendente", "aguardando", "validação", "seta", "laranja"]
