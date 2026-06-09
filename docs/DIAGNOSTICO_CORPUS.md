# Diagnóstico do Corpus — Sprint 8.1

Gerado em: 2026-06-08 22:30:58

CORPUS_PATH: `G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs`

Índice analisado: `C:\projetos\central_automacoes\automacoes\despachadora\corpus_index.json`

## Resumo Executivo

- O corpus indexado atual tem 729 entradas e o inventário físico encontrou 922 arquivos sob `CORPUS_PATH`.
- A base é forte em documentos reais da casa e modelos/precedentes: espécies detectadas somam 436 ocorrências por heurística.
- A nova seção `Normas` existe e concentra 9 arquivos físicos, todos recentes na curadoria.
- Normativos internos PMESP aparecem de forma consistente: 213 sinais/citações de I-PM, NI, DTZ, POP ou NORSOP.
- A camada de legislação-base é desigual: RDPM/LC 893, CTB, CPP/CPM/CPPM aparecem; Lei 18.442/2026 não apareceu por presença textual.
- A camada de jurisprudência operacional é apenas parcial: 13 item(ns) foram classificados como jurisprudência por heurística, sem validação de fonte oficial.
- Há 193 arquivos físicos não indexados no inventário bruto; 0 não parecem excluídos pelas regras atuais do indexador.
- Há 0 entradas órfãs no índice e 4 entradas com erro registrado.
- Foram detectados 82 grupos com nomes repetidos e 83 grupos com hash idêntico.
- O diagnóstico não avalia vigência; ele só aponta presença, lacunas e riscos para orientar o Sprint 8.2.

## Integridade Somente Leitura

| Item | Valor |
| --- | --- |
| SHA-256 antes | a0fd86cec068712a9ef4acd05400ccddad64a46ba6cfbe35af6ef9b33ef39c5e |
| SHA-256 depois | a0fd86cec068712a9ef4acd05400ccddad64a46ba6cfbe35af6ef9b33ef39c5e |
| Hash idêntico? | SIM |
| Modificação do índice antes da leitura | 2026-06-08 22:01:46 |
| Entradas no índice | 729 |

## 1. Inventário Físico

| Seção | Arquivos | Tamanho | Mais antigo | Mais recente | Extensões principais |
| --- | --- | --- | --- | --- | --- |
| JD | 149 | 71.01 MB | 2013-09-09 12:33:10 | 2026-05-07 11:09:46 | .pdf:55, .doc:45, .docx:34, .htm:10, .jpeg:3, .mht:2 |
| Normas | 9 | 3.65 MB | 2020-04-07 07:30:20 | 2020-04-10 08:06:54 | .pdf:9 |
| Notebooklm | 11 | 139.01 MB | 2025-08-26 17:05:14 | 2026-02-16 10:32:23 | .pdf:11 |
| P1 | 325 | 132.11 MB | 2018-05-17 11:14:58 | 2026-02-26 06:09:37 | .pdf:214, .docx:67, .doc:18, .xlsx:9, .png:6, .jpeg:5, .jpg:2, .txt:2 |
| P2 | 24 | 4.11 MB | 2018-06-06 16:27:21 | 2024-10-17 17:16:37 | .docx:12, .pdf:7, .xlsx:3, .pptx:1, .doc:1 |
| P3 | 316 | 208.38 MB | 2016-11-22 12:39:16 | 2026-05-19 16:06:09 | .pdf:189, .docx:48, .xlsx:39, .doc:17, .jpeg:10, .jpg:5, .ppt:2, .rtf:2 |
| P4 | 64 | 149.72 MB | 2017-08-15 14:00:37 | 2026-01-27 15:54:40 | .pdf:26, .xlsx:15, .jpg:12, .docx:7, .png:2, .rar:1, .doc:1 |
| P5 | 16 | 1.82 MB | 2017-08-15 14:00:59 | 2025-09-04 08:59:40 | .docx:8, .xlsx:3, .pdf:2, .doc:1, .jpg:1, .png:1 |
| __pycache__ | 1 | 0.02 MB | 2026-06-04 23:23:30 | 2026-06-04 23:23:30 | .pyc:1 |
| __raiz__ | 7 | 31.57 MB | 2026-06-04 22:59:38 | 2026-06-08 22:01:46 | .py:3, .md:2, .json:1, .txt:1 |

