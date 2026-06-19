import subprocess

def test_ambiente_ocr():
    print("Testando ambiente OCR...")
    
    # 1. Tesseract
    try:
        resultado = subprocess.run(["tesseract", "--version"], capture_output=True, text=True)
        print("Tesseract: Encontrado")
    except FileNotFoundError:
        print("Tesseract: Não encontrado (não está no PATH)")

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
