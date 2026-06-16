#!/usr/bin/env python3
"""
nucleo_despachadora/classificar_corpus.py

Sprint 8.2: adiciona metadados ao corpus_index.json de forma aditiva.

Uso:
    cd automacoes/despachadora/nucleo_despachadora
    python classificar_corpus.py
    python classificar_corpus.py --reimport ../../../saidas/revisao_classificacao.csv

Regras centrais:
  - Classifica apenas a partir do indice ja existente.
  - Nao reabre arquivos do corpus para extrair conteudo.
  - Baixa confianca fica no indice como NAO_CLASSIFICADO/especie null.
  - Sugestoes de baixa confianca ficam apenas na planilha de revisao.
  - Escrita atomica e backup antes de modificar corpus_index.json.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Garante que nucleo/ seja importavel mesmo rodando standalone.
_NUCLEO_DESP = Path(__file__).resolve().parent
_DESP_DIR = _NUCLEO_DESP.parent
_ROOT = _DESP_DIR.parent.parent
for _p in (str(_ROOT), str(_NUCLEO_DESP)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from nucleo.segredos import Segredos

INDEX_FILE = _DESP_DIR / "corpus_index.json"
SAIDAS_DIR = _ROOT / "saidas"
DOCS_DIR = _ROOT / "docs"

NATUREZAS = {
    "NORMA",
    "MODELO_DE_REDACAO",
    "MODELO_PRECEDENTE",
    "PRECEDENTE",
    "JURISPRUDENCIA",
    "PROCEDIMENTAL",
    "OUTRO",
    "NAO_CLASSIFICADO",
}
ESPECIES = {
    "parte",
    "oficio",
    "despacho",
    "sindicancia",
    "ipm",
    "tc",
    "relatorio",
    "escala",
    "ata",
    "outro",
}
HIERARQUIAS = {"lei_federal", "lei_estadual", "decreto", "resolucao", "norma_interna"}
METADATA_FIELDS = {
    "natureza",
    "especie",
    "vigencia",
    "hierarquia",
    "fonte",
    "classificacao_confianca",
    "classificacao_origem",
    "classificacao_sinais",
}
ORIGINAL_FIELDS = {"section", "arquivo", "tipo", "texto", "error"}

EXCLUDED_DIR_PREFIXES = [
    Path("P1") / "Holerites",
    Path("P1") / "Holerites Bonus DEJEM",
    Path("P4") / "enderecos de ip",
    Path("P4") / "endereços de ip",
]
EXCLUDED_FILE_NAMES = {
    "despachadora.py",
    "indexar_corpus.py",
    "corpus_index.json",
}
EXCLUDED_EXTENSIONS = {
    ".pfx",
    ".cer",
    ".rar",
    ".mp4",
    ".jpg",
    ".jpeg",
    ".png",
    ".pptx",
    ".ppt",
}
DOC_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt", ".md", ".htm", ".html", ".rtf", ".mht"}


@dataclass
class Classification:
    natureza_index: str
    especie_index: str | None
    hierarquia: str | None
    confianca: str
    natureza_sugerida: str
    especie_sugerida: str | None
    sinais: list[str]


@dataclass
class StructureScore:
    promove: bool
    quase: bool
    score: int
    limiar: int
    categorias: list[str]
    obrigatorios_faltantes: list[str]
    categorias_faltantes: list[str]
    sinais: str


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value or "")
    without_accents = "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
    return without_accents.lower()


def key_for(entry: dict[str, Any]) -> str:
    section = entry.get("section") or ""
    arquivo = entry.get("arquivo") or ""
    return f"{section}/{arquivo}" if section else arquivo


def rel_to_posix(path: Path) -> str:
    return str(path).replace(os.sep, "/")


def load_index(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Indice nao encontrado: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Formato invalido em {path}: esperado lista JSON.")
    return data


def save_index_atomic(path: Path, data: list[dict[str, Any]]) -> None:
    tmp_path = path.with_name(f"{path.name}.tmp")
    try:
        tmp_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass


def create_backups(index_path: Path, corpus_root: Path) -> tuple[Path, Path]:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_name = f"corpus_index.backup.{timestamp}.json"
    local_backup = index_path.with_name(backup_name)
    drive_backup_dir = corpus_root.parent / "backups_corpus_index_despachadora"
    drive_backup_dir.mkdir(parents=True, exist_ok=True)
    drive_backup = drive_backup_dir / backup_name
    shutil.copy2(index_path, local_backup)
    shutil.copy2(index_path, drive_backup)
    return local_backup, drive_backup


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def has_any(haystack: str, patterns: list[str]) -> list[str]:
    found: list[str] = []
    for pattern in patterns:
        if pattern.startswith("re:"):
            if re.search(pattern[3:], haystack):
                found.append(pattern)
        elif pattern in haystack:
                found.append(pattern)
    return found


def head_tail_window(texto: str, head_chars: int = 12000, tail_chars: int = 6000) -> str:
    if len(texto) <= head_chars + tail_chars:
        return texto
    return f"{texto[:head_chars]} {texto[-tail_chars:]}"


def detect_i7pm_structure(entry: dict[str, Any]) -> StructureScore:
    section = str(entry.get("section") or "")
    arquivo = str(entry.get("arquivo") or "")
    texto = str(entry.get("texto") or "")
    janela = head_tail_window(texto)
    haystack = normalize(f"{section} {arquivo} {janela}")
    section_norm = normalize(section)
    is_jd = section_norm == "jd"

    category_patterns = {
        "opm": [
            "policia militar do estado de sao paulo",
            "pmesp",
            "2o bpm",
            "2º bpm",
            "2 bpm/i",
            "2º bpm/i",
            "5a cia",
            "5ª cia",
            "opm",
            "cmt",
        ],
        "tipo": [
            "oficio",
            "parte n",
            "parte nº",
            "despacho",
            "relatorio",
            "portaria",
            "informacao",
            "encaminhamento",
            "re:oficio\\s*(n|nº|no|numero)",
            "re:parte\\s*(n|nº|no|numero)",
        ],
        "enderecamento": [
            "ao senhor",
            "a senhora",
            "excelentissimo",
            "ilustrissimo",
            "senhor comandante",
            "senhor delegado",
            "senhor promotor",
            "senhor juiz",
            "senhor prefeito",
        ],
        "corpo": [
            "encaminho",
            "solicito",
            "informo",
            "determino",
            "decido",
            "opino",
            "considerando",
            "manifesto-me",
            "proponho",
            "remeto",
        ],
        "fecho": [
            "atenciosamente",
            "respeitosamente",
            "quartel em",
            "renovo protestos",
            "aproveito o ensejo",
            "nos policiais militares sob a protecao de deus",
            "assinado no original",
            "certifico que o presente arquivo eletronico confere",
        ],
        "assinatura": [
            "cap pm",
            "ten pm",
            "maj pm",
            "cel pm",
            "sgt pm",
            "sd pm",
            "encarregado",
            "presidente",
            "oficial ppjm",
            "chefe p/3",
            "chefe p3",
            "cmt",
            "cmt pel",
            "cmt cia",
            "comandante",
            "subcomandante",
            "re:\\brg\\s*\\d",
            "re:\\b[a-z]{2,}(?:\\s+[a-z]{2,}){1,5}\\s+(cap|ten|maj|cel|sgt|sd)\\s+pm\\b",
            "re:\\b(cap|ten|maj|cel|sgt|sd)\\s+pm\\s+[a-z]{2,}(?:\\s+[a-z]{2,}){1,5}\\b",
        ],
    }

    categorias = [
        category
        for category, patterns in category_patterns.items()
        if has_any(haystack, patterns)
    ]
    categorias_set = set(categorias)
    score = len(categorias)
    limiar = 5 if is_jd else 4

    obrigatorios_faltantes: list[str] = []
    if is_jd:
        for required in ("tipo", "corpo", "assinatura"):
            if required not in categorias_set:
                obrigatorios_faltantes.append(required)
    else:
        if not ({"tipo", "corpo"} & categorias_set):
            obrigatorios_faltantes.append("tipo_ou_corpo")
        if not ({"fecho", "assinatura"} & categorias_set):
            obrigatorios_faltantes.append("fecho_ou_assinatura")

    promove = (
        not entry.get("error")
        and len(texto.strip()) >= 300
        and score >= limiar
        and not obrigatorios_faltantes
    )

    categorias_faltantes = [
        category for category in category_patterns if category not in categorias_set
    ]
    bateu_limiar_menos_um = score == limiar - 1
    bateu_tudo_menos_obrigatorio = score >= limiar and len(obrigatorios_faltantes) == 1
    quase = (
        not promove
        and not entry.get("error")
        and len(texto.strip()) >= 300
        and (bateu_limiar_menos_um or bateu_tudo_menos_obrigatorio)
    )

    sinais = (
        f"segunda_passada_i7pm; score={score}/6; limiar={limiar}; "
        f"categorias={','.join(categorias) or 'nenhuma'}"
    )
    if obrigatorios_faltantes:
        sinais += f"; obrigatorios_faltantes={','.join(obrigatorios_faltantes)}"
    if is_jd:
        sinais += "; regua=JD"

    return StructureScore(
        promove=promove,
        quase=quase,
        score=score,
        limiar=limiar,
        categorias=categorias,
        obrigatorios_faltantes=obrigatorios_faltantes,
        categorias_faltantes=categorias_faltantes,
        sinais=sinais,
    )


def detect_species(text: str) -> tuple[str | None, list[str]]:
    checks: list[tuple[str, list[str]]] = [
        ("sindicancia", ["sindicancia"]),
        ("ipm", ["inquerito policial militar", " ipm", "ipm ", "portaria ipm"]),
        ("tc", ["termo circunstanciado", " tco", " tc "]),
        ("oficio", ["oficio", "oficio n", "oficio solicitando"]),
        ("despacho", ["despacho", "despacho de analise"]),
        ("parte", ["parte ", "parte n", "parte especial", "parte de"]),
        ("relatorio", ["relatorio"]),
        ("escala", ["escala"]),
        ("ata", [" ata ", "ata de"]),
    ]
    for especie, patterns in checks:
        matches = has_any(text, patterns)
        if matches:
            return especie, [f"especie={especie}"]
    return None, []


def detect_hierarchy(text: str) -> tuple[str | None, list[str]]:
    if has_any(text, ["lei complementar federal", "lei federal", "decreto-lei", "decreto lei"]):
        return "lei_federal", ["hierarquia=lei_federal"]
    if has_any(text, ["lei complementar estadual", "lei estadual"]):
        return "lei_estadual", ["hierarquia=lei_estadual"]
    if has_any(text, ["decreto estadual", "decreto federal", "decreto n", "re:decreto\\s+\\d"]):
        return "decreto", ["hierarquia=decreto"]
    if has_any(text, ["resolucao", "resolução"]):
        return "resolucao", ["hierarquia=resolucao"]
    if has_any(
        text,
        [
            "i-",
            "i ",
            "nota de instrucao",
            "nota de instrução",
            "ni pm",
            "norsop",
            "portaria",
            "bol g",
            "boletim geral",
            "diretriz",
            "manual",
            "regulamento",
        ],
    ):
        return "norma_interna", ["hierarquia=norma_interna"]
    return None, []


def classify_entry(entry: dict[str, Any]) -> Classification:
    section = str(entry.get("section") or "")
    arquivo = str(entry.get("arquivo") or "")
    texto = str(entry.get("texto") or "")
    error = entry.get("error")
    tipo = str(entry.get("tipo") or "")

    section_norm = normalize(section)
    arquivo_norm = normalize(arquivo)
    text_norm = normalize(texto[:8000])
    joined = f"{section_norm} {arquivo_norm} {text_norm}"

    sinais: list[str] = [f"pasta={section or 'raiz'}", f"tipo={tipo or 'sem_tipo'}"]
    if error:
        sinais.append(f"error={error}")
    if len(texto.strip()) < 150:
        sinais.append("texto_curto")

    especie, especie_sinais = detect_species(joined)
    sinais.extend(especie_sinais)

    norm_signals = has_any(
        joined,
        [
            "nota de instrucao",
            "nota de instrução",
            "instrucao policial militar",
            "instrucoes para",
            "i-",
            "ni pm",
            "pm3_",
            "rdpm",
            "r-200",
            "codigo penal",
            "codigo de processo penal",
            "codigo penal militar",
            "cppm",
            "ctb",
            "eca",
            "lei maria da penha",
            "lei complementar",
            "decreto",
            "resolucao",
            "portaria",
            "regulamento",
            "manual",
            "norma",
            "norsop",
        ],
    )
    model_signals = has_any(
        joined,
        [
            "modelo",
            "modelos",
            "minuta",
            "exemplo",
            "oficio solicitando",
            "despacho de analise",
            "conclusao, despacho e data",
            "portaria instaurada",
        ],
    )
    jurisprudence_signals = has_any(
        joined,
        [
            "jurisprudencia",
            "supremo tribunal federal",
            "superior tribunal de justica",
            "stf",
            "stj",
            "sumula",
            "habeas corpus",
            "recurso especial",
            "recurso extraordinario",
        ],
    )
    procedural_signals = has_any(
        joined,
        [
            "procedimento operacional",
            "passo a passo",
            "checklist",
            "fluxograma",
            "tutorial",
            "roteiro",
            "procedimento",
        ],
    )

    if section_norm == "notebooklm":
        sinais.append("notebooklm=nunca_modelo")

    hierarchy, hierarchy_signals = detect_hierarchy(joined)
    sinais.extend(hierarchy_signals)

    natureza = "OUTRO"
    high_reason = False

    if section_norm == "normas":
        natureza = "NORMA"
        high_reason = bool(norm_signals or hierarchy)
        sinais.append("secao_normas")
    elif section_norm == "notebooklm":
        natureza = "NORMA" if norm_signals or hierarchy else "OUTRO"
        high_reason = bool(norm_signals or hierarchy)
    elif jurisprudence_signals and not norm_signals:
        natureza = "JURISPRUDENCIA"
        high_reason = True
        sinais.append("jurisprudencia_nome_texto")
    elif model_signals and section_norm != "notebooklm":
        natureza = "MODELO_DE_REDACAO"
        high_reason = True
        sinais.append("modelo_nome_texto")
    elif norm_signals and not model_signals:
        natureza = "NORMA"
        high_reason = section_norm in {"jd", "p1", "p2", "p3", "p4", "p5"} or bool(hierarchy)
        sinais.append("norma_nome_texto")
    elif procedural_signals:
        natureza = "PROCEDIMENTAL"
        high_reason = True
        sinais.append("procedimento_nome_texto")
    elif section_norm in {"jd", "p1", "p2", "p3", "p4", "p5"} and especie:
        natureza = "PRECEDENTE"
        high_reason = True
        sinais.append("pasta_operacional_com_especie")

    conflicts = 0
    if norm_signals and model_signals and section_norm != "normas":
        conflicts += 1
        sinais.append("conflito_norma_modelo")
    if jurisprudence_signals and norm_signals:
        conflicts += 1
        sinais.append("conflito_jurisprudencia_norma")

    low = bool(error) or len(texto.strip()) < 150 or conflicts > 0 or not high_reason
    confianca = "baixa" if low else "alta"

    if natureza != "NORMA":
        hierarchy = None

    if confianca == "baixa":
        return Classification(
            natureza_index="NAO_CLASSIFICADO",
            especie_index=None,
            hierarquia=None,
            confianca="baixa",
            natureza_sugerida=natureza,
            especie_sugerida=especie,
            sinais=sinais,
        )

    return Classification(
        natureza_index=natureza,
        especie_index=especie or ("outro" if natureza in {"MODELO_DE_REDACAO", "PRECEDENTE"} else None),
        hierarquia=hierarchy,
        confianca="alta",
        natureza_sugerida=natureza,
        especie_sugerida=especie,
        sinais=sinais,
    )


def apply_classification(entry: dict[str, Any], cls: Classification) -> None:
    if entry.get("classificacao_origem") == "humana":
        return
    entry["natureza"] = cls.natureza_index
    entry["especie"] = cls.especie_index
    entry["vigencia"] = "nao_avaliado"
    entry["hierarquia"] = cls.hierarquia
    entry["fonte"] = None
    entry["classificacao_confianca"] = cls.confianca
    entry["classificacao_origem"] = "heuristica"
    entry["classificacao_sinais"] = "; ".join(cls.sinais[:8])


def sample_text(texto: str, limit: int = 300) -> str:
    cleaned = re.sub(r"\s+", " ", texto or "").strip()
    return cleaned[:limit]


def write_review_csv(rows: list[dict[str, str]], path: Path) -> None:
    fieldnames = [
        "chave",
        "nome",
        "pasta",
        "trecho_amostra",
        "natureza_sugerida",
        "especie_sugerida",
        "confianca",
        "sinais",
        "natureza_correta",
        "especie_correta",
        "observacao",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def is_excluded_dir(rel_path: Path) -> bool:
    rel_norm = Path(normalize(rel_to_posix(rel_path)))
    for prefix in EXCLUDED_DIR_PREFIXES:
        prefix_norm = Path(normalize(rel_to_posix(prefix)))
        try:
            rel_norm.relative_to(prefix_norm)
            return True
        except ValueError:
            continue
    return False


def exclusion_reason(rel_path: Path) -> str:
    name = rel_path.name
    if name.startswith("~$"):
        return "temporario_office"
    if name.lower() in EXCLUDED_FILE_NAMES:
        return "arquivo_excluido_nome"
    if is_excluded_dir(rel_path.parent):
        return "pasta_excluida"
    ext = rel_path.suffix.lower()
    if ext in EXCLUDED_EXTENSIONS:
        return f"extensao_excluida:{ext}"
    return "nao_indexado_sem_regra_explicita"


def looks_candidate(rel_path: Path) -> bool:
    ext = rel_path.suffix.lower()
    if ext not in DOC_EXTENSIONS:
        return False
    haystack = normalize(rel_to_posix(rel_path))
    patterns = [
        "norma",
        "instrucao",
        "instrução",
        "modelo",
        "oficio",
        "ofício",
        "parte",
        "despacho",
        "portaria",
        "relatorio",
        "relatório",
        "manual",
        "regulamento",
        "rdpm",
        "r-200",
        "boletim",
        "procedimento",
    ]
    return bool(has_any(haystack, patterns))


def generate_non_indexed_report(corpus_root: Path, original_data: list[dict[str, Any]], path: Path) -> Counter:
    indexed = {key_for(entry) for entry in original_data}
    rows: list[dict[str, Any]] = []
    reason_counts: Counter = Counter()

    for file_path in corpus_root.rglob("*"):
        if not file_path.is_file():
            continue
        rel_path = file_path.relative_to(corpus_root)
        rel_key = rel_to_posix(rel_path)
        if rel_key in indexed:
            continue
        reason = exclusion_reason(rel_path)
        reason_counts[reason] += 1
        rows.append(
            {
                "caminho_relativo": rel_key,
                "extensao": rel_path.suffix.lower(),
                "tamanho_kb": f"{file_path.stat().st_size / 1024:.1f}",
                "motivo_exclusao": reason,
                "candidato": "sim" if looks_candidate(rel_path) else "nao",
            }
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["caminho_relativo", "extensao", "tamanho_kb", "motivo_exclusao", "candidato"],
        )
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["caminho_relativo"]))

    return reason_counts


def verify_aditivity(before: list[dict[str, Any]], after: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    messages: list[str] = []
    ok = True
    if len(after) < len(before):
        ok = False
        messages.append(f"FALHA: entradas diminuiram: antes={len(before)} depois={len(after)}")
    else:
        messages.append(f"OK: entradas nao diminuiram: antes={len(before)} depois={len(after)}")

    before_by_key = {key_for(entry): entry for entry in before}
    after_by_key = {key_for(entry): entry for entry in after}

    missing = sorted(set(before_by_key) - set(after_by_key))
    if missing:
        ok = False
        messages.append(f"FALHA: {len(missing)} chaves originais ausentes.")
    else:
        messages.append("OK: todas as chaves section/arquivo originais permanecem.")

    changed_original_fields = 0
    unexpected_extra_fields: Counter = Counter()
    for key, original in before_by_key.items():
        current = after_by_key.get(key)
        if current is None:
            continue
        for field in ORIGINAL_FIELDS:
            if original.get(field) != current.get(field):
                changed_original_fields += 1
        extras = set(current) - set(original)
        for extra in extras - METADATA_FIELDS:
            unexpected_extra_fields[extra] += 1

    if changed_original_fields:
        ok = False
        messages.append(f"FALHA: {changed_original_fields} campos originais tiveram valor alterado.")
    else:
        messages.append("OK: nenhum campo original section/arquivo/tipo/texto/error foi alterado.")

    if unexpected_extra_fields:
        ok = False
        extras = ", ".join(f"{k}={v}" for k, v in sorted(unexpected_extra_fields.items()))
        messages.append(f"FALHA: campos extras inesperados: {extras}")
    else:
        messages.append("OK: as unicas mudancas estruturais sao campos novos de metadados.")

    vigencia_ok = sum(1 for entry in after if entry.get("vigencia") == "nao_avaliado")
    if vigencia_ok != len(after):
        ok = False
        messages.append(f"FALHA: vigencia nao_avaliado em {vigencia_ok}/{len(after)} entradas.")
    else:
        messages.append(f"OK: vigencia='nao_avaliado' em 100% ({len(after)}/{len(after)}).")

    return ok, messages


def write_summary(
    path: Path,
    final_data: list[dict[str, Any]],
    review_rows: list[dict[str, str]],
    local_backup: Path,
    drive_backup: Path,
    verify_messages: list[str],
    non_indexed_counts: Counter,
    non_indexed_candidates: int,
    reimport_test_summary: str,
    py_compile_summary: str,
) -> None:
    natureza_counts = Counter(entry.get("natureza") for entry in final_data)
    especie_counts = Counter(str(entry.get("especie")) for entry in final_data)
    confidence_counts = Counter(entry.get("classificacao_confianca") for entry in final_data)
    origin_counts = Counter(entry.get("classificacao_origem") for entry in final_data)

    def md_counts(counter: Counter) -> str:
        lines = ["| Valor | Quantidade |", "|---|---:|"]
        for key, value in sorted(counter.items(), key=lambda item: str(item[0])):
            lines.append(f"| {key} | {value} |")
        return "\n".join(lines)

    non_indexed_lines = ["| Motivo | Quantidade |", "|---|---:|"]
    for key, value in sorted(non_indexed_counts.items()):
        non_indexed_lines.append(f"| {key} | {value} |")

    verify_block = "\n".join(verify_messages)
    non_indexed_block = "\n".join(non_indexed_lines)

    content = f"""# Metadados 8.2