### Distribuição por extensão

| Extensão | Arquivos |
| --- | --- |
| .pdf | 513 |
| .docx | 176 |
| .doc | 83 |
| .xlsx | 69 |
| .jpg | 20 |
| .jpeg | 18 |
| .htm | 10 |
| .png | 9 |
| .txt | 5 |
| .py | 3 |
| .md | 2 |
| .mht | 2 |
| .ppt | 2 |
| .rtf | 2 |
| .json | 1 |
| .cer | 1 |
| .pfx | 1 |
| .pptx | 1 |
| .html | 1 |
| .mp4 | 1 |
| .rar | 1 |
| .pyc | 1 |

## 2. Cruzamento Drive × Índice

| Métrica | Valor |
| --- | --- |
| Arquivos físicos no CORPUS_PATH | 922 |
| Entradas no corpus_index.json | 729 |
| Arquivos físicos não indexados (bruto) | 193 |
| Arquivos físicos não indexados e aparentemente indexáveis | 0 |
| Entradas órfãs no índice | 0 |
| Entradas com error | 4 |
| Entradas sem error e texto < 150 chars | 9 |
| Chaves duplicadas no índice | 0 |

### Entradas com erro

| Entrada | Erro |
| --- | --- |
| __pycache__/indexar_corpus.cpython-314.pyc | tipo_nao_suportado |
| JD/PPJM/Manuais, Leis, Regulamentos/PAP Sindicância.mht | tipo_nao_suportado |
| JD/PPJM/Manuais, Leis, Regulamentos/RIOG.mht | tipo_nao_suportado |
| ocr_pdfs_imagem.py | tipo_nao_suportado |

### Arquivos físicos não indexados — amostra

