"""
nucleo/segredos.py — Acesso seguro a credenciais.

Lê de segredos.env (via python-dotenv) e expõe get(servico).
Interface abstrata: trocar por keyring no futuro não exige mudança nos chamadores.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

from dotenv import dotenv_values


# Chaves esperadas por serviço → mapeadas para campos no dict retornado
_SCHEMA: Dict[str, List[str]] = {
    "vpn":    ["VPN_USER",      "VPN_PASSWORD"],
    "siopm":  ["SIOPM_USER",    "SIOPM_PASSWORD"],
    "dejem":  ["DEJEM_USUARIO", "DEJEM_SENHA"],
    "orion":  ["ORION_USER",    "ORION_PASSWORD"],
    # Fase 7 — Despachadora
    # get("gemini")  → {"api_key": "..."}
    # get("corpus")  → {"path": "G:\\Meu Drive\\..."}  (letra de unidade por máquina)
    "gemini": ["GEMINI_API_KEY"],
    "corpus": ["CORPUS_PATH"],
}

# Raiz do projeto: nucleo/ está um nível abaixo da raiz
_PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Segredos:
    """
    Acesso centralizado a credenciais. Nunca expõe senhas em log.

    Uso:
        s = Segredos()
        s.get("siopm")   # -> {"user": "...", "password": "..."}
        s.get("vpn")     # -> {"user": "...", "password": "..."}
    """

    def __init__(self, env_path: Optional[Path] = None) -> None:
        if env_path is None:
            env_path = _PROJECT_ROOT / "segredos.env"
        env_path = Path(env_path)
        if not env_path.exists():
            raise FileNotFoundError(
                f"Arquivo de segredos não encontrado: {env_path}\n"
                "Copie segredos.env.exemplo para segredos.env e preencha."
            )
        self._values: Dict[str, str] = dotenv_values(env_path)  # type: ignore[assignment]

    def get(self, servico: str) -> Dict[str, str]:
        """
        Retorna as credenciais do serviço como dict com chaves 'user' e 'password'.
        Levanta KeyError se o serviço for desconhecido ou as chaves estiverem vazias.
        """
        keys = _SCHEMA.get(servico)
        if keys is None:
            raise KeyError(
                f"Serviço desconhecido: {servico!r}. "
                f"Disponíveis: {list(_SCHEMA)}"
            )

        result: Dict[str, str] = {}
        missing: List[str] = []

        for key in keys:
            val = (self._values.get(key) or "").strip()
            if not val:
                missing.append(key)
            # Remove o prefixo do serviço: VPN_USER → user, SIOPM_PASSWORD → password
            field = key.split("_", 1)[1].lower()
            result[field] = val

        if missing:
            raise KeyError(
                f"Credenciais ausentes em segredos.env para '{servico}': {missing}"
            )

        return result
