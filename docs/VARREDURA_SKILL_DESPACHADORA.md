# Varredura Completa da Skill Despachadora

## A. Escopo e data da varredura
* **Data da Varredura:** 2026-06-17 13:25:46
* **Pasta Raiz:** `G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs`
* **Total de Arquivos Físicos Varridos:** 991

## B. Índice analisado
* **Índice Runtime (C:):** `C:\Projetos\central_automacoes\automacoes\despachadora\corpus_index.json`
  * Tamanho: 36,904,233 bytes
  * Modificação: 2026-06-16 18:31:14
  * SHA-256: `a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`
  * Chunks: 674
* **Índice Drive (G:):** `G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\corpus_index.json`
  * Tamanho: 36,904,233 bytes
  * Modificação: 2026-06-16 18:31:14
  * SHA-256: `a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`

> [!NOTE]
> Ambos os índices principal (C:) e do Drive (G:) são **byte-a-byte idênticos**.

## C. Totais gerais

| Classificação recomendada | Quantidade | Descrição |
|---|---|---|
| `JA_INDEXADO_OK` | 171 | Arquivos já indexados no tamanho ideal ou aceitável |
| `JA_SEGMENTADO` | 3 | Arquivos originais que já possuem segmentos ativos no índice |
| `PRONTO_SEM_SEGMENTACAO` | 6 | Novos arquivos dentro da faixa ideal de 20k-150k chars |
| `AVALIAR_AGRUPAMENTO` | 396 | Arquivos normativos pequenos (< 20k chars) |
| `PRECISA_OCR` | 51 | PDFs digitalizados sem texto extraível |
| `PRECISA_SEGMENTACAO` | 18 | Arquivos muito grandes (> 150k chars) |
| `REVISAR_NATUREZA` | 337 | Documentos fáticos, modelos, planilhas, holerites ou transitórios |
| `ERRO_LEITURA` | 9 | Arquivos corrompidos ou formatos não suportados |
| **TOTAL** | **991** | |

## D. Tabela geral de todos os arquivos