| Arquivo | Tipo | KB | Excluído pelo indexador? |
| --- | --- | --- | --- |
| corpus_index.json | .json | 32245.5 | sim |
| despachadora.py | .py | 42.0 | sim |
| indexar_corpus.py | .py | 13.8 | sim |
| JD/Arquivo/2019/fotos rg civis agressão coroados.jpeg | .jpeg | 148.0 | sim |
| JD/Arquivo/2024/WhatsApp Image 2024-04-12 at 09.08.30.jpeg | .jpeg | 391.2 | sim |
| JD/PPJM/Orientações MDIP.jpeg | .jpeg | 192.9 | sim |
| P1/20230830_144806.jpg | .jpg | 1209.2 | sim |
| P1/Assinatura Cmt 3 Cia.PNG | .png | 52.8 | sim |
| P1/Assinatura email Cmt Interino 3 Cia.PNG | .png | 51.7 | sim |
| P1/CertExchange.cer | .cer | 1.0 | sim |
| P1/Efetivo Atualizado 5ª Cia 20jan26.jpeg | .jpeg | 273.3 | sim |
| P1/JOSEMARDEPAULA,CapPM121876-0.pfx | .pfx | 2.6 | sim |
| P1/Relação do Efetivo 5ª Cia jul25 por fração.jpeg | .jpeg | 593.8 | sim |
| P1/Relação do efetivo 5ª Cia jul25 por antiguidade.jpeg | .jpeg | 497.8 | sim |
| P1/Ten Josemar assinatura email 5 cia.JPG | .jpg | 32.0 | sim |
| P1/aSSINATURA EMAIL CARTAO.PNG | .png | 51.2 | sim |
| P1/movimentações classificações onde trabalhei.png | .png | 54.0 | sim |
| P1/2023/assinatura e-mail.png | .png | 88.8 | sim |
| P1/2023/assinatura para funcional digital.png | .png | 29.1 | sim |
| P1/2024/Efetivo atualizado 5 cia 29fev24.jpeg | .jpeg | 454.2 | sim |
| P1/2024/Previa Escala Supervisor Regional abr24.jpeg | .jpeg | 191.6 | sim |
| P1/Holerites/2014/Demonstrativo_09_2014(1).pdf | .pdf | 33.2 | sim |
| P1/Holerites/2014/Demonstrativo_09_2014.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2014/Demonstrativo_10_2014.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2014/Demonstrativo_11_2014(1).pdf | .pdf | 33.2 | sim |
| P1/Holerites/2014/Demonstrativo_11_2014.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2014/Demonstrativo_12_2014.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_01_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_02_2015.pdf | .pdf | 46.7 | sim |
| P1/Holerites/2015/Demonstrativo_03_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_04_2015(1).pdf | .pdf | 33.2 | sim |
| P1/Holerites/2015/Demonstrativo_04_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_05_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_06_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_07_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_08_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_09_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_10_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_11_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2015/Demonstrativo_12_2015.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_01_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_02_2016.pdf | .pdf | 46.7 | sim |
| P1/Holerites/2016/Demonstrativo_03_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_04_2016.pdf | .pdf | 46.7 | sim |
| P1/Holerites/2016/Demonstrativo_05_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_06_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_07_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_08_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_09_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_10_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_11_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2016/Demonstrativo_12_2016.pdf | .pdf | 33.8 | sim |
| P1/Holerites/2017/Demonstrativo_01_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_02_2017.pdf | .pdf | 47.4 | sim |
| P1/Holerites/2017/Demonstrativo_03_2017.pdf | .pdf | 47.4 | sim |
| P1/Holerites/2017/Demonstrativo_04_2017(1).pdf | .pdf | 33.8 | sim |
| P1/Holerites/2017/Demonstrativo_04_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_05_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_06_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_07_2017(1).pdf | .pdf | 33.8 | sim |
| P1/Holerites/2017/Demonstrativo_07_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_08_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_09_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_10_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_11_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2017/Demonstrativo_12_2017.pdf | .pdf | 34.5 | sim |
| P1/Holerites/2018/Demonstrativo_01_2018(1).pdf | .pdf | 34.0 | sim |
| P1/Holerites/2018/Demonstrativo_01_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_02_2018(1).pdf | .pdf | 34.0 | sim |
| P1/Holerites/2018/Demonstrativo_02_2018.pdf | .pdf | 47.6 | sim |
| P1/Holerites/2018/Demonstrativo_03_2018.pdf | .pdf | 47.6 | sim |
| P1/Holerites/2018/Demonstrativo_04_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_05_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_06_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_07_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_08_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_09_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_10_2018(1).pdf | .pdf | 34.0 | sim |
| P1/Holerites/2018/Demonstrativo_10_2018.pdf | .pdf | 34.6 | sim |
| P1/Holerites/2018/Demonstrativo_11_2018.pdf | .pdf | 34.6 | sim |

### Entradas órfãs — amostra

(nenhuma)

### Textos abaixo do mínimo — amostra

| Entrada | Chars |
| --- | --- |
| P1/2023/assinatura para funcional digital.pdf | 11 |
| P1/Anos anteriores/2020/EEP___Usuário_da_Arma_de_Incapacitação_Neuromuscular___2020-Certificado_3536.pdf | 50 |
| P1/Anos anteriores/2021/Metas para a Cia 2020 Cap Brito.pdf | 115 |
| P1/normas i-7-pm/Anexo 2_OSv 013 30 19_Instruções para correspondencia I-31-PM.docx | 9 |
| P1/sade/sade 2022/Recurso Celeste/Requerimento juntar/13.pdf | 64 |
| P3/Pauta Reunião Efetivo.docx | 42 |
| P3/Outros/Preleção/orientações uso de granadas espargidores munições químicas na PM elastômero de fev de 2020 1929.txt | 78 |
| P4/Relatório de Vistoria 5ª Cia.xlsx | 0 |
| P4/Senha Spark.docx | 0 |

### Prováveis duplicatas por nome — top 30

