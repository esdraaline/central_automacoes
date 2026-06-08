#!/usr/bin/env python3
"""
nucleo_despachadora/ocr_pdfs_imagem.py

Uso:
    cd automacoes/despachadora/nucleo_despachadora
    python ocr_pdfs_imagem.py

Atualiza apenas as entradas do corpus_index.json marcadas com
error:"pdf_imagem_sem_ocr" e texto vazio, aplicando OCR com pdf2image +
pytesseract. Todas as demais entradas do índice são preservadas.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

# Garante que nucleo/ seja importável mesmo rodando standalone, igual ao indexador.
_NUCLEO_DESP = Path(__file__).resolve().parent          # nucleo_despachadora/
_DESP_DIR = _NUCLEO_DESP.parent                         # automacoes/despachadora/
_ROOT = _DESP_DIR.parent.parent                         # raiz do projeto
for _p in (str(_ROOT), str(_NUCLEO_DESP)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from nucleo.segredos import Segredos

_OUTPUT_FILE = _DESP_DIR / "corpus_index.json"
_TARGET_ERROR = "pdf_imagem_sem_ocr"


def print_dependency_error(detail: str | None = None) -> None:
    print("ERRO: dependência ausente. Instale com:")
    print("pip install pdf2image pytesseract")
    print("E instale o Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki")
    if detail:
        print(f"Detalhe: {detail}")


def find_tesseract_exe() -> str | None:
    found = shutil.which("tesseract")
    if found:
        return found

    default_path = Path("C:/Program Files/Tesseract-OCR/tesseract.exe")
    if default_path.exists():
        return str(default_path)

    return None


def find_tessdata_prefix() -> str | None:
    candidates = [
        Path(os.environ.get("LOCALAPPDATA", "")) / "Tesseract-OCR" / "tessdata",
        Path("C:/Program Files/Tesseract-OCR/tessdata"),
    ]
    for candidate in candidates:
        if (candidate / "por.traineddata").exists():
            return str(candidate)
    return None


def find_poppler_path() -> str | None:
    found = shutil.which("pdftoppm")
    if found:
        return str(Path(found).parent)

    packages = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
    if packages.exists():
        for pdftoppm in packages.glob("oschwartz10612.Poppler*/**/pdftoppm.exe"):
            return str(pdftoppm.parent)

    return None


def load_ocr_dependencies():
    try:
        from pdf2image import convert_from_path
        import pytesseract
    except ImportError as exc:
        print_dependency_error(str(exc))
        sys.exit(1)

    tesseract_exe = find_tesseract_exe()
    if tesseract_exe:
        pytesseract.pytesseract.tesseract_cmd = tesseract_exe

    tessdata_prefix = find_tessdata_prefix()
    if tessdata_prefix:
        os.environ["TESSDATA_PREFIX"] = tessdata_prefix

    try:
        pytesseract.get_tesseract_version()
    except Exception as exc:
        print_dependency_error(f"Tesseract OCR não encontrado ou indisponível ({exc})")
        sys.exit(1)

    return convert_from_path, pytesseract, find_poppler_path()


def load_index(path: Path) -> list[dict]:
    if not path.exists():
        print(f"ERRO: índice não encontrado: {path}")
        sys.exit(1)

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERRO: falha ao ler {path}: {exc}")
        sys.exit(1)

    if not isinstance(data, list):
        print(f"ERRO: formato inválido em {path}: esperado lista JSON.")
        sys.exit(1)

    return data


def physical_path(corpus_root: Path, entry: dict) -> Path:
    section = entry.get("section") or ""
    arquivo = entry.get("arquivo") or ""
    if section:
        return corpus_root / section / arquivo
    return corpus_root / arquivo


def ocr_pdf(path: Path, convert_from_path, pytesseract, poppler_path: str | None) -> tuple[str, str | None]:
    try:
        kwargs = {"dpi": 300}
        if poppler_path:
            kwargs["poppler_path"] = poppler_path
        imagens = convert_from_path(str(path), **kwargs)
        partes = []
        for imagem in imagens:
            texto_pagina = pytesseract.image_to_string(imagem, lang="por")
            partes.append(texto_pagina)
        texto = "\n".join(partes).strip()
        if texto:
            return texto, None
        return "", "ocr_falhou"
    except Exception as exc:
        return "", f"ocr_falhou: {exc}"


def save_index_atomic(path: Path, data: list[dict]) -> None:
    tmp_path = path.with_name(f"{path.name}.tmp")
    try:
        tmp_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass


def main() -> int:
    convert_from_path, pytesseract, poppler_path = load_ocr_dependencies()

    corpus_root = Path(Segredos().get("corpus")["path"])
    index_data = load_index(_OUTPUT_FILE)

    targets = [
        entry
        for entry in index_data
        if entry.get("error") == _TARGET_ERROR and not (entry.get("texto") or "").strip()
    ]

    total = len(targets)
    ok = 0
    errors = 0
    chars_added = 0

    print(f"Entradas alvo encontradas: {total}")

    for pos, entry in enumerate(targets, start=1):
        section = entry.get("section") or ""
        arquivo = entry.get("arquivo") or ""
        label_section = section or "root"
        print(f"[{pos}/{total}] [{label_section}] {arquivo} ... ", end="", flush=True)

        pdf_path = physical_path(corpus_root, entry)
        if not pdf_path.exists():
            entry["texto"] = ""
            entry["error"] = "arquivo_nao_encontrado"
            errors += 1
            print("ERRO: arquivo_nao_encontrado", flush=True)
            continue

        texto, error = ocr_pdf(pdf_path, convert_from_path, pytesseract, poppler_path)
        if error:
            entry["texto"] = ""
            entry["error"] = "ocr_falhou"
            errors += 1
            print(f"ERRO: {error}", flush=True)
            continue

        entry["texto"] = texto
        entry["error"] = None
        ok += 1
        chars_added += len(texto)
        print(f"OK ({len(texto):,} chars)", flush=True)

    save_index_atomic(_OUTPUT_FILE, index_data)

    print("\nRESUMO FINAL")
    print(f"  Total processados                  : {total}")
    print(f"  Total OK                           : {ok}")
    print(f"  Total com erro                     : {errors}")
    print(f"  Total de chars novos adicionados   : {chars_added:,}")
    print(f"  Índice salvo em                    : {_OUTPUT_FILE}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