Sprint 8.2 executado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}.

## Resultado executivo

- Entradas no indice: {len(final_data)}
- Alta confianca: {confidence_counts.get("alta", 0)}
- Baixa confianca: {confidence_counts.get("baixa", 0)}
- Linhas geradas para revisao humana: {len(review_rows)}
- Vigencia: `nao_avaliado` em 100% das entradas
- Backup local: `{local_backup}`
- Backup Drive: `{drive_backup}`

## Contagem por natureza

{md_counts(natureza_counts)}

## Contagem por especie

{md_counts(especie_counts)}

## Contagem por confianca

{md_counts(confidence_counts)}

## Contagem por origem

{md_counts(origin_counts)}

## Prova de aditividade

```
{verify_block}
```

## Reimportador

{reimport_test_summary}

## Relatorio dos arquivos nao indexados

- Arquivo: `saidas/relatorio_193_nao_indexados.csv`
- Candidatos por nome/extensao: {non_indexed_candidates}

{non_indexed_block}

## Compilacao

```
{py_compile_summary}
```

## Observacoes

- Entradas de baixa confianca foram gravadas no indice como `natureza=NAO_CLASSIFICADO` e `especie=null`.
- As sugestoes da heuristica para baixa confianca foram preservadas apenas em `saidas/revisao_classificacao.csv`.
- O corpus fisico no Drive nao foi reindexado, movido, renomeado ou editado.
"""
    path.write_text(content, encoding="utf-8")


def classify_index(index_path: Path, corpus_root: Path) -> dict[str, Any]:
    SAIDAS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    original_data = load_index(index_path)
    original_snapshot = json.loads(json.dumps(original_data, ensure_ascii=False))
    local_backup, drive_backup = create_backups(index_path, corpus_root)

    review_rows: list[dict[str, str]] = []
    classified_data = json.loads(json.dumps(original_data, ensure_ascii=False))

    for entry in classified_data:
        cls = classify_entry(entry)
        apply_classification(entry, cls)
        if cls.confianca == "baixa":
            review_rows.append(
                {
                    "chave": key_for(entry),
                    "nome": str(entry.get("arquivo") or ""),
                    "pasta": str(entry.get("section") or ""),
                    "trecho_amostra": sample_text(str(entry.get("texto") or "")),
                    "natureza_sugerida": cls.natureza_sugerida,
                    "especie_sugerida": cls.especie_sugerida or "",
                    "confianca": cls.confianca,
                    "sinais": "; ".join(cls.sinais[:8]),
                    "natureza_correta": "",
                    "especie_correta": "",
                    "observacao": "",
                }
            )

    review_csv = SAIDAS_DIR / "revisao_classificacao.csv"
    write_review_csv(review_rows, review_csv)

    report_csv = SAIDAS_DIR / "relatorio_193_nao_indexados.csv"
    non_indexed_counts = generate_non_indexed_report(corpus_root, original_snapshot, report_csv)
    non_indexed_candidates = count_candidates(report_csv)

    save_index_atomic(index_path, classified_data)
    final_data = load_index(index_path)
    verify_ok, verify_messages = verify_aditivity(original_snapshot, final_data)
    if not verify_ok:
        raise RuntimeError("Falha na verificacao de aditividade:\n" + "\n".join(verify_messages))

    return {
        "final_data": final_data,
        "review_rows": review_rows,
        "review_csv": review_csv,
        "report_csv": report_csv,
        "local_backup": local_backup,
        "drive_backup": drive_backup,
        "verify_messages": verify_messages,
        "non_indexed_counts": non_indexed_counts,
        "non_indexed_candidates": non_indexed_candidates,
    }


def load_review_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Planilha de revisao nao encontrada: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def verify_second_pass(
    before: list[dict[str, Any]],
    after: list[dict[str, Any]],
) -> tuple[bool, list[str], list[str]]:
    messages: list[str] = []
    errors: list[str] = []

    before_by_key = {key_for(entry): entry for entry in before}
    after_by_key = {key_for(entry): entry for entry in after}

    if len(before) == len(after):
        messages.append(f"OK: total de entradas preservado: {len(after)}")
    else:
        errors.append(f"FALHA: total mudou: antes={len(before)} depois={len(after)}")

    missing = sorted(set(before_by_key) - set(after_by_key))
    if not missing:
        messages.append("OK: todas as chaves originais permanecem.")
    else:
        errors.append(f"FALHA: {len(missing)} chaves sumiram.")

    original_changed = 0
    human_changed = 0
    unexpected_changes: list[str] = []
    protected_changed: list[str] = []
    promoted_keys: list[str] = []

    protected_keys = {
        key
        for key, entry in before_by_key.items()
        if entry.get("classificacao_confianca") == "alta"
        and entry.get("natureza") in {"MODELO_DE_REDACAO", "PRECEDENTE"}
    }
    protected_counts = Counter(before_by_key[key].get("natureza") for key in protected_keys)

    for key, original in before_by_key.items():
        current = after_by_key.get(key)
        if current is None:
            continue

        for field in ORIGINAL_FIELDS:
            if original.get(field) != current.get(field):
                original_changed += 1

        if original == current:
            continue

        if original.get("classificacao_origem") == "humana":
            human_changed += 1

        if key in protected_keys:
            protected_changed.append(key)
            continue

        changed_fields = {field for field in set(original) | set(current) if original.get(field) != current.get(field)}
        if not changed_fields <= METADATA_FIELDS:
            unexpected_changes.append(f"{key}: campos nao metadata alterados {sorted(changed_fields - METADATA_FIELDS)}")
            continue

        allowed = (
            original.get("classificacao_confianca") == "baixa"
            and original.get("classificacao_origem") != "humana"
            and current.get("classificacao_confianca") == "alta"
            and current.get("classificacao_origem") == "heuristica"
            and current.get("natureza") == "MODELO_PRECEDENTE"
            and current.get("vigencia") == "nao_avaliado"
        )
        if allowed:
            promoted_keys.append(key)
        else:
            unexpected_changes.append(f"{key}: mudanca fora do padrao baixa->MODELO_PRECEDENTE")

    if original_changed == 0:
        messages.append("OK: nenhum campo original section/arquivo/tipo/texto/error foi alterado.")
    else:
        errors.append(f"FALHA: {original_changed} campos originais foram alterados.")

    if human_changed == 0:
        messages.append("OK: nenhuma entrada classificacao_origem=humana foi sobrescrita.")
    else:
        errors.append(f"FALHA: {human_changed} entradas humanas foram alteradas.")

    if not protected_changed:
        messages.append(
            "OK: altas MODELO_DE_REDACAO/PRECEDENTE permaneceram identicas "
            f"({protected_counts.get('MODELO_DE_REDACAO', 0)} MODELO_DE_REDACAO; "
            f"{protected_counts.get('PRECEDENTE', 0)} PRECEDENTE)."
        )
    else:
        errors.append(f"FALHA: {len(protected_changed)} altas protegidas foram alteradas.")

    if not unexpected_changes:
        messages.append(f"OK: unicas mudancas foram {len(promoted_keys)} promocao(oes) baixa->MODELO_PRECEDENTE.")
    else:
        errors.extend([f"FALHA: {item}" for item in unexpected_changes[:20]])
        if len(unexpected_changes) > 20:
            errors.append(f"FALHA: mais {len(unexpected_changes) - 20} mudancas inesperadas omitidas.")

    vigencia_ok = sum(1 for entry in after if entry.get("vigencia") == "nao_avaliado")
    if vigencia_ok == len(after):
        messages.append(f"OK: vigencia='nao_avaliado' em 100% ({len(after)}/{len(after)}).")
    else:
        errors.append(f"FALHA: vigencia nao_avaliado em {vigencia_ok}/{len(after)}.")

    return not errors, messages, errors


def write_second_pass_summary(
    path: Path,
    promoted_rows: list[dict[str, str]],
    near_rows: list[dict[str, str]],
    review_rows: list[dict[str, str]],
    local_backup: Path,
    drive_backup: Path,
    verify_messages: list[str],
    py_compile_summary: str,
    final_sha256: str,
) -> None:
    promoted_by_section = Counter(row["pasta"] or "[raiz]" for row in promoted_rows)
    remaining_by_section = Counter(row["pasta"] or "[raiz]" for row in review_rows)
    remaining_by_section_nature = Counter(
        (row["pasta"] or "[raiz]", row["natureza_sugerida"] or "[vazio]")
        for row in review_rows
    )

    def simple_table(counter: Counter, col1: str) -> str:
        lines = [f"| {col1} | Quantidade |", "|---|---:|"]
        for key, value in sorted(counter.items(), key=lambda item: (-item[1], str(item[0]))):
            lines.append(f"| {key} | {value} |")
        return "\n".join(lines)

    remaining_lines = ["| Pasta | Sugestao | Quantidade |", "|---|---|---:|"]
    for (section, nature), value in sorted(
        remaining_by_section_nature.items(),
        key=lambda item: (-item[1], item[0][0], item[0][1]),
    ):
        remaining_lines.append(f"| {section} | {nature} | {value} |")

    near_lines = [
        "| Chave | Pasta | Score | Faltou | Categorias presentes |",
        "|---|---|---:|---|---|",
    ]
    if near_rows:
        for row in near_rows:
            near_lines.append(
                "| {chave} | {pasta} | {score} | {faltou} | {categorias} |".format(**row)
            )
    else:
        near_lines.append("| - | - | - | - | - |")

    section_content = f"""## Patch cabeça+cauda