| Nome | Qtd | Exemplos |
| --- | --- | --- |
| Relatório de Utilização de AIN.pdf | 3 | JD/Relatório de Utilização de AIN.pdf; P3/Outros/Relatório de Utilização de AIN.pdf; P4/Relatório de Utilização de AIN.pdf |
| Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf | 3 | P3/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf; P3/OS/NI_002_02_17 acidente de trânsito com viatura/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf; P4/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf |
| Modelo - CROQUI CADAVÉRICO.doc | 2 | JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.doc; JD/PPJM/Modelo - CROQUI CADAVÉRICO.doc |
| Modelo - CROQUI CADAVÉRICO.pdf | 2 | JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.pdf; JD/PPJM/Modelo - CROQUI CADAVÉRICO.pdf |
| dpj_riog_mdip.doc | 2 | JD/Arquivo/2024/Sup Reg/dpj_riog_mdip.doc; JD/PPJM/dpj_riog_mdip.doc |
| Despacho para avaliador.docx | 2 | P1/Despacho para avaliador.docx; P1/sade/sade 2022/Recurso Celeste/Despacho para avaliador.docx |
| I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf | 2 | P1/I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf; P1/sade/I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf |
| PMP142.doc | 2 | P1/PMP142.doc; P1/sade/PMP142.doc |
| movimentações classificações onde trabalhei.png | 2 | P1/movimentações classificações onde trabalhei.png; P5/movimentações classificações onde trabalhei.png |
| PMP118 DS Cap Josemar.doc | 2 | P1/2022/PMP118 DS Cap Josemar.doc; P1/Anos anteriores/2021/PMP118 DS Cap Josemar.doc |
| Demonstrativo_09_2014(1).pdf | 2 | P1/Holerites/2014/Demonstrativo_09_2014(1).pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_09_2014(1).pdf |
| Demonstrativo_10_2014.pdf | 2 | P1/Holerites/2014/Demonstrativo_10_2014.pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_10_2014.pdf |
| Demonstrativo_11_2014(1).pdf | 2 | P1/Holerites/2014/Demonstrativo_11_2014(1).pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014(1).pdf |
| Demonstrativo_11_2014.pdf | 2 | P1/Holerites/2014/Demonstrativo_11_2014.pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014.pdf |
| Demonstrativo_12_2014.pdf | 2 | P1/Holerites/2014/Demonstrativo_12_2014.pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_12_2014.pdf |
| Demonstrativo_01_2015.pdf | 2 | P1/Holerites/2015/Demonstrativo_01_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_01_2015.pdf |
| Demonstrativo_03_2015.pdf | 2 | P1/Holerites/2015/Demonstrativo_03_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_03_2015.pdf |
| Demonstrativo_04_2015(1).pdf | 2 | P1/Holerites/2015/Demonstrativo_04_2015(1).pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_04_2015(1).pdf |
| Demonstrativo_07_2015.pdf | 2 | P1/Holerites/2015/Demonstrativo_07_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_07_2015.pdf |
| Demonstrativo_08_2015.pdf | 2 | P1/Holerites/2015/Demonstrativo_08_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_08_2015.pdf |
| Demonstrativo_09_2015.pdf | 2 | P1/Holerites/2015/Demonstrativo_09_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_09_2015.pdf |
| Demonstrativo_10_2015.pdf | 2 | P1/Holerites/2015/Demonstrativo_10_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_10_2015.pdf |
| Demonstrativo_01_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_01_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_01_2016.pdf |
| Demonstrativo_02_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_02_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_02_2016.pdf |
| Demonstrativo_03_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_03_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_03_2016.pdf |
| Demonstrativo_04_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_04_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_04_2016.pdf |
| Demonstrativo_05_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_05_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_05_2016.pdf |
| Demonstrativo_06_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_06_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_06_2016.pdf |
| Demonstrativo_07_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_07_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_07_2016.pdf |
| Demonstrativo_08_2016.pdf | 2 | P1/Holerites/2016/Demonstrativo_08_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_08_2016.pdf |

### Prováveis duplicatas por hash idêntico — top 30

