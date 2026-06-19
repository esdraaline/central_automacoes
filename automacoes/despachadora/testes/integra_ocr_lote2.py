import os
import glob
import re

TEXTS_DIR = r"C:\Projetos\central_automacoes\saidas\ocr_lote2"
DEST_DIR = r"C:\Projetos\central_automacoes\automacoes\despachadora\corpus_ocr"
os.makedirs(DEST_DIR, exist_ok=True)

MAPPINGS = {
    "NI_001_02_15_resolução 57.pdf.txt": "NI_001_02_15_Resolucao_57.md",
    "DTZ PM3_002_02_16 DEJEM.pdf.txt": "DTZ_PM3_002_02_16_DEJEM.md",
    "Ordem de Serviço nº CoordOpPM-028.21.24, de 15OUT24 (3) (1).pdf.txt": "OS_CoordOpPM_028_21_24.md",
    "Nota de Serviço nº CoordOpPM-001-03-16 Operação Direção Segura Integrada - I-2016.pdf.txt": "Nota_Servico_CoordOpPM_001_03_16.md",
    "OS NOta urgente copom OSv Coord Op PM 005 04 19 - Ocor de grav ou repercussão (1).pdf.txt": "Nota_Urgente_COPOM_OS_005_04_19.md",
    "NI - B - Exercícios de aquecimento prévio de condução de viatura policial de duas rodas.pdf.txt": "NI_Exercicios_Aquecimento_Conducao_Moto.md",
    "Sinopse nº 02-18 Fiscal. de Ciclomotor.pdf.txt": "Sinopse_02_18_Fiscal_Ciclomotor.md",
    "OC PM3_007_02_16 DEJEM.pdf.txt": "OC_PM3_007_02_16_DEJEM.md"
}

# The goal is to clean up formatting
def clean_text(text):
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

for txt_file in glob.glob(os.path.join(TEXTS_DIR, "*.txt")):
    basename = os.path.basename(txt_file)
    if basename in MAPPINGS:
        dest_filename = MAPPINGS[basename]
        dest_path = os.path.join(DEST_DIR, dest_filename)
        
        with open(txt_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = clean_text(content)
        
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Integrado: {dest_filename}")
    else:
        print(f"Ignorado (sem mapping): {basename}")

print("Integração concluída.")