| Arquivo | Pasta | Ext | Tamanho (KB) | Páginas | Chars | TOC | Já Indexado? | Natureza Atual | Classificação | Observação |
|---|---|---|---|---|---|---|---|---|---|---|
| `CONTEXTO_CHAT.md` | raiz | .md | 2.7 | N/A | 2,644 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,644 chars), avaliar agrupamento. |
| `corpus_index.json` | raiz | .json | 36039.3 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de controle do indexador. |
| `despachadora.py` | raiz | .py | 42.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de controle do indexador. |
| `indexar_corpus.py` | raiz | .py | 13.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de controle do indexador. |
| `JD/01 - DESPACHO DE ANÁLISE DE REQUERIMENTO E RECEBIMENTO.doc` | JD | .doc | 163.5 | N/A | 907 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (907 chars). Avaliar agrupamento. |
| `JD/2025/Dano vtr 504/7277583_112216 (1).pdf` | JD | .pdf | 3545.5 | 5 | 6,141 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (6,141 chars), avaliar agrupamento. |
| `JD/2025/Dano vtr 504/BO2025-8-171326905.pdf` | JD | .pdf | 4074.4 | 17 | 17,846 | NÃO | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (17,846 chars). Avaliar agrupamento. |
| `JD/2025/Dano vtr 504/Despacho Dano VTR 504.pdf` | JD | .pdf | 113.2 | 2 | 3,840 | SIM | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/2025/Dano vtr 504/Parte 2BPMI_228_500_25 Dano em Vtr.docx` | JD | .docx | 92.1 | N/A | 3,549 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/2025/Dano vtr 504/Parte Dano vtr 504 (1).pdf` | JD | .pdf | 5662.6 | 4 | 5,393 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/2025/Despacho Disparo de Taser.docx` | JD | .docx | 31.9 | N/A | 1,442 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,442 chars). Avaliar agrupamento. |
| `JD/2025/Parte 2BPMI_228_500_25 Movimentação Conveniência da Disciplina.pdf` | JD | .pdf | 57.9 | 4 | 8,932 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,932 chars). Avaliar agrupamento. |
| `JD/2025/RIOG Apreensão de Entorpecente.doc` | JD | .doc | 29.0 | N/A | 2,627 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,627 chars). Avaliar agrupamento. |
| `JD/Arquivo/2018/OF - Mandado de Busca e Apreesão - GPS - 07mai18.docx` | JD | .docx | 46.8 | N/A | 1,972 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,972 chars). Avaliar agrupamento. |
| `JD/Arquivo/2018/PARTE 309 300 18 encaminhamento IP 159.doc` | JD | .doc | 99.0 | N/A | 1,930 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,930 chars). Avaliar agrupamento. |
| `JD/Arquivo/2018/Parte Instauração Sindicância Honorio.docx` | JD | .docx | 58.8 | N/A | 1,531 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,531 chars). Avaliar agrupamento. |
| `JD/Arquivo/2018/Relatório Sindicancia PT .40 -  19FEV18.docx` | JD | .docx | 37.8 | N/A | 8,259 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,259 chars). Avaliar agrupamento. |
| `JD/Arquivo/2019/fotos rg civis agressão coroados.jpeg` | JD | .jpeg | 148.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `JD/Arquivo/2019/Parte CFP 4 04out19.docx` | JD | .docx | 44.5 | N/A | 2,260 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,260 chars). Avaliar agrupamento. |
| `JD/Arquivo/2019/Parte Denuncia agressão Coroados.doc` | JD | .doc | 45.5 | N/A | 1,878 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2019/Parte Disparo de elastomero FT.doc` | JD | .doc | 49.0 | N/A | 3,737 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,737 chars). Avaliar agrupamento. |
| `JD/Arquivo/2019/Relatório Apuração Preliminar Nº 2bpmi-005-12-18.docx` | JD | .docx | 18.3 | N/A | 3,659 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,659 chars). Avaliar agrupamento. |
| `JD/Arquivo/2019/TD Lucas Guilherme Goulart Arrué de Andrade.docx` | JD | .docx | 19.6 | N/A | 4,130 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,130 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Bol G 132 - 21JUL20 - Instruções IPM e Susp do PAE.pdf` | JD | .pdf | 1421.1 | 4 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `JD/Arquivo/2020/DESPACHO Instauração de IP 5 Cia.docx` | JD | .docx | 31.6 | N/A | 660 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (660 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Parte Furto arma cindy.docx` | JD | .docx | 35.9 | N/A | 1,784 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,784 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Parte furto e acidente de transito com vítima.docx` | JD | .docx | 49.7 | N/A | 3,086 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2020/Parte L08 alunos soldados.docx` | JD | .docx | 36.3 | N/A | 2,032 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,032 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Parte Manifestação Preliminar atrasa Projeto Básico.docx` | JD | .docx | 36.6 | N/A | 3,173 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,173 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Parte Nº 181 500 20 Encaminhamento de documentação sobre dano em VTR I-02502.docx` | JD | .docx | 39.0 | N/A | 2,428 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2020/Parte PM aa.docx` | JD | .docx | 40.1 | N/A | 1,689 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,689 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Parte PM aa.pdf` | JD | .pdf | 102.3 | 1 | 2,050 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,050 chars). Avaliar agrupamento. |
| `JD/Arquivo/2020/Relatório IPM 028-12-20.docx` | JD | .docx | 50.5 | N/A | 23,392 | N/A | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2021/AIJ - Cb Mendes.docx` | JD | .docx | 170.8 | N/A | 5,627 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,627 chars). Avaliar agrupamento. |
| `JD/Arquivo/2021/BOPC 458-21.pdf` | JD | .pdf | 143.5 | 2 | 4,556 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2021/DESPACHO Nº 2BPMI-20-300-21 - Decisão IP 071.docx` | JD | .docx | 38.2 | N/A | 2,437 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,437 chars). Avaliar agrupamento. |
| `JD/Arquivo/2021/Parecer Santos uso arma fogo.pdf` | JD | .pdf | 503.9 | 1 | 716 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (716 chars). Avaliar agrupamento. |
| `JD/Arquivo/2021/Parecer Sgt Teixeira  uso arma de fogo.pdf` | JD | .pdf | 434.4 | 1 | 705 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (705 chars). Avaliar agrupamento. |
| `JD/Arquivo/2021/PARTE 2BPMI 012-200-20  ENCAMINHAMENTO DE IP 2 cia.doc` | JD | .doc | 54.5 | N/A | 2,928 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,928 chars). Avaliar agrupamento. |
| `JD/Arquivo/2021/PARTE Nº 2BPMI-11-300-22 -Dano viatura 319..docx` | JD | .docx | 88.4 | N/A | 4,987 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,987 chars). Avaliar agrupamento. |
| `JD/Arquivo/2022/Croqui Diego.pdf` | JD | .pdf | 97.5 | 1 | 0 | NÃO | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2022/Croqui Jeferson.pdf` | JD | .pdf | 98.8 | 1 | 0 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2022/Port IPM 12BAEP-1-12-22 e anexos.pdf` | JD | .pdf | 739.7 | 24 | 13,174 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (13,174 chars), avaliar agrupamento. |
| `JD/Arquivo/2022/PORTARIA IPM 12BAEP-1-12-22.doc` | JD | .doc | 138.5 | N/A | 4,520 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,520 chars). Avaliar agrupamento. |
| `JD/Arquivo/2022/RELATORIO CD N 2BPMI-001-12-22 - SD PM THIAGO ALVES COLON atualizado em 11NOVT22.doc` | JD | .doc | 146.5 | N/A | 59,388 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2022/RIOG MDIP BIRIGUI-SP.docx` | JD | .docx | 40.9 | N/A | 32,501 | N/A | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2022/RIOG MDIP BIRIGUI-SP.pdf` | JD | .pdf | 253.5 | 21 | 33,473 | NÃO | NÃO | - | `PRONTO_SEM_SEGMENTACAO` | Tamanho ideal (33,473 chars), pronto para indexação. |
| `JD/Arquivo/2023/bo202307031314758 acidente de transito via rondon 3-520 viatura atropelamento capivara.pdf` | JD | .pdf | 2129.4 | 10 | 11,970 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/Croqui Cadavérico Cristiano Birigui.pdf` | JD | .pdf | 587.4 | 1 | 614 | NÃO | SIM | PROCEDIMENTAL | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/Croqui Cadavérico Cristiano.pdf` | JD | .pdf | 246.1 | 1 | 0 | NÃO | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/croqui cristiano.pdf` | JD | .pdf | 496.4 | 1 | 790 | NÃO | SIM | PROCEDIMENTAL | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/PARTE Nº 2BPMI-06-30-23 -Dano viatura 3-520.docx` | JD | .docx | 77.2 | N/A | 3,370 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,370 chars). Avaliar agrupamento. |
| `JD/Arquivo/2023/Portaria IPM 021.pdf` | JD | .pdf | 271.7 | 2 | 3,831 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,831 chars). Avaliar agrupamento. |
| `JD/Arquivo/2023/Portaria IPM021.doc` | JD | .doc | 138.0 | N/A | 3,542 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,542 chars). Avaliar agrupamento. |
| `JD/Arquivo/2023/RIOG_2BPMI-004_12_23.doc` | JD | .doc | 81.0 | N/A | 21,675 | N/A | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2023/RIOG_2BPMI-004_12_23.pdf` | JD | .pdf | 330.1 | 14 | 22,143 | NÃO | NÃO | - | `PRONTO_SEM_SEGMENTACAO` | Tamanho ideal (22,143 chars), pronto para indexação. |
| `JD/Arquivo/2024/Auto de exibição e apreensão.doc` | JD | .doc | 33.0 | N/A | 1,793 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,793 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/BO2024-12-27135521.pdf` | JD | .pdf | 1063.8 | 15 | 15,355 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (15,355 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/CITAÇÃO 1º Ten PM Arcanjo.doc` | JD | .doc | 52.5 | N/A | 1,919 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,919 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/CITAÇÃO 2º Sgt PM Rodrigo.doc` | JD | .doc | 52.5 | N/A | 1,904 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,904 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/croqui cadavérico lado Batista pereira.pdf` | JD | .pdf | 500.8 | 1 | 846 | NÃO | SIM | PROCEDIMENTAL | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/Croqui Everton.pdf` | JD | .pdf | 74.6 | 1 | 0 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/DECISÃO - Cb PM 125898-2 - Cap Montanari.docx.doc` | JD | .doc | 71.5 | N/A | 15,363 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (15,363 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Inquirição Cb PM Gustavo.docx` | JD | .docx | 47.9 | N/A | 4,571 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,571 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Inquirição Cb PM Machado.docx` | JD | .docx | 47.3 | N/A | 4,196 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,196 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Inquirição Sd PM Bernine.docx` | JD | .docx | 46.8 | N/A | 4,558 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,558 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Inquirição Sd PM Wilyan.docx` | JD | .docx | 47.7 | N/A | 4,987 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,987 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Mdip Gpes 27DEZ24.doc` | JD | .doc | 83.0 | N/A | 22,825 | N/A | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/Mdip Gpes 27DEZ24.pdf` | JD | .pdf | 121.9 | 15 | 23,338 | SIM | NÃO | - | `PRONTO_SEM_SEGMENTACAO` | Tamanho ideal (23,338 chars), pronto para indexação. |
| `JD/Arquivo/2024/RELATORIO CD N 2BPMI-001-12-23 Cb PM Everton Carlos (1).doc` | JD | .doc | 180.5 | N/A | 92,506 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/RELATORIO CD N 2BPMI-001-12-23 Cb PM Everton Carlos (5).doc` | JD | .doc | 226.5 | N/A | 115,225 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/Relatório IP 2BPMI 050-12.5-24.doc` | JD | .doc | 160.5 | N/A | 82,787 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/RELATÓRIO IPM 009-12-24.docx` | JD | .docx | 81.1 | N/A | 32,860 | N/A | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/RELATÓRIO SINDICANCIA 009-12-14 161700JUL24.docx` | JD | .docx | 46.2 | N/A | 15,629 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (15,629 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Riog Mdip 25ago24.docx` | JD | .docx | 25.8 | N/A | 19,583 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (19,583 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Riog Mdip 2bpmi 003-12-24 25ago24.docx.doc` | JD | .doc | 90.0 | N/A | 23,437 | N/A | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/Riog Mdip 2bpmi 003-12-24 25ago24.pdf` | JD | .pdf | 156.8 | 15 | 23,949 | SIM | NÃO | - | `PRONTO_SEM_SEGMENTACAO` | Tamanho ideal (23,949 chars), pronto para indexação. |
| `JD/Arquivo/2024/RX1996.2024.pdf` | JD | .pdf | 140.7 | 4 | 8,847 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,847 chars). Avaliar agrupamento. |
| `JD/Arquivo/2024/Sup Reg/dpj_riog_mdip.doc` | JD | .doc | 79.5 | N/A | 20,085 | N/A | SIM | MODELO_DE_REDACAO | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.doc` | JD | .doc | 763.7 | N/A | 989 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.pdf` | JD | .pdf | 155.2 | 1 | 1,103 | NÃO | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/Arquivo/2024/Termo de Declaração Cb PM Ataídes.docx` | JD | .docx | 46.7 | N/A | 3,483 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/Termo de Declaração Cb PM Fransosso.docx` | JD | .docx | 46.7 | N/A | 4,003 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/WhatsApp Image 2024-04-12 at 09.08.30.jpeg` | JD | .jpeg | 391.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `JD/Arquivo/minhas ocorrências/Flagrante B04 a traseunte 05out20.pdf` | JD | .pdf | 969.6 | 2 | 4,915 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,915 chars). Avaliar agrupamento. |
| `JD/Arquivo/minhas ocorrências/Oitiva como testemunha acusacao sd garcia.pdf` | JD | .pdf | 1655.0 | 8 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `JD/Conclusão, Despacho e Data.doc` | JD | .doc | 37.0 | N/A | 614 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (614 chars). Avaliar agrupamento. |
| `JD/Delegada Valparaíso.docx` | JD | .docx | 18.0 | N/A | 5,539 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,539 chars). Avaliar agrupamento. |
| `JD/Despacho arquivamento de Manifestação Preliminar.docx` | JD | .docx | 50.1 | N/A | 1,695 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,695 chars). Avaliar agrupamento. |
| `JD/Despacho para não instauração de Sindicância.docx` | JD | .docx | 115.7 | N/A | 4,025 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,025 chars). Avaliar agrupamento. |
| `JD/Despacho para não instauração de Sindicância.pdf` | JD | .pdf | 104.2 | 2 | 4,344 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,344 chars). Avaliar agrupamento. |
| `JD/OFÍCIO 2BPMI-040-12-22 - DP PENAPOLIS - NÃO APRESENTAÇÃO CB MAGNO E RUFINO.pdf` | JD | .pdf | 203.0 | 3 | 8,743 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,743 chars). Avaliar agrupamento. |
| `JD/Ofício Solicitando a Expedição de Mandado de Busca e Apreensão Domiciliar.doc` | JD | .doc | 40.5 | N/A | 1,699 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,699 chars). Avaliar agrupamento. |
| `JD/Ofício Solicitando a Expedição de Mandado de Prisão Preventiva.doc` | JD | .doc | 40.0 | N/A | 1,669 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,669 chars). Avaliar agrupamento. |
| `JD/Ofício Solicitando a Expedição de Mandado de Prisão Temporária.doc` | JD | .doc | 44.5 | N/A | 1,620 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,620 chars). Avaliar agrupamento. |
| `JD/Portaria Instaurada Pelo Cmt.doc` | JD | .doc | 36.0 | N/A | 859 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (859 chars). Avaliar agrupamento. |
| `JD/PPJM/APFD/Modelo de Auto de Prisão em Flagrante Delito.doc` | JD | .doc | 242.0 | N/A | 43,940 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/PPJM/APFD/Normas Referentes Embriaguez de PM_BgRes011-87.doc` | JD | .doc | 40.5 | N/A | 4,545 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,545 chars). Avaliar agrupamento. |
| `JD/PPJM/APFD/Relatório Aditivo APFD.doc` | JD | .doc | 64.5 | N/A | 1,360 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,360 chars). Avaliar agrupamento. |
| `JD/PPJM/artigo_Roth_Atuacao do Advogado no IPM.pdf` | JD | .pdf | 3223.5 | 6 | 26,668 | NÃO | SIM | OUTRO | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/AUTO de RECONHECIMENTO FOTOGRAFICO - MODELO.doc` | JD | .doc | 27.0 | N/A | 1,880 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/PPJM/dpj_riog2.doc` | JD | .doc | 27.5 | N/A | 3,118 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,118 chars). Avaliar agrupamento. |
| `JD/PPJM/dpj_riog_mdip.doc` | JD | .doc | 77.0 | N/A | 19,780 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (19,780 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/apreensão de instrumentos e objetos, Provimento 0407 - CGer.pdf` | JD | .pdf | 7.7 | 1 | 3,450 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,450 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Apresentação de PM em Juízo_Bg175-94.doc` | JD | .doc | 71.5 | N/A | 13,104 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (13,104 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/bg_126_09_anexo_riog_I40PM.pdf` | JD | .pdf | 144.4 | 24 | 59,405 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/BO2021-12-221320070.pdf` | JD | .pdf | 1063.4 | 4 | 4,086 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,086 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CC.htm` | JD | .htm | 717.1 | N/A | 718,490 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (718,490 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CF.htm` | JD | .htm | 743.0 | N/A | 747,527 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (747,527 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CP.htm` | JD | .htm | 446.3 | N/A | 448,753 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (448,753 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPC.htm` | JD | .htm | 661.7 | N/A | 664,305 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (664,305 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPM.htm` | JD | .htm | 540.3 | N/A | 542,553 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (542,553 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPP.htm` | JD | .htm | 643.3 | N/A | 648,118 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (648,118 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPPM.htm` | JD | .htm | 706.4 | N/A | 711,581 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (711,581 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Crimes e Transgressões Disciplinares - Determinação.doc` | JD | .doc | 30.0 | N/A | 2,336 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,336 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/csp.pdf` | JD | .pdf | 410.4 | 120 | 372,648 | NÃO | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (372,648 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/CTB.htm` | JD | .htm | 456.4 | N/A | 459,311 | N/A | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (459,311 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Estatuto dos Militares.pdf` | JD | .pdf | 135.5 | 25 | 116,839 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/I-16-PM.pdf` | JD | .pdf | 878.3 | 71 | 160,162 | NÃO | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (160,162 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/I-40-PM - (Bol G PM 101-23) II 1.pdf` | JD | .pdf | 604.5 | 33 | 93,534 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/I-40-PM - (Bol G PM 101-23) II.pdf` | JD | .pdf | 604.5 | 33 | 93,534 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/I-40-PM.pdf` | JD | .pdf | 156.4 | 25 | 61,896 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/I-7-PM_7ª ed. Atual.pdf` | JD | .pdf | 1337.2 | 54 | 95,443 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/LCP.htm` | JD | .htm | 50.3 | N/A | 50,551 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/lcp.pdf` | JD | .pdf | 42.9 | 7 | 26,752 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/M-02-PM.pdf` | JD | .pdf | 160.4 | 43 | 98,482 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/MANUAL_BRASILEIRO_DE_FISCALIZACAO_DE_TRANSITO_27.09.2011[1].doc` | JD | .doc | 158.0 | N/A | 35,983 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/OS0110272011 RIOG.pdf` | JD | .pdf | 287.0 | 2 | 6 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/PAP Sindicância.mht` | JD | .mht | 724.4 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Sem texto extraível. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Perguntas RSM.htm` | JD | .htm | 16.6 | N/A | 16,386 | N/A | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (16,386 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Portaria dispoe sobre armas na PM.pdf` | JD | .pdf | 433.9 | 56 | 227,278 | SIM | SIM | MODELO_PRECEDENTE | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (227,278 chars). Precisa segmentar. |
| `JD/PPJM/Manuais, Leis, Regulamentos/RDPM atualizado 21MAR25.pdf` | JD | .pdf | 1550.3 | 54 | 134,871 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/RDPM_LC915_out07.pdf` | JD | .pdf | 837.0 | 54 | 140,343 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/resolução contran 432 alcoolemia.pdf` | JD | .pdf | 51.3 | 9 | 16,151 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (16,151 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/RIOG.mht` | JD | .mht | 9.4 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Sem texto extraível. |
| `JD/PPJM/Manuais, Leis, Regulamentos/RIOG_RSM.pdf` | JD | .pdf | 38.7 | 15 | 23,588 | NÃO | SIM | MODELO_DE_REDACAO | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `JD/PPJM/Manuais, Leis, Regulamentos/Rito do PD.doc` | JD | .doc | 71.5 | N/A | 10,282 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (10,282 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Saneamento Sindicância.pdf` | JD | .pdf | 8.3 | 1 | 3,927 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,927 chars). Avaliar agrupamento. |
| `JD/PPJM/Manuais, Leis, Regulamentos/Utilização de Armas Portáteis na PM_NIPM1-0010205.doc` | JD | .doc | 58.5 | N/A | 7,245 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,245 chars). Avaliar agrupamento. |
| `JD/PPJM/Modelo - CROQUI CADAVÉRICO.doc` | JD | .doc | 763.7 | N/A | 989 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/PPJM/Modelo - CROQUI CADAVÉRICO.pdf` | JD | .pdf | 155.2 | 1 | 1,103 | NÃO | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/PPJM/MODELO DE RIOG PARA PPJM.doc` | JD | .doc | 75.5 | N/A | 23,565 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/PPJM/Modelos Relativos ao Crime de Deserção.doc` | JD | .doc | 139.0 | N/A | 28,026 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `JD/PPJM/Orientações MDIP.jpeg` | JD | .jpeg | 192.9 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `JD/PPJM/Orientações PJMD MDIP e LCDIP.pdf` | JD | .pdf | 291.8 | 6 | 18,663 | NÃO | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (18,663 chars). Avaliar agrupamento. |
| `JD/PPJM/providencias em caso de morte de policial militar.docx` | JD | .docx | 20.6 | N/A | 17,803 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (17,803 chars). Avaliar agrupamento. |
| `JD/PPJM/Súmulas do STJ Sobre Prisão/Súmula 171 STJ.doc` | JD | .doc | 37.5 | N/A | 2,182 | N/A | SIM | JURISPRUDENCIA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,182 chars). Avaliar agrupamento. |
| `JD/PPJM/Súmulas do STJ Sobre Prisão/Súmula 21 STJ.doc` | JD | .doc | 30.5 | N/A | 1,695 | N/A | SIM | JURISPRUDENCIA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,695 chars). Avaliar agrupamento. |
| `JD/PPJM/Súmulas do STJ Sobre Prisão/Súmula 267 STJ.doc` | JD | .doc | 30.0 | N/A | 1,631 | N/A | SIM | JURISPRUDENCIA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,631 chars). Avaliar agrupamento. |
| `JD/PPJM/Súmulas do STJ Sobre Prisão/Súmula 280 STJ.doc` | JD | .doc | 28.5 | N/A | 1,234 | N/A | SIM | JURISPRUDENCIA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,234 chars). Avaliar agrupamento. |
| `JD/PPJM/termo reconhecimento de culpa 29nov14 generico.doc` | JD | .doc | 132.5 | N/A | 1,684 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,684 chars). Avaliar agrupamento. |
| `JD/Processo Baile Clandestino 1001653-74.2025.8.26.0218.pdf` | JD | .pdf | 20492.6 | 306 | 483,513 | NÃO | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (483,513 chars). Precisa segmentar. |
| `JD/Relatório de Utilização de AIN.pdf` | JD | .pdf | 134.0 | 2 | 7,725 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,725 chars). Avaliar agrupamento. |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_D88777_R200.txt` | Normas | .txt | 47.1 | N/A | 45,797 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_DireitosHumanos_Pt1.txt` | Normas | .txt | 97.9 | N/A | 95,057 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_DireitosHumanos_Pt2.txt` | Normas | .txt | 98.1 | N/A | 95,535 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_Fundamentos_Pt1.txt` | Normas | .txt | 119.6 | N/A | 116,390 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_Fundamentos_Pt2.txt` | Normas | .txt | 121.7 | N/A | 117,529 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_I16PM_Pt1.txt` | Normas | .txt | 78.9 | N/A | 76,400 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_I16PM_Pt2.txt` | Normas | .txt | 80.6 | N/A | 78,026 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_I40PM.txt` | Normas | .txt | 97.2 | N/A | 95,142 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M03PM_DefesaPessoal.txt` | Normas | .txt | 116.5 | N/A | 114,417 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M04PM_CmtCia.txt` | Normas | .txt | 32.2 | N/A | 31,320 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M10PM_Eventos_Pt1.txt` | Normas | .txt | 123.4 | N/A | 120,290 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M10PM_Eventos_Pt2.txt` | Normas | .txt | 122.1 | N/A | 119,354 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M19PM_Tiro_Pt1.txt` | Normas | .txt | 124.6 | N/A | 121,279 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M19PM_Tiro_Pt2.txt` | Normas | .txt | 127.7 | N/A | 120,522 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M19PM_Tiro_Pt3.txt` | Normas | .txt | 125.9 | N/A | 120,666 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M19PM_Tiro_Pt4.txt` | Normas | .txt | 127.0 | N/A | 121,604 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M19PM_Tiro_Pt5.txt` | Normas | .txt | 129.1 | N/A | 123,767 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_M19PM_Tiro_Pt6.txt` | Normas | .txt | 125.9 | N/A | 120,378 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_NORSOP_Pt1.txt` | Normas | .txt | 84.7 | N/A | 82,809 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_NORSOP_Pt2.txt` | Normas | .txt | 87.7 | N/A | 85,464 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_PM3_AtivDelegada.txt` | Normas | .txt | 46.7 | N/A | 45,562 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_PM3_Escolar_Comunitario.txt` | Normas | .txt | 61.2 | N/A | 59,844 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_PM3_EscoltaTransito.txt` | Normas | .txt | 49.9 | N/A | 48,785 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_PM3_RadioForca.txt` | Normas | .txt | 33.3 | N/A | 32,654 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_PM3_Rural_Reintegracao.txt` | Normas | .txt | 70.5 | N/A | 68,470 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_PM3_VistoriaEventos.txt` | Normas | .txt | 116.8 | N/A | 113,194 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_R5PM_Uniformes_Pt1.txt` | Normas | .txt | 112.3 | N/A | 109,408 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_R5PM_Uniformes_Pt2.txt` | Normas | .txt | 111.7 | N/A | 109,232 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_R5PM_Uniformes_Pt3.txt` | Normas | .txt | 111.9 | N/A | 109,231 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_RDPM.txt` | Normas | .txt | 138.9 | N/A | 135,324 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Doutrinas_PM_Segmentos/Doutrinas_RegGeral_SSP57.txt` | Normas | .txt | 137.7 | N/A | 134,909 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/I-1-PM Publicações.pdf` | Normas | .pdf | 206.5 | 30 | 50,977 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/I-15-PM Transportes Motorizados.pdf` | Normas | .pdf | 627.8 | 71 | 168,773 | NÃO | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (168,773 chars). Precisa segmentar. |
| `Normas/I-36-PM Afastamentos.pdf` | Normas | .pdf | 400.4 | 36 | 94,511 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/NI PM3_001_02_17 Assuncao de Comando de OPM.pdf` | Normas | .pdf | 237.6 | 22 | 51,313 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/NI PM3_004_03_13 ICC.pdf` | Normas | .pdf | 165.8 | 5 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Normas/NI PM3_005_03_17 NUMEC.pdf` | Normas | .pdf | 134.5 | 19 | 48,437 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/NI PM3_007_03_17 BO Eletrônico - com alterações.pdf` | Normas | .pdf | 458.7 | 27 | 63,056 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/NI_001_02_20 Atuacao da PM em eventos de perturbacao do sossego.pdf` | Normas | .pdf | 1247.4 | 18 | 38,466 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/PM3_002_03_20 Armas de incapacitação neuromuscular.pdf` | Normas | .pdf | 259.2 | 9 | 21,742 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_1_01_00_Abordagem_Pessoas_a_Pe.txt` | Normas | .txt | 96.6 | N/A | 94,378 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_1_02_00_Abordagem_Policial_Vtr_4_Rodas.txt` | Normas | .txt | 68.6 | N/A | 66,648 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_3_01_00_Acidente_Transito.txt` | Normas | .txt | 32.2 | N/A | 31,233 | N/A | SIM | PROCEDIMENTAL | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `Normas/POPs_Segmentos/POP_3_02_00_Ocorrencia_Envolvendo_Autoridades.txt` | Normas | .txt | 25.8 | N/A | 25,096 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_3_03_00_Transporte_Guarda_Presos.txt` | Normas | .txt | 69.0 | N/A | 67,742 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_3_04_00_Atendimento_Ocorrencia_Horario_Folga.txt` | Normas | .txt | 20.4 | N/A | 20,243 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_4_01_00_Acompanhamento_e_Cerco.txt` | Normas | .txt | 25.0 | N/A | 24,353 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_4_02_00_Bloqueio_Policial.txt` | Normas | .txt | 42.1 | N/A | 40,891 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_4_04_00_Cumprimento_Mandado_Judicial.txt` | Normas | .txt | 24.9 | N/A | 24,287 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_4_05_00_Forca_Tatica_Contencao.txt` | Normas | .txt | 28.1 | N/A | 27,126 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_4_06_00_Atuacao_Manifestacoes.txt` | Normas | .txt | 38.7 | N/A | 37,319 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_03_00_Uso_de_Algemas.txt` | Normas | .txt | 29.2 | N/A | 28,696 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_12_00_Emprego_Municao_Elastomero.txt` | Normas | .txt | 22.0 | N/A | 21,320 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_13_00_Transposicao_Obstaculo.txt` | Normas | .txt | 40.2 | N/A | 39,098 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_14_00_Municao_Impacto_FN303.txt` | Normas | .txt | 22.1 | N/A | 21,482 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_15_5_25_Armas_Brancas.txt` | Normas | .txt | 45.2 | N/A | 44,710 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_16_00_Cameras_Operacionais_Portateis.txt` | Normas | .txt | 31.9 | N/A | 31,138 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_18_00_Granadas_Policiais.txt` | Normas | .txt | 43.5 | N/A | 42,479 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_19_00_Resgate_Tatico_PM_Ferido.txt` | Normas | .txt | 43.1 | N/A | 42,148 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_20_00_Incapacitacao_Neuromuscular.txt` | Normas | .txt | 24.8 | N/A | 24,128 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_21_00_TASER_X2.txt` | Normas | .txt | 26.3 | N/A | 25,518 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_22_00_Municao_Bean_Bag.txt` | Normas | .txt | 21.8 | N/A | 21,235 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_27_00_Atendimento_Ocorrencia_PcD.txt` | Normas | .txt | 28.9 | N/A | 28,163 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_5_28_00_Cameras_Operacionais_Portateis_Motorola.txt` | Normas | .txt | 46.2 | N/A | 44,897 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_Deslocamento_Estacionamento_Passagem.txt` | Normas | .txt | 38.0 | N/A | 37,008 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_GasPimenta_Tonfa_Cinto.txt` | Normas | .txt | 25.0 | N/A | 24,250 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_Ocorrencias_Gerais.txt` | Normas | .txt | 48.1 | N/A | 46,577 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_Policiamento_com_Motocicleta.txt` | Normas | .txt | 114.7 | N/A | 112,194 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_PreservacaoLocal_MortePM_Bombas.txt` | Normas | .txt | 36.5 | N/A | 35,565 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_Roubo_Estabelecimento_Comercial.txt` | Normas | .txt | 23.8 | N/A | 23,571 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_Violencia_Domestica.txt` | Normas | .txt | 32.4 | N/A | 31,515 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/POPs_Segmentos/POP_Vistoria_Drogas.txt` | Normas | .txt | 49.8 | N/A | 49,321 | N/A | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Vademecum_Segmentos/Vademecum_CP_Militar.txt` | Normas | .txt | 21.8 | N/A | 21,287 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Vademecum_Segmentos/Vademecum_CPP_Flagrante.txt` | Normas | .txt | 39.9 | N/A | 39,123 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Vademecum_Segmentos/Vademecum_CTB.txt` | Normas | .txt | 31.2 | N/A | 30,383 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Vademecum_Segmentos/Vademecum_Drogas_11343.txt` | Normas | .txt | 22.5 | N/A | 22,123 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Vademecum_Segmentos/Vademecum_ECA.txt` | Normas | .txt | 40.0 | N/A | 39,103 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Normas/Vademecum_Segmentos/Vademecum_Lei_Maria_da_Penha.txt` | Normas | .txt | 22.7 | N/A | 22,171 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Notebooklm/Supervisor Regional/Doutrinas pm_compressed (1).pdf` | Notebooklm | .pdf | 42259.2 | 1643 | 3,093,809 | SIM | SIM | NORMA | `JA_SEGMENTADO` | JA_SEGMENTADO — fonte original preservada |
| `Notebooklm/Supervisor Regional/DTZ PM3_002_02_16 DEJEM.pdf` | Notebooklm | .pdf | 7273.9 | 16 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Notebooklm/Supervisor Regional/ESCALA DE OFICIAL SUPERVISOR REGIONAL - DEZ25 (2).pdf` | Notebooklm | .pdf | 688.5 | 1 | 4,672 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `Notebooklm/Supervisor Regional/ESCALA DE OFICIAL SUPERVISOR REGIONAL - NOV25 (1).pdf` | Notebooklm | .pdf | 91.7 | 1 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `Notebooklm/Supervisor Regional/NI_001_02_15 SISTEMÁTICA DE ATUAÇÃO DA POLÍCIA MILITAR NO  ATENDIMENTO E REGISTRO DE OCORRÊNCIAS – RESOLUÇÃO SSP-57.2015.pdf` | Notebooklm | .pdf | 2634.3 | 46 | 88,470 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `Notebooklm/Supervisor Regional/OC PM3_007_02_16 DEJEM.pdf` | Notebooklm | .pdf | 386.6 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Notebooklm/Supervisor Regional/OC PM3_008_02_16 DEJEM.pdf` | Notebooklm | .pdf | 332.2 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Notebooklm/Supervisor Regional/orientações direito militar.pdf` | Notebooklm | .pdf | 13682.1 | 481 | 1,153,578 | SIM | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (1,153,578 chars). Precisa segmentar. |
| `Notebooklm/Supervisor Regional/POPs.pdf` | Notebooklm | .pdf | 42456.8 | 824 | 1,415,187 | SIM | SIM | NORMA | `JA_SEGMENTADO` | JA_SEGMENTADO — fonte original preservada |
| `Notebooklm/Supervisor Regional/Relatório Ronda do Oficial  Supervisor Regional 23ago25 -  Modelo.pdf` | Notebooklm | .pdf | 120.6 | 3 | 8,213 | NÃO | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `Notebooklm/Supervisor Regional/Vademecum.pdf` | Notebooklm | .pdf | 32424.2 | 2807 | 7,374,439 | SIM | SIM | NORMA | `JA_SEGMENTADO` | JA_SEGMENTADO — fonte original preservada |
| `Notebooklm/Supervisor Regional.zip` | Notebooklm | .zip | 132690.2 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Sem texto extraível. |
| `ocr_pdfs_imagem.py` | raiz | .py | 6.6 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Sem texto extraível. |
| `P1/09052023_Ordem Serviço Atividade Física_082633.pdf` | P1 | .pdf | 164.1 | 2 | 3,428 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,428 chars). Avaliar agrupamento. |
| `P1/1415-1993 código de postura valparaiso.PDF` | P1 | .pdf | 2615.9 | 16 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/1870-1994 decreto regulamenta codigo de postura valparaiso.PDF` | P1 | .pdf | 223.9 | 2 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/2022/EAPEAD_2022___Oficiais_(Turma_IV)_de_16ABR22_a_30ABR22-Certificado_de_Conclusão_183317.pdf` | P1 | .pdf | 524.0 | 1 | 283 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (283 chars), avaliar agrupamento. |
| `P1/2022/Email Convocação.pdf` | P1 | .pdf | 509.2 | 5 | 8,579 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,579 chars). Avaliar agrupamento. |
| `P1/2022/FICHA DE SOLICITAÇÃO DE RESERVA DE VAGA hotel de trânsito alojamento central.docx` | P1 | .docx | 29.1 | N/A | 16,061 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (16,061 chars). Avaliar agrupamento. |
| `P1/2022/FICHA DE SOLICITAÇÃO DE RESERVA DE VAGA hotel de trânsito alojamento central.pdf` | P1 | .pdf | 366.6 | 1 | 2,746 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,746 chars). Avaliar agrupamento. |
| `P1/2022/Metas Avaliação Desempenho/Metas.docx` | P1 | .docx | 13.0 | N/A | 859 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (859 chars). Avaliar agrupamento. |
| `P1/2022/Oficio DER 2.doc` | P1 | .doc | 605.5 | N/A | 975 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (975 chars). Avaliar agrupamento. |
| `P1/2022/Passagem Ida e Volta Treinamento Qualidade .pdf` | P1 | .pdf | 522.5 | 1 | 2,281 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,281 chars). Avaliar agrupamento. |
| `P1/2022/PMESPEXP202241072A documentação reserva hotel de trânsito alojamento central.pdf` | P1 | .pdf | 297.8 | 8 | 9,717 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,717 chars). Avaliar agrupamento. |
| `P1/2022/PMESPEXP202241072A.pdf` | P1 | .pdf | 297.8 | 8 | 9,717 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,717 chars). Avaliar agrupamento. |
| `P1/2022/PMP 118 DS Cap Josemar.pdf` | P1 | .pdf | 365.3 | 3 | 6,118 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,118 chars). Avaliar agrupamento. |
| `P1/2022/PMP118 DS Cap Josemar.doc` | P1 | .doc | 76.5 | N/A | 5,847 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,847 chars). Avaliar agrupamento. |
| `P1/2022/TREINAMENTO_COMPLEMENTAR___ATUALIZAÇÃO_DE_AGENTE_DE_TRÂNSITO___32_ha__TURMA_XI22-Certificado_61643.pdf` | P1 | .pdf | 490.8 | 1 | 278 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (278 chars), avaliar agrupamento. |
| `P1/2023/assinatura e-mail.png` | P1 | .png | 88.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/2023/assinatura para funcional digital.pdf` | P1 | .pdf | 9.7 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/2023/assinatura para funcional digital.png` | P1 | .png | 29.1 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/2023/Ficha Controle de Tráfego vtr 15-141 vectra.pdf` | P1 | .pdf | 888.8 | 2 | 1,235 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,235 chars). Avaliar agrupamento. |
| `P1/20230830_144806.jpg` | P1 | .jpg | 1209.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/2024/EAPEAD_2024___Oficiais_(Turma_II)_de_09MAR24_a_23MAR24-Certificado_326526.pdf` | P1 | .pdf | 860.5 | 1 | 283 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (283 chars), avaliar agrupamento. |
| `P1/2024/Efetivo atualizado 5 cia 29fev24.jpeg` | P1 | .jpeg | 454.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/2024/Escala Geral 5ª Cia 2024 - JUN24.pdf` | P1 | .pdf | 399.1 | 2 | 15,791 | NÃO | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P1/2024/Escala_Geral_5ª_Cia_2024_-_MAR24-1.pdf` | P1 | .pdf | 398.6 | 2 | 15,786 | NÃO | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P1/2024/Ofício Doação Óleos Menu.doc` | P1 | .doc | 67.0 | N/A | 1,293 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,293 chars). Avaliar agrupamento. |
| `P1/2024/Previa Escala Supervisor Regional abr24.jpeg` | P1 | .jpeg | 191.6 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/2024/Sade 2024.docx` | P1 | .docx | 13.7 | N/A | 501 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (501 chars), avaliar agrupamento. |
| `P1/2025/ALOJ CENTRAL CAP PM JOSEMAR 2 Assinada.pdf` | P1 | .pdf | 203.8 | 1 | 2,995 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,995 chars), avaliar agrupamento. |
| `P1/2025/ALOJ CENTRAL CAP PM JOSEMAR 2.pdf` | P1 | .pdf | 167.3 | 1 | 2,858 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,858 chars), avaliar agrupamento. |
| `P1/2025/ALOJ CENTRAL CAP PM JOSEMAR Assinada.pdf` | P1 | .pdf | 205.2 | 1 | 3,010 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (3,010 chars), avaliar agrupamento. |
| `P1/2025/ALOJ CENTRAL CAP PM JOSEMAR.pdf` | P1 | .pdf | 200.6 | 1 | 2,874 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,874 chars), avaliar agrupamento. |
| `P1/2025/ALOJ_CENTRAL_CAP_PM_JOSEMAR_28OUT25 Assinada Preenchida.pdf` | P1 | .pdf | 255.7 | 1 | 3,009 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (3,009 chars), avaliar agrupamento. |
| `P1/2025/ALOJ_CENTRAL_CAP_PM_JOSEMAR_28OUT25 Assinada.pdf` | P1 | .pdf | 230.3 | 1 | 3,282 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (3,282 chars), avaliar agrupamento. |
| `P1/2025/ALOJ_CENTRAL_CAP_PM_JOSEMAR_28OUT25.pdf` | P1 | .pdf | 181.4 | 1 | 3,144 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (3,144 chars), avaliar agrupamento. |
| `P1/2025/EAP-CAP-25_CERTIFICADO.pdf` | P1 | .pdf | 345.8 | 1 | 186 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (186 chars), avaliar agrupamento. |
| `P1/2025/Metas 1 semestre.docx` | P1 | .docx | 13.0 | N/A | 1,125 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,125 chars). Avaliar agrupamento. |
| `P1/2025/Metas 2 semestre.docx` | P1 | .docx | 14.2 | N/A | 1,034 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,034 chars). Avaliar agrupamento. |
| `P1/2025/Minha avaliação de desempenho 2 de 2024.pdf` | P1 | .pdf | 74.7 | 4 | 4,124 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,124 chars). Avaliar agrupamento. |
| `P1/2025/Recadastramento 2025.pdf` | P1 | .pdf | 15.1 | 1 | 640 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (640 chars). Avaliar agrupamento. |
| `P1/2025/SEI_057.00526627_2025_89.pdf` | P1 | .pdf | 858.6 | 13 | 21,225 | SIM | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P1/2025  - 11FEV25 - 5ª Cia PM - CPF e e-mail efetivo.xlsx` | P1 | .xlsx | 20.7 | N/A | 8,942 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/2026/CERTIFICADO EAP 2026.pdf` | P1 | .pdf | 293.2 | 1 | 190 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (190 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2018/08 - ESCALA DE OFICIAL SUPERIOR DE SOBREAVISO AGO18.pdf` | P1 | .pdf | 282.6 | 1 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/08 - ESCALA DE SUPERVISOR REGIONAL -  AGO18.pdf` | P1 | .pdf | 341.4 | 1 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/08. Escala dos Tenentes 2º BPMI - 01 a 31AGO18.xlsx` | P1 | .xlsx | 708.0 | N/A | 17,068 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/Calendário de Visitas Técnicas.pdf` | P1 | .pdf | 300.3 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/Anos anteriores/2018/COPIA EFETIVO TELEFONE - 13DEZ17.xlsx` | P1 | .xlsx | 28.1 | N/A | 5,778 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Anos anteriores/2018/EFETIVO POR POSTO-ANTIG. -19JUL18.docx` | P1 | .docx | 18.2 | N/A | 2,965 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,965 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2018/Escala mensal outubro 5ª cia.pdf` | P1 | .pdf | 1365.4 | 2 | 0 | NÃO | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/Estudo do efetivo 2º BPMI.xlsx` | P1 | .xlsx | 238.1 | N/A | 89,495 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Anos anteriores/2018/Metas Sgt 1 2018.docx` | P1 | .docx | 13.0 | N/A | 2,745 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,745 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2018/OFICIO DE RENOVAÇÃO DE CONVENIO DE TRANSITO valparaiso 2018.doc` | P1 | .doc | 49.5 | N/A | 1,294 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,294 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2018/Planilha de Férias 2018 Josemar.xlsx` | P1 | .xlsx | 10.3 | N/A | 580 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Anos anteriores/2019/Metas Sgt 1 2019.docx` | P1 | .docx | 9.6 | N/A | 619 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (619 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2019/Metas Sgt 2 2019.docx` | P1 | .docx | 13.4 | N/A | 401 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (401 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2019/Ofício Reforma Pelotão Valparaiso.docx` | P1 | .docx | 54.7 | N/A | 1,604 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,604 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/certificado eap ead 2020 Estágio_de_Atualização_Profissional_2020_(Turma_IV___Período_16ABR20_a_30ABR20)-Certificado_49706.pdf` | P1 | .pdf | 713.3 | 1 | 311 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (311 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2020/EEP___Usuário_da_Arma_de_Incapacitação_Neuromuscular___2020-Certificado_3536.pdf` | P1 | .pdf | 565.5 | 1 | 50 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (50 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2020/Metas Sgt 1 2020.docx` | P1 | .docx | 13.5 | N/A | 422 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (422 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2020/Metas Sgt 2 2020.docx` | P1 | .docx | 14.1 | N/A | 1,452 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,452 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2020/OF - 206 RESPOSTA PROMOTORIA - C-01.doc` | P1 | .doc | 65.5 | N/A | 2,274 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,274 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/OF - 288 RESPOSTA PROMOTORIA c01 cadeiras.doc` | P1 | .doc | 62.5 | N/A | 1,340 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,340 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/OFÍCIO  MP RAIA COVID.doc` | P1 | .doc | 73.5 | N/A | 974 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (974 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/OFÍCIO 245 RESPOSTA MP COVID.doc` | P1 | .doc | 78.0 | N/A | 3,357 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,357 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/OFÍCIO 266 MP RAIA COVID.doc` | P1 | .doc | 73.0 | N/A | 1,017 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,017 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/Parte Manifestação Preliminar atrasa Projeto Básico.doc` | P1 | .doc | 49.0 | N/A | 3,200 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,200 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2020/Relatório passar para Cap Duarte.docx` | P1 | .docx | 14.6 | N/A | 2,933 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,933 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2020/Relação EFETIVO nov20.xlsx` | P1 | .xlsx | 12.3 | N/A | 2,624 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Anos anteriores/2020/Situação do efetivo 5 Cia.pdf` | P1 | .pdf | 72.0 | 1 | 973 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (973 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2020/Situação do efetivo 5 Cia.xlsx` | P1 | .xlsx | 12.4 | N/A | 865 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Anos anteriores/2021/ANEXO - O.S. Nº CPI10-002-10-21 Atualização do cadastro de dependentes.docx` | P1 | .docx | 38.7 | N/A | 3,362 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (3,362 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ata Reunião Sgt 15jun21.docx` | P1 | .docx | 14.1 | N/A | 2,228 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,228 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ata Reunião Sgt 17ago21.docx` | P1 | .docx | 14.7 | N/A | 689 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (689 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Atestado Cb Cardoso 14out21.pdf` | P1 | .pdf | 393.8 | 1 | 389 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (389 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2021/Claro efetivo 3 cia considerações.pdf` | P1 | .pdf | 108.7 | 2 | 1,014 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,014 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Claro Efetivo 3ª Cia.pdf` | P1 | .pdf | 120.9 | 1 | 1,790 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,790 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2021/Claro Efetivo 3ª Cia.xlsx` | P1 | .xlsx | 16.0 | N/A | 3,035 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Anos anteriores/2021/DS Cap Josemar 29dez21.pdf` | P1 | .pdf | 447.6 | 1 | 1,490 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,490 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/EAPEAD_2021___Oficiais_(Turma_IX)_de_16SET21_a_30SET21-Certificado_151660.pdf` | P1 | .pdf | 1012.3 | 1 | 286 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (286 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ficha Individual Ten Josemar .pdf` | P1 | .pdf | 432.4 | 1 | 863 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (863 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Metas para a Cia 2020 Cap Brito.pdf` | P1 | .pdf | 1784.1 | 4 | 115 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (115 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2021/Metas Sgt 2 2021.docx` | P1 | .docx | 14.2 | N/A | 932 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (932 chars), avaliar agrupamento. |
| `P1/Anos anteriores/2021/Oficio de Apresentação assunção cmd 3ª cia.doc` | P1 | .doc | 52.5 | N/A | 1,379 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,379 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Oficio MP Cicero.pdf` | P1 | .pdf | 619.3 | 1 | 2,402 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,402 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/OFÍCIO 22-200-20 carnafunk.doc` | P1 | .doc | 52.5 | N/A | 1,379 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,379 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Aracanguá.docx` | P1 | .docx | 85.2 | N/A | 1,091 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,091 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Auriflama.docx` | P1 | .docx | 85.2 | N/A | 1,091 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,091 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Gastão.docx` | P1 | .docx | 85.2 | N/A | 1,091 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,091 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Guzolândia.docx` | P1 | .docx | 85.2 | N/A | 1,091 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,091 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Iracema.docx` | P1 | .docx | 85.2 | N/A | 1,091 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,091 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Luzitânia.docx` | P1 | .docx | 85.2 | N/A | 1,091 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,091 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz  Araçatuba.docx` | P1 | .docx | 85.2 | N/A | 1,094 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,094 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz  Nhandeara.docx` | P1 | .docx | 85.2 | N/A | 1,094 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,094 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz  Salgado.docx` | P1 | .docx | 121.1 | N/A | 1,292 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,292 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz Auriflama.docx` | P1 | .docx | 85.2 | N/A | 1,094 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,094 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Aracanguá.docx` | P1 | .docx | 85.4 | N/A | 1,147 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,147 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Auriflama.docx` | P1 | .docx | 85.2 | N/A | 1,132 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,132 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Gastão.docx` | P1 | .docx | 85.3 | N/A | 1,142 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,142 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Guzolândia.docx` | P1 | .docx | 85.2 | N/A | 1,123 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,123 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Iracema.docx` | P1 | .docx | 85.2 | N/A | 1,144 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,144 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Luzitânia.docx` | P1 | .docx | 85.3 | N/A | 1,133 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,133 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Nova Castilho.docx` | P1 | .docx | 85.2 | N/A | 1,125 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,125 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Prefeito Salgado.docx` | P1 | .docx | 85.2 | N/A | 1,082 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,082 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor Auriflama.docx` | P1 | .docx | 85.2 | N/A | 1,084 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,084 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor de Araçatuba.docx` | P1 | .docx | 85.2 | N/A | 1,084 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,084 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor Nhandeara Rasfael.docx` | P1 | .docx | 85.2 | N/A | 1,084 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,084 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor Salgado.docx` | P1 | .docx | 121.0 | N/A | 1,158 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,158 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Parte 2BPMI 001-206-21.pdf` | P1 | .pdf | 490.5 | 1 | 1,663 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,663 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Parte Modelo 2021.doc` | P1 | .doc | 597.0 | N/A | 571 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P1/Anos anteriores/2021/PARTE Nº 2BPMI-318-300-21.docx` | P1 | .docx | 72.0 | N/A | 2,150 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,150 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/PMP118 DS Cap Josemar.doc` | P1 | .doc | 77.0 | N/A | 5,860 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,860 chars). Avaliar agrupamento. |
| `P1/Anos anteriores/2021/Relatório Médico Cb Cardoso 14out21.pdf` | P1 | .pdf | 374.1 | 1 | 172 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (172 chars). Avaliar agrupamento. |
| `P1/Assinatura Cmt 3 Cia.PNG` | P1 | .png | 52.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/aSSINATURA EMAIL CARTAO.PNG` | P1 | .png | 51.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/Assinatura email Cmt Interino 3 Cia.PNG` | P1 | .png | 51.7 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/CertExchange.cer` | P1 | .cer | 1.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Certificado de segurança (deve ser excluído). |
| `P1/conceito sargento.docx` | P1 | .docx | 15.3 | N/A | 3,205 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (3,205 chars), avaliar agrupamento. |
| `P1/Conseg/Oficio Comunicando Reativação.docx` | P1 | .docx | 1652.0 | N/A | 971 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (971 chars). Avaliar agrupamento. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Associação Comercial.docx` | P1 | .docx | 56.7 | N/A | 4,075 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Camara Municipal.docx` | P1 | .docx | 56.8 | N/A | 4,107 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Conselho Tutelar.docx` | P1 | .docx | 56.5 | N/A | 4,088 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg CPP.docx` | P1 | .docx | 56.7 | N/A | 4,106 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Detran.docx` | P1 | .docx | 56.6 | N/A | 4,065 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Lions Clube.docx` | P1 | .docx | 56.6 | N/A | 4,083 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Maçonaria.docx` | P1 | .docx | 56.5 | N/A | 4,044 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg OAB.docx` | P1 | .docx | 56.5 | N/A | 4,075 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Penitenciária.docx` | P1 | .docx | 56.7 | N/A | 4,085 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Prefeito.docx` | P1 | .docx | 56.8 | N/A | 4,076 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Rotary Club.docx` | P1 | .docx | 56.7 | N/A | 4,084 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Sindicato Rural.docx` | P1 | .docx | 56.6 | N/A | 4,099 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P1/Conseg/Pauta Padrão.docx` | P1 | .docx | 30.9 | N/A | 1,331 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,331 chars). Avaliar agrupamento. |
| `P1/Conseg/PLANILHA BALANÇO CPI.DEINTER 10.xlsx` | P1 | .xlsx | 27.7 | N/A | 2,999 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P1/Conseg/Processo Eleitoral Conseg Guararapes 2021.docx` | P1 | .docx | 11145.7 | N/A | 16,279 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (16,279 chars). Avaliar agrupamento. |
| `P1/Conseg/Relação do publico basico.doc` | P1 | .doc | 32.5 | N/A | 6,385 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,385 chars). Avaliar agrupamento. |
| `P1/Conseg/Resolução SSP n° 013, 28.02.2018 - Regulamento dos CONSEGs (TEXTO NORMATIVO).pdf` | P1 | .pdf | 502.0 | 45 | 79,512 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P1/Conseg/Roteiro para reativação.doc` | P1 | .doc | 142.5 | N/A | 5,054 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,054 chars). Avaliar agrupamento. |
| `P1/Contatos Justiça Eleitoral 5 Cia.docx` | P1 | .docx | 13.7 | N/A | 432 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (432 chars), avaliar agrupamento. |
| `P1/despacho avaliação diária de diligência.txt` | P1 | .txt | 0.2 | N/A | 164 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (164 chars). Avaliar agrupamento. |
| `P1/Despacho para avaliador.docx` | P1 | .docx | 49.5 | N/A | 931 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (931 chars). Avaliar agrupamento. |
| `P1/EAPEAD_2023___Oficiais_(Turma_III)_de_09ABR23_a_23ABR23-Certificado_de_Conclusão_259290.pdf` | P1 | .pdf | 741.2 | 1 | 284 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (284 chars), avaliar agrupamento. |
| `P1/Efetivo Atualizado 5ª Cia 20jan26.jpeg` | P1 | .jpeg | 273.3 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/Efetivo cpi e btl que faz croeste.pdf` | P1 | .pdf | 846.1 | 1 | 3,511 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,511 chars). Avaliar agrupamento. |
| `P1/Holerites/2014/Demonstrativo_09_2014(1).pdf` | P1 | .pdf | 33.2 | 1 | 1,420 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_09_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,216 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_10_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,460 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_11_2014(1).pdf` | P1 | .pdf | 33.2 | 1 | 1,443 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_11_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,492 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_12_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,336 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_01_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,392 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_02_2015.pdf` | P1 | .pdf | 46.7 | 1 | 2,641 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_03_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,443 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_04_2015(1).pdf` | P1 | .pdf | 33.2 | 1 | 1,429 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_04_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,368 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_05_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,275 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_06_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,396 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_07_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,315 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_08_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,344 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_09_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,492 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_10_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,463 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_11_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,385 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_12_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,436 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_01_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,373 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_02_2016.pdf` | P1 | .pdf | 46.7 | 1 | 2,721 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_03_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,565 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_04_2016.pdf` | P1 | .pdf | 46.7 | 1 | 2,587 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_05_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,432 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_06_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,372 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_07_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,413 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_08_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,481 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_09_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,450 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_10_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,426 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_11_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,434 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_12_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,562 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_01_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,516 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_02_2017.pdf` | P1 | .pdf | 47.4 | 1 | 2,784 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_03_2017.pdf` | P1 | .pdf | 47.4 | 1 | 2,599 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_04_2017(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,405 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_04_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,472 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_05_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,497 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_06_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,318 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_07_2017(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,405 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_07_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,557 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_08_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,426 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_09_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,561 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_10_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,399 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_11_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,357 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_12_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,396 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_01_2018(1).pdf` | P1 | .pdf | 34.0 | 1 | 1,414 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_01_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,296 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_02_2018(1).pdf` | P1 | .pdf | 34.0 | 1 | 1,404 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_02_2018.pdf` | P1 | .pdf | 47.6 | 1 | 2,624 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_03_2018.pdf` | P1 | .pdf | 47.6 | 1 | 2,648 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_04_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,264 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_05_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,317 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_06_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,414 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_07_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,233 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_08_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,484 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_09_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,425 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_10_2018(1).pdf` | P1 | .pdf | 34.0 | 1 | 1,384 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_10_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,466 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_11_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,473 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_12_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,499 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_01_2019(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,395 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_01_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,341 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_02_2019.pdf` | P1 | .pdf | 47.1 | 1 | 2,798 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_03_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,532 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_04_2019(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,439 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_04_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,527 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_05_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,499 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_06_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,306 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_07_2019(1).pdf` | P1 | .pdf | 34.1 | 1 | 2,385 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_07_2019(2).pdf` | P1 | .pdf | 33.8 | 1 | 1,366 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_08_2019(1).pdf` | P1 | .pdf | 34.1 | 1 | 2,389 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_09_2014(1).pdf` | P1 | .pdf | 33.2 | 1 | 1,420 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_10_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,460 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014(1).pdf` | P1 | .pdf | 33.2 | 1 | 1,443 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,492 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_12_2014.pdf` | P1 | .pdf | 33.8 | 1 | 2,336 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_01_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,392 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_03_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,443 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_04_2015(1).pdf` | P1 | .pdf | 33.2 | 1 | 1,429 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_07_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,315 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_08_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,344 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_09_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,492 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_10_2015.pdf` | P1 | .pdf | 33.8 | 1 | 2,463 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_01_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,373 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_02_2016.pdf` | P1 | .pdf | 46.7 | 1 | 2,721 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_03_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,565 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_04_2016.pdf` | P1 | .pdf | 46.7 | 1 | 2,587 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_05_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,432 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_06_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,372 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_07_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,413 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_08_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,481 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_09_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,450 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_10_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,426 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_11_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,434 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_12_2016.pdf` | P1 | .pdf | 33.8 | 1 | 2,562 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_01_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,516 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_02_2017.pdf` | P1 | .pdf | 47.4 | 1 | 2,784 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_03_2017.pdf` | P1 | .pdf | 47.4 | 1 | 2,599 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_04_2017(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,405 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_04_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,472 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_05_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,497 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_06_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,318 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_07_2017(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,405 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_07_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,557 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_08_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,426 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_09_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,561 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_10_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,399 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_11_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,357 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_12_2017.pdf` | P1 | .pdf | 34.5 | 1 | 2,396 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_01_2018(1).pdf` | P1 | .pdf | 34.0 | 1 | 1,414 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_01_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,296 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_02_2018(1).pdf` | P1 | .pdf | 34.0 | 1 | 1,404 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_02_2018.pdf` | P1 | .pdf | 47.6 | 1 | 2,624 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_03_2018.pdf` | P1 | .pdf | 47.6 | 1 | 2,648 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_04_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,264 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_05_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,317 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_06_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,414 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_07_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,233 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_08_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,484 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_09_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,425 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_10_2018(1).pdf` | P1 | .pdf | 34.0 | 1 | 1,384 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_10_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,466 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_11_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,473 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_12_2018.pdf` | P1 | .pdf | 34.6 | 1 | 2,499 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_01_2019(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,395 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_01_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,341 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_02_2019.pdf` | P1 | .pdf | 47.1 | 1 | 2,798 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_03_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,532 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_04_2019(1).pdf` | P1 | .pdf | 33.8 | 1 | 1,439 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_04_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,527 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_05_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,499 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_06_2019.pdf` | P1 | .pdf | 34.1 | 1 | 2,306 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_07_2019(1).pdf` | P1 | .pdf | 34.1 | 1 | 2,385 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_07_2019(2).pdf` | P1 | .pdf | 33.8 | 1 | 1,366 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_08_2019(1).pdf` | P1 | .pdf | 34.1 | 1 | 2,389 | NÃO | NÃO | - | `REVISAR_NATUREZA` | Holerite pessoal (deve ser excluído do corpus). |
| `P1/I-02-PM.pdf` | P1 | .pdf | 157.3 | 13 | 25,227 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P1/I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf` | P1 | .pdf | 453.6 | 20 | 45,408 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P1/JOSEMARDEPAULA,CapPM121876-0.pfx` | P1 | .pfx | 2.6 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Certificado de segurança (deve ser excluído). |
| `P1/lista 1 de 2 telefone email 3 cia.pdf` | P1 | .pdf | 588.4 | 1 | 4,719 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,719 chars). Avaliar agrupamento. |
| `P1/lista 2 de 2 telefone efetivo 3 cia.pdf` | P1 | .pdf | 608.3 | 1 | 4,410 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,410 chars). Avaliar agrupamento. |
| `P1/Modelo Despacho SEI.txt` | P1 | .txt | 0.2 | N/A | 190 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P1/movimentações classificações onde trabalhei.png` | P1 | .png | 54.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/normas i-7-pm/1Anexo 1_OSv 013 30 19_Instruções para correspondencia I-7-PM.docx` | P1 | .docx | 143.6 | N/A | 2,209 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,209 chars). Avaliar agrupamento. |
| `P1/normas i-7-pm/Anexo 2_OSv 013 30 19_Instruções para correspondencia I-31-PM.docx` | P1 | .docx | 269.3 | N/A | 9 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (9 chars), avaliar agrupamento. |
| `P1/normas i-7-pm/bg19054.pdf` | P1 | .pdf | 791.4 | 45 | 175,244 | NÃO | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (175,244 chars). Precisa segmentar. |
| `P1/normas i-7-pm/I-7-PM_7ª Edição Bol G 54_19.pdf` | P1 | .pdf | 1246.9 | 55 | 102,624 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P1/normas i-7-pm/OSv 015 30 19 Instruções para correspondencia.docx` | P1 | .docx | 44.5 | N/A | 1,321 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,321 chars). Avaliar agrupamento. |
| `P1/número codigo sei do batalhão e cpi.pdf` | P1 | .pdf | 414.4 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/PMP142.doc` | P1 | .doc | 87.0 | N/A | 804 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (804 chars). Avaliar agrupamento. |
| `P1/Relação do efetivo 5ª Cia jul25 por antiguidade.jpeg` | P1 | .jpeg | 497.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/Relação do Efetivo 5ª Cia jul25 por fração.jpeg` | P1 | .jpeg | 593.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P1/sade/I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf` | P1 | .pdf | 453.6 | 20 | 45,408 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P1/sade/PMP142.doc` | P1 | .doc | 89.5 | N/A | 722 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (722 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho e anexo para Sgt Gustavo.pdf` | P1 | .pdf | 16412.7 | 39 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho Escaneado.pdf` | P1 | .pdf | 260.2 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho para avaliador 2.docx` | P1 | .docx | 60.7 | N/A | 1,036 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,036 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho para avaliador.docx` | P1 | .docx | 50.5 | N/A | 931 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (931 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho para Celeste.docx` | P1 | .docx | 60.5 | N/A | 850 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (850 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho para Gustavo.docx` | P1 | .docx | 60.5 | N/A | 994 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (994 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho para P1.docx` | P1 | .docx | 59.9 | N/A | 918 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (918 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Parte para Cmt.docx` | P1 | .docx | 54.1 | N/A | 1,216 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,216 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/PMESPOFI2023136099A.pdf` | P1 | .pdf | 7935.2 | 46 | 18,209 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (18,209 chars). Avaliar agrupamento. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento Escaneado.pdf` | P1 | .pdf | 16152.9 | 38 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/1.pdf` | P1 | .pdf | 821.2 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/10.pdf` | P1 | .pdf | 291.8 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/11.pdf` | P1 | .pdf | 319.5 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/12.pdf` | P1 | .pdf | 229.2 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/13.pdf` | P1 | .pdf | 228.2 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/14.pdf` | P1 | .pdf | 232.7 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/2.pdf` | P1 | .pdf | 850.6 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/3.pdf` | P1 | .pdf | 876.8 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/4.pdf` | P1 | .pdf | 567.0 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/5.pdf` | P1 | .pdf | 597.9 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/6.pdf` | P1 | .pdf | 214.4 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/7.pdf` | P1 | .pdf | 696.9 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/8.pdf` | P1 | .pdf | 743.8 | 1 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/9.pdf` | P1 | .pdf | 690.9 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/Requerimento 2-3.pdf` | P1 | .pdf | 4229.2 | 7 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/Requerimento 3-3.pdf` | P1 | .pdf | 3064.9 | 7 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/Requerimento1-3.pdf` | P1 | .pdf | 8801.1 | 24 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/TAF-3 Manual de Treinamento_251119_162144.pdf` | P1 | .pdf | 13884.9 | 50 | 17,739 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (17,739 chars). Avaliar agrupamento. |
| `P1/telefones funcionais Comandantes oficiais cpi-10.pdf` | P1 | .pdf | 475.3 | 1 | 909 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (909 chars). Avaliar agrupamento. |
| `P1/Ten Josemar assinatura email 5 cia.JPG` | P1 | .jpg | 32.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P2/5ª Cia Medidas de Segurança S2.docx` | P2 | .docx | 13.0 | N/A | 973 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (973 chars), avaliar agrupamento. |
| `P2/Denúncia Bar do Max.docx` | P2 | .docx | 59.0 | N/A | 929 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (929 chars), avaliar agrupamento. |
| `P2/Ordem de Serviço nº CoordOpPM-028.21.24, de 15OUT24 (3) (1).pdf` | P2 | .pdf | 642.8 | 3 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P2/OS CPI10-002-30-16 regularização revista de armários.pdf` | P2 | .pdf | 203.6 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P2/OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf` | P2 | .pdf | 1569.8 | 4 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P2/Plano de Chamada/PLANO DE CHAMA.pptx` | P2 | .pptx | 47.1 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Formato de apresentação não suportado. |
| `P2/Plano de Chamada/Plano de Chamada 2019 - 5 CIA (1).doc` | P2 | .doc | 84.0 | N/A | 10,720 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (10,720 chars). Avaliar agrupamento. |
| `P2/Plano de Chamada/Plano de Chamada 2023  - 09AGO23 - 5ª Cia PM.xlsx` | P2 | .xlsx | 109.6 | N/A | 20,752 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P2/Plano de Chamada/Plano de Chamada 5 Cia Nomes.pdf` | P2 | .pdf | 381.3 | 1 | 1,280 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,280 chars), avaliar agrupamento. |
| `P2/Plano de segurança de Bento - 04JUN18.docx` | P2 | .docx | 34.6 | N/A | 6,648 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (6,648 chars), avaliar agrupamento. |
| `P2/Plano de segurança de Rubiácea - 04JUN18 (1).docx` | P2 | .docx | 34.0 | N/A | 6,594 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (6,594 chars), avaliar agrupamento. |
| `P2/Plano de segurança de Rubiácea - 04JUN18.docx` | P2 | .docx | 34.0 | N/A | 6,543 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (6,543 chars), avaliar agrupamento. |
| `P2/PLANO DE SEGURANÇA GUARARAPES 2019.docx` | P2 | .docx | 37.1 | N/A | 10,128 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (10,128 chars). Avaliar agrupamento. |
| `P2/PLANO DE SEGURANÇA VALPARAISO 2019.pdf` | P2 | .pdf | 74.7 | 3 | 5,042 | SIM | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (5,042 chars), avaliar agrupamento. |
| `P2/Pontos de Tráfico Valparaíso 12fev19.docx` | P2 | .docx | 4.7 | N/A | 834 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (834 chars). Avaliar agrupamento. |
| `P2/QTHs.docx` | P2 | .docx | 13.4 | N/A | 1,153 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,153 chars). Avaliar agrupamento. |
| `P2/QUALIFICAÇÃO de fotos.docx` | P2 | .docx | 70.3 | N/A | 652 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (652 chars). Avaliar agrupamento. |
| `P2/Relatorio revista de armario 2018.docx` | P2 | .docx | 22.0 | N/A | 2,732 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,732 chars). Avaliar agrupamento. |
| `P2/Relatório Revista de armario 5ª Cia nov20.pdf` | P2 | .pdf | 85.5 | 2 | 2,117 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,117 chars). Avaliar agrupamento. |
| `P2/Relatório Revista de armario 5ª Cia nov20.xlsx` | P2 | .xlsx | 13.0 | N/A | 2,641 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P2/Relatório Revista de Armários 1º Semestre 2017.docx` | P2 | .docx | 18.9 | N/A | 2,985 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,985 chars). Avaliar agrupamento. |
| `P2/Relação efetivo p2.pdf` | P2 | .pdf | 597.1 | 1 | 1,837 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,837 chars). Avaliar agrupamento. |
| `P2/Revista de armario EFETIVO nov20.xlsx` | P2 | .xlsx | 12.3 | N/A | 2,624 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P2/Solicitação de Mandados 13FEV19 -.docx` | P2 | .docx | 47.7 | N/A | 1,833 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,833 chars). Avaliar agrupamento. |
| `P3/08. Locais de ronda Supervisor Regional - AGO25.pdf` | P3 | .pdf | 423.4 | 1 | 1,085 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,085 chars). Avaliar agrupamento. |
| `P3/2023/ALTERAÇÃO ESCALA DOS GPS.ppt` | P3 | .ppt | 348.5 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Formato de apresentação não suportado. |
| `P3/2023/Apresentação 5 Cia.ppt` | P3 | .ppt | 803.5 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Formato de apresentação não suportado. |
| `P3/2023/Indices 5 Cia 2023.xlsx` | P3 | .xlsx | 25.7 | N/A | 4,879 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2023/PAP 1º 2º GP PM.pdf` | P3 | .pdf | 84.0 | 2 | 2,423 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,423 chars). Avaliar agrupamento. |
| `P3/2023/PAP 2023 Cia PM - Sargenteação.pdf` | P3 | .pdf | 167.1 | 4 | 5,353 | NÃO | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,353 chars). Avaliar agrupamento. |
| `P3/2023/PAP 2023 PEL.pdf` | P3 | .pdf | 55.7 | 4 | 3,892 | NÃO | SIM | PROCEDIMENTAL | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,892 chars). Avaliar agrupamento. |
| `P3/2023/Plano de Comando.xlsx` | P3 | .xlsx | 11.2 | N/A | 916 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2023/ROTINA PAP 07NOV23.xlsx` | P3 | .xlsx | 17.6 | N/A | 4,020 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/20241029_162708.jpg` | P3 | .jpg | 1567.3 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/2024/20241029_162713.jpg` | P3 | .jpg | 1463.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/2024/Ata Reunião com Prefeito Assinada.pdf` | P3 | .pdf | 404.5 | 4 | 0 | NÃO | SIM | MODELO_PRECEDENTE | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/2024/BOS 5ª Cia.xlsx` | P3 | .xlsx | 23.7 | N/A | 5,440 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso 09out24.xlsx` | P3 | .xlsx | 53.5 | N/A | 10,208 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso 26OUT24.xlsx` | P3 | .xlsx | 62.7 | N/A | 12,724 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso 29OUT24.xlsx` | P3 | .xlsx | 53.9 | N/A | 12,738 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso.xlsx` | P3 | .xlsx | 43.5 | N/A | 6,778 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Controle do TDS Treinamento Durante o Serviço.xlsx` | P3 | .xlsx | 20.9 | N/A | 5,935 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Cópia OFÍCIO Reunião Trânsito.pdf` | P3 | .pdf | 50.4 | 1 | 2,540 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,540 chars). Avaliar agrupamento. |
| `P3/2024/e) Valparaíso - Plano de Trabalho Atividade Delegada.docx` | P3 | .docx | 116.1 | N/A | 11,842 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (11,842 chars). Avaliar agrupamento. |
| `P3/2024/f) Valparaíso - Minuta do Convênio Atividade Delegada.docx` | P3 | .docx | 58.0 | N/A | 15,878 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P3/2024/Indices 5 Cia 2024 1 1.xlsx` | P3 | .xlsx | 29.3 | N/A | 10,352 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Of. 158-500-24 - Perturbação do Sossego Avenida.doc` | P3 | .doc | 1069.5 | N/A | 5,030 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,030 chars). Avaliar agrupamento. |
| `P3/2024/Of. 158-500-24 - Perturbação do Sossego Avenida.pdf` | P3 | .pdf | 142.6 | 3 | 5,564 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,564 chars). Avaliar agrupamento. |
| `P3/2024/OFICIO_PROMOTORIA Bento Eleição Carreata_01OUT24.docx` | P3 | .docx | 53.4 | N/A | 4,827 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,827 chars). Avaliar agrupamento. |
| `P3/2024/OFICIO_PROMOTORIA Bento Eleição.pdf` | P3 | .pdf | 240.0 | 2 | 5,506 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,506 chars). Avaliar agrupamento. |
| `P3/2024/OFÍCIO 157 Reunião Prefeito Guararapes.pdf` | P3 | .pdf | 138.3 | 1 | 2,667 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,667 chars). Avaliar agrupamento. |
| `P3/2024/OFÍCIO 2BPMI-0234024 Cessão de Uso de Imóvel Pel PM Valparaíso.doc` | P3 | .doc | 417.5 | N/A | 2,007 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/2024/OFÍCIO 2prefeito transito.docx` | P3 | .docx | 81.7 | N/A | 2,045 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,045 chars). Avaliar agrupamento. |
| `P3/2024/OFÍCIO Conselho Tutelar.docx` | P3 | .docx | 81.6 | N/A | 2,942 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,942 chars). Avaliar agrupamento. |
| `P3/2024/OFÍCIO Conselho Tutelar.pdf` | P3 | .pdf | 116.5 | 2 | 3,593 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,593 chars). Avaliar agrupamento. |
| `P3/2024/OFÍCIO prefeito transito.docx` | P3 | .docx | 90.1 | N/A | 17,281 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (17,281 chars). Avaliar agrupamento. |
| `P3/2024/ofício prefeitura 10out24.pdf` | P3 | .pdf | 530.8 | 1 | 2,051 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,051 chars). Avaliar agrupamento. |
| `P3/2024/Ofício Vigilância Sanitária 1.docx` | P3 | .docx | 731.4 | N/A | 1,975 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,975 chars). Avaliar agrupamento. |
| `P3/2024/Painel de Produtitividade.xlsx` | P3 | .xlsx | 14.9 | N/A | 2,884 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2024/Reuniao Prefeitura de Guararapes e Polícia Militar 24SET24.doc` | P3 | .doc | 101.5 | N/A | 10,682 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (10,682 chars). Avaliar agrupamento. |
| `P3/2025/Controle do TDS Treinamento Durante o Serviço.xlsx` | P3 | .xlsx | 20.9 | N/A | 5,935 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2025/Indices 5 Cia 2025.xlsx` | P3 | .xlsx | 41.3 | N/A | 15,171 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2025/Material de orientação para a condução de Escolares (1).pdf` | P3 | .pdf | 125.4 | 5 | 9,662 | NÃO | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,662 chars). Avaliar agrupamento. |
| `P3/2025/OFICIO FESTA DO PEÃO Rubiácea 2025.docx` | P3 | .docx | 130.8 | N/A | 5,191 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,191 chars). Avaliar agrupamento. |
| `P3/2025/Ofício MP - Perturbação do Sossego.docx` | P3 | .docx | 91.6 | N/A | 3,870 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,870 chars). Avaliar agrupamento. |
| `P3/2025/Ofício MP - Perturbação do Sossego.pdf` | P3 | .pdf | 113.3 | 2 | 4,158 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,158 chars). Avaliar agrupamento. |
| `P3/2025/Ofício MP - veículos abandonados.docx` | P3 | .docx | 91.8 | N/A | 4,817 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,817 chars). Avaliar agrupamento. |
| `P3/2025/Ofício MP - veículos abandonados.pdf` | P3 | .pdf | 115.6 | 2 | 5,152 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,152 chars). Avaliar agrupamento. |
| `P3/2025/OFÍCIO Prefeito Guararapes Festa Folclore.pdf` | P3 | .pdf | 97.4 | 2 | 5,229 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,229 chars). Avaliar agrupamento. |
| `P3/2025/OFÍCIO Prefeito Guararapes Festa Folclore.rtf` | P3 | .rtf | 250.4 | N/A | 4,984 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,984 chars). Avaliar agrupamento. |
| `P3/2025/OFÍCIO Transito Reveillon Guararapes.docx` | P3 | .docx | 81.7 | N/A | 2,963 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,963 chars). Avaliar agrupamento. |
| `P3/2025/OFÍCIO Transito Reveillon Valparaiso.docx` | P3 | .docx | 81.9 | N/A | 3,449 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,449 chars). Avaliar agrupamento. |
| `P3/2025/Parte 2BPMI 182-500-25.pdf` | P3 | .pdf | 739.5 | 2 | 3,948 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,948 chars). Avaliar agrupamento. |
| `P3/2025/PARTE Nº 2BPMI-219-500-25 - Comunicação de Fato.docx` | P3 | .docx | 61.8 | N/A | 3,265 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,265 chars). Avaliar agrupamento. |
| `P3/2025/PARTE Nº 2BPMI-XX-500-25 - Apresentação de ocorrência na Polícia Civil.docx` | P3 | .docx | 60.3 | N/A | 1,896 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,896 chars). Avaliar agrupamento. |
| `P3/2025/PARTE_2BPMI_DEJEM_Valparaiso.docx` | P3 | .docx | 63.9 | N/A | 5,754 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,754 chars). Avaliar agrupamento. |
| `P3/2025/Pauta Reuniao Sobre Rodeio 2025 RUB.docx` | P3 | .docx | 15.5 | N/A | 434 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (434 chars). Avaliar agrupamento. |
| `P3/2025/Planejamento Atividade Delegada Arraia Bento.xlsx` | P3 | .xlsx | 17.7 | N/A | 3,553 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2025/Portaria Detran Transporte de Escolar Nº 11, DE 10 DE NOVEMBRO DE 2023.pdf` | P3 | .pdf | 482.0 | 4 | 3,730 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,730 chars). Avaliar agrupamento. |
| `P3/2025/Programação Fim de ano 5ª Cia.xlsx` | P3 | .xlsx | 21.0 | N/A | 6,937 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 08ago25 N Luzitânia e S A Aracanguá.doc` | P3 | .doc | 131.5 | N/A | 8,150 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,150 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 08ago25.pdf` | P3 | .pdf | 120.8 | 3 | 8,171 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,171 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 11abr25.doc` | P3 | .doc | 131.5 | N/A | 8,346 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,346 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 11abr25.pdf` | P3 | .pdf | 179.6 | 3 | 8,367 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,367 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 15fev25 Auriflama e G Salgado.doc` | P3 | .doc | 130.5 | N/A | 8,030 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,030 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 15fev25 Auriflama e G Salgado.pdf` | P3 | .pdf | 120.2 | 3 | 8,051 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,051 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 22NOV25 Valparaíso e Bento de Abreu.doc` | P3 | .doc | 128.5 | N/A | 8,086 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,086 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 22NOV25 Valparaíso e Bento de Abreu.pdf` | P3 | .pdf | 56.6 | 3 | 7,968 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,968 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 23ago25 Araçatuba Braúna.doc` | P3 | .doc | 131.5 | N/A | 8,194 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,194 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 23ago25.pdf` | P3 | .pdf | 120.6 | 3 | 8,213 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,213 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 29NOV25 Castilho e Mirandópolis.doc` | P3 | .doc | 129.5 | N/A | 8,034 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,034 chars). Avaliar agrupamento. |
| `P3/2025/Relatório Ronda do Oficial  Supervisor Regional 29NOV25.pdf` | P3 | .pdf | 120.3 | 3 | 8,055 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,055 chars). Avaliar agrupamento. |
| `P3/2025/sugestao policiamento.docx` | P3 | .docx | 16.6 | N/A | 454 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (454 chars), avaliar agrupamento. |
| `P3/2025/Tabela de indicadores criminais e operacionais 2023–2024 – 2025 - CAPSSP-SP.pdf` | P3 | .pdf | 128.5 | 2 | 4,037 | SIM | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (4,037 chars), avaliar agrupamento. |
| `P3/2025/Tabela_de_indicadores_criminais_2023_2024_2025_CAPSSP-SP.pdf` | P3 | .pdf | 75.0 | 1 | 2,409 | SIM | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,409 chars), avaliar agrupamento. |
| `P3/2025/Tabela_de_indicadores_criminais_e_operacionais_2023_2024_2025_CAPSSP-SP.xlsx` | P3 | .xlsx | 24.1 | N/A | 4,452 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2025/Tabela_de_indicadores_operacionais_2023_2024_2025_CAPSSP-SP.pdf` | P3 | .pdf | 63.3 | 1 | 1,628 | SIM | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,628 chars), avaliar agrupamento. |
| `P3/2026/Balanço Atividade Delegada (1).xlsx` | P3 | .xlsx | 18.2 | N/A | 2,556 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2026/Indices 5 Cia 2026.xlsx` | P3 | .xlsx | 39.3 | N/A | 11,712 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/2026/Oficio 01.pdf` | P3 | .pdf | 71.5 | 2 | 4,948 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,948 chars). Avaliar agrupamento. |
| `P3/2026/OFICIO_Final_Paulistao_2026.pdf` | P3 | .pdf | 119.2 | 3 | 7,378 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,378 chars). Avaliar agrupamento. |
| `P3/2026/Oficio_Terezinha Delegada.docx` | P3 | .docx | 28.9 | N/A | 3,874 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,874 chars). Avaliar agrupamento. |
| `P3/2026/Oficio_Terezinha Delegada.pdf` | P3 | .pdf | 94.4 | 2 | 4,124 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,124 chars). Avaliar agrupamento. |
| `P3/2026/OFÍCIO Carnaval Bento de Abreu.pdf` | P3 | .pdf | 95.1 | 2 | 4,296 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,296 chars). Avaliar agrupamento. |
| `P3/2026/OFÍCIO Carnaval Bento de Abreu.rtf` | P3 | .rtf | 228.3 | N/A | 4,052 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,052 chars). Avaliar agrupamento. |
| `P3/2026/Ordem de Serviço Patrulhamento Escolar.docx` | P3 | .docx | 116.0 | N/A | 2,144 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,144 chars). Avaliar agrupamento. |
| `P3/2026/Ordem de Serviço Patrulhamento Escolar.pdf` | P3 | .pdf | 110.2 | 2 | 2,602 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,602 chars). Avaliar agrupamento. |
| `P3/2026/Proposta_Atividade_Delegada_Bento de Abreu.pdf` | P3 | .pdf | 29.5 | 2 | 4,302 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,302 chars). Avaliar agrupamento. |
| `P3/2026/Proposta_Atividade_Delegada_Final.docx` | P3 | .docx | 18.6 | N/A | 4,172 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,172 chars). Avaliar agrupamento. |
| `P3/2026/Proposta_Atividade_Delegada_Guararapes.docx` | P3 | .docx | 20.4 | N/A | 6,035 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,035 chars). Avaliar agrupamento. |
| `P3/2026/Proposta_Atividade_Delegada_Guararapes_Comunitaria.pdf` | P3 | .pdf | 84.4 | 2 | 4,475 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,475 chars). Avaliar agrupamento. |
| `P3/2026/Relatorio_de_Ronda_-_CPI-10_assinado.pdf` | P3 | .pdf | 148.8 | 3 | 7,296 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,296 chars). Avaliar agrupamento. |
| `P3/2026/Relatorio_Ronda_do_Oficial_Supervisor_Regional_06mar26.pdf` | P3 | .pdf | 157.5 | 3 | 7,973 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,973 chars). Avaliar agrupamento. |
| `P3/2026/Relatório Ronda do Oficial  Supervisor Regional 06mar26.doc` | P3 | .doc | 128.5 | N/A | 8,089 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,089 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Autoridades - 3ª Cia.xlsx` | P3 | .xlsx | 11.5 | N/A | 2,243 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2021/Cumprimento Mandados de Busca 25fev21.pdf` | P3 | .pdf | 1794.1 | 4 | 9,502 | NÃO | SIM | JURISPRUDENCIA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,502 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Dados estatísticos 3 Cia.xlsx` | P3 | .xlsx | 23.9 | N/A | 10,034 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2021/ORDEM DE SERVIÇO 016-300-21 - Operação Narco Brasil.doc` | P3 | .doc | 63.0 | N/A | 3,099 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,099 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 04set21 - CPI-10.docx` | P3 | .docx | 36.8 | N/A | 32,041 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 04set21 - CPI-10.pdf` | P3 | .pdf | 177.7 | 3 | 9,163 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,163 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 06ago21 - CPI-10.docx` | P3 | .docx | 36.3 | N/A | 29,472 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 06ago21 - CPI-10.pdf` | P3 | .pdf | 178.4 | 3 | 8,466 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,466 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 09out21 - CPI-10.docx` | P3 | .docx | 36.1 | N/A | 28,289 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 09out21 - CPI-10.pdf` | P3 | .pdf | 176.4 | 3 | 8,421 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,421 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 10jul21 - CPI-10.docx` | P3 | .docx | 35.1 | N/A | 31,371 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 19nov21 - CPI-10.docx` | P3 | .docx | 36.2 | N/A | 27,276 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 19nov21 - CPI-10.pdf` | P3 | .pdf | 177.3 | 3 | 8,205 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,205 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 25dez21 - CPI-10.docx` | P3 | .docx | 35.8 | N/A | 28,251 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2021/Relatório Ronda Supervisor Regional 25dez21 - CPI-10.pdf` | P3 | .pdf | 176.8 | 3 | 8,432 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,432 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relação PMs deslocamento.xlsx` | P3 | .xlsx | 21.8 | N/A | 5,925 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2021/Relátorio Indices 3ª Cia abrmai 21.docx` | P3 | .docx | 16.8 | N/A | 6,343 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (6,343 chars), avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relátorio Indices 3ª Cia junjul 21.docx` | P3 | .docx | 17.6 | N/A | 5,408 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (5,408 chars), avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relátorio Indices 3ª Cia novdez 21.docx` | P3 | .docx | 18.0 | N/A | 7,173 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,173 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Relátorio Indices 3ª Cia setout 21.docx` | P3 | .docx | 18.4 | N/A | 6,547 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,547 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2021/Reunião sobre BO Social 15mar21.docx` | P3 | .docx | 13.2 | N/A | 585 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (585 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Ata Reuniao com Cap sobre nova sistematica de plantao da pc.docx` | P3 | .docx | 13.3 | N/A | 905 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (905 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Controle Agro SP Mais Seguro.pdf` | P3 | .pdf | 152.3 | 1 | 2,025 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (2,025 chars), avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Controle enem.xlsx` | P3 | .xlsx | 10.9 | N/A | 549 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Cópia Controle da DEJEM de Oficiais - 2022.xlsx` | P3 | .xlsx | 79.0 | N/A | 27,999 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/1ª Cia - 01out Guarda de Urna.pdf` | P3 | .pdf | 59.6 | 1 | 8,775 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,775 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Eleições/1ª Cia - 02out LOCAIS DE VOTAÇÃO.pdf` | P3 | .pdf | 75.7 | 1 | 11,424 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (11,424 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Eleições/1ª Cia - 02out RECOLHA DE URNAS.pdf` | P3 | .pdf | 38.8 | 1 | 6,031 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,031 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Eleições/1ª Cia - DISTRIBUIÇÃO DE URNAS - 01OUT.pdf` | P3 | .pdf | 38.4 | 1 | 6,191 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,191 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Eleições/2ª CIA - Escala FINAL.pdf` | P3 | .pdf | 122.3 | 5 | 18,091 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/2ª CIA - Escala FINAL.xlsx` | P3 | .xlsx | 41.2 | N/A | 22,723 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/3ª CIa - Escala Eleiçoes 3ª Cia 02OUT22 FINAL.xlsx` | P3 | .xlsx | 28.1 | N/A | 9,679 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/4ª CIA - Escala FINAL.pdf` | P3 | .pdf | 247.8 | 1 | 6,299 | NÃO | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/5ª Cia - Escala Atual Eleições 2022 - 5ª Cia (final).xlsx` | P3 | .xlsx | 31.0 | N/A | 12,606 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/AMBIENTAL APOIO ELEIÇÕES 2BPMI.xlsx` | P3 | .xlsx | 10.5 | N/A | 4,676 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/AMBIENTAL ELEIÇÕES 2BPMI.pdf` | P3 | .pdf | 418.9 | 1 | 4,583 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,583 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Eleições/CPI - 10 - Escala DEFINITIVA Eleição Policiais com Restrição.pdf` | P3 | .pdf | 23.4 | 1 | 2,274 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/ESCALA DE OFICIAIS E APOIO.xlsx` | P3 | .xlsx | 10.7 | N/A | 3,263 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/Escala DEFINITIVA Eleição Policiais com Restrição.xlsx` | P3 | .xlsx | 10.5 | N/A | 2,522 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/Escala GERAL (Salvo automaticamente).xlsx` | P3 | .xlsx | 88.7 | N/A | 54,135 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/OFICIAIS E APOIO.pdf` | P3 | .pdf | 26.7 | 1 | 2,868 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,868 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Eleições/Problemas sugestoes.xlsx` | P3 | .xlsx | 8.6 | N/A | 673 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/RODOVIARIO APOIO ELEIÇÕES 2BPMI.xlsx` | P3 | .xlsx | 9.9 | N/A | 1,982 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/RODOVIARIO ELEIÇÕES 2BPMI.pdf` | P3 | .pdf | 18.3 | 1 | 1,776 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,776 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Parte CFP 2bpmi 057-30-22.pdf` | P3 | .pdf | 721.5 | 2 | 3,501 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,501 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional 12ago22.doc` | P3 | .doc | 130.5 | N/A | 8,618 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,618 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional 12ago22.pdf` | P3 | .pdf | 188.8 | 3 | 8,627 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,627 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional 19fev22.doc` | P3 | .doc | 128.0 | N/A | 8,761 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,761 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional 19fev22.pdf` | P3 | .pdf | 189.1 | 3 | 8,772 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,772 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional 23abr22.doc` | P3 | .doc | 129.5 | N/A | 8,517 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,517 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional 23abr22.pdf` | P3 | .pdf | 188.9 | 3 | 8,526 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,526 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda do Oficial  Supervisor Regional do CPI-10 - 12FEV22.doc` | P3 | .doc | 141.0 | N/A | 9,041 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,041 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relatório Ronda Supervisor Regional 28jan22 - CPI-10.docx` | P3 | .docx | 44.5 | N/A | 28,940 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Anos Anteriores/2022/Relatório Ronda Supervisor Regional 28jan22 - CPI-10.pdf` | P3 | .pdf | 187.9 | 3 | 8,508 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,508 chars). Avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Relação Delegada.pdf` | P3 | .pdf | 183.5 | 1 | 1,424 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,424 chars), avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Resumo delegada veiculo agro.docx` | P3 | .docx | 13.8 | N/A | 767 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (767 chars), avaliar agrupamento. |
| `P3/Anos Anteriores/2022/Vtr Pol Rural - 28BPMI.xlsx` | P3 | .xlsx | 10.9 | N/A | 924 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Manual de Operação SGO_240822_095708.pdf` | P3 | .pdf | 1971.9 | 23 | 30,135 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/Medidas Para Implantação do Termo Circunstanciado TC - ORDEM PREPARATÓRIA Nº PM3-0010224.pdf` | P3 | .pdf | 343.7 | 12 | 30,236 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/NI_001_02_15_resolução 57.pdf` | P3 | .pdf | 7765.2 | 46 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.pdf` | P3 | .pdf | 283.4 | 3 | 1,754 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI - B - Exercícios de aquecimento prévio de condução de viatura policial de duas rodas.pdf` | P3 | .pdf | 709.4 | 6 | 6,725 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,725 chars). Avaliar agrupamento. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI - C - Placar de acidente de trânsito com viatura.pdf` | P3 | .pdf | 202.9 | 1 | 589 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI Nº PM3-002-02-17 - Acidente Vtr.pdf` | P3 | .pdf | 287.8 | 11 | 26,064 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/OSPM3_008_02_17_CIRCULAR.pdf` | P3 | .pdf | 172.9 | 2 | 3,899 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,899 chars). Avaliar agrupamento. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf` | P3 | .pdf | 77.8 | 2 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/OS/Nota de Instrução Esbulho Possessório.pdf` | P3 | .pdf | 512.9 | 8 | 21,275 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/Nota de Instrução Operação Impacto Pronta Resposta.pdf` | P3 | .pdf | 344.0 | 9 | 23,554 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/Nota de Instrução PM3-001-01-21 Violencia Domestica patrulha maria da penha.pdf` | P3 | .pdf | 241.1 | 12 | 26,955 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/ODS/Nota de Serviço nº CoordOpPM-001-03-16 Operação Direção Segura Integrada - I-2016.pdf` | P3 | .pdf | 65.8 | 2 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/ODS/PM3_001_02_14.pdf` | P3 | .pdf | 280.1 | 6 | 13,660 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (13,660 chars), avaliar agrupamento. |
| `P3/OS/ODS/Resolução CONTRAN nº 432-13.pdf` | P3 | .pdf | 1441.4 | 10 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf` | P3 | .pdf | 336.7 | 2 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/Ordem de Serviço Resolução Contran 810 de 15DEZ20.doc` | P3 | .doc | 97.0 | N/A | 1,936 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,936 chars). Avaliar agrupamento. |
| `P3/OS/Ordem de Serviço Resolução Contran 810 de 15DEZ20.pdf` | P3 | .pdf | 92.5 | 1 | 2,348 | SIM | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,348 chars). Avaliar agrupamento. |
| `P3/OS/Ordem sobre policiamento em eventos.pdf` | P3 | .pdf | 775.1 | 16 | 37,703 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/OS 4 Cia 038-400-20 parte 01.jpeg` | P3 | .jpeg | 108.1 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS 4 Cia 038-400-20 parte 2 de 2.jpeg` | P3 | .jpeg | 92.7 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS 4 Cia 041-400-20 parte 1 de 2].jpeg` | P3 | .jpeg | 128.7 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS 4 Cia 041-400-20 parte 2 de 2.jpeg` | P3 | .jpeg | 77.6 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS NOta urgente copom OSv Coord Op PM 005 04 19 - Ocor de grav ou repercussão (1).pdf` | P3 | .pdf | 2414.2 | 3 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/OSPM3_003_03_14-1.pdf` | P3 | .pdf | 71.4 | 5 | 11,810 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (11,810 chars). Avaliar agrupamento. |
| `P3/OS/PM3-002_02_14 Norma Atividade Delegada.pdf` | P3 | .pdf | 939.1 | 20 | 46,746 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/PM3_001_02_21 ocorrencias tentativa de suicidio.pdf` | P3 | .pdf | 222.2 | 4 | 8,768 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,768 chars). Avaliar agrupamento. |
| `P3/OS/PM3_002_02_23 Diretriz Ações Especiais de Polícia BAEP.pdf` | P3 | .pdf | 651.7 | 18 | 36,723 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/OS/PM3_010_02_19.pdf` | P3 | .pdf | 214.3 | 2 | 4,344 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,344 chars). Avaliar agrupamento. |
| `P3/OS/Portaria Conjunta nº PC_PM – 1 resolução 57.pdf` | P3 | .pdf | 101.4 | 2 | 5,078 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,078 chars). Avaliar agrupamento. |
| `P3/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf` | P3 | .pdf | 77.8 | 2 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/OS/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` | P3 | .pdf | 951.0 | 37 | 82,004 | NÃO | NÃO | - | `PRONTO_SEM_SEGMENTACAO` | Tamanho ideal (82,004 chars), pronto para indexação. |
| `P3/OS/Resolução SSP-57.pdf` | P3 | .pdf | 100.7 | 2 | 5,551 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,551 chars). Avaliar agrupamento. |
| `P3/OS/Revogação da OS Cavalo de aço.pdf` | P3 | .pdf | 92.0 | 1 | 1,803 | SIM | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,803 chars). Avaliar agrupamento. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/cópia do e-mail sobre NI PM3-002-02-17.pdf` | P3 | .pdf | 215.8 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/Deslocamentos de Viatura - preferencia e prioridades no transito..pdf` | P3 | .pdf | 401.3 | 5 | 9,031 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,031 chars). Avaliar agrupamento. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/MSG17-152- Circular.pdf` | P3 | .pdf | 193.4 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.docx` | P3 | .docx | 1453.1 | N/A | 2,372 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.pdf` | P3 | .pdf | 872.1 | 3 | 0 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - B - Exercícios de aquecimento prévio de condução de viatura policial de duas rodas.pdf` | P3 | .pdf | 1817.5 | 6 | 0 | NÃO | NÃO | - | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - C - Placar de acidente de trânsito com viatura.pdf` | P3 | .pdf | 260.0 | 1 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17 (1).docx` | P3 | .docx | 52.5 | N/A | 1,735 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,735 chars). Avaliar agrupamento. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf` | P3 | .pdf | 3759.7 | 11 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/OS 023-30-17 - SISTEMATICA DE PREVENÇÃO DE ACIDENTES DE TRÂNSITO.pdf` | P3 | .pdf | 86.7 | 2 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/Placar de acidente de trânsito com viatura (2).jpg` | P3 | .jpg | 163.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/Placar de acidente de Viatura.docx` | P3 | .docx | 456.3 | N/A | 200 | N/A | NÃO | - | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/Outros/Convênios Prontos/Atividade Delegada Bento de Abreu (GS 413_23).pdf` | P3 | .pdf | 628.0 | 17 | 40,532 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Guararapes (GS 714_23).pdf` | P3 | .pdf | 360.9 | 20 | 32,240 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Guararapes.pdf` | P3 | .pdf | 360.9 | 20 | 32,240 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Olimpia.pdf` | P3 | .pdf | 2506.9 | 27 | 33,242 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Rio Preto.pdf` | P3 | .pdf | 239.0 | 14 | 33,333 | SIM | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Sao José dos Campos.pdf` | P3 | .pdf | 1067.3 | 22 | 56,157 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Sao Paulo.pdf` | P3 | .pdf | 942.5 | 59 | 112,565 | SIM | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Atividade Delegada Valparaiso (GS 058_22).pdf` | P3 | .pdf | 9261.9 | 16 | 4,924 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,924 chars). Avaliar agrupamento. |
| `P3/Outros/Convênios Prontos/Atividade Delegada Valparaiso.pdf` | P3 | .pdf | 233.9 | 14 | 31,506 | SIM | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/Lei Atividade Delegada Valparaíso.pdf` | P3 | .pdf | 1402.2 | 2 | 668 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (668 chars), avaliar agrupamento. |
| `P3/Outros/Convênios Prontos/PMESPEXP202323709A.pdf` | P3 | .pdf | 9155.9 | 56 | 118,876 | SIM | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Convênios Prontos/SEI_057.00033862_2023_40 Processo Completo Guararapes.pdf` | P3 | .pdf | 11098.2 | 130 | 267,794 | SIM | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (267,794 chars). Precisa segmentar. |
| `P3/Outros/Organograma  2º BPMI.xlsx` | P3 | .xlsx | 25.1 | N/A | 5,511 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Outros/Preleção/Codigo para tipificação de ocorrências 1961_190416104118_001.pdf` | P3 | .pdf | 506.5 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf` | P3 | .pdf | 487.8 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Desp Nº PM3 005 02 19 - Acesso a dados em celular.pdf` | P3 | .pdf | 1349.1 | 2 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Fiscalização Ciclo elétricos.pdf` | P3 | .pdf | 201.7 | 2 | 4,244 | NÃO | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,244 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Fiscalização de ciclomotores.pdf` | P3 | .pdf | 21.1 | 1 | 3,176 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,176 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Instrução Lei Maria da Penha/Resumo da instrução on line.docx` | P3 | .docx | 12.0 | N/A | 259 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (259 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 1 Cia.jpeg` | P3 | .jpeg | 121.3 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 2 BPMI.jpeg` | P3 | .jpeg | 190.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 2 Cia.jpeg` | P3 | .jpeg | 133.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 3 Cia.jpeg` | P3 | .jpeg | 137.5 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 4 Cia.jpeg` | P3 | .jpeg | 132.6 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 5 Cia.jpeg` | P3 | .jpeg | 126.4 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapas Copom 2 BPMI.pdf` | P3 | .pdf | 1475.3 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Mapas Copom/Mapas Copom 2BPMI.jpg` | P3 | .jpg | 2081.9 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/orientações uso de granadas espargidores munições químicas na PM elastômero de fev de 2020 1929.txt` | P3 | .txt | 0.1 | N/A | 78 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (78 chars), avaliar agrupamento. |
| `P3/Outros/Preleção/PNEUS.doc.docx` | P3 | .docx | 699.1 | N/A | 1,654 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,654 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Portaria Cmt G nº PM4-001_1.2_16 atualizada até 05JUL17.pdf` | P3 | .pdf | 354.2 | 59 | 116,578 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Preleção/Reintegração de posse OS/An A_Conceituacao.pdf` | P3 | .pdf | 419.9 | 6 | 12,674 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (12,674 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Reintegração de posse OS/An B_Rel prov previas obrigat Op Reint Posse.pdf` | P3 | .pdf | 189.7 | 2 | 1,979 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,979 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Reintegração de posse OS/An C_Plan Dig Análise Riscos Gerenciais_assinatura.pdf` | P3 | .pdf | 181.6 | 1 | 638 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (638 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Reintegração de posse OS/An D_Modelo de Plano de Acao.pdf` | P3 | .pdf | 477.1 | 1 | 897 | NÃO | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P3/Outros/Preleção/Reintegração de posse OS/An E_ Fluxograma Op Reintegração Posse.pdf` | P3 | .pdf | 187.7 | 1 | 1,273 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,273 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Reintegração de posse OS/COC15-004 assinado no original.pdf` | P3 | .pdf | 231.5 | 2 | 3,178 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,178 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Reintegração de posse OS/PM3_009_02_14 Com alterações.pdf` | P3 | .pdf | 425.3 | 14 | 35,987 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Preleção/Relatorio de Avarias.docx` | P3 | .docx | 14.3 | N/A | 2,577 | N/A | SIM | PROCEDIMENTAL | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,577 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Resolucao7292018_nova.pdf` | P3 | .pdf | 883.6 | 26 | 58,885 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Preleção/RESOLUÇÃO Nº 741, DE 17 DE SETEMBRO DE 2018 - Diário Oficial da União - Imprensa.pdf` | P3 | .pdf | 128.3 | 2 | 3,279 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,279 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Screenshot_20181025-053010_WhatsApp.jpg` | P3 | .jpg | 557.7 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Sinopse nº 02-18 Fiscal. de Ciclomotor.pdf` | P3 | .pdf | 253.3 | 4 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Transporte de Escolar.pdf` | P3 | .pdf | 169.4 | 2 | 4,337 | NÃO | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,337 chars). Avaliar agrupamento. |
| `P3/Outros/Preleção/Video Treinamento Zona de Perigo e Zona de Segurança 2018.mp4` | P3 | .mp4 | 34845.1 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de controle do indexador. |
| `P3/Outros/Projeto VIDA/BTL - CADASTRO PM.xlsx` | P3 | .xlsx | 17.2 | N/A | 5,735 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/Cap_PM_Ferrarez_Dissertação_CAO24.pdf` | P3 | .pdf | 1691.5 | 124 | 245,958 | NÃO | NÃO | - | `PRECISA_SEGMENTACAO` | Muito longo (245,958 chars). Necessita segmentação. |
| `P3/Outros/Projeto VIDA/CIAS - CADASTRO PM.xlsx` | P3 | .xlsx | 37.2 | N/A | 18,522 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/Controle da implantação.xlsx` | P3 | .xlsx | 10.5 | N/A | 504 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/CPI10 - CADASTRO PM.xlsx` | P3 | .xlsx | 55.3 | N/A | 7,141 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/Decisão Corregedor TJ implantação estadual - 23abr21.pdf` | P3 | .pdf | 242.2 | 6 | 12,728 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (12,728 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Decisão Corregedoria - Autoriza Implantação Projeto V.I.D.A. Araçatuba - 14-03-2023 - Processo 2023-23707  1.pdf` | P3 | .pdf | 54.5 | 2 | 3,577 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,577 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Manual de Administrador Policia Militar Nov21.pdf` | P3 | .pdf | 3441.7 | 64 | 37,635 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Projeto VIDA/Manual de usua_rio app 1.2.1 Set21.pdf` | P3 | .pdf | 3713.1 | 43 | 13,464 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (13,464 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Manual de usuário app 1.2.1 Set21.pdf` | P3 | .pdf | 3713.1 | 43 | 13,464 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (13,464 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Matéria Projeto Vida DJE TJSP 04-08-2021-1 (1).pdf` | P3 | .pdf | 1831.1 | 2 | 5,636 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,636 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/null (1).pdf` | P3 | .pdf | 2686.9 | 26 | 34,859 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Outros/Projeto VIDA/null.pdf` | P3 | .pdf | 659.2 | 2 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Projeto VIDA/OF_23_143_Informações_para_implantação_do_Projeto_VIDA_-_02OUT23.doc` | P3 | .doc | 75.5 | N/A | 3,917 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,917 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Oficio Juízo de direito 1 Vara Coamrca de Andradina (1).pdf` | P3 | .pdf | 1097.1 | 1 | 1,669 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,669 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/OFÍCIO - IMPLANTAÇÃO PROJETO V.I.D.A - COMARCA DE ARAÇATUBA - 2ª RAJ - com anexos.pdf` | P3 | .pdf | 1231.2 | 10 | 12,728 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (12,728 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Ofício 179-100-23 Descumprimento de saída temporária 21set23 (1).pdf` | P3 | .pdf | 251.0 | 2 | 3,049 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,049 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/OFÍCIO DA CPI 10 à 2ª RAJ - Projeto V.I.D.A.pdf` | P3 | .pdf | 773.2 | 2 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Projeto VIDA/Ofício Projeto VIDA - General Salgado.docx` | P3 | .docx | 44.2 | N/A | 2,515 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,515 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Ofício Projeto Vida - Guararapes.docx` | P3 | .docx | 93.2 | N/A | 6,080 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,080 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Ofício Projeto Vida - Guararapes.pdf` | P3 | .pdf | 117.2 | 3 | 6,409 | SIM | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,409 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Ofício Projeto Vida - Valparaiso.docx` | P3 | .docx | 93.4 | N/A | 6,072 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,072 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/Ofício Projeto Vida - Valparaiso.pdf` | P3 | .pdf | 53.8 | 3 | 6,262 | SIM | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (6,262 chars). Avaliar agrupamento. |
| `P3/Outros/Projeto VIDA/PROJETO VIDA.docx` | P3 | .docx | 7178.9 | N/A | 787 | N/A | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (787 chars). Avaliar agrupamento. |
| `P3/Outros/Relatório de Utilização de AIN.pdf` | P3 | .pdf | 134.0 | 2 | 7,725 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,725 chars). Avaliar agrupamento. |
| `P3/Outros/Relatório Jurídico-Operacional – Interdição de Baile Clandestino.pdf` | P3 | .pdf | 38.2 | 5 | 13,954 | SIM | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (13,954 chars). Avaliar agrupamento. |
| `P3/Outros/Relatório Jurídico-Operacional_ Interdição de Baile Clandestino em Guararapes-SP.pdf` | P3 | .pdf | 28.9 | 3 | 10,078 | SIM | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (10,078 chars), avaliar agrupamento. |
| `P3/Outros/Relatório Ronda do Oficial  Supervisor Regional do CPI-10 - MODELO 2022.docx` | P3 | .docx | 41.1 | N/A | 23,768 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Modelo de redação / formulário. |
| `P3/Outros/Relação AISP 2º BPM-I.pdf` | P3 | .pdf | 16.9 | 1 | 916 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (916 chars), avaliar agrupamento. |
| `P3/Outros/Retificação BOPM.txt` | P3 | .txt | 1.7 | N/A | 1,689 | N/A | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/Outros/Senhas p3.docx` | P3 | .docx | 13.2 | N/A | 302 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (302 chars), avaliar agrupamento. |
| `P3/PAP 2023 PEL.pdf` | P3 | .pdf | 55.7 | 4 | 3,892 | NÃO | SIM | PROCEDIMENTAL | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,892 chars). Avaliar agrupamento. |
| `P3/Pauta Reunião Efetivo.docx` | P3 | .docx | 13.2 | N/A | 42 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (42 chars), avaliar agrupamento. |
| `P3/Planejamento Atividade Delegada orçamento.xlsx` | P3 | .xlsx | 10.2 | N/A | 634 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P3/POPs/bg22036a_POP_4.01.00_Acompanhamento_e_Cerco.pdf` | P3 | .pdf | 742.8 | 16 | 30,033 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/bg22068a_POP_5_12_00_Emprego_de_municao_elastomero.pdf` | P3 | .pdf | 673.2 | 14 | 27,137 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/bg22147b.pdf (PROTEGIDO).pdf` | P3 | .pdf | 905.3 | 20 | 48,433 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/policiamento com motocicleta.pdf` | P3 | .pdf | 8268.9 | 71 | 125,360 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-1.01.00-Abordagem-de-Pessoas-a-Pe.pdf` | P3 | .pdf | 1515.2 | 50 | 109,359 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-1.02.00-AbordagemPolVtr4Rodas.pdf` | P3 | .pdf | 1797.6 | 40 | 71,017 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-1.05.00-Vistoria-de-veiculos.pdf` | P3 | .pdf | 822.2 | 21 | 32,019 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-1.06.00-Drogas-Ilicitas_Bol-G-033_25.pdf` | P3 | .pdf | 400.2 | 10 | 20,887 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-2.01.00-Veículo-Localizado.pdf` | P3 | .pdf | 162.2 | 7 | 14,122 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (14,122 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-2.02.00-Desinteligência.pdf` | P3 | .pdf | 159.1 | 6 | 11,410 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (11,410 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-2.03.00-Pertubacao-do-sossego-publico.pdf` | P3 | .pdf | 260.0 | 7 | 13,971 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (13,971 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-2.04.00-Alarme-disparado.pdf` | P3 | .pdf | 559.1 | 9 | 14,799 | NÃO | SIM | PROCEDIMENTAL | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (14,799 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-2.05.00-Preservacao-Local-de-Crime.pdf` | P3 | .pdf | 79.6 | 9 | 20,018 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-3.01.00-Acidente-de-Transito.pdf` | P3 | .pdf | 731.4 | 16 | 33,211 | NÃO | SIM | PROCEDIMENTAL | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P3/POPs/Processo-3.02.00-Ocorrencia-Envolvendo-Autoridades.pdf` | P3 | .pdf | 196.0 | 12 | 27,910 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` | P3 | .pdf | 839.7 | 37 | 82,004 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-3.04.00-Atendimento-Ocor-Horario-Folga.pdf` | P3 | .pdf | 185.5 | 11 | 21,252 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-3.05.00-Morte-de-PM.pdf` | P3 | .pdf | 346.3 | 4 | 4,781 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,781 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-3.06.00-Ocorrencia-c-bombas.pdf` | P3 | .pdf | 167.0 | 7 | 15,965 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (15,965 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-4.02.00-Bloqueio-Policial.pdf` | P3 | .pdf | 1035.7 | 25 | 45,945 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-4.04.00-Cumprimento-de-Mandado-Judicial.pdf` | P3 | .pdf | 255.8 | 12 | 30,017 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-4.05.00-Atuação-de-Força-Tática-em-ações-de-contenção.pdf` | P3 | .pdf | 362.0 | 17 | 31,576 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-4.06.00-Atuação-em-manifestações-públicas.pdf` | P3 | .pdf | 892.2 | 18 | 40,873 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.03.00_Uso-de-algemas.pdf` | P3 | .pdf | 1295.4 | 27 | 34,941 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.05.00-Deslocamento-de-Vtr-em-Patrulhamento.pdf` | P3 | .pdf | 781.1 | 10 | 11,990 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (11,990 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-5.07.00-Estacionamento-da-US.pdf` | P3 | .pdf | 540.7 | 12 | 16,902 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (16,902 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-5.08.00-Passagem-Sv-Motorizado.pdf` | P3 | .pdf | 506.8 | 8 | 15,877 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (15,877 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-5.09.00-Uso-do-Espagidor-Gas-Pimenta.pdf` | P3 | .pdf | 392.9 | 4 | 5,297 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,297 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-5.10.00-Uso-Bastão-Tonfa.pdf` | P3 | .pdf | 282.4 | 4 | 3,120 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (3,120 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-5.13.00-Transposição-de-Obstáculo.pdf` | P3 | .pdf | 1805.9 | 40 | 44,555 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.14.00-Emprego-munição-de-impacto-controlado-lançador-fn303.pdf` | P3 | .pdf | 458.8 | 13 | 23,894 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.15.00_Defesa-contra-instrumentos-utilizados-como-armas-brancas.pdf` | P3 | .pdf | 136.1 | 10 | 23,070 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.17.00-Ativacao-e-desativacao-do-cinto-de-seguranca.pdf` | P3 | .pdf | 3268.2 | 27 | 19,095 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (19,095 chars). Avaliar agrupamento. |
| `P3/POPs/Processo-5.18.00-Emprego-de-Granadas-Policiais.pdf` | P3 | .pdf | 2972.0 | 43 | 47,708 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.19.00-Resgate-Tático-ao-PM-Ferido.pdf` | P3 | .pdf | 3836.1 | 38 | 48,982 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.20.00-Uso-de-Armas-de-Incapacitação-Neuromuscular.pdf` | P3 | .pdf | 1189.4 | 26 | 26,828 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.21.00-Uso-de-arma-de-incapacitação-neuromuscular-TASER-X-2.pdf` | P3 | .pdf | 2674.8 | 33 | 28,690 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.22.00-Emprego-de-municao-Bean-Bag.pdf` | P3 | .pdf | 902.5 | 14 | 27,081 | NÃO | SIM | PROCEDIMENTAL | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.25.00-_Atendimento-de-ocorrencia-envolvendo-pessoas-com-proposito-suicida-em-posse-de-arma-branca.pdf` | P3 | .pdf | 138.5 | 11 | 22,830 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.27.00-Atendimento-de-ocorrencia-envolvendo-PcD.pdf` | P3 | .pdf | 263.3 | 15 | 32,787 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/Processo-5.28.00-Cameras-Operacionais-Portateis-Motorola-08JUL25.pdf` | P3 | .pdf | 847.0 | 25 | 49,987 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/roubo estabelecimento comercial.pdf` | P3 | .pdf | 783.9 | 11 | 24,222 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/POPs/violencia domestica.pdf` | P3 | .pdf | 429.1 | 14 | 35,232 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/relatorio_ronda.html` | P3 | .html | 106.7 | N/A | 108,421 | N/A | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P3/Relação AISP 2º BPMI.pdf` | P3 | .pdf | 5.3 | 2 | 1,953 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,953 chars). Avaliar agrupamento. |
| `P4/2023/SEI_057.00048913_2023_38 processo cessão de uso gp de rubiacea.pdf` | P4 | .pdf | 16480.8 | 108 | 95,023 | SIM | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/CESSÃO DE USO DE IMÓVEL.pdf` | P4 | .pdf | 810.3 | 14 | 0 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/Memorial Fotográfico.pdf` | P4 | .pdf | 2943.8 | 7 | 4,783 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,783 chars). Avaliar agrupamento. |
| `P4/2024/Oficio Emenda Parlamentar Deputado Telhadan PM  Valparaiso.pdf` | P4 | .pdf | 3353.0 | 14 | 27,464 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR TELHADA PELOTAO VALPARAISO.docx` | P4 | .docx | 84.2 | N/A | 4,867 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR TELHADA PELOTAO VALPARAISO.pdf` | P4 | .pdf | 118.8 | 2 | 5,534 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR.docx` | P4 | .docx | 85.9 | N/A | 4,860 | N/A | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR.pdf` | P4 | .pdf | 119.0 | 2 | 5,521 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/Ofício Valparaíso Emenda Parlamentar Deputado Mecca.pdf` | P4 | .pdf | 3353.3 | 14 | 27,451 | NÃO | SIM | MODELO_PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/2024/PESQUISA DE PREÇOS COMPRAS SP VALPARAÍSO.pdf` | P4 | .pdf | 73.3 | 3 | 5,286 | NÃO | SIM | PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (5,286 chars). Avaliar agrupamento. |
| `P4/2024/PLANILHA ORÇAMENTÁRIA 2024.pdf` | P4 | .pdf | 252.4 | 2 | 11,861 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (11,861 chars). Avaliar agrupamento. |
| `P4/2025/INVENTÁRIO FISICO 2025 - 5ª CIA_PM.xlsx` | P4 | .xlsx | 236.2 | N/A | 90,435 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/2025/LCM 5cia NOV24 (INVENTÁRIO).xlsx` | P4 | .xlsx | 98.2 | N/A | 112,113 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/2025/orçamento pedido fardamento deputado.xlsx` | P4 | .xlsx | 47.6 | N/A | 968 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/2025/Relação de Armas e Materiais da 5ª Cia-09JAN25 (1).xlsx` | P4 | .xlsx | 40.1 | N/A | 18,310 | N/A | SIM | MODELO_DE_REDACAO | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/2025/SEI_057.00048913_2023_38 Processo Cessão de Uso GP Rubiácea.pdf` | P4 | .pdf | 24608.6 | 298 | 507,937 | SIM | SIM | PRECEDENTE | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/3 Cia/8. DADOS COMPLETOS DAS VTR's (Rádios, prefixo).xlsx` | P4 | .xlsx | 25.2 | N/A | 6,378 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/3 Cia/Certidão Negativa de Ônus Gastão Vidigal.pdf` | P4 | .pdf | 795.0 | 2 | 1,784 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,784 chars), avaliar agrupamento. |
| `P4/3 Cia/Inventario Bélico - DL - 3ª CIA PM.xlsx` | P4 | .xlsx | 82.6 | N/A | 2,312 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/3 Cia/PMESPEXP202006170A (1) - Processso doação terreno GP de Gastão.pdf` | P4 | .pdf | 16794.8 | 126 | 87,638 | SIM | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P4/3 Cia/RELAÇÃO DE ALGEMAS, ARMAS  e COLETES COM POLICIAS E NO COFRE.xlsx` | P4 | .xlsx | 26.9 | N/A | 7,379 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/5 Cia/quadro relacao de viaturas 5 cia.jpg` | P4 | .jpg | 158.1 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P4/5 Cia/Relação de Armas Geral Reservas da 5ª Cia.xlsx` | P4 | .xlsx | 31.7 | N/A | 9,333 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/5 Cia/Relação de Armas Portateis  da 5ª Cia.xlsx` | P4 | .xlsx | 17.2 | N/A | 3,123 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/Adobe.Acrobat.Pro.DC.v2021.001.20155.rar` | P4 | .rar | 0.7 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Compactado não suportado (.rar). |
| `P4/ARMAS PORTÁTEIS 20JUN24.pdf` | P4 | .pdf | 102.8 | 1 | 920 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (920 chars), avaliar agrupamento. |
| `P4/Compras Capitão.xlsx` | P4 | .xlsx | 11.1 | N/A | 972 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/Defesa Prévia Recurso AIT 1k105809-7.docx` | P4 | .docx | 89.5 | N/A | 1,639 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,639 chars). Avaliar agrupamento. |
| `P4/Defesa Prévia Recurso AIT 1k105850-7.docx` | P4 | .docx | 89.7 | N/A | 1,633 | N/A | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,633 chars). Avaliar agrupamento. |
| `P4/endereços de ip/20171207_093726.jpg` | P4 | .jpg | 9787.1 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20171207_113136.jpg` | P4 | .jpg | 6493.4 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20180105_095833.jpg` | P4 | .jpg | 9687.6 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20180105_095944.jpg` | P4 | .jpg | 10100.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20180105_095950.jpg` | P4 | .jpg | 10446.3 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/endereço de ip cmt 3 cia.jpg` | P4 | .jpg | 1168.2 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/Endereço IP Pel GPS.docx` | P4 | .docx | 113.6 | N/A | 1 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/ENDEREÇO ip pel Valparaíso.jpg` | P4 | .jpg | 7291.5 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/numero ip pc 3 cia.jpg` | P4 | .jpg | 1859.9 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/número algema 32876-07.jpg` | P4 | .jpg | 2761.4 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P4/número arma bncv395.jpg` | P4 | .jpg | 2788.5 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P4/número colete 2732643 v01abr25.jpg` | P4 | .jpg | 2565.5 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P4/OS/Anexo I da Portaria CmtG nº PM4_001_1.2_20 de 13JUL20.pdf` | P4 | .pdf | 327.4 | 9 | 18,612 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (18,612 chars). Avaliar agrupamento. |
| `P4/OS/Anexo II da Portaria CmtG nº PM4_001_1.2_20 de 13JUL20.pdf` | P4 | .pdf | 277.5 | 5 | 10,972 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (10,972 chars). Avaliar agrupamento. |
| `P4/OS/Anexo III da Portaria CmtG nº PM4_001_1.2_20 de 13JUL20.pdf` | P4 | .pdf | 361.7 | 7 | 8,844 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,844 chars). Avaliar agrupamento. |
| `P4/OS/OS CPI10-002-30-16 regularização revista de armários.pdf` | P4 | .pdf | 203.6 | 1 | 0 | NÃO | SIM | NORMA | `PRECISA_OCR` | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P4/OS/Port Cmt G PM4-001-1.2-24 - Material Bélico (Alterações Port Cmt G PM4-003-1.2-24).pdf` | P4 | .pdf | 1297.9 | 79 | 145,120 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P4/OS/Portaria de Registro e Porte Armas Cmt G nº PM4_001_1.2_20 de 13JUL20.pdf` | P4 | .pdf | 457.6 | 27 | 51,999 | NÃO | SIM | MODELO_PRECEDENTE | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P4/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf` | P4 | .pdf | 77.8 | 2 | 0 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P4/PARTE 303 300 18 Informaçaõ ao Cel. Motooka km acima da VTR I-02303..doc` | P4 | .doc | 99.5 | N/A | 2,284 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (2,284 chars). Avaliar agrupamento. |
| `P4/PDF UNIFORME OPERACIONAL - 1º Ten PM Josemar.xlsx` | P4 | .xlsx | 73.3 | N/A | 4,312 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/PDF UNIFORME PASSEIO - 1º Ten PM Josemar.xlsx` | P4 | .xlsx | 61.8 | N/A | 3,528 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/Planilha de Armamento e Munição - 1º DIA UTUL MES (FECHAMENTO DE MÊS).xlsx` | P4 | .xlsx | 23.2 | N/A | 8,122 | N/A | SIM | NORMA | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/Plaqueta Tarjeta na Blusa.png` | P4 | .png | 1464.9 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P4/PNEUS.doc.docx` | P4 | .docx | 699.1 | N/A | 1,654 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,654 chars). Avaliar agrupamento. |
| `P4/portaria-pm4 Uso de equipamento policial.pdf` | P4 | .pdf | 454.6 | 6 | 9,804 | NÃO | SIM | MODELO_PRECEDENTE | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (9,804 chars). Avaliar agrupamento. |
| `P4/PosicaoAtivo_Classico.pdf` | P4 | .pdf | 1.8 | 1 | 8,744 | NÃO | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (8,744 chars), avaliar agrupamento. |
| `P4/Quadro de viaturas Atual 2024.xlsx` | P4 | .xlsx | 19.8 | N/A | 3,563 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/R-5-PM - 5ª edição - alt. Bol G PM 59_23.pdf` | P4 | .pdf | 9018.2 | 336 | 737,732 | SIM | SIM | NORMA | `PRECISA_SEGMENTACAO` | Indexado, mas muito longo (737,732 chars). Precisa segmentar. |
| `P4/Recibo entrega notebook mini hp.pdf` | P4 | .pdf | 431.6 | 1 | 559 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (559 chars). Avaliar agrupamento. |
| `P4/Relatório de Utilização de AIN.pdf` | P4 | .pdf | 134.0 | 2 | 7,725 | NÃO | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (7,725 chars). Avaliar agrupamento. |
| `P4/Relatório de Vistoria 5ª Cia.xlsx` | P4 | .xlsx | 6.4 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P4/RESUMO REGULAMENTO DE UNIFORME.pdf` | P4 | .pdf | 1545.5 | 29 | 12,805 | SIM | SIM | OUTRO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (12,805 chars). Avaliar agrupamento. |
| `P4/Senha Spark.docx` | P4 | .docx | 211.2 | N/A | 0 | N/A | NÃO | - | `ERRO_LEITURA` | Sem texto extraível. |
| `P4/Slogan email PM 2.png` | P4 | .png | 74.6 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P5/2016 - Roteiro a ser lido  SOLENIDADE 7 DE SETEMBRO.doc` | P5 | .doc | 106.0 | N/A | 30,449 | N/A | NÃO | - | `PRONTO_SEM_SEGMENTACAO` | Tamanho ideal (30,449 chars), pronto para indexação. |
| `P5/AUTORIDADES_5ª_CIA.xlsx` | P5 | .xlsx | 14.2 | N/A | 2,746 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P5/BOPC Flagrante Roubo Araçatuba Bilac.pdf` | P5 | .pdf | 382.0 | 5 | 18,820 | NÃO | SIM | NORMA | `REVISAR_NATUREZA` | Documento fático ou caso concreto. |
| `P5/Currículo Comandante.docx` | P5 | .docx | 12.6 | N/A | 1,118 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (1,118 chars), avaliar agrupamento. |
| `P5/DADOS DE BENTO DE ABREU - TEN.docx` | P5 | .docx | 13.2 | N/A | 629 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (629 chars), avaliar agrupamento. |
| `P5/DADOS DE RUBIÁCEA.docx` | P5 | .docx | 13.4 | N/A | 582 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (582 chars), avaliar agrupamento. |
| `P5/DtzPM5-001-55-06-Portavoz-com-Alteracoes.pdf` | P5 | .pdf | 400.1 | 18 | 35,286 | NÃO | SIM | NORMA | `JA_INDEXADO_OK` | Já indexado em 1 chunk(s). |
| `P5/elogio individual comando p3.jpg` | P5 | .jpg | 112.8 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P5/Estatitica.xlsx` | P5 | .xlsx | 33.5 | N/A | 2,688 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P5/movimentações classificações onde trabalhei.png` | P5 | .png | 54.0 | N/A | 0 | N/A | NÃO | - | `REVISAR_NATUREZA` | Arquivo de imagem (sem valor normativo direto). |
| `P5/Nota de Imprensa Ptr Rural.docx` | P5 | .docx | 593.6 | N/A | 1,973 | N/A | SIM | MODELO_DE_REDACAO | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,973 chars). Avaliar agrupamento. |
| `P5/Parte Elogio Roubo Araçatuba Bilac.docx` | P5 | .docx | 48.4 | N/A | 4,114 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (4,114 chars). Avaliar agrupamento. |
| `P5/Planilha de controle mediação Cap.xlsx` | P5 | .xlsx | 13.0 | N/A | 1,353 | N/A | NÃO | - | `REVISAR_NATUREZA` | Planilha de controle administrativo. |
| `P5/Roteiro a ser lido desfile de viaturas 07set23.docx` | P5 | .docx | 13.1 | N/A | 1,191 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,191 chars). Avaliar agrupamento. |
| `P5/Roteiro a ser lido desfile de viaturas.docx` | P5 | .docx | 13.1 | N/A | 1,297 | N/A | SIM | PROCEDIMENTAL | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (1,297 chars). Avaliar agrupamento. |
| `P5/VEREADORES - VALPARAÍSO- 2016.docx` | P5 | .docx | 40.9 | N/A | 956 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (956 chars), avaliar agrupamento. |
| `README.md` | raiz | .md | 6.0 | N/A | 5,918 | N/A | NÃO | - | `AVALIAR_AGRUPAMENTO` | Pequeno (5,918 chars), avaliar agrupamento. |
| `teste_dano_vtr.txt` | raiz | .txt | 8.7 | N/A | 8,635 | N/A | SIM | NORMA | `AVALIAR_AGRUPAMENTO` | Indexado, mas pequeno (8,635 chars). Avaliar agrupamento. |

## E. Arquivos `PRECISA_OCR`

| Arquivo | Tamanho (KB) | Páginas | Porte | Observação |
|---|---|---|---|---|
| `JD/Arquivo/2020/Bol G 132 - 21JUL20 - Instruções IPM e Susp do PAE.pdf` | 1421.1 | 4 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Normas/NI PM3_004_03_13 ICC.pdf` | 165.8 | 5 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Notebooklm/Supervisor Regional/DTZ PM3_002_02_16 DEJEM.pdf` | 7273.9 | 16 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Notebooklm/Supervisor Regional/OC PM3_007_02_16 DEJEM.pdf` | 386.6 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `Notebooklm/Supervisor Regional/OC PM3_008_02_16 DEJEM.pdf` | 332.2 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/1415-1993 código de postura valparaiso.PDF` | 2615.9 | 16 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/1870-1994 decreto regulamenta codigo de postura valparaiso.PDF` | 223.9 | 2 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/2023/assinatura para funcional digital.pdf` | 9.7 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/Anos anteriores/2018/Calendário de Visitas Técnicas.pdf` | 300.3 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/número codigo sei do batalhão e cpi.pdf` | 414.4 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho e anexo para Sgt Gustavo.pdf` | 16412.7 | 39 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Despacho Escaneado.pdf` | 260.2 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento Escaneado.pdf` | 16152.9 | 38 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/1.pdf` | 821.2 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/10.pdf` | 291.8 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/11.pdf` | 319.5 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/12.pdf` | 229.2 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/13.pdf` | 228.2 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/14.pdf` | 232.7 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/2.pdf` | 850.6 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/3.pdf` | 876.8 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/4.pdf` | 567.0 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/5.pdf` | 597.9 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/6.pdf` | 214.4 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/7.pdf` | 696.9 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/8.pdf` | 743.8 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/9.pdf` | 690.9 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/Requerimento 2-3.pdf` | 4229.2 | 7 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/Requerimento 3-3.pdf` | 3064.9 | 7 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/Requerimento1-3.pdf` | 8801.1 | 24 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P2/Ordem de Serviço nº CoordOpPM-028.21.24, de 15OUT24 (3) (1).pdf` | 642.8 | 3 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P2/OS CPI10-002-30-16 regularização revista de armários.pdf` | 203.6 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P2/OS Informativo On line Ordem Serviço nº CPI10-003.20.17.pdf` | 1569.8 | 4 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/2024/Ata Reunião com Prefeito Assinada.pdf` | 404.5 | 4 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/NI_001_02_15_resolução 57.pdf` | 7765.2 | 46 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/ODS/Nota de Serviço nº CoordOpPM-001-03-16 Operação Direção Segura Integrada - I-2016.pdf` | 65.8 | 2 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/ODS/Resolução CONTRAN nº 432-13.pdf` | 1441.4 | 10 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/ORDEM DE SERVIÇO Nº 2BPMI-001-30-14.pdf` | 336.7 | 2 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/OS/OS NOta urgente copom OSv Coord Op PM 005 04 19 - Ocor de grav ou repercussão (1).pdf` | 2414.2 | 3 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/cópia do e-mail sobre NI PM3-002-02-17.pdf` | 215.8 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/MSG17-152- Circular.pdf` | 193.4 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - B - Exercícios de aquecimento prévio de condução de viatura policial de duas rodas.pdf` | 1817.5 | 6 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI Nº PM3-002-02-17.pdf` | 3759.7 | 11 | Médio | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Codigo para tipificação de ocorrências 1961_190416104118_001.pdf` | 506.5 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Codigos para encerramento de ocorrencia 1962_190416104134_001.pdf` | 487.8 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Desp Nº PM3 005 02 19 - Acesso a dados em celular.pdf` | 1349.1 | 2 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Mapas Copom/Mapas Copom 2 BPMI.pdf` | 1475.3 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Preleção/Sinopse nº 02-18 Fiscal. de Ciclomotor.pdf` | 253.3 | 4 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Projeto VIDA/null.pdf` | 659.2 | 2 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P3/Outros/Projeto VIDA/OFÍCIO DA CPI 10 à 2ª RAJ - Projeto V.I.D.A.pdf` | 773.2 | 2 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |
| `P4/OS/OS CPI10-002-30-16 regularização revista de armários.pdf` | 203.6 | 1 | Pequeno | PDF imagem (0 chars extraídos). Precisa OCR. |

## F. Arquivos `PRECISA_SEGMENTACAO`

| Arquivo | Páginas | Chars | TOC | Já tem segmentos? | Observação | Prioridade |
|---|---|---|---|---|---|---|
| `JD/PPJM/Manuais, Leis, Regulamentos/CC.htm` | N/A | 718,490 | N/A | SIM (2 chunks) | Indexado, mas muito longo (718,490 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CF.htm` | N/A | 747,527 | N/A | SIM (3 chunks) | Indexado, mas muito longo (747,527 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CP.htm` | N/A | 448,753 | N/A | SIM (32 chunks) | Indexado, mas muito longo (448,753 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPC.htm` | N/A | 664,305 | N/A | SIM (1 chunks) | Indexado, mas muito longo (664,305 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPM.htm` | N/A | 542,553 | N/A | SIM (1 chunks) | Indexado, mas muito longo (542,553 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPP.htm` | N/A | 648,118 | N/A | SIM (4 chunks) | Indexado, mas muito longo (648,118 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CPPM.htm` | N/A | 711,581 | N/A | SIM (1 chunks) | Indexado, mas muito longo (711,581 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/csp.pdf` | 120 | 372,648 | NÃO | SIM (1 chunks) | Indexado, mas muito longo (372,648 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/CTB.htm` | N/A | 459,311 | N/A | SIM (2 chunks) | Indexado, mas muito longo (459,311 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/I-16-PM.pdf` | 71 | 160,162 | NÃO | SIM (1 chunks) | Indexado, mas muito longo (160,162 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/PPJM/Manuais, Leis, Regulamentos/Portaria dispoe sobre armas na PM.pdf` | 56 | 227,278 | SIM | SIM (1 chunks) | Indexado, mas muito longo (227,278 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `JD/Processo Baile Clandestino 1001653-74.2025.8.26.0218.pdf` | 306 | 483,513 | NÃO | SIM (1 chunks) | Indexado, mas muito longo (483,513 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `Normas/I-15-PM Transportes Motorizados.pdf` | 71 | 168,773 | NÃO | SIM (1 chunks) | Indexado, mas muito longo (168,773 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `Notebooklm/Supervisor Regional/orientações direito militar.pdf` | 481 | 1,153,578 | SIM | SIM (1 chunks) | Indexado, mas muito longo (1,153,578 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `P1/normas i-7-pm/bg19054.pdf` | 45 | 175,244 | NÃO | SIM (1 chunks) | Indexado, mas muito longo (175,244 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `P3/Outros/Convênios Prontos/SEI_057.00033862_2023_40 Processo Completo Guararapes.pdf` | 130 | 267,794 | SIM | SIM (1 chunks) | Indexado, mas muito longo (267,794 chars). Precisa segmentar. | prioridade a definir por Josemar |
| `P3/Outros/Projeto VIDA/Cap_PM_Ferrarez_Dissertação_CAO24.pdf` | 124 | 245,958 | NÃO | NÃO | Muito longo (245,958 chars). Necessita segmentação. | prioridade a definir por Josemar |
| `P4/R-5-PM - 5ª edição - alt. Bol G PM 59_23.pdf` | 336 | 737,732 | SIM | SIM (1 chunks) | Indexado, mas muito longo (737,732 chars). Precisa segmentar. | prioridade a definir por Josemar |

## G. Arquivos `PRONTO_SEM_SEGMENTACAO`

| Arquivo | Páginas | Chars | Já está no índice? | Observação |
|---|---|---|---|---|
| `JD/Arquivo/2022/RIOG MDIP BIRIGUI-SP.pdf` | 21 | 33,473 | NÃO | Tamanho ideal (33,473 chars), pronto para indexação. |
| `JD/Arquivo/2023/RIOG_2BPMI-004_12_23.pdf` | 14 | 22,143 | NÃO | Tamanho ideal (22,143 chars), pronto para indexação. |
| `JD/Arquivo/2024/Mdip Gpes 27DEZ24.pdf` | 15 | 23,338 | NÃO | Tamanho ideal (23,338 chars), pronto para indexação. |
| `JD/Arquivo/2024/Riog Mdip 2bpmi 003-12-24 25ago24.pdf` | 15 | 23,949 | NÃO | Tamanho ideal (23,949 chars), pronto para indexação. |
| `P3/OS/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf` | 37 | 82,004 | NÃO | Tamanho ideal (82,004 chars), pronto para indexação. |
| `P5/2016 - Roteiro a ser lido  SOLENIDADE 7 DE SETEMBRO.doc` | N/A | 30,449 | NÃO | Tamanho ideal (30,449 chars), pronto para indexação. |

## H. Arquivos `JA_SEGMENTADO`

| Arquivo | Páginas | Chars | Observação |
|---|---|---|---|
| `Notebooklm/Supervisor Regional/Doutrinas pm_compressed (1).pdf` | 1643 | 3,093,809 | JA_SEGMENTADO — fonte original preservada |
| `Notebooklm/Supervisor Regional/POPs.pdf` | 824 | 1,415,187 | JA_SEGMENTADO — fonte original preservada |
| `Notebooklm/Supervisor Regional/Vademecum.pdf` | 2807 | 7,374,439 | JA_SEGMENTADO — fonte original preservada |

## I. Arquivos `REVISAR_NATUREZA`

Estes arquivos contêm informações administrativas, planilhas de trabalho, modelos de peças, documentos fáticos de casos passados ou holerites. Eles representam poluição potencial se forem indexados como normas de fundamento.

| Arquivo | Tamanho (KB) | Categoria Suspeita | Chars | Observação |
|---|---|---|---|---|
| `corpus_index.json` | 36039.3 | **Outro** | 0 | Arquivo de controle do indexador. |
| `despachadora.py` | 42.0 | **Outro** | 0 | Arquivo de controle do indexador. |
| `indexar_corpus.py` | 13.8 | **Outro** | 0 | Arquivo de controle do indexador. |
| `JD/2025/Dano vtr 504/Despacho Dano VTR 504.pdf` | 113.2 | **Caso Fático / Concreto** | 3,840 | Documento fático ou caso concreto. |
| `JD/2025/Dano vtr 504/Parte 2BPMI_228_500_25 Dano em Vtr.docx` | 92.1 | **Caso Fático / Concreto** | 3,549 | Documento fático ou caso concreto. |
| `JD/2025/Dano vtr 504/Parte Dano vtr 504 (1).pdf` | 5662.6 | **Caso Fático / Concreto** | 5,393 | Documento fático ou caso concreto. |
| `JD/Arquivo/2019/fotos rg civis agressão coroados.jpeg` | 148.0 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `JD/Arquivo/2019/Parte Denuncia agressão Coroados.doc` | 45.5 | **Caso Fático / Concreto** | 1,878 | Documento fático ou caso concreto. |
| `JD/Arquivo/2020/Parte furto e acidente de transito com vítima.docx` | 49.7 | **Caso Fático / Concreto** | 3,086 | Documento fático ou caso concreto. |
| `JD/Arquivo/2020/Parte Nº 181 500 20 Encaminhamento de documentação sobre dano em VTR I-02502.docx` | 39.0 | **Caso Fático / Concreto** | 2,428 | Documento fático ou caso concreto. |
| `JD/Arquivo/2021/BOPC 458-21.pdf` | 143.5 | **Caso Fático / Concreto** | 4,556 | Documento fático ou caso concreto. |
| `JD/Arquivo/2022/Croqui Diego.pdf` | 97.5 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `JD/Arquivo/2022/Croqui Jeferson.pdf` | 98.8 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/bo202307031314758 acidente de transito via rondon 3-520 viatura atropelamento capivara.pdf` | 2129.4 | **Caso Fático / Concreto** | 11,970 | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/Croqui Cadavérico Cristiano Birigui.pdf` | 587.4 | **Caso Fático / Concreto** | 614 | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/Croqui Cadavérico Cristiano.pdf` | 246.1 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `JD/Arquivo/2023/croqui cristiano.pdf` | 496.4 | **Caso Fático / Concreto** | 790 | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/croqui cadavérico lado Batista pereira.pdf` | 500.8 | **Caso Fático / Concreto** | 846 | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/Croqui Everton.pdf` | 74.6 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.doc` | 763.7 | **Modelo / Formulário** | 989 | Modelo de redação / formulário. |
| `JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.pdf` | 155.2 | **Modelo / Formulário** | 1,103 | Modelo de redação / formulário. |
| `JD/Arquivo/2024/Termo de Declaração Cb PM Ataídes.docx` | 46.7 | **Caso Fático / Concreto** | 3,483 | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/Termo de Declaração Cb PM Fransosso.docx` | 46.7 | **Caso Fático / Concreto** | 4,003 | Documento fático ou caso concreto. |
| `JD/Arquivo/2024/WhatsApp Image 2024-04-12 at 09.08.30.jpeg` | 391.2 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `JD/Arquivo/minhas ocorrências/Oitiva como testemunha acusacao sd garcia.pdf` | 1655.0 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `JD/PPJM/APFD/Modelo de Auto de Prisão em Flagrante Delito.doc` | 242.0 | **Modelo / Formulário** | 43,940 | Modelo de redação / formulário. |
| `JD/PPJM/AUTO de RECONHECIMENTO FOTOGRAFICO - MODELO.doc` | 27.0 | **Modelo / Formulário** | 1,880 | Modelo de redação / formulário. |
| `JD/PPJM/Modelo - CROQUI CADAVÉRICO.doc` | 763.7 | **Modelo / Formulário** | 989 | Modelo de redação / formulário. |
| `JD/PPJM/Modelo - CROQUI CADAVÉRICO.pdf` | 155.2 | **Modelo / Formulário** | 1,103 | Modelo de redação / formulário. |
| `JD/PPJM/MODELO DE RIOG PARA PPJM.doc` | 75.5 | **Modelo / Formulário** | 23,565 | Modelo de redação / formulário. |
| `JD/PPJM/Modelos Relativos ao Crime de Deserção.doc` | 139.0 | **Modelo / Formulário** | 28,026 | Modelo de redação / formulário. |
| `JD/PPJM/Orientações MDIP.jpeg` | 192.9 | **Controle de IP / Rede** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `Normas/POPs_Segmentos/POP_3_01_00_Acidente_Transito.txt` | 32.2 | **Caso Fático / Concreto** | 31,233 | Documento fático ou caso concreto. |
| `Notebooklm/Supervisor Regional/ESCALA DE OFICIAL SUPERVISOR REGIONAL - DEZ25 (2).pdf` | 688.5 | **Escala / Serviço** | 4,672 | Documento transitório de escala ou vencimento. |
| `Notebooklm/Supervisor Regional/ESCALA DE OFICIAL SUPERVISOR REGIONAL - NOV25 (1).pdf` | 91.7 | **Escala / Serviço** | 0 | Documento transitório de escala ou vencimento. |
| `Notebooklm/Supervisor Regional/Relatório Ronda do Oficial  Supervisor Regional 23ago25 -  Modelo.pdf` | 120.6 | **Modelo / Formulário** | 8,213 | Modelo de redação / formulário. |
| `P1/2023/assinatura e-mail.png` | 88.8 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/2023/assinatura para funcional digital.png` | 29.1 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/20230830_144806.jpg` | 1209.2 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/2024/Efetivo atualizado 5 cia 29fev24.jpeg` | 454.2 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/2024/Escala Geral 5ª Cia 2024 - JUN24.pdf` | 399.1 | **Escala / Serviço** | 15,791 | Documento transitório de escala ou vencimento. |
| `P1/2024/Escala_Geral_5ª_Cia_2024_-_MAR24-1.pdf` | 398.6 | **Escala / Serviço** | 15,786 | Documento transitório de escala ou vencimento. |
| `P1/2024/Previa Escala Supervisor Regional abr24.jpeg` | 191.6 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/2025  - 11FEV25 - 5ª Cia PM - CPF e e-mail efetivo.xlsx` | 20.7 | **Planilha / Dados** | 8,942 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2018/08 - ESCALA DE OFICIAL SUPERIOR DE SOBREAVISO AGO18.pdf` | 282.6 | **Escala / Serviço** | 0 | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/08 - ESCALA DE SUPERVISOR REGIONAL -  AGO18.pdf` | 341.4 | **Escala / Serviço** | 0 | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/08. Escala dos Tenentes 2º BPMI - 01 a 31AGO18.xlsx` | 708.0 | **Planilha / Dados** | 17,068 | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/COPIA EFETIVO TELEFONE - 13DEZ17.xlsx` | 28.1 | **Planilha / Dados** | 5,778 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2018/Escala mensal outubro 5ª cia.pdf` | 1365.4 | **Escala / Serviço** | 0 | Documento transitório de escala ou vencimento. |
| `P1/Anos anteriores/2018/Estudo do efetivo 2º BPMI.xlsx` | 238.1 | **Planilha / Dados** | 89,495 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2018/Planilha de Férias 2018 Josemar.xlsx` | 10.3 | **Planilha / Dados** | 580 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2020/Relação EFETIVO nov20.xlsx` | 12.3 | **Planilha / Dados** | 2,624 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2020/Situação do efetivo 5 Cia.xlsx` | 12.4 | **Planilha / Dados** | 865 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2021/Claro Efetivo 3ª Cia.xlsx` | 16.0 | **Planilha / Dados** | 3,035 | Planilha de controle administrativo. |
| `P1/Anos anteriores/2021/Parte Modelo 2021.doc` | 597.0 | **Modelo / Formulário** | 571 | Modelo de redação / formulário. |
| `P1/Assinatura Cmt 3 Cia.PNG` | 52.8 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/aSSINATURA EMAIL CARTAO.PNG` | 51.2 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/Assinatura email Cmt Interino 3 Cia.PNG` | 51.7 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/CertExchange.cer` | 1.0 | **Outro** | 0 | Certificado de segurança (deve ser excluído). |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Associação Comercial.docx` | 56.7 | **Caso Fático / Concreto** | 4,075 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Camara Municipal.docx` | 56.8 | **Controle de IP / Rede** | 4,107 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Conselho Tutelar.docx` | 56.5 | **Caso Fático / Concreto** | 4,088 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg CPP.docx` | 56.7 | **Caso Fático / Concreto** | 4,106 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Detran.docx` | 56.6 | **Caso Fático / Concreto** | 4,065 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Lions Clube.docx` | 56.6 | **Caso Fático / Concreto** | 4,083 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Maçonaria.docx` | 56.5 | **Caso Fático / Concreto** | 4,044 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg OAB.docx` | 56.5 | **Caso Fático / Concreto** | 4,075 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Penitenciária.docx` | 56.7 | **Caso Fático / Concreto** | 4,085 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Prefeito.docx` | 56.8 | **Caso Fático / Concreto** | 4,076 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Rotary Club.docx` | 56.7 | **Caso Fático / Concreto** | 4,084 | Documento fático ou caso concreto. |
| `P1/Conseg/Oficios Convites Conseg/Ofício Convite Conseg Sindicato Rural.docx` | 56.6 | **Caso Fático / Concreto** | 4,099 | Documento fático ou caso concreto. |
| `P1/Conseg/PLANILHA BALANÇO CPI.DEINTER 10.xlsx` | 27.7 | **Planilha / Dados** | 2,999 | Planilha de controle administrativo. |
| `P1/Efetivo Atualizado 5ª Cia 20jan26.jpeg` | 273.3 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/Holerites/2014/Demonstrativo_09_2014(1).pdf` | 33.2 | **Holerite Pessoal** | 1,420 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_09_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,216 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_10_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,460 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_11_2014(1).pdf` | 33.2 | **Holerite Pessoal** | 1,443 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_11_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,492 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2014/Demonstrativo_12_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,336 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_01_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,392 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_02_2015.pdf` | 46.7 | **Holerite Pessoal** | 2,641 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_03_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,443 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_04_2015(1).pdf` | 33.2 | **Holerite Pessoal** | 1,429 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_04_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,368 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_05_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,275 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_06_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,396 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_07_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,315 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_08_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,344 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_09_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,492 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_10_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,463 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_11_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,385 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2015/Demonstrativo_12_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,436 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_01_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,373 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_02_2016.pdf` | 46.7 | **Holerite Pessoal** | 2,721 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_03_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,565 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_04_2016.pdf` | 46.7 | **Holerite Pessoal** | 2,587 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_05_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,432 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_06_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,372 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_07_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,413 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_08_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,481 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_09_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,450 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_10_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,426 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_11_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,434 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2016/Demonstrativo_12_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,562 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_01_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,516 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_02_2017.pdf` | 47.4 | **Holerite Pessoal** | 2,784 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_03_2017.pdf` | 47.4 | **Holerite Pessoal** | 2,599 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_04_2017(1).pdf` | 33.8 | **Holerite Pessoal** | 1,405 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_04_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,472 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_05_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,497 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_06_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,318 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_07_2017(1).pdf` | 33.8 | **Holerite Pessoal** | 1,405 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_07_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,557 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_08_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,426 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_09_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,561 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_10_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,399 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_11_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,357 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2017/Demonstrativo_12_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,396 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_01_2018(1).pdf` | 34.0 | **Holerite Pessoal** | 1,414 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_01_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,296 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_02_2018(1).pdf` | 34.0 | **Holerite Pessoal** | 1,404 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_02_2018.pdf` | 47.6 | **Holerite Pessoal** | 2,624 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_03_2018.pdf` | 47.6 | **Holerite Pessoal** | 2,648 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_04_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,264 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_05_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,317 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_06_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,414 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_07_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,233 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_08_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,484 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_09_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,425 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_10_2018(1).pdf` | 34.0 | **Holerite Pessoal** | 1,384 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_10_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,466 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_11_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,473 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2018/Demonstrativo_12_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,499 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_01_2019(1).pdf` | 33.8 | **Holerite Pessoal** | 1,395 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_01_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,341 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_02_2019.pdf` | 47.1 | **Holerite Pessoal** | 2,798 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_03_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,532 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_04_2019(1).pdf` | 33.8 | **Holerite Pessoal** | 1,439 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_04_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,527 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_05_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,499 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_06_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,306 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_07_2019(1).pdf` | 34.1 | **Holerite Pessoal** | 2,385 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_07_2019(2).pdf` | 33.8 | **Holerite Pessoal** | 1,366 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites/2019/Demonstrativo_08_2019(1).pdf` | 34.1 | **Holerite Pessoal** | 2,389 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_09_2014(1).pdf` | 33.2 | **Holerite Pessoal** | 1,420 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_10_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,460 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014(1).pdf` | 33.2 | **Holerite Pessoal** | 1,443 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,492 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2014/Demonstrativo_12_2014.pdf` | 33.8 | **Holerite Pessoal** | 2,336 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_01_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,392 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_03_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,443 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_04_2015(1).pdf` | 33.2 | **Holerite Pessoal** | 1,429 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_07_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,315 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_08_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,344 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_09_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,492 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2015/Demonstrativo_10_2015.pdf` | 33.8 | **Holerite Pessoal** | 2,463 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_01_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,373 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_02_2016.pdf` | 46.7 | **Holerite Pessoal** | 2,721 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_03_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,565 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_04_2016.pdf` | 46.7 | **Holerite Pessoal** | 2,587 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_05_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,432 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_06_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,372 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_07_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,413 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_08_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,481 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_09_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,450 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_10_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,426 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_11_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,434 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2016/Demonstrativo_12_2016.pdf` | 33.8 | **Holerite Pessoal** | 2,562 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_01_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,516 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_02_2017.pdf` | 47.4 | **Holerite Pessoal** | 2,784 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_03_2017.pdf` | 47.4 | **Holerite Pessoal** | 2,599 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_04_2017(1).pdf` | 33.8 | **Holerite Pessoal** | 1,405 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_04_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,472 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_05_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,497 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_06_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,318 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_07_2017(1).pdf` | 33.8 | **Holerite Pessoal** | 1,405 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_07_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,557 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_08_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,426 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_09_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,561 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_10_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,399 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_11_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,357 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2017/Demonstrativo_12_2017.pdf` | 34.5 | **Holerite Pessoal** | 2,396 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_01_2018(1).pdf` | 34.0 | **Holerite Pessoal** | 1,414 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_01_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,296 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_02_2018(1).pdf` | 34.0 | **Holerite Pessoal** | 1,404 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_02_2018.pdf` | 47.6 | **Holerite Pessoal** | 2,624 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_03_2018.pdf` | 47.6 | **Holerite Pessoal** | 2,648 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_04_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,264 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_05_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,317 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_06_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,414 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_07_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,233 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_08_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,484 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_09_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,425 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_10_2018(1).pdf` | 34.0 | **Holerite Pessoal** | 1,384 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_10_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,466 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_11_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,473 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2018/Demonstrativo_12_2018.pdf` | 34.6 | **Holerite Pessoal** | 2,499 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_01_2019(1).pdf` | 33.8 | **Holerite Pessoal** | 1,395 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_01_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,341 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_02_2019.pdf` | 47.1 | **Holerite Pessoal** | 2,798 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_03_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,532 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_04_2019(1).pdf` | 33.8 | **Holerite Pessoal** | 1,439 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_04_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,527 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_05_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,499 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_06_2019.pdf` | 34.1 | **Holerite Pessoal** | 2,306 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_07_2019(1).pdf` | 34.1 | **Holerite Pessoal** | 2,385 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_07_2019(2).pdf` | 33.8 | **Holerite Pessoal** | 1,366 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/Holerites Bonus DEJEM/2019/Demonstrativo_08_2019(1).pdf` | 34.1 | **Holerite Pessoal** | 2,389 | Holerite pessoal (deve ser excluído do corpus). |
| `P1/JOSEMARDEPAULA,CapPM121876-0.pfx` | 2.6 | **Outro** | 0 | Certificado de segurança (deve ser excluído). |
| `P1/Modelo Despacho SEI.txt` | 0.2 | **Modelo / Formulário** | 190 | Modelo de redação / formulário. |
| `P1/movimentações classificações onde trabalhei.png` | 54.0 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/Relação do efetivo 5ª Cia jul25 por antiguidade.jpeg` | 497.8 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/Relação do Efetivo 5ª Cia jul25 por fração.jpeg` | 593.8 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P1/Ten Josemar assinatura email 5 cia.JPG` | 32.0 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P2/Plano de Chamada/Plano de Chamada 2023  - 09AGO23 - 5ª Cia PM.xlsx` | 109.6 | **Planilha / Dados** | 20,752 | Planilha de controle administrativo. |
| `P2/Relatório Revista de armario 5ª Cia nov20.xlsx` | 13.0 | **Planilha / Dados** | 2,641 | Planilha de controle administrativo. |
| `P2/Revista de armario EFETIVO nov20.xlsx` | 12.3 | **Planilha / Dados** | 2,624 | Planilha de controle administrativo. |
| `P3/2023/Indices 5 Cia 2023.xlsx` | 25.7 | **Planilha / Dados** | 4,879 | Planilha de controle administrativo. |
| `P3/2023/Plano de Comando.xlsx` | 11.2 | **Planilha / Dados** | 916 | Planilha de controle administrativo. |
| `P3/2023/ROTINA PAP 07NOV23.xlsx` | 17.6 | **Planilha / Dados** | 4,020 | Planilha de controle administrativo. |
| `P3/2024/20241029_162708.jpg` | 1567.3 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/2024/20241029_162713.jpg` | 1463.0 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/2024/BOS 5ª Cia.xlsx` | 23.7 | **Planilha / Dados** | 5,440 | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso 09out24.xlsx` | 53.5 | **Planilha / Dados** | 10,208 | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso 26OUT24.xlsx` | 62.7 | **Planilha / Dados** | 12,724 | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso 29OUT24.xlsx` | 53.9 | **Planilha / Dados** | 12,738 | Planilha de controle administrativo. |
| `P3/2024/Controle DELEGADA Oficiais Valparaíso.xlsx` | 43.5 | **Planilha / Dados** | 6,778 | Planilha de controle administrativo. |
| `P3/2024/Controle do TDS Treinamento Durante o Serviço.xlsx` | 20.9 | **Planilha / Dados** | 5,935 | Planilha de controle administrativo. |
| `P3/2024/f) Valparaíso - Minuta do Convênio Atividade Delegada.docx` | 58.0 | **Modelo / Formulário** | 15,878 | Modelo de redação / formulário. |
| `P3/2024/Indices 5 Cia 2024 1 1.xlsx` | 29.3 | **Planilha / Dados** | 10,352 | Planilha de controle administrativo. |
| `P3/2024/OFÍCIO 2BPMI-0234024 Cessão de Uso de Imóvel Pel PM Valparaíso.doc` | 417.5 | **Caso Fático / Concreto** | 2,007 | Documento fático ou caso concreto. |
| `P3/2024/Painel de Produtitividade.xlsx` | 14.9 | **Planilha / Dados** | 2,884 | Planilha de controle administrativo. |
| `P3/2025/Controle do TDS Treinamento Durante o Serviço.xlsx` | 20.9 | **Planilha / Dados** | 5,935 | Planilha de controle administrativo. |
| `P3/2025/Indices 5 Cia 2025.xlsx` | 41.3 | **Planilha / Dados** | 15,171 | Planilha de controle administrativo. |
| `P3/2025/Planejamento Atividade Delegada Arraia Bento.xlsx` | 17.7 | **Planilha / Dados** | 3,553 | Planilha de controle administrativo. |
| `P3/2025/Programação Fim de ano 5ª Cia.xlsx` | 21.0 | **Planilha / Dados** | 6,937 | Planilha de controle administrativo. |
| `P3/2025/Tabela_de_indicadores_criminais_e_operacionais_2023_2024_2025_CAPSSP-SP.xlsx` | 24.1 | **Planilha / Dados** | 4,452 | Planilha de controle administrativo. |
| `P3/2026/Balanço Atividade Delegada (1).xlsx` | 18.2 | **Planilha / Dados** | 2,556 | Planilha de controle administrativo. |
| `P3/2026/Indices 5 Cia 2026.xlsx` | 39.3 | **Planilha / Dados** | 11,712 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2021/Autoridades - 3ª Cia.xlsx` | 11.5 | **Planilha / Dados** | 2,243 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2021/Dados estatísticos 3 Cia.xlsx` | 23.9 | **Planilha / Dados** | 10,034 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2021/Relação PMs deslocamento.xlsx` | 21.8 | **Planilha / Dados** | 5,925 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Controle enem.xlsx` | 10.9 | **Planilha / Dados** | 549 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Cópia Controle da DEJEM de Oficiais - 2022.xlsx` | 79.0 | **Planilha / Dados** | 27,999 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/2ª CIA - Escala FINAL.pdf` | 122.3 | **Escala / Serviço** | 18,091 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/2ª CIA - Escala FINAL.xlsx` | 41.2 | **Planilha / Dados** | 22,723 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/3ª CIa - Escala Eleiçoes 3ª Cia 02OUT22 FINAL.xlsx` | 28.1 | **Planilha / Dados** | 9,679 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/4ª CIA - Escala FINAL.pdf` | 247.8 | **Escala / Serviço** | 6,299 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/5ª Cia - Escala Atual Eleições 2022 - 5ª Cia (final).xlsx` | 31.0 | **Planilha / Dados** | 12,606 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/AMBIENTAL APOIO ELEIÇÕES 2BPMI.xlsx` | 10.5 | **Planilha / Dados** | 4,676 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/CPI - 10 - Escala DEFINITIVA Eleição Policiais com Restrição.pdf` | 23.4 | **Escala / Serviço** | 2,274 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/ESCALA DE OFICIAIS E APOIO.xlsx` | 10.7 | **Planilha / Dados** | 3,263 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/Escala DEFINITIVA Eleição Policiais com Restrição.xlsx` | 10.5 | **Planilha / Dados** | 2,522 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/Escala GERAL (Salvo automaticamente).xlsx` | 88.7 | **Planilha / Dados** | 54,135 | Documento transitório de escala ou vencimento. |
| `P3/Anos Anteriores/2022/Eleições/Problemas sugestoes.xlsx` | 8.6 | **Planilha / Dados** | 673 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Eleições/RODOVIARIO APOIO ELEIÇÕES 2BPMI.xlsx` | 9.9 | **Planilha / Dados** | 1,982 | Planilha de controle administrativo. |
| `P3/Anos Anteriores/2022/Vtr Pol Rural - 28BPMI.xlsx` | 10.9 | **Planilha / Dados** | 924 | Planilha de controle administrativo. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.pdf` | 283.4 | **Modelo / Formulário** | 1,754 | Modelo de redação / formulário. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI - C - Placar de acidente de trânsito com viatura.pdf` | 202.9 | **Caso Fático / Concreto** | 589 | Documento fático ou caso concreto. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/NI Nº PM3-002-02-17 - Acidente Vtr.pdf` | 287.8 | **Caso Fático / Concreto** | 26,064 | Documento fático ou caso concreto. |
| `P3/OS/NI_002_02_17 acidente de trânsito com viatura/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf` | 77.8 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `P3/OS/OS 4 Cia 038-400-20 parte 01.jpeg` | 108.1 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS 4 Cia 038-400-20 parte 2 de 2.jpeg` | 92.7 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS 4 Cia 041-400-20 parte 1 de 2].jpeg` | 128.7 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/OS 4 Cia 041-400-20 parte 2 de 2.jpeg` | 77.6 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf` | 77.8 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.docx` | 1453.1 | **Modelo / Formulário** | 2,372 | Modelo de redação / formulário. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - A - Modelo de Relatório de Estudo de Caso de acidente de trânsito envolvendo viatuira.pdf` | 872.1 | **Modelo / Formulário** | 0 | Modelo de redação / formulário. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/NI - C - Placar de acidente de trânsito com viatura.pdf` | 260.0 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/OS 023-30-17 - SISTEMATICA DE PREVENÇÃO DE ACIDENTES DE TRÂNSITO.pdf` | 86.7 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/Placar de acidente de trânsito com viatura (2).jpg` | 163.8 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Acidente de trânsito vtr - PAAVI/Placar de acidente de Viatura.docx` | 456.3 | **Caso Fático / Concreto** | 200 | Documento fático ou caso concreto. |
| `P3/Outros/Organograma  2º BPMI.xlsx` | 25.1 | **Planilha / Dados** | 5,511 | Planilha de controle administrativo. |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 1 Cia.jpeg` | 121.3 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 2 BPMI.jpeg` | 190.2 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 2 Cia.jpeg` | 133.2 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 3 Cia.jpeg` | 137.5 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 4 Cia.jpeg` | 132.6 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapa Copom 5 Cia.jpeg` | 126.4 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Mapas Copom/Mapas Copom 2BPMI.jpg` | 2081.9 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Reintegração de posse OS/An D_Modelo de Plano de Acao.pdf` | 477.1 | **Modelo / Formulário** | 897 | Modelo de redação / formulário. |
| `P3/Outros/Preleção/Screenshot_20181025-053010_WhatsApp.jpg` | 557.7 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P3/Outros/Preleção/Video Treinamento Zona de Perigo e Zona de Segurança 2018.mp4` | 34845.1 | **Outro** | 0 | Arquivo de controle do indexador. |
| `P3/Outros/Projeto VIDA/BTL - CADASTRO PM.xlsx` | 17.2 | **Planilha / Dados** | 5,735 | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/CIAS - CADASTRO PM.xlsx` | 37.2 | **Planilha / Dados** | 18,522 | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/Controle da implantação.xlsx` | 10.5 | **Planilha / Dados** | 504 | Planilha de controle administrativo. |
| `P3/Outros/Projeto VIDA/CPI10 - CADASTRO PM.xlsx` | 55.3 | **Planilha / Dados** | 7,141 | Planilha de controle administrativo. |
| `P3/Outros/Relatório Ronda do Oficial  Supervisor Regional do CPI-10 - MODELO 2022.docx` | 41.1 | **Modelo / Formulário** | 23,768 | Modelo de redação / formulário. |
| `P3/Outros/Retificação BOPM.txt` | 1.7 | **Caso Fático / Concreto** | 1,689 | Documento fático ou caso concreto. |
| `P3/Planejamento Atividade Delegada orçamento.xlsx` | 10.2 | **Planilha / Dados** | 634 | Planilha de controle administrativo. |
| `P3/POPs/Processo-3.01.00-Acidente-de-Transito.pdf` | 731.4 | **Caso Fático / Concreto** | 33,211 | Documento fático ou caso concreto. |
| `P4/2023/SEI_057.00048913_2023_38 processo cessão de uso gp de rubiacea.pdf` | 16480.8 | **Caso Fático / Concreto** | 95,023 | Documento fático ou caso concreto. |
| `P4/2024/CESSÃO DE USO DE IMÓVEL.pdf` | 810.3 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `P4/2024/Oficio Emenda Parlamentar Deputado Telhadan PM  Valparaiso.pdf` | 3353.0 | **Caso Fático / Concreto** | 27,464 | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR TELHADA PELOTAO VALPARAISO.docx` | 84.2 | **Caso Fático / Concreto** | 4,867 | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR TELHADA PELOTAO VALPARAISO.pdf` | 118.8 | **Caso Fático / Concreto** | 5,534 | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR.docx` | 85.9 | **Caso Fático / Concreto** | 4,860 | Documento fático ou caso concreto. |
| `P4/2024/OFÍCIO EMENDA PARLAMENTAR.pdf` | 119.0 | **Caso Fático / Concreto** | 5,521 | Documento fático ou caso concreto. |
| `P4/2024/Ofício Valparaíso Emenda Parlamentar Deputado Mecca.pdf` | 3353.3 | **Caso Fático / Concreto** | 27,451 | Documento fático ou caso concreto. |
| `P4/2025/INVENTÁRIO FISICO 2025 - 5ª CIA_PM.xlsx` | 236.2 | **Planilha / Dados** | 90,435 | Planilha de controle administrativo. |
| `P4/2025/LCM 5cia NOV24 (INVENTÁRIO).xlsx` | 98.2 | **Planilha / Dados** | 112,113 | Planilha de controle administrativo. |
| `P4/2025/orçamento pedido fardamento deputado.xlsx` | 47.6 | **Planilha / Dados** | 968 | Planilha de controle administrativo. |
| `P4/2025/Relação de Armas e Materiais da 5ª Cia-09JAN25 (1).xlsx` | 40.1 | **Planilha / Dados** | 18,310 | Planilha de controle administrativo. |
| `P4/2025/SEI_057.00048913_2023_38 Processo Cessão de Uso GP Rubiácea.pdf` | 24608.6 | **Caso Fático / Concreto** | 507,937 | Documento fático ou caso concreto. |
| `P4/3 Cia/8. DADOS COMPLETOS DAS VTR's (Rádios, prefixo).xlsx` | 25.2 | **Planilha / Dados** | 6,378 | Planilha de controle administrativo. |
| `P4/3 Cia/Inventario Bélico - DL - 3ª CIA PM.xlsx` | 82.6 | **Planilha / Dados** | 2,312 | Planilha de controle administrativo. |
| `P4/3 Cia/RELAÇÃO DE ALGEMAS, ARMAS  e COLETES COM POLICIAS E NO COFRE.xlsx` | 26.9 | **Planilha / Dados** | 7,379 | Planilha de controle administrativo. |
| `P4/5 Cia/quadro relacao de viaturas 5 cia.jpg` | 158.1 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P4/5 Cia/Relação de Armas Geral Reservas da 5ª Cia.xlsx` | 31.7 | **Planilha / Dados** | 9,333 | Planilha de controle administrativo. |
| `P4/5 Cia/Relação de Armas Portateis  da 5ª Cia.xlsx` | 17.2 | **Planilha / Dados** | 3,123 | Planilha de controle administrativo. |
| `P4/Compras Capitão.xlsx` | 11.1 | **Planilha / Dados** | 972 | Planilha de controle administrativo. |
| `P4/endereços de ip/20171207_093726.jpg` | 9787.1 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20171207_113136.jpg` | 6493.4 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20180105_095833.jpg` | 9687.6 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20180105_095944.jpg` | 10100.0 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/20180105_095950.jpg` | 10446.3 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/endereço de ip cmt 3 cia.jpg` | 1168.2 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/Endereço IP Pel GPS.docx` | 113.6 | **Controle de IP / Rede** | 1 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/ENDEREÇO ip pel Valparaíso.jpg` | 7291.5 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/endereços de ip/numero ip pc 3 cia.jpg` | 1859.9 | **Controle de IP / Rede** | 0 | Controle técnico de rede / IPs (deve ser excluído). |
| `P4/número algema 32876-07.jpg` | 2761.4 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P4/número arma bncv395.jpg` | 2788.5 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P4/número colete 2732643 v01abr25.jpg` | 2565.5 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P4/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf` | 77.8 | **Caso Fático / Concreto** | 0 | Documento fático ou caso concreto. |
| `P4/PDF UNIFORME OPERACIONAL - 1º Ten PM Josemar.xlsx` | 73.3 | **Planilha / Dados** | 4,312 | Planilha de controle administrativo. |
| `P4/PDF UNIFORME PASSEIO - 1º Ten PM Josemar.xlsx` | 61.8 | **Planilha / Dados** | 3,528 | Planilha de controle administrativo. |
| `P4/Planilha de Armamento e Munição - 1º DIA UTUL MES (FECHAMENTO DE MÊS).xlsx` | 23.2 | **Planilha / Dados** | 8,122 | Planilha de controle administrativo. |
| `P4/Plaqueta Tarjeta na Blusa.png` | 1464.9 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P4/Quadro de viaturas Atual 2024.xlsx` | 19.8 | **Planilha / Dados** | 3,563 | Planilha de controle administrativo. |
| `P4/Relatório de Vistoria 5ª Cia.xlsx` | 6.4 | **Planilha / Dados** | 0 | Planilha de controle administrativo. |
| `P4/Slogan email PM 2.png` | 74.6 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P5/AUTORIDADES_5ª_CIA.xlsx` | 14.2 | **Planilha / Dados** | 2,746 | Planilha de controle administrativo. |
| `P5/BOPC Flagrante Roubo Araçatuba Bilac.pdf` | 382.0 | **Caso Fático / Concreto** | 18,820 | Documento fático ou caso concreto. |
| `P5/elogio individual comando p3.jpg` | 112.8 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P5/Estatitica.xlsx` | 33.5 | **Planilha / Dados** | 2,688 | Planilha de controle administrativo. |
| `P5/movimentações classificações onde trabalhei.png` | 54.0 | **Imagem / Mídia** | 0 | Arquivo de imagem (sem valor normativo direto). |
| `P5/Planilha de controle mediação Cap.xlsx` | 13.0 | **Planilha / Dados** | 1,353 | Planilha de controle administrativo. |

## J. Arquivos com erro de leitura

| Arquivo | Extensão | Erro de Leitura / Limitação |
|---|---|---|
| `JD/PPJM/Manuais, Leis, Regulamentos/PAP Sindicância.mht` | .mht | Sem texto extraível. |
| `JD/PPJM/Manuais, Leis, Regulamentos/RIOG.mht` | .mht | Sem texto extraível. |
| `Notebooklm/Supervisor Regional.zip` | .zip | Sem texto extraível. |
| `ocr_pdfs_imagem.py` | .py | Sem texto extraível. |
| `P2/Plano de Chamada/PLANO DE CHAMA.pptx` | .pptx | Formato de apresentação não suportado. |
| `P3/2023/ALTERAÇÃO ESCALA DOS GPS.ppt` | .ppt | Formato de apresentação não suportado. |
| `P3/2023/Apresentação 5 Cia.ppt` | .ppt | Formato de apresentação não suportado. |
| `P4/Adobe.Acrobat.Pro.DC.v2021.001.20155.rar` | .rar | Compactado não suportado (.rar). |
| `P4/Senha Spark.docx` | .docx | Sem texto extraível. |

## K. Extensões fora do esperado

Extensões que diferem dos formatos textuais normais (.pdf, .docx, .doc, .txt, .md):

| Extensão | Arquivos | Quantidade |
|---|---|---|
| `.cer` | `P1/CertExchange.cer` | 1 |
| `.htm` | `JD/PPJM/Manuais, Leis, Regulamentos/CC.htm`, `JD/PPJM/Manuais, Leis, Regulamentos/CF.htm`, `JD/PPJM/Manuais, Leis, Regulamentos/CP.htm`... | 10 |
| `.html` | `P3/relatorio_ronda.html` | 1 |
| `.jpeg` | `JD/Arquivo/2019/fotos rg civis agressão coroados.jpeg`, `JD/Arquivo/2024/WhatsApp Image 2024-04-12 at 09.08.30.jpeg`, `JD/PPJM/Orientações MDIP.jpeg`... | 18 |
| `.jpg` | `P1/20230830_144806.jpg`, `P1/Ten Josemar assinatura email 5 cia.JPG`, `P3/2024/20241029_162708.jpg`... | 20 |
| `.json` | `corpus_index.json` | 1 |
| `.mht` | `JD/PPJM/Manuais, Leis, Regulamentos/PAP Sindicância.mht`, `JD/PPJM/Manuais, Leis, Regulamentos/RIOG.mht` | 2 |
| `.mp4` | `P3/Outros/Preleção/Video Treinamento Zona de Perigo e Zona de Segurança 2018.mp4` | 1 |
| `.pfx` | `P1/JOSEMARDEPAULA,CapPM121876-0.pfx` | 1 |
| `.png` | `P1/2023/assinatura e-mail.png`, `P1/2023/assinatura para funcional digital.png`, `P1/Assinatura Cmt 3 Cia.PNG`... | 9 |
| `.ppt` | `P3/2023/ALTERAÇÃO ESCALA DOS GPS.ppt`, `P3/2023/Apresentação 5 Cia.ppt` | 2 |
| `.pptx` | `P2/Plano de Chamada/PLANO DE CHAMA.pptx` | 1 |
| `.py` | `despachadora.py`, `indexar_corpus.py`, `ocr_pdfs_imagem.py` | 3 |
| `.rar` | `P4/Adobe.Acrobat.Pro.DC.v2021.001.20155.rar` | 1 |
| `.rtf` | `P3/2025/OFÍCIO Prefeito Guararapes Festa Folclore.rtf`, `P3/2026/OFÍCIO Carnaval Bento de Abreu.rtf` | 2 |
| `.xlsx` | `P1/2025  - 11FEV25 - 5ª Cia PM - CPF e e-mail efetivo.xlsx`, `P1/Anos anteriores/2018/08. Escala dos Tenentes 2º BPMI - 01 a 31AGO18.xlsx`, `P1/Anos anteriores/2018/COPIA EFETIVO TELEFONE - 13DEZ17.xlsx`... | 69 |
| `.zip` | `Notebooklm/Supervisor Regional.zip` | 1 |

## L. Observações finais

* O relatório apresenta a classificação puramente recomendada com base nas heurísticas estruturais do indexador e contagens de texto.
* A decisão de priorização de OCR, segmentação ou saneamento de fáticos/holerites é de competência exclusiva de Josemar.
* Nenhuma alteração de filesystem foi efetuada nas pastas de dados do Google Drive ou nos arquivos do indexador canônico da central de automações.