| Hash | Qtd | Exemplos |
| --- | --- | --- |
| 9f9e8bd79feb | 6 | P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Aracanguá.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Auriflama.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Gastão.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Guzolândia.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Delegado Iracema.docx |
| db2abe27d854 | 3 | JD/Relatório de Utilização de AIN.pdf; P3/Outros/Relatório de Utilização de AIN.pdf; P4/Relatório de Utilização de AIN.pdf |
| d2a16dbacbc4 | 3 | P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz  Araçatuba.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz  Nhandeara.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Juiz Auriflama.docx |
| 9598328fd7a8 | 3 | P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor Auriflama.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor Nhandeara Rasfael.docx; P1/Anos anteriores/2021/Ofícios apresentação 3 cia/Promotor de Araçatuba.docx |
| 16690e2c6373 | 3 | P3/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf; P3/OS/NI_002_02_17 acidente de trânsito com viatura/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf; P4/OS/Procedimentos nas ocorrências de acidente de trâansito sem vítim envolvendo viatura.pdf |
| 08334cb2ba46 | 2 | JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.doc; JD/PPJM/Modelo - CROQUI CADAVÉRICO.doc |
| 2075ebf923d4 | 2 | JD/Arquivo/2024/Sup Reg/Modelo - CROQUI CADAVÉRICO.pdf; JD/PPJM/Modelo - CROQUI CADAVÉRICO.pdf |
| 1b50ed05ee6a | 2 | JD/PPJM/Manuais, Leis, Regulamentos/I-40-PM - (Bol G PM 101-23) II 1.pdf; JD/PPJM/Manuais, Leis, Regulamentos/I-40-PM - (Bol G PM 101-23) II.pdf |
| ac03b1e99f71 | 2 | Notebooklm/Supervisor Regional/Relatório Ronda do Oficial  Supervisor Regional 23ago25 -  Modelo.pdf; P3/2025/Relatório Ronda do Oficial  Supervisor Regional 23ago25.pdf |
| 05767f5b1ff0 | 2 | P1/I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf; P1/sade/I-24-PM - 3ª Edicao 10NOV15-alterada pela Port PM1-010_02_15.pdf |
| 2bd7feabd75a | 2 | P1/movimentações classificações onde trabalhei.png; P5/movimentações classificações onde trabalhei.png |
| b5b6e8193073 | 2 | P1/2022/PMESPEXP202241072A documentação reserva hotel de trânsito alojamento central.pdf; P1/2022/PMESPEXP202241072A.pdf |
| fd3b278d47cc | 2 | P1/Anos anteriores/2020/Relação EFETIVO nov20.xlsx; P2/Revista de armario EFETIVO nov20.xlsx |
| 8c1adba9988c | 2 | P1/Holerites/2014/Demonstrativo_09_2014(1).pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_09_2014(1).pdf |
| 8992aea6b8b4 | 2 | P1/Holerites/2014/Demonstrativo_10_2014.pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_10_2014.pdf |
| 60c6cf3e6b0e | 2 | P1/Holerites/2014/Demonstrativo_11_2014(1).pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014(1).pdf |
| 22a017dacbcc | 2 | P1/Holerites/2014/Demonstrativo_11_2014.pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_11_2014.pdf |
| 8f00e1a37db8 | 2 | P1/Holerites/2014/Demonstrativo_12_2014.pdf; P1/Holerites Bonus DEJEM/2014/Demonstrativo_12_2014.pdf |
| be8ebd4f6cad | 2 | P1/Holerites/2015/Demonstrativo_01_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_01_2015.pdf |
| b0b7b06ffcca | 2 | P1/Holerites/2015/Demonstrativo_03_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_03_2015.pdf |
| 6ef60387bdee | 2 | P1/Holerites/2015/Demonstrativo_04_2015(1).pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_04_2015(1).pdf |
| 57ed17903a7d | 2 | P1/Holerites/2015/Demonstrativo_07_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_07_2015.pdf |
| 4575f5ffcd7d | 2 | P1/Holerites/2015/Demonstrativo_08_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_08_2015.pdf |
| d92d5b77241c | 2 | P1/Holerites/2015/Demonstrativo_09_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_09_2015.pdf |
| f9e1d9864980 | 2 | P1/Holerites/2015/Demonstrativo_10_2015.pdf; P1/Holerites Bonus DEJEM/2015/Demonstrativo_10_2015.pdf |
| 1facd6a97b2a | 2 | P1/Holerites/2016/Demonstrativo_01_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_01_2016.pdf |
| 3c1c9eb7f813 | 2 | P1/Holerites/2016/Demonstrativo_02_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_02_2016.pdf |
| 424ddd6decce | 2 | P1/Holerites/2016/Demonstrativo_03_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_03_2016.pdf |
| b13cdcedf4be | 2 | P1/Holerites/2016/Demonstrativo_04_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_04_2016.pdf |
| 604472dde19f | 2 | P1/Holerites/2016/Demonstrativo_05_2016.pdf; P1/Holerites Bonus DEJEM/2016/Demonstrativo_05_2016.pdf |

