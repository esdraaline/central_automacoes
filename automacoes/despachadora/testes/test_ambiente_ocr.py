import subprocess
import os

def test_ambiente_ocr():
    print("Testando ambiente OCR...")
    
    # 1. Tesseract
    tesseract_cmd = "tesseract"
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    try:
        subprocess.run([tesseract_cmd, "--version"], capture_output=True, text=True)
        print("Tesseract: Encontrado no PATH")
    except FileNotFoundError:
        if os.path.exists(tesseract_path):
            tesseract_cmd = tesseract_path
            print(f"Tesseract: Encontrado em {tesseract_path}")
        else:
            print("Tesseract: Não encontrado (não está no PATH nem no diretório padrão)")
            tesseract_cmd = None

    if tesseract_cmd:
        try:
            resultado_langs = subprocess.run([tesseract_cmd, "--list-langs"], capture_output=True, text=True)
            if "por" in resultado_langs.stdout:
                print("Tesseract Idiomas: 'por' (Português) DISPONÍVEL")
            else:
                print("Tesseract Idiomas: 'por' (Português) AUSENTE")
        except Exception as e:
            print(f"Erro ao listar idiomas: {e}")

    # 2. pytesseract
    try:
        import pytesseract
        print("pytesseract: OK")
    except ImportError:
        print("pytesseract: Não instalado")

    # 3. pdf2image
    try:
        import pdf2image
        print("pdf2image: OK")
    except ImportError:
        print("pdf2image: Não instalado")

    # 4. fitz (pymupdf)
    try:
        import fitz
        print("pymupdf (fitz): OK")
    except ImportError:
        print("pymupdf (fitz): Não instalado")

if __name__ == "__main__":
    test_ambiente_ocr()
