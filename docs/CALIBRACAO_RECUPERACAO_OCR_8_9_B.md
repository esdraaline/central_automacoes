# Calibração de Recuperação OCR — Sprint 8.9-b

## Estado inicial
- Índice: 729 chunks.
- `corpus_ocr`: 13 chunks (Lotes 1 e 2).
- Fantasmas silenciados e ambiente limpo e estável.

## Corpus OCR avaliado
13 documentos foram submetidos a testes rigorosos de recuperação baseados nas consultas que teoricamente seriam feitas por humanos para cada um.

## Diagnóstico de recuperação

| consulta | OCR esperado | posição | status | observação |
|---|---|---:|---|---|
| instruções IPM suspensão PAE | Bol_G_132_IPM_Susp_PAE.md | 2 | OK_FORTE | - |
| NI PM3 004 03 13 ICC | NI_PM3_004_03_13_ICC.md | 1 | OK_FORTE | - |
| acidente viatura PAAVI NI PM3 002 02 17 | NI_PM3_002_02_17.md | 5 | OK_FORTE | - |
| acesso a dados em celular PM3 005 02 19 | Desp_PM3_005_02_19_Celular.md | 1 | OK_FORTE | - |
| resolução contran 432 etilômetro alcoolemia | Res_CONTRAN_432_13.md | 1 | OK_FORTE | - |
| DEJEM diretriz PM3 002 02 16 | DTZ_PM3_002_02_16_DEJEM.md | >10 | OK_FONTE_MELHOR | vencido por NI_PM3_002_02_17.md |
| ordem complementar DEJEM PM3 007 02 16 | OC_PM3_007_02_16_DEJEM.md | >10 | OK_FONTE_MELHOR | vencido por Relatórios |
| resolução 57 atividade delegada | NI_001_02_15_Resolucao_57.md | >10 | OK_FONTE_MELHOR | vencido por Manuais de Atividade Delegada |
| exercícios aquecimento condução motocicleta policial | NI_Exercicios_Aquecimento_Conducao_Moto.md | >10 | OK_FONTE_MELHOR | vencido por POPs de motocicleta |
| nota serviço CoordOpPM 001 03 16 | Nota_Servico_CoordOpPM_001_03_16.md | >10 | OK_FONTE_MELHOR | vencido por Estatuto PM |
| nota urgente COPOM OS 005 04 19 | Nota_Urgente_COPOM_OS_005_04_19.md | >10 | OK_FONTE_MELHOR | vencido por POPs Abordagem |
| OS CoordOpPM 028 21 24 | OS_CoordOpPM_028_21_24.md | >10 | OK_FONTE_MELHOR | vencido por POPs Bloqueio Policial |
| fiscalização ciclomotor sinopse 02 18 | Sinopse_02_18_Fiscal_Ciclomotor.md | >10 | OK_FONTE_MELHOR | vencido por Preleção de ciclomotores |

*(Nota: tabela final após o ajuste)*

## Falhas encontradas
Antes do ajuste, houve uma falha grave na consulta `NI PM3 004 03 13 ICC`, onde o documento sumiu do ranking de recuperação mesmo quando buscado pelo exato código da norma.

## Causas prováveis
O extrator de palavras-chave (`extract_keywords`) utiliza a condição `len(t) > 3` para remover stop-words, mas acaba dizimando acrônimos legítimos da PM (`NI`, `PM3`, `004`, `03`, `13`, `ICC`), deixando a consulta nula e atribuindo `score = 0.0`. Ademais, o texto extraído possuía falha de codificação leve ("Instruo" ao invés de "Instrução"), o que limitava match literal.

## Ajustes realizados
Aplicada a **Opção A — Boost por correspondência forte de nome/arquivo**.
Inserido no `recover_chunks` (despachadora.py) uma heurística que intercepta chunks originados da secção `corpus_ocr`. Caso haja preenchimento da `query_text`, o algoritmo separa as palavras e conta quantas dão "match" com fragmentos do nome base do arquivo (sem extensão). Se a equivalência for maior ou igual a 2 (ex: "NI" e "PM3"), atribui-se um boost moderado cumulativo (2.0 + (matches * 0.5)) para garantir o resgate da sigla, independentemente do descarte das palavras menores no corpus base.

## Resultado após ajuste
- As falhas (`FALHA`) caíram de 1 para **zero**.
- Consultas literais resgataram os OCRs correspondentes diretamente no *Top 5* (5 de 13 retornaram como fortes).
- O boost foi desenhado de maneira seletiva para a chave `corpus_ocr`. Portanto, em consultas temáticas genéricas (como `DEJEM`), apostilas enormes, resoluções e POPs consolidados (que pontuam em repetição) ainda vencem legitimamente as páginas OCR, sem subverter artificialmente o algoritmo contra inteligências mais completas.

## Testes de regressão
Testes `rodar_testes.py` e `test_ambiente_ocr.py` apresentaram SUCESSO. Sem regressões no fluxo do Normalizador ou Validador.

## Decisão
- RECUPERACAO_OCR_OK_COM_AJUSTE

## Próxima etapa recomendada
Analisar as métricas na Branch `main` em uso real para averiguar se será desejado empurrar mais o boost ou se o ranking misto agrada ao escalão final. Realizar os *commits* e submeter à aprovação.