## 3. Classificação por Natureza

| Natureza | Arquivos |
| --- | --- |
| NORMA | 297 |
| NAO_CLASSIFICADO | 192 |
| PRECEDENTE | 192 |
| OUTRO | 174 |
| MODELO_DE_REDACAO | 37 |
| PROCEDIMENTAL | 17 |
| JURISPRUDENCIA | 13 |

## 4. Classificação por Espécie

| Espécie | Arquivos |
| --- | --- |
| outro | 486 |
| oficio | 131 |
| parte | 107 |
| relatorio | 104 |
| despacho | 32 |
| escala | 30 |
| ipm | 20 |
| tc | 5 |
| ata | 5 |
| sindicancia | 2 |

## 5. Normas Presentes ou Citadas

Presença textual apenas; este diagnóstico não afirma vigência, revogação nem suficiência como fonte oficial.

| Norma/sinal | Ocorrências em arquivos físicos |
| --- | --- |
| DTZ/Diretriz | 56 |
| POP | 50 |
| CTB | 41 |
| CPP | 37 |
| NI PM | 33 |
| Resolução SSP | 32 |
| CPM | 30 |
| CP | 22 |
| UFESP | 20 |
| NORSOP | 20 |
| CONTRAN | 19 |
| CPPM | 17 |
| Lei 11.340 | 16 |
| LC 893/RDPM | 14 |
| I-1-PM | 13 |
| I-16-PM | 11 |
| I-42-PM | 11 |
| I-7-PM | 10 |
| ECA | 7 |
| I-24-PM | 7 |
| I-38-PM | 6 |
| Res PGE 9/2024 | 4 |
| I-40-PM | 4 |
| I-36-PM | 4 |
| I-31-PM | 3 |
| I-02-PM | 2 |
| I-15-PM | 2 |
| I-23-PM | 2 |
| I-43-PM | 1 |
| I-5-PM | 1 |
| I-2-PM | 1 |
| Lei 616/1974 | 1 |

## 6. Lacunas por Camada

| Camada/item | Status | Sinais | Observação |
| --- | --- | --- | --- |
| Camada 1 - CP | PRESENTE | 22 | Presença textual; vigência não avaliada. |
| Camada 1 - CPP | PRESENTE | 37 | Presença textual; vigência não avaliada. |
| Camada 1 - CTB | PRESENTE | 41 | Presença textual; vigência não avaliada. |
| Camada 1 - Lei 11.343 | AUSENTE | 0 | Presença textual; vigência não avaliada. |
| Camada 1 - Lei 11.340 | PRESENTE | 16 | Presença textual; vigência não avaliada. |
| Camada 1 - ECA | PRESENTE | 7 | Presença textual; vigência não avaliada. |
| Camada 1 - CPM | PRESENTE | 30 | Presença textual; vigência não avaliada. |
| Camada 1 - CPPM | PRESENTE | 17 | Presença textual; vigência não avaliada. |
| Camada 1 - RDPM/LC 893 | PRESENTE | 14 | Presença textual; vigência não avaliada. |
| Camada 1 - Lei 616/1974 | PRESENTE | 1 | Presença textual; vigência não avaliada. |
| Camada 1 - Lei 18.442/2026 | AUSENTE | 0 | Presença textual; vigência não avaliada. |
| Camada 2 - Normativos internos PMESP | PRESENTE | 213 | Há instruções, NIs, diretrizes/POPs; não foi avaliada vigência. |
| Camada 3 - Modelos por espécie | PRESENTE | 436 | Contagem por espécie mistura modelos e precedentes; precisa metadado no 8.2. |
| Camada 4 - Jurisprudência operacional | PARCIAL | 13 | Detectado por heurística textual; sem validação de fonte oficial. |
| Camada 5 - Procedimental | PRESENTE | 17 | POPs, fluxos e checklists aparecem por heurística. |

