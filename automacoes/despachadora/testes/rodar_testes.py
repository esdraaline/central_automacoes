import sys
import os
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def rodar_testes():
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    testes_dir = project_root / "automacoes" / "despachadora" / "testes"
    despachadora_dir = project_root / "automacoes" / "despachadora" / "nucleo_despachadora"
    
    print("="*40)
    print("RODANDO TESTES DA DESPACHADORA")
    print("="*40)
    
    # 1. Teste do Validador
    print("\n>>> TESTE DO VALIDADOR")
    validador_result = subprocess.run([sys.executable, str(testes_dir / "test_validador.py")], capture_output=True, text=True, encoding="utf-8")
    if validador_result.returncode == 0:
        print("VALIDADOR: OK")
    else:
        print("VALIDADOR: FALHOU")
        print(validador_result.stdout)
        print(validador_result.stderr)
        
    # 2. Teste do Normalizador
    print("\n>>> TESTE DO NORMALIZADOR")
    normalizador_result = subprocess.run([sys.executable, str(testes_dir / "test_normalizador.py")], capture_output=True, text=True, encoding="utf-8")
    if normalizador_result.returncode == 0:
        print("NORMALIZADOR: OK")
    else:
        print("NORMALIZADOR: FALHOU")
        print(normalizador_result.stdout)
        print(normalizador_result.stderr)

    # 3. Teste de recuperação da fonte autônoma de IP
    print("\n>>> TESTE DE RECUPERAÇÃO DA INVESTIGAÇÃO PRELIMINAR")
    recuperacao_ip_result = subprocess.run(
        [sys.executable, str(testes_dir / "test_recuperacao_ip.py")],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if recuperacao_ip_result.returncode == 0:
        print("RECUPERAÇÃO IP: OK")
    else:
        print("RECUPERAÇÃO IP: FALHOU")
        print(recuperacao_ip_result.stdout)
        print(recuperacao_ip_result.stderr)

    # 4. Compile check
    print("\n>>> TESTE DE SINTAXE (PY_COMPILE)")
    modulos = [
        despachadora_dir / "despachadora.py",
        despachadora_dir / "indexar_corpus.py",
        despachadora_dir / "classificar_corpus.py"
    ]
    compile_ok = True
    for mod in modulos:
        res = subprocess.run([sys.executable, "-m", "py_compile", str(mod)], capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            compile_ok = False
            print(f"Erro ao compilar {mod.name}:")
            print(res.stderr)
            
    if compile_ok:
        print("PY_COMPILE: OK")
    else:
        print("PY_COMPILE: FALHOU")

    print("\n" + "="*40)
    if (validador_result.returncode == 0
            and normalizador_result.returncode == 0
            and recuperacao_ip_result.returncode == 0
            and compile_ok):
        print("RESULTADO GERAL: SUCESSO")
        sys.exit(0)
    else:
        print("RESULTADO GERAL: FALHA")
        sys.exit(1)

if __name__ == "__main__":
    rodar_testes()
