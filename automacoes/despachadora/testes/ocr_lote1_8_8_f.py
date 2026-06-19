import os
import fitz
import pytesseract
from PIL import Image
import time

PDFS = [
    r"G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\JD\Arquivo\2020\Bol G 132 - 21JUL20 - Instruções IPM e Susp do PAE.pdf",
    r"G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\Normas\NI PM3_004_03_13 ICC.pdf",
    r"G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\P3\Outros\Acidente de trânsito vtr - PAAVI\NI Nº PM3-002-02-17.pdf",
    r"G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\P3\Outros\Preleção\Desp Nº PM3 005 02 19 - Acesso a dados em celular.pdf",
    r"G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\P3\OS\ODS\Resolução CONTRAN nº 432-13.pdf"
]

OUT_DIR = r"C:\Projetos\central_automacoes\saidas\ocr_lote1"
os.makedirs(OUT_DIR, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tessdata_dir = r"C:\Projetos\central_automacoes\saidas\tessdata"
custom_config = f'--tessdata-dir {tessdata_dir} -l por --psm 6'

print(f"Iniciando OCR Lote 1 - {len(PDFS)} PDFs...")

resultados = []

for idx, pdf_path in enumerate(PDFS, 1):
    print(f"\n--- Processando {idx}/{len(PDFS)} ---")
    filename = os.path.basename(pdf_path)
    print(f"Arquivo: {filename}")
    
    if not os.path.exists(pdf_path):
        print("ERRO: Arquivo não encontrado.")
        resultados.append({"arquivo": filename, "status": "FALHOU", "erro": "Não encontrado"})
        continue

    start_time = time.time()
    texto_completo = []
    
    try:
        doc = fitz.open(pdf_path)
        total_paginas = min(len(doc), 15)  # Limite razoável de 15 páginas para não demorar demais
        print(f"Páginas para processar: {total_paginas} (total: {len(doc)})")
        
        for pag_num in range(total_paginas):
            page = doc.load_page(pag_num)
            pix = page.get_pixmap(dpi=150) # DPI 150 para equilíbrio de velocidade/qualidade
            img_temp_path = os.path.join(OUT_DIR, f"temp_{idx}_{pag_num}.png")
            pix.save(img_temp_path)
            
            img = Image.open(img_temp_path)
            texto_pagina = pytesseract.image_to_string(img, config=custom_config)
            texto_completo.append(texto_pagina)
            
            # Limpar imagem
            img.close()
            os.remove(img_temp_path)
            
        texto_final = "\n\n".join(texto_completo)
        
        out_txt = os.path.join(OUT_DIR, f"{filename}.txt")
        with open(out_txt, "w", encoding="utf-8") as f:
            f.write(texto_final)
            
        chars = len(texto_final.strip())
        linhas_uteis = len([l for l in texto_final.split('\n') if len(l.strip()) > 3])
        elapsed = time.time() - start_time
        
        print(f"Sucesso! {chars} chars, {linhas_uteis} linhas em {elapsed:.1f}s")
        resultados.append({
            "arquivo": filename,
            "status": "OK",
            "paginas": total_paginas,
            "caracteres": chars,
            "linhas_uteis": linhas_uteis,
            "tempo_s": elapsed,
            "caminho_txt": out_txt
        })
        
    except Exception as e:
        print(f"ERRO ao processar {filename}: {e}")
        resultados.append({"arquivo": filename, "status": "FALHOU", "erro": str(e)})

print("\n\n=== RESUMO LOTE 1 ===")
for r in resultados:
    if r["status"] == "OK":
        print(f"[{r['status']}] {r['arquivo']} -> Pags: {r['paginas']}, Chars: {r['caracteres']}, Linhas: {r['linhas_uteis']}, Tempo: {r['tempo_s']:.1f}s")
    else:
        print(f"[{r['status']}] {r['arquivo']} -> Erro: {r['erro']}")