## Anomalias e Pendências de Decisão

- `__pycache__` aparece no corpus/índice; reportado como anomalia, sem tocar. Candidato para exclusão no Sprint 8.2.
- Pendência documental: D-09 em `docs/DECISOES.md` diz que `corpus_index.json` vai no git, mas o fluxo real recente usa Drive + `.gitignore`. Reconciliar com nova decisão, sem resolver no 8.1.
- Histórico incompleto detectado: STATUS registrava 728 entradas após enriquecimento, mas o índice atual tem 729; a diferença é o OCR do `NI PM3_004_03_13 ICC.pdf` executado em 08/06/2026, com 10.090 chars adicionados.

## Suposições de Classificação

- `NORMA`: detectada por nome/texto contendo I-NN-PM, NI, DTZ, POP, portaria, resolução, lei, RDPM, CTB, CONTRAN, NORSOP ou termos normativos equivalentes.
- `MODELO_DE_REDACAO`: detectado por termos como modelo, minuta, template, exemplo ou modelos nominais de ofício/despacho/portaria.
- `PRECEDENTE`: documento da casa com espécie administrativa detectável, sem marcador claro de modelo.
- `JURISPRUDENCIA`: presença de STF, STJ, súmula, HC, recurso especial/extraordinário ou termo jurisprudência.
- `PROCEDIMENTAL`: presença de checklist, fluxograma, POP, roteiro, tutorial, processo ou procedimento.
- `NAO_CLASSIFICADO`: sem texto útil e sem sinal seguro no nome/caminho; não houve presunção de conteúdo.

## Itens NAO_CLASSIFICADO — amostra

