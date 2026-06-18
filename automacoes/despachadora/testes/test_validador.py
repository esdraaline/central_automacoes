#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testar_validador_8_6_b.py — Testes simulados do validador pós-Gemini
Sprint 8.6-b — Validação das regras D, E, G ajustadas.

Executa cenários que devem PASSAR e cenários que devem BLOQUEAR.
NÃO chama Gemini. NÃO altera corpus.
"""

import sys
from pathlib import Path

# Resolve o caminho do projeto a partir da localização deste arquivo
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "automacoes" / "despachadora" / "nucleo_despachadora"))

from despachadora import validar_saida_despachadora

# Contexto normativo simulado contendo SV11 e Súmula 473
CTX_NORMATIVO = """
[FONTE: corpus_manual/Sumula_Vinculante_11_Algemas.md]
Súmula Vinculante nº 11, do Supremo Tribunal Federal (STF):
"Só é lícito o uso de algemas em caso de resistência e de fundado receio de fuga
ou de perigo à integridade física própria ou alheia, por parte do preso ou de
terceiros, justificada a excepcionalidade por escrito."

[FONTE: corpus_manual/Sumula_473_Autotutela.md]
Súmula 473 do STF: A administração pode anular seus próprios atos, quando eivados
de vícios que os tornem ilegais.

[FONTE: corpus_manual/Competencia_IPM.md]
Competência para IPM: delegação do Cmt de Batalhão. O Cmt de Cia elabora Parte
propondo a instauração. incompetência da autoridade instauradora gera nulidade.
"""

CTX_MODELOS = """
[FONTE: JD/2025/Modelo_Despacho.pdf]
Modelo de despacho padrão da 5ª Cia PM.
"""


def run_test(name, resposta, expect_block, ctx_norm=CTX_NORMATIVO, ctx_mod=CTX_MODELOS):
    bloqueada, violacoes, alertas = validar_saida_despachadora(resposta, ctx_norm, ctx_mod)
    status = "BLOQUEADO" if bloqueada else ("ALERTA" if alertas else "OK")
    passed = (bloqueada == expect_block)
    marker = "✅" if passed else "❌"
    print(f"  {marker} [{status:>9s}] {name}")
    if not passed:
        if violacoes:
            for v in violacoes:
                print(f"       VIOLAÇÃO: {v[:120]}")
        if alertas:
            for a in alertas:
                print(f"       ALERTA: {a[:120]}")
    return passed


results = []

print("=" * 70)
print("CENÁRIOS QUE DEVEM PASSAR (não bloquear)")
print("=" * 70)

# 1. [PADRÃO] factual/cauteloso com CTB
results.append(run_test(
    "PADRÃO factual com CTB e expressão cautelosa",
    """**2. ANÁLISE JURÍDICA**

[PADRÃO] **Situação da vítima civil (falta de CNH compatível):** A suspeita de falta de CNH compatível por parte do civil constitui possível infração ao CTB, ponto que deve ser verificado junto aos documentos de trânsito apresentados.

**4. TEXTO PRONTO**

Texto pronto sem termos sensíveis.""",
    expect_block=False
))

# 2. Cabeçalho protocolar com "incompetência"
results.append(run_test(
    "Cabeçalho protocolar com incompetência",
    """**2. ANÁLISE JURÍDICA**

A incompetência da autoridade instauradora foi identificada. [FUNDAMENTO] [FONTE: corpus_manual/Competencia_IPM.md]

**4. TEXTO PRONTO**

Assunto: Remessa de autos de IPM por incompetência da autoridade instauradora.

1. Considerando que o militar pertence a outra subunidade, submeto à análise superior quanto ao fundamento aplicável.""",
    expect_block=False
))

# 3. Referência com IPM em cabeçalho
results.append(run_test(
    "Referência com IPM em cabeçalho protocolar",
    """**2. ANÁLISE JURÍDICA**

Análise simples sem termos sensíveis.

**4. TEXTO PRONTO**

Referência: IPM instaurado para apuração de uso irregular de viatura.