Executado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}.

### Resultado executivo

- Novas promoções para `MODELO_PRECEDENTE`: {len(promoted_rows)}
- Linhas restantes na revisão manual: {len(review_rows)}
- Entradas que ficaram a um marcador do limiar: {len(near_rows)}
- Backup local: `{local_backup}`
- Backup Drive: `{drive_backup}`
- SHA-256 do índice final: `{final_sha256}`

### Promovidas por pasta

{simple_table(promoted_by_section, "Pasta")}

### Revisão restante por pasta

{simple_table(remaining_by_section, "Pasta")}

### Revisão restante por pasta e sugestão

{chr(10).join(remaining_lines)}

### Quase promovidas

Entradas que ficaram a exatamente um marcador do limiar de promoção, ou bateram o limiar mas falharam em um obrigatório.

{chr(10).join(near_lines)}

### Prova de aditividade pura

```
{chr(10).join(verify_messages)}
```

### Compilação

```
{py_compile_summary}
```

### Observações

- O patch analisou cabeça de 12.000 caracteres e cauda de 6.000 caracteres do texto já indexado.
- As réguas foram mantidas: P1-P5 com 4/6 e JD com 5/6.
- O corpus físico não foi reindexado, movido, renomeado ou editado.
"""

    if path.exists():
        existing = path.read_text(encoding="utf-8")
        marker = "\n## Patch cabeça+cauda\n"
        if marker in existing:
            existing = existing.split(marker, 1)[0].rstrip() + "\n"
        content = existing.rstrip() + "\n\n" + section_content
    else:
        content = f"""# Segunda Passada 8.3

