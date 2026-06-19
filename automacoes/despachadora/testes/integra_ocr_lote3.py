import os
import json

TXT_DIR = r"C:\Projetos\central_automacoes\saidas\ocr_lote3"
CORPUS_OCR_DIR = r"C:\Projetos\central_automacoes\automacoes\despachadora\corpus_ocr"
CURADORIA_FILE = r"C:\Projetos\central_automacoes\automacoes\despachadora\curadoria_corpus.json"

FILES_MAPPING = {
    "OS CPI10-002-30-16 regularização revista de armários.pdf.txt": {
        "titulo": "OS CPI10-002-30-16 - Regularização Revista de Armários",
        "natureza": "NORMA",
        "arquivo_origem": "P2/OS CPI10-002-30-16 regularização revista de armários.pdf",
        "pdf_name": "OS CPI10-002-30-16 regularização revista de armários.pdf"
    },
    "OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf.txt": {
        "titulo": "OS Informativo On line Ordem Serviço nº CPI10-003.20.17",
        "natureza": "NORMA",
        "arquivo_origem": "P2/OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf",
        "pdf_name": "OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf"
    },
    "ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf.txt": {
        "titulo": "ORDEM DE SERVIÇO Nº 2BPMI-001-30-14",
        "natureza": "NORMA",
        "arquivo_origem": "P3/OS/ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf",
        "pdf_name": "ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf"
    },
    "OC PM3_008_02_16 DEJEM.pdf.txt": {
        "titulo": "OC PM3 008 02 16 DEJEM",
        "natureza": "NORMA",
        "arquivo_origem": "Notebooklm/Supervisor Regional/OC PM3_008_02_16 DEJEM.pdf",
        "pdf_name": "OC PM3_008_02_16 DEJEM.pdf"
    },
    "Codigo para tipificação de ocorrências 1961_190416104118_001.pdf.txt": {
        "titulo": "Codigo para tipificação de ocorrências",
        "natureza": "PROCEDIMENTAL",
        "arquivo_origem": "P3/Outros/Preleção/Codigo para tipificação de ocorrências 1961_190416104118_001.pdf",
        "pdf_name": "Codigo para tipificação de ocorrências 1961_190416104118_001.pdf"
    },
    "Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf.txt": {
        "titulo": "Codigos para encerramento de ocorrencia",
        "natureza": "PROCEDIMENTAL",
        "arquivo_origem": "P3/Outros/Preleção/Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf",
        "pdf_name": "Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf"
    }
}

TEMPLATE = """---
titulo: "{titulo}"
natureza: "{natureza}"
origem: "OCR"
arquivo_origem: "{arquivo_origem}"
qualidade_ocr: "OCR_OK"
lote_ocr: "8.9-c"
---

{texto}
"""

def limpar_nome(nome):
    nome = nome.replace('.txt', '.md')
    # Remover trechos problemáticos ou longos do nome do arquivo para ficar limpo
    nome = nome.replace("regularização revista de armários", "Revista_Armarios")
    nome = nome.replace("Informativo On line ", "")
    nome = nome.replace("nº ", "")
    nome = nome.replace(" ", "_")
    nome = nome.replace("ç", "c").replace("ã", "a").replace("í", "i").replace("ê", "e").replace("ó", "o")
    # Simplify names based on file content mapping
    if "Codigo_para_tipificacao" in nome:
        return "Codigos_Tipificacao_Ocorrencias.md"
    if "Codigos_para_encerramento" in nome:
        return "Codigos_Encerramento_Ocorrencia.md"
    if "ORDEM_DE_SERVIÇO_Nº_2BPMI-001-30-14" in nome:
        return "OS_2BPMI_001_30_14.md"
    if "OS_CPI10-002-30-16_Revista_Armarios" in nome:
        return "OS_CPI10_002_30_16_Revista_Armarios.md"
    if "OS_Ordem_Servico_CPI10-003.20.17" in nome:
        return "OS_CPI10_003_20_17.md"
    return nome

# 1. Integrar MD
novos_arquivos = []
for file_txt in os.listdir(TXT_DIR):
    if not file_txt.endswith(".txt"):
        continue
    
    if file_txt not in FILES_MAPPING:
        print(f"Ignorando arquivo desconhecido: {file_txt}")
        continue
        
    txt_path = os.path.join(TXT_DIR, file_txt)
    with open(txt_path, "r", encoding="utf-8") as f:
        texto = f.read()
        
    meta = FILES_MAPPING[file_txt]
    md_content = TEMPLATE.format(
        titulo=meta["titulo"],
        natureza=meta["natureza"],
        arquivo_origem=meta["arquivo_origem"],
        texto=texto
    )
    
    md_filename = limpar_nome(file_txt)
    md_path = os.path.join(CORPUS_OCR_DIR, md_filename)
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"Criado: {md_filename}")
    novos_arquivos.append(meta["pdf_name"])

# 2. Atualizar curadoria
with open(CURADORIA_FILE, "r", encoding="utf-8") as f:
    curadoria = json.load(f)

for pdf in novos_arquivos:
    curadoria["excluir_do_indice"].append({
        "padrao_arquivo": pdf,
        "motivo": "SUBSTITUIDO_POR_OCR_LOTE_3",
        "observacao": "Substituido pelo .md correspondente extraido no OCR Lote 3"
    })

with open(CURADORIA_FILE, "w", encoding="utf-8") as f:
    json.dump(curadoria, f, indent=4, ensure_ascii=False)
    
print("Curadoria atualizada com os arquivos substituídos.")