1. Texto cauteloso sem conclusão definitiva.""",
    expect_block=False
))

# 4. Texto Pronto com cabeçalho + corpo cauteloso [VERIFICAR]
results.append(run_test(
    "Cabeçalho + corpo cauteloso com VERIFICAR",
    """**2. ANÁLISE JURÍDICA**

Análise geral sem termos sensíveis.

**4. TEXTO PRONTO**

Assunto: Remessa por incompetência da autoridade instauradora.

1. Diante dos fatos narrados, a competência da autoridade instauradora merece ser verificada. [VERIFICAR: confirmar competência junto ao Batalhão]""",
    expect_block=False
))

print()
print("=" * 70)
print("CENÁRIOS QUE DEVEM BLOQUEAR")
print("=" * 70)

# 5. [PADRÃO] mascarando conclusão jurídica definitiva
results.append(run_test(
    "PADRÃO mascarando competência com conclusão forte",
    """**2. ANÁLISE JURÍDICA**

[PADRÃO] O Comandante de Cia não detém competência para instaurar IPM. O fato configura crime militar previsto no CPM.""",
    expect_block=True
))

# 6. [PADRÃO] com crime militar e conclusão forte
results.append(run_test(
    "PADRÃO com crime militar + configura",
    """**2. ANÁLISE JURÍDICA**

[PADRÃO] O fato configura crime militar previsto no CPM, sendo imperiosa a instauração de IPM.""",
    expect_block=True
))

# 7. Conclusão definitiva com peculato
results.append(run_test(
    "Peculato sem fonte documental",
    """**2. ANÁLISE JURÍDICA**

O fato configura peculato-desvio, nos termos do Código Penal Militar.

**4. TEXTO PRONTO**

Texto pronto simples.""",
    expect_block=True
))

# 8. Frutos da árvore envenenada sem fonte
results.append(run_test(
    "Frutos da árvore envenenada sem fonte",
    """**2. ANÁLISE JURÍDICA**

A prova está contaminada pela teoria dos frutos da árvore envenenada.

**4. TEXTO PRONTO**

Texto sem termos sensíveis.""",
    expect_block=True
))

# 9. [FUNDAMENTO] sem [FONTE:]
results.append(run_test(
    "FUNDAMENTO sem FONTE",
    """**2. ANÁLISE JURÍDICA**

[FUNDAMENTO] A competência é do Batalhão, conforme RDPM.

**4. TEXTO PRONTO**

Texto simples.""",
    expect_block=True
))

# 10. [VERIFICAR] seguido de conclusão forte
results.append(run_test(
    "VERIFICAR seguido de conclusão forte",
    """**2. ANÁLISE JURÍDICA**

[VERIFICAR: fundamento não localizado]. Contudo, o ato é nulo e padece de vício insanável.

**4. TEXTO PRONTO**

Texto simples.""",
    expect_block=True
))

# 11. Bloco 4.1 (termo proibido absoluto)
results.append(run_test(
    "Bloco 4.1 (termo proibido absoluto)",
    """**2. ANÁLISE JURÍDICA**

Análise simples.

**4. TEXTO PRONTO**

Bloco 4.1 — subitens adicionais do texto pronto.

Texto simples.""",
    expect_block=True
))

# 12. Fundamento novo no Bloco 4 (incompetência como conclusão argumentativa)
results.append(run_test(
    "Fundamento novo no Bloco 4 como conclusão argumentativa",
    """**2. ANÁLISE JURÍDICA**

Análise sem mencionar incompetência.

**4. TEXTO PRONTO**

1. Conclui-se que a autoridade instauradora é incompetente, padecendo o ato de vício insanável, devendo ser remetido ao Batalhão.""",
    expect_block=True
))

print()
print("=" * 70)
total = len(results)
passed = sum(results)
failed = total - passed
print(f"RESULTADO: {passed}/{total} testes passaram, {failed} falharam")
if failed == 0:
    print("✅ TODOS OS TESTES PASSARAM")
else:
    print("❌ ALGUNS TESTES FALHARAM — revisar ajustes")
print("=" * 70)