Sprint 8.3 executado em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}.

## Resultado executivo

- Entradas promovidas para `MODELO_PRECEDENTE`: {len(promoted_rows)}
- Linhas restantes na revisão manual: {len(review_rows)}
- Entradas que ficaram a um marcador do limiar: {len(near_rows)}
- Backup local: `{local_backup}`
- Backup Drive: `{drive_backup}`

## Promovidas por pasta

{simple_table(promoted_by_section, "Pasta")}

## Revisão restante por pasta

{simple_table(remaining_by_section, "Pasta")}

## Revisão restante por pasta e sugestão

{chr(10).join(remaining_lines)}

## Quase promovidas

Entradas que ficaram a exatamente um marcador do limiar de promoção, ou bateram o limiar mas falharam em um obrigatório.

{chr(10).join(near_lines)}

## Prova de aditividade pura

```
{chr(10).join(verify_messages)}
```

## Compilacao

```
{py_compile_summary}
```

## Observacoes

- As 20 entradas `MODELO_DE_REDACAO` e 38 `PRECEDENTE` já em alta confiança permaneceram intocadas.
- A segunda passada leu apenas o texto já indexado e não reabriu arquivos do corpus físico.
- Entradas não promovidas continuam em `saidas/revisao_classificacao.csv` para revisão humana.
"""
    path.write_text(content, encoding="utf-8")


def run_second_pass(index_path: Path, review_csv: Path, corpus_root: Path) -> dict[str, Any]:
    original_data = load_index(index_path)
    original_snapshot = json.loads(json.dumps(original_data, ensure_ascii=False))
    review_rows = load_review_rows(review_csv)
    review_by_key = {row.get("chave", ""): row for row in review_rows}

    local_backup, drive_backup = create_backups(index_path, corpus_root)
    updated_data = json.loads(json.dumps(original_data, ensure_ascii=False))
    promoted_rows: list[dict[str, str]] = []
    near_rows: list[dict[str, str]] = []
    promoted_keys: set[str] = set()

    for entry in updated_data:
        key = key_for(entry)
        review_row = review_by_key.get(key)
        if not review_row:
            continue
        if review_row.get("natureza_sugerida") != "MODELO_DE_REDACAO":
            continue
        if entry.get("classificacao_confianca") != "baixa":
            continue
        if entry.get("classificacao_origem") == "humana":
            continue

        score = detect_i7pm_structure(entry)
        if score.promove:
            especie = normalize_species(review_row.get("especie_sugerida") or "")
            if especie is None:
                detected, _ = detect_species(
                    normalize(f"{entry.get('section') or ''} {entry.get('arquivo') or ''} {entry.get('texto') or ''}")
                )
                especie = detected or "outro"

            entry["natureza"] = "MODELO_PRECEDENTE"
            entry["especie"] = especie
            entry["vigencia"] = "nao_avaliado"
            entry["hierarquia"] = None
            entry["fonte"] = entry.get("fonte")
            entry["classificacao_confianca"] = "alta"
            entry["classificacao_origem"] = "heuristica"
            entry["classificacao_sinais"] = score.sinais
            promoted_keys.add(key)
            promoted_rows.append(
                {
                    "chave": key,
                    "pasta": str(entry.get("section") or ""),
                    "nome": str(entry.get("arquivo") or ""),
                    "score": str(score.score),
                    "categorias": ",".join(score.categorias),
                }
            )
        elif score.quase:
            missing = score.obrigatorios_faltantes or score.categorias_faltantes
            near_rows.append(
                {
                    "chave": key,
                    "pasta": str(entry.get("section") or "[raiz]"),
                    "score": f"{score.score}/{score.limiar}",
                    "faltou": ",".join(missing[:4]) or "-",
                    "categorias": ",".join(score.categorias) or "-",
                }
            )

    remaining_review_rows = [row for row in review_rows if row.get("chave") not in promoted_keys]
    write_review_csv(remaining_review_rows, review_csv)
    save_index_atomic(index_path, updated_data)

    final_data = load_index(index_path)
    final_sha256 = file_sha256(index_path)
    verify_ok, verify_messages, verify_errors = verify_second_pass(original_snapshot, final_data)
    if not verify_ok:
        raise RuntimeError("Falha na verificacao da segunda passada:\n" + "\n".join(verify_errors))

    py_compile_summary = run_py_compile()
    write_second_pass_summary(
        DOCS_DIR / "SEGUNDA_PASSADA_8_3.md",
        promoted_rows,
        near_rows,
        remaining_review_rows,
        local_backup,
        drive_backup,
        verify_messages,
        py_compile_summary,
        final_sha256,
    )

    return {
        "final_data": final_data,
        "promoted_rows": promoted_rows,
        "near_rows": near_rows,
        "review_rows": remaining_review_rows,
        "local_backup": local_backup,
        "drive_backup": drive_backup,
        "verify_messages": verify_messages,
        "final_sha256": final_sha256,
    }


def count_candidates(csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        return sum(1 for row in csv.DictReader(f) if row.get("candidato") == "sim")


def normalize_species(value: str) -> str | None:
    value = normalize(value.strip())
    if not value or value in {"null", "none", "nulo"}:
        return None
    if value not in ESPECIES:
        raise ValueError(f"especie invalida: {value}")
    return value


def reimport_review(index_path: Path, csv_path: Path, make_backup: bool = True) -> dict[str, int]:
    data = load_index(index_path)
    corpus_root = Path(Segredos().get("corpus")["path"])
    if make_backup:
        create_backups(index_path, corpus_root)

    by_key = {key_for(entry): entry for entry in data}
    counts = Counter()

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            chave = (row.get("chave") or "").strip()
            natureza = normalize((row.get("natureza_correta") or "").strip()).upper()
            especie_raw = (row.get("especie_correta") or "").strip()
            observacao = (row.get("observacao") or "").strip()

            if not chave or not natureza:
                counts["linhas_vazias_ou_incompletas"] += 1
                continue

            entry = by_key.get(chave)
            if entry is None:
                counts["chave_nao_encontrada"] += 1
                continue

            if natureza == "EXCLUIR":
                if entry.get("classificacao_origem") == "humana":
                    counts["ja_humana_preservada"] += 1
                    continue
                data.remove(entry)
                del by_key[chave]
                counts["excluidas"] += 1
                continue

            if natureza not in NATUREZAS:
                counts["natureza_invalida"] += 1
                continue
            try:
                especie = normalize_species(especie_raw)
            except ValueError:
                counts["especie_invalida"] += 1
                continue
            if entry.get("classificacao_origem") == "humana":
                counts["ja_humana_preservada"] += 1
                continue

            entry["natureza"] = natureza
            entry["especie"] = especie
            entry["vigencia"] = "nao_avaliado"
            entry["hierarquia"] = entry.get("hierarquia") if natureza == "NORMA" else None
            entry["fonte"] = entry.get("fonte")
            entry["classificacao_confianca"] = "alta"
            entry["classificacao_origem"] = "humana"
            signal = "revisao_humana"
            if observacao:
                signal += f"; observacao={observacao[:120]}"
            entry["classificacao_sinais"] = signal
            counts["aplicadas"] += 1

    save_index_atomic(index_path, data)
    return dict(counts)


def create_reimport_test(classified_data: list[dict[str, Any]]) -> str:
    test_index = SAIDAS_DIR / "reimport_teste_index.json"
    test_csv = SAIDAS_DIR / "revisao_classificacao_exemplo.csv"
    candidates = [
        entry
        for entry in classified_data
        if entry.get("classificacao_confianca") == "baixa"
    ][:3]
    if not candidates:
        return "Teste de reimportacao nao executado: nao houve entradas de baixa confianca."

    test_index.write_text(json.dumps(classified_data, ensure_ascii=False, indent=2), encoding="utf-8")
    rows = []
    for entry in candidates:
        rows.append(
            {
                "chave": key_for(entry),
                "nome": entry.get("arquivo") or "",
                "pasta": entry.get("section") or "",
                "trecho_amostra": sample_text(str(entry.get("texto") or "")),
                "natureza_sugerida": entry.get("natureza") or "",
                "especie_sugerida": entry.get("especie") or "",
                "confianca": entry.get("classificacao_confianca") or "",
                "sinais": entry.get("classificacao_sinais") or "",
                "natureza_correta": "OUTRO",
                "especie_correta": "outro",
                "observacao": "teste automatico do reimportador",
            }
        )
    write_review_csv(rows, test_csv)
    first = reimport_review(test_index, test_csv, make_backup=False)
    second = reimport_review(test_index, test_csv, make_backup=False)
    return (
        f"Reimportador testado com `{test_csv}` em copia temporaria `{test_index}`. "
        f"Primeira execucao: {first}. Segunda execucao idempotente: {second}."
    )


def run_py_compile() -> str:
    import py_compile

    targets = [
        _NUCLEO_DESP / "classificar_corpus.py",
    ]
    lines = []
    for target in targets:
        py_compile.compile(str(target), doraise=True)
        lines.append(f"OK py_compile {target}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Classifica metadados do corpus da Despachadora.")
    parser.add_argument("--index", type=Path, default=INDEX_FILE, help="Caminho do corpus_index.json.")
    parser.add_argument("--reimport", type=Path, help="CSV revisado para aplicar ao indice.")
    parser.add_argument(
        "--segunda-passada",
        action="store_true",
        help="Promove baixas com estrutura I-7-PM inequivoca para MODELO_PRECEDENTE.",
    )
    parser.add_argument(
        "--review-csv",
        type=Path,
        default=SAIDAS_DIR / "revisao_classificacao.csv",
        help="Planilha de revisao usada pela segunda passada.",
    )
    args = parser.parse_args()

    if args.reimport:
        counts = reimport_review(args.index, args.reimport, make_backup=True)
        print("REIMPORTACAO CONCLUIDA")
        for key, value in sorted(counts.items()):
            print(f"  {key}: {value}")
        print(f"Indice salvo em: {args.index}")
        return 0

    corpus_root = Path(Segredos().get("corpus")["path"])
    if args.segunda_passada:
        result = run_second_pass(args.index, args.review_csv, corpus_root)
        print("SEGUNDA PASSADA CONCLUIDA")
        print(f"  Entradas no indice: {len(result['final_data'])}")
        print(f"  Promovidas para MODELO_PRECEDENTE: {len(result['promoted_rows'])}")
        print(f"  Restantes na planilha: {len(result['review_rows'])}")
        print(f"  Quase promovidas: {len(result['near_rows'])}")
        print(f"  Backup local: {result['local_backup']}")
        print(f"  Backup Drive: {result['drive_backup']}")
        print(f"  Resumo: {DOCS_DIR / 'SEGUNDA_PASSADA_8_3.md'}")
        print("\nPROVA DE ADITIVIDADE PURA")
        for message in result["verify_messages"]:
            print(f"  {message}")
        return 0

    result = classify_index(args.index, corpus_root)
    reimport_summary = create_reimport_test(result["final_data"])
    py_compile_summary = run_py_compile()
    write_summary(
        DOCS_DIR / "METADADOS_8_2.md",
        result["final_data"],
        result["review_rows"],
        result["local_backup"],
        result["drive_backup"],
        result["verify_messages"],
        result["non_indexed_counts"],
        result["non_indexed_candidates"],
        reimport_summary,
        py_compile_summary,
    )

    confidence_counts = Counter(entry.get("classificacao_confianca") for entry in result["final_data"])
    print("CLASSIFICACAO CONCLUIDA")
    print(f"  Entradas no indice: {len(result['final_data'])}")
    print(f"  Alta confianca: {confidence_counts.get('alta', 0)}")
    print(f"  Baixa confianca: {confidence_counts.get('baixa', 0)}")
    print(f"  Planilha de revisao: {result['review_csv']}")
    print(f"  Relatorio nao indexados: {result['report_csv']}")
    print(f"  Backup local: {result['local_backup']}")
    print(f"  Backup Drive: {result['drive_backup']}")
    print(f"  Resumo: {DOCS_DIR / 'METADADOS_8_2.md'}")
    print("\nPROVA DE ADITIVIDADE")
    for message in result["verify_messages"]:
        print(f"  {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
