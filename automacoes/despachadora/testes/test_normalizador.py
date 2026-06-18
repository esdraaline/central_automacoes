import sys
from pathlib import Path

# Resolve o caminho do projeto a partir da localização deste arquivo
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "automacoes" / "despachadora" / "nucleo_despachadora"))

from despachadora import normalizar_resposta_antes_validador, validar_saida_despachadora

def run_tests():
    print("=== DEVE SANEAR E PASSAR ===")
    
    testes_passar = [
        """[VERIFICAR: confirmar fundamento específico]
Configurando, em tese, situação que demanda análise da autoridade competente.""",

        """[VERIFICAR: confirmar fundamento específico]
A situação pode configurar vício de competência.""",

        """- [VERIFICAR: confirmar fundamento de autotutela]
- Configurando possível vício administrativo.""",

        """[VERIFICAR: fundamento não localizado]
legitimando o uso da medida."""
    ]

    for i, texto in enumerate(testes_passar, 1):
        norm, aj = normalizar_resposta_antes_validador(texto)
        b, v, a = validar_saida_despachadora(norm, "", "")
        print(f"\n[TESTE {i}]")
        if not b:
            print("✅ PASSOU")
        else:
            print(f"❌ BLOQUEOU: {v}")

    print("\n=== DEVE CONTINUAR BLOQUEANDO ===")
    
    testes_bloquear = [
        "O fato configura peculato-desvio.",
        "Aplica-se a teoria dos frutos da árvore envenenada.",
        "[PADRÃO] O fato configura crime militar.",
        "Declaro nulidade absoluta por vício insanável."
    ]

    for i, texto in enumerate(testes_bloquear, 1):
        norm, aj = normalizar_resposta_antes_validador(texto)
        b, v, a = validar_saida_despachadora(norm, "", "")
        print(f"\n[BLOQUEIO {i}]")
        if b:
            print("✅ BLOQUEOU")
        else:
            print("❌ PASSOU (Falha na segurança)")

    print("\n=== NÃO DEVE ALTERAR DESTRUTIVAMENTE ===")
    
    testes_manter = [
        "[FUNDAMENTO] A Súmula Vinculante nº 11 exige justificativa por escrito. [FONTE: corpus_manual/Sumula_Vinculante_11_Algemas.md]",
        "[RE não informado]",
        "[FONTE: corpus_manual/Acidente_Viatura_Providencias.md]",
        "Assunto: Proposta de remessa de autos para análise de competência pela autoridade competente."
    ]

    for i, texto in enumerate(testes_manter, 1):
        norm, aj = normalizar_resposta_antes_validador(texto)
        print(f"\n[MANTER {i}]")
        if norm.strip() == texto.strip() or "Proposta de remessa de autos" in norm:
            print("✅ MANTEVE")
        else:
            print(f"❌ ALTEROU: {norm}")

if __name__ == "__main__":
    run_tests()
