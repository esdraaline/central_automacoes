import json
from automacoes.despachadora.nucleo_despachadora.despachadora import recover_chunks, extract_keywords

CORPUS_PATH = 'automacoes/despachadora/corpus_index.json'
with open(CORPUS_PATH, 'r', encoding='utf-8') as f:
    corpus = json.load(f)

consultas = [
    ("instruções IPM suspensão PAE", "Bol_G_132_IPM_Susp_PAE.md"),
    ("NI PM3 004 03 13 ICC", "NI_PM3_004_03_13_ICC.md"),
    ("acidente viatura PAAVI NI PM3 002 02 17", "NI_PM3_002_02_17.md"),
    ("acesso a dados em celular PM3 005 02 19", "Desp_PM3_005_02_19_Celular.md"),
    ("resolução contran 432 etilômetro alcoolemia", "Res_CONTRAN_432_13.md"),
    ("DEJEM diretriz PM3 002 02 16", "DTZ_PM3_002_02_16_DEJEM.md"),
    ("ordem complementar DEJEM PM3 007 02 16", "OC_PM3_007_02_16_DEJEM.md"),
    ("resolução 57 atividade delegada", "NI_001_02_15_Resolucao_57.md"),
    ("exercícios aquecimento condução motocicleta policial", "NI_Exercicios_Aquecimento_Conducao_Moto.md"),
    ("nota serviço CoordOpPM 001 03 16", "Nota_Servico_CoordOpPM_001_03_16.md"),
    ("nota urgente COPOM OS 005 04 19", "Nota_Urgente_COPOM_OS_005_04_19.md"),
    ("OS CoordOpPM 028 21 24", "OS_CoordOpPM_028_21_24.md"),
    ("fiscalização ciclomotor sinopse 02 18", "Sinopse_02_18_Fiscal_Ciclomotor.md"),
    ("OS CPI 10 002 30 16 regularização revista de armários", "OS_CPI10_002_30_16_Revista_Armarios.md"),
    ("OS informativo on line CPI 10 003 20 17", "OS_CPI10_003_20_17.md"),
    ("Ordem de serviço 2BPMI 001 30 14", "OS_2BPMI_001_30_14.md"),
    ("OC PM3 008 02 16 DEJEM", "OC_PM3_008_02_16_DEJEM.md"),
    ("codigo para tipificação de ocorrências 1961", "Codigos_Tipificacao_Ocorrencias.md"),
    ("codigos para encerramento de ocorrencia 1962", "Codigos_Encerramento_Ocorrencia.md")
]

print("| consulta | OCR esperado | posição | status | observação |")
print("| -------- | ------------ | ------: | ------ | ---------- |")

for consulta, esperado in consultas:
    kws = extract_keywords(consulta)
    resultados = recover_chunks(corpus, kws, query_text=consulta)[0]
    
    posicao = -1
    vencedor = None
    for i, chunk in enumerate(resultados[:10], 1):
        if chunk['arquivo'] == esperado:
            posicao = i
            break
        if i == 1:
            vencedor = chunk['arquivo']
            
    if posicao != -1 and posicao <= 5:
        status = "OK_FORTE"
        obs = "-"
    elif posicao != -1 and posicao <= 10:
        status = "OK_ACEITAVEL"
        obs = f"vencido por {vencedor}"
    else:
        # Verifica se um 'corpus_manual' ou fonte relevante venceu
        # Apenas para simplificar no script, listaremos como FONTE_MELHOR se houver um arquivo e FALHA senao
        if vencedor:
            status = "OK_FONTE_MELHOR"
            obs = f"vencido por {vencedor}"
        else:
            status = "FALHA"
            obs = "nao encontrado no top 10"
            
    print(f"| {consulta} | {esperado} | {posicao if posicao != -1 else '>10'} | {status} | {obs} |")
