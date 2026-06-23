"""Testes locais do Sprint 3.1 do Órion; não acessam rede nem credenciais reais."""

import importlib.util
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from nucleo.login_orion import _assert_sessao_ativa, _sessao_ativa
from nucleo.segredos import Segredos


class Element:
    def __init__(self, visible=True):
        self.visible = visible

    def is_visible(self):
        return self.visible

    def evaluate(self, _script):
        return "INPUT"

    def get_attribute(self, name):
        return "password" if name == "type" else ""


class Locator:
    def __init__(self, text):
        self.text = text

    def inner_text(self, timeout=0):
        return self.text


class Page:
    def __init__(self, url, text, password_visible=False):
        self.url = url
        self.frames = [self]
        self.text = text
        self.password_visible = password_visible

    def query_selector_all(self, selector):
        if "password" in selector and self.password_visible:
            return [Element()]
        return []

    def locator(self, _selector):
        return Locator(self.text)


def test_segredos_orion():
    with tempfile.TemporaryDirectory() as temp:
        env = Path(temp) / "segredos.env"
        env.write_text(
            "ORION_USER=usuario_teste\n"
            "ORION_PASSWORD=senha_teste\n"
            "ORION_URL=https://orion.exemplo/login\n",
            encoding="utf-8",
        )
        assert Segredos(env).get("orion") == {
            "user": "usuario_teste",
            "password": "senha_teste",
            "url": "https://orion.exemplo/login",
        }


def test_manifesto_orion():
    path = ROOT / "automacoes" / "orion_indicadores" / "manifesto.py"
    spec = importlib.util.spec_from_file_location("manifesto_orion_teste", path)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    assert modulo.MANIFESTO["id"] == "orion_indicadores"
    assert modulo.MANIFESTO["precisa_vpn"] is True
    assert modulo.MANIFESTO["destrutivo"] is False


def test_sessao_ativa():
    login_url = "https://orion.exemplo/login"
    assert not _sessao_ativa(Page(login_url, "Entrar", True), login_url)
    ativa = Page("https://orion.exemplo/dashboard", "Painel de indicadores")
    assert _sessao_ativa(ativa, login_url)
    _assert_sessao_ativa(ativa, login_url)


if __name__ == "__main__":
    test_segredos_orion()
    test_manifesto_orion()
    test_sessao_ativa()
    print("SPRINT 3.1 ÓRION: TESTES LOCAIS OK")