| Arquivo |
| --- |
| corpus_index.json |
| despachadora.py |
| indexar_corpus.py |
| ocr_pdfs_imagem.py |
| JD/Arquivo/2019/fotos rg civis agressão coroados.jpeg |
| JD/Arquivo/2024/WhatsApp Image 2024-04-12 at 09.08.30.jpeg |
| JD/PPJM/Orientações MDIP.jpeg |
| JD/PPJM/Manuais, Leis, Regulamentos/PAP Sindicância.mht |
| JD/PPJM/Manuais, Leis, Regulamentos/RIOG.mht |
| P1/20230830_144806.jpg |
| P1/Assinatura Cmt 3 Cia.PNG |
| P1/Assinatura email Cmt Interino 3 Cia.PNG |
| P1/CertExchange.cer |
| P1/Efetivo Atualizado 5ª Cia 20jan26.jpeg |
| P1/JOSEMARDEPAULA,CapPM121876-0.pfx |
| P1/Relação do Efetivo 5ª Cia jul25 por fração.jpeg |
| P1/Relação do efetivo 5ª Cia jul25 por antiguidade.jpeg |
| P1/Ten Josemar assinatura email 5 cia.JPG |
| P1/aSSINATURA EMAIL CARTAO.PNG |
| P1/movimentações classificações onde trabalhei.png |
| P1/2023/assinatura e-mail.png |
| P1/2023/assinatura para funcional digital.png |
| P1/2024/Efetivo atualizado 5 cia 29fev24.jpeg |
| P1/Holerites/2014/Demonstrativo_09_2014(1).pdf |
| P1/Holerites/2014/Demonstrativo_09_2014.pdf |
| P1/Holerites/2014/Demonstrativo_10_2014.pdf |
| P1/Holerites/2014/Demonstrativo_11_2014(1).pdf |
| P1/Holerites/2014/Demonstrativo_11_2014.pdf |
| P1/Holerites/2014/Demonstrativo_12_2014.pdf |
| P1/Holerites/2015/Demonstrativo_01_2015.pdf |
| P1/Holerites/2015/Demonstrativo_02_2015.pdf |
| P1/Holerites/2015/Demonstrativo_03_2015.pdf |
| P1/Holerites/2015/Demonstrativo_04_2015(1).pdf |
| P1/Holerites/2015/Demonstrativo_04_2015.pdf |
| P1/Holerites/2015/Demonstrativo_05_2015.pdf |
| P1/Holerites/2015/Demonstrativo_06_2015.pdf |
| P1/Holerites/2015/Demonstrativo_07_2015.pdf |
| P1/Holerites/2015/Demonstrativo_08_2015.pdf |
| P1/Holerites/2015/Demonstrativo_09_2015.pdf |
| P1/Holerites/2015/Demonstrativo_10_2015.pdf |
| P1/Holerites/2015/Demonstrativo_11_2015.pdf |
| P1/Holerites/2015/Demonstrativo_12_2015.pdf |
| P1/Holerites/2016/Demonstrativo_01_2016.pdf |
| P1/Holerites/2016/Demonstrativo_02_2016.pdf |
| P1/Holerites/2016/Demonstrativo_03_2016.pdf |
| P1/Holerites/2016/Demonstrativo_04_2016.pdf |
| P1/Holerites/2016/Demonstrativo_05_2016.pdf |
| P1/Holerites/2016/Demonstrativo_06_2016.pdf |
| P1/Holerites/2016/Demonstrativo_07_2016.pdf |
| P1/Holerites/2016/Demonstrativo_08_2016.pdf |
| P1/Holerites/2016/Demonstrativo_09_2016.pdf |
| P1/Holerites/2016/Demonstrativo_10_2016.pdf |
| P1/Holerites/2016/Demonstrativo_11_2016.pdf |
| P1/Holerites/2016/Demonstrativo_12_2016.pdf |
| P1/Holerites/2017/Demonstrativo_01_2017.pdf |
| P1/Holerites/2017/Demonstrativo_02_2017.pdf |
| P1/Holerites/2017/Demonstrativo_03_2017.pdf |
| P1/Holerites/2017/Demonstrativo_04_2017(1).pdf |
| P1/Holerites/2017/Demonstrativo_04_2017.pdf |
| P1/Holerites/2017/Demonstrativo_05_2017.pdf |
| P1/Holerites/2017/Demonstrativo_06_2017.pdf |
| P1/Holerites/2017/Demonstrativo_07_2017(1).pdf |
| P1/Holerites/2017/Demonstrativo_07_2017.pdf |
| P1/Holerites/2017/Demonstrativo_08_2017.pdf |
| P1/Holerites/2017/Demonstrativo_09_2017.pdf |
| P1/Holerites/2017/Demonstrativo_10_2017.pdf |
| P1/Holerites/2017/Demonstrativo_11_2017.pdf |
| P1/Holerites/2017/Demonstrativo_12_2017.pdf |
| P1/Holerites/2018/Demonstrativo_01_2018(1).pdf |
| P1/Holerites/2018/Demonstrativo_01_2018.pdf |
| P1/Holerites/2018/Demonstrativo_02_2018(1).pdf |
| P1/Holerites/2018/Demonstrativo_02_2018.pdf |
| P1/Holerites/2018/Demonstrativo_03_2018.pdf |
| P1/Holerites/2018/Demonstrativo_04_2018.pdf |
| P1/Holerites/2018/Demonstrativo_05_2018.pdf |
| P1/Holerites/2018/Demonstrativo_06_2018.pdf |
| P1/Holerites/2018/Demonstrativo_07_2018.pdf |
| P1/Holerites/2018/Demonstrativo_08_2018.pdf |
| P1/Holerites/2018/Demonstrativo_09_2018.pdf |
| P1/Holerites/2018/Demonstrativo_10_2018(1).pdf |

## Arquivos Gerados

- Inventário CSV: `saidas\inventario_corpus.csv`
- Diagnóstico Markdown: `docs\DIAGNOSTICO_CORPUS.md`
