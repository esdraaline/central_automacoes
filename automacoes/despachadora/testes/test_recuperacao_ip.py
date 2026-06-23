#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regressão da recuperação da fonte autônoma de Investigação Preliminar."""

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(project_root / "automacoes" / "despachadora" / "nucleo_despachadora"))

from despachadora import (
    build_user_prompt,
    extract_keywords,
    normalizar_resposta_antes_validador,
    recover_chunks,
    validar_saida_despachadora,
)


manual_path = (
    project_root
    / "automacoes"
    / "despachadora"
    / "corpus_manual"
    / "Investigacao_Preliminar_I16.md"
)
raw = manual_path.read_text(encoding="utf-8")
partes = raw.replace("\r\n", "\n").split("---\n", 2)
texto = partes[2] if len(partes) == 3 else raw

corpus = [{
    "section": "corpus_manual",
    "arquivo": manual_path.name,
    "tipo": ".md",
    "texto": texto,
    "error": None,
    "natureza": "NORMA",
}]

expediente = """
Acidente sem vítima envolvendo viatura. O condutor não percebeu o obstáculo
durante a colisão. Submeto o dano ao erário para apuração e providências
administrativas, pois ainda faltam elementos para uma decisão definitiva.
"""

keywords = extract_keywords(expediente)
_, pool_f, pool_m = recover_chunks(corpus, keywords, expediente)
fontes = {item["_key"] for item in pool_f}
fonte_esperada = "corpus_manual/Investigacao_Preliminar_I16.md"

assert fonte_esperada in fontes, "Fonte autônoma de IP não foi recuperada."

prompt = build_user_prompt(
    [("entrada_texto", expediente, None)],
    pool_f,
    pool_m,
    False,
    keywords,
)
assert "10 (dez) dias" in prompt, "Prazo correto não chegou ao contexto do modelo."
assert "entrevistar as pessoas" in prompt, "Forma correta de instrução não chegou ao contexto."
assert "vedada a adoção de meios formais" in prompt, "Vedação da I-16-PM foi truncada."
assert "posto de coronel a capitão" in prompt, "Regra de competência do RDPM não chegou ao contexto."

decisao_com_lastro = """[FUNDAMENTO] Determino a instauração da Investigação Preliminar. [FONTE: corpus_manual/Investigacao_Preliminar_I16.md] [VERIFICAR: confirmar subordinação funcional dos envolvidos]."""
decisao_normalizada, _ = normalizar_resposta_antes_validador(decisao_com_lastro)
assert "Determino a instauração" in decisao_normalizada, "Normalizador apagou decisão de IP já fundamentada."

inferencias_orcamento = [
    "A ausência de orçamento consolidado inviabiliza a instauração imediata de Sindicância.",
    "A falta de laudo técnico impede a instauração de Sindicância neste momento.",
    "A inexistência de orçamento impossibilita a instauração imediata da Sindicância.",
]
for inferencia in inferencias_orcamento:
    texto_saneado, ajustes = normalizar_resposta_antes_validador(inferencia)
    assert "subsídio pendente" in texto_saneado, "Inferência sobre orçamento não foi saneada."
    assert "sem impedir automaticamente" in texto_saneado, "Saneamento não ficou cauteloso."
    assert ajustes, "Saneamento de orçamento não foi registrado."
    bloqueada, violacoes, _ = validar_saida_despachadora(
        texto_saneado,
        "Investigação Preliminar; prazo de 10 (dez) dias; entrevistas.",
        "",
    )
    assert not bloqueada, f"Texto saneado ainda foi bloqueado: {violacoes}"

termos_iniciais_incorretos = [
    "O prazo será de 10 dias, contados a partir da data de publicação deste despacho.",
    "O prazo será de 10 dias, contados ininterruptamente a partir da data de assinatura/publicação do despacho.",
    "O prazo será de 10 dias, contados a partir da data de recebimento do encargo.",
    "O prazo improrrogável de 10 dias será contado da publicação do despacho.",
    "Prazo: 10 dias, a contar da assinatura deste ato.",
]
for prazo_incorreto in termos_iniciais_incorretos:
    texto_saneado, ajustes = normalizar_resposta_antes_validador(
        "Investigação Preliminar. " + prazo_incorreto
    )
    assert "a partir do despacho de sua instauração" in texto_saneado
    assert ajustes

diligencia_indevida = """Investigação Preliminar.
* [PADRÃO] Determino ao encarregado que oficie ao setor de manutenção para obter laudo técnico e três orçamentos."""
diligencia_saneada, ajustes = normalizar_resposta_antes_validador(diligencia_indevida)
assert "já disponíveis" in diligencia_saneada
assert "oficie" not in diligencia_saneada.lower()
assert ajustes

rotulo_misto = """Investigação Preliminar.
[SUGESTÃO IA] O ressarcimento exige autorização escrita. [FUNDAMENTO] [FONTE: corpus_manual/Acidente_Viatura_Providencias.md]"""
rotulo_saneado, ajustes = normalizar_resposta_antes_validador(rotulo_misto)
assert "[SUGESTÃO IA]" not in rotulo_saneado
assert "[FUNDAMENTO]" in rotulo_saneado
assert ajustes

competencia_absoluta = """Investigação Preliminar.
[FUNDAMENTO] Cabimento da IP. [FONTE: corpus_manual/Investigacao_Preliminar_I16.md]
* DECIDO — competência direta do Cmt de Cia para instaurar a Investigação Preliminar."""
competencia_saneada, ajustes = normalizar_resposta_antes_validador(competencia_absoluta)
assert "competência direta" not in competencia_saneada.lower()
assert "condicionada à confirmação da subordinação funcional" in competencia_saneada
assert "[FONTE: corpus_manual/Investigacao_Preliminar_I16.md]" in competencia_saneada
assert ajustes

meios_formais_positivos = [
    "O encarregado deverá proceder à oitiva do condutor.",
    "O encarregado deverá realizar oitivas das testemunhas.",
    "O encarregado deverá lavrar Termo de Declaração.",
    "O encarregado deverá solicitar pedido de Exames Periciais.",
]
for meio_formal in meios_formais_positivos:
    saneado, ajustes = normalizar_resposta_antes_validador(
        "Investigação Preliminar.\n" + meio_formal
    )
    assert "oitiva" not in saneado.lower()
    assert "termo de declaração" not in saneado.lower()
    assert "pedido de exames periciais" not in saneado.lower()
    assert ajustes

proibicao_formal = """Investigação Preliminar.
[FUNDAMENTO] O encarregado não deve utilizar Termo de Declaração nem solicitar pedido de Exames Periciais. [FONTE: corpus_manual/Investigacao_Preliminar_I16.md]"""
proibicao_normalizada, _ = normalizar_resposta_antes_validador(proibicao_formal)
bloqueada, violacoes, _ = validar_saida_despachadora(
    proibicao_normalizada,
    "Investigação Preliminar; vedada a adoção de meios formais.",
    "",
)
assert not bloqueada, f"Descrição da proibição foi tratada como ordem positiva: {violacoes}"

print("RECUPERAÇÃO IP: OK")
