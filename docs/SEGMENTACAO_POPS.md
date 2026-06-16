# Segmentacao dos POPs

Executado em 16/06/2026, como parte do Sprint 8.4 - Curadoria de fontes oficiais.

## Origem

Arquivo original:

`G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\Notebooklm\Supervisor Regional\POPs.pdf`

Destino dos segmentos:

`G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\Normas\POPs_Segmentos\`

O compilado de POPs foi segmentado para melhorar a recuperacao por densidade da Despachadora. A regra final foi consolidar POPs pequenos apenas quando havia relacao operacional real, preservando os demais 1:1.

## Segmentos criados

| Arquivo | POPs / paginas | Caracteres | Natureza |
|---|---|---:|---|
| `POP_1_01_00_Abordagem_Pessoas_a_Pe.txt` | 1.01 / 122-171 | 94.378 | PROCEDIMENTAL |
| `POP_1_02_00_Abordagem_Policial_Vtr_4_Rodas.txt` | 1.02 / 172-211 | 66.648 | PROCEDIMENTAL |
| `POP_3_01_00_Acidente_Transito.txt` | 3.01 / 281-296 | 31.233 | PROCEDIMENTAL |
| `POP_3_02_00_Ocorrencia_Envolvendo_Autoridades.txt` | 3.02 / 297-308 | 25.096 | PROCEDIMENTAL |
| `POP_3_03_00_Transporte_Guarda_Presos.txt` | 3.03 / 309-345 | 67.742 | NORMA |
| `POP_3_04_00_Atendimento_Ocorrencia_Horario_Folga.txt` | 3.04 / 346-356 | 20.243 | PROCEDIMENTAL |
| `POP_4_01_00_Acompanhamento_e_Cerco.txt` | 4.01 / 1-16 | 24.353 | PROCEDIMENTAL |
| `POP_4_02_00_Bloqueio_Policial.txt` | 4.02 / 368-392 | 40.891 | PROCEDIMENTAL |
| `POP_4_04_00_Cumprimento_Mandado_Judicial.txt` | 4.04 / 393-404 | 24.287 | PROCEDIMENTAL |
| `POP_4_05_00_Forca_Tatica_Contencao.txt` | 4.05 / 405-421 | 27.126 | PROCEDIMENTAL |
| `POP_4_06_00_Atuacao_Manifestacoes.txt` | 4.06 / 422-439 | 37.319 | PROCEDIMENTAL |
| `POP_5_03_00_Uso_de_Algemas.txt` | 5.03 / 440-466 | 28.696 | NORMA |
| `POP_5_12_00_Emprego_Municao_Elastomero.txt` | 5.12 / 17-30 | 21.320 | PROCEDIMENTAL |
| `POP_5_13_00_Transposicao_Obstaculo.txt` | 5.13 / 505-544 | 39.098 | PROCEDIMENTAL |
| `POP_5_14_00_Municao_Impacto_FN303.txt` | 5.14 / 545-557 | 21.482 | PROCEDIMENTAL |
| `POP_5_15_5_25_Armas_Brancas.txt` | 5.15 / 558-567 + 5.25 / 749-759 | 44.710 | PROCEDIMENTAL |
| `POP_5_16_00_Cameras_Operacionais_Portateis.txt` | 5.16 / 31-50 | 31.138 | PROCEDIMENTAL |
| `POP_5_18_00_Granadas_Policiais.txt` | 5.18 / 595-637 | 42.479 | PROCEDIMENTAL |
| `POP_5_19_00_Resgate_Tatico_PM_Ferido.txt` | 5.19 / 638-675 | 42.148 | PROCEDIMENTAL |
| `POP_5_20_00_Incapacitacao_Neuromuscular.txt` | 5.20 / 676-701 | 24.128 | PROCEDIMENTAL |
| `POP_5_21_00_TASER_X2.txt` | 5.21 / 702-734 | 25.518 | PROCEDIMENTAL |
| `POP_5_22_00_Municao_Bean_Bag.txt` | 5.22 / 735-748 | 21.235 | PROCEDIMENTAL |
| `POP_5_27_00_Atendimento_Ocorrencia_PcD.txt` | 5.27 / 760-774 | 28.163 | PROCEDIMENTAL |
| `POP_5_28_00_Cameras_Operacionais_Portateis_Motorola.txt` | 5.28 / 775-799 | 44.897 | PROCEDIMENTAL |
| `POP_Deslocamento_Estacionamento_Passagem.txt` | 5.04-5.06 / 467-496 | 37.008 | PROCEDIMENTAL |
| `POP_GasPimenta_Tonfa_Cinto.txt` | 5.10, 5.11, 5.17 / 497-504; 568-594 | 24.250 | PROCEDIMENTAL |
| `POP_Ocorrencias_Gerais.txt` | 1.07, 1.08, 1.09, 2.01 / 243-271 | 46.577 | PROCEDIMENTAL |
| `POP_Policiamento_com_Motocicleta.txt` | Policiamento com motocicleta / 51-121 | 112.194 | PROCEDIMENTAL |
| `POP_PreservacaoLocal_MortePM_Bombas.txt` | 2.02, 3.05, 3.06 / 272-280; 357-367 | 35.565 | PROCEDIMENTAL |
| `POP_Roubo_Estabelecimento_Comercial.txt` | 2.07 / 800-810 | 23.571 | PROCEDIMENTAL |
| `POP_Violencia_Domestica.txt` | Violencia domestica / 811-824 | 31.515 | PROCEDIMENTAL |
| `POP_Vistoria_Drogas.txt` | 1.05 / 212-232 + 1.06 / 233-242 | 49.321 | PROCEDIMENTAL |

Todos os 32 segmentos ficaram entre 20k e 150k caracteres, com `error=None`.

## Decisoes de extracao

O POP 5.16.00, sobre Cameras Operacionais Portateis, foi extraido de trecho cujo PDF original estava rotulado como `(PROTEGIDO)`. A decisao de curadoria foi manter apenas o procedimento operacional, removendo trechos sobre classificacao de sigilo dos dados/videos produzidos pela COP. A observacao registrada no indice foi:

`POP 5.16.00. Trechos sobre classificação de sigilo dos dados/vídeos da COP removidos na extração — mantido apenas o procedimento operacional. Fonte original rotulada (PROTEGIDO) no nome do arquivo PDF mesclado.`

O POP 5.16.00 foi comparado com o POP 5.28.00, tambem sobre Cameras Operacionais Portateis. A comparacao retornou `sequence_ratio=0,17`, suficiente para descartar duplicidade. Ambos foram mantidos como entradas separadas: o 5.16 trata do procedimento operacional geral de uso da COP, enquanto o 5.28 trata do fluxo especifico da COP Motorola.

## Auditoria bruto-limpo

Cinco POPs pequenos tiveram queda de caracteres acima do esperado na primeira limpeza. A auditoria mostrou que havia conteudo operacional removido indevidamente, como `MATERIAL NECESSARIO`, `ATIVIDADES CRITICAS`, `ACOES CORRETIVAS` e `ESCLARECIMENTOS`. Foi reaplicada extracao minima somente nesses cinco casos.

| POP | Paginas | Bruto | Limpo corrigido | Delta |
|---|---:|---:|---:|---:|
| 1.06 Drogas Ilicitas | 233-242 | 20.896 | 20.356 | 540 |
| 3.04 Horario de folga | 346-356 | 21.262 | 20.243 | 1.019 |
| 5.15 Defesa armas brancas | 558-567 | 23.079 | 22.422 | 657 |
| 5.25 Pessoa suicida/arma branca | 749-759 | 22.840 | 22.213 | 627 |
| Roubo estabelecimento comercial | 800-810 | 24.232 | 23.571 | 661 |

Apos a correcao, dois agrupamentos tematicos foram aplicados:

- `POP_Vistoria_Drogas.txt`: POPs 1.05 e 1.06, por relacao operacional entre vistoria de veiculo e drogas ilicitas.
- `POP_5_15_5_25_Armas_Brancas.txt`: POPs 5.15 e 5.25, por relacao operacional em ocorrencias com arma branca.

## Classificacao

O enum do classificador nao possui categoria intermediaria do tipo `PROCEDIMENTAL_COM_FUNDAMENTO`. A decisao final foi:

- 30 POPs puramente operacionais: `natureza=PROCEDIMENTAL`, `classificacao_origem=humana`.
- 2 POPs com fundamento juridico embutido: `natureza=NORMA`, `classificacao_origem=humana`.

Os dois mantidos como `NORMA` foram:

- `POP_3_03_00_Transporte_Guarda_Presos.txt`, por citar fundamentos juridicos sobre algemas no transporte/guarda de presos, incluindo Decreto 8.858/2016 e Sumula Vinculante 11/STF.
- `POP_5_03_00_Uso_de_Algemas.txt`, por tratar diretamente do uso de algemas com fundamento no Decreto Federal 8.858/2016 e na Sumula Vinculante 11.

## Prova de aditividade

```text
TOTAL_ANTES 642
TOTAL_DEPOIS 674
ADICIONADAS 32
POPS_ADICIONADOS 32
CHAVES_ANTIGAS_FALTANDO 0
OBJETOS_ANTIGOS_ALTERADOS 0
ADITIVIDADE_OK True
```

## SHA-256 final

O `corpus_index.json` final foi copiado para:

`G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs\corpus_index.json`

SHA-256 final:

`a31b54687e62fe0be12ad9a3aec00a8e1c807c2fba864f951a359108665f7384`

O SHA local e o SHA do Drive foram conferidos apos a copia e bateram, ambos com 64 caracteres.

## Caminho e backups

O caminho canonico atual do corpus foi confirmado como:

`G:\Meu Drive\Arquivos Josemar\projetos nao vercionados\5 Cia\Skill despachadora de Docs`

A referencia antiga com acento (`Projetos não vercionados`) ficou desatualizada em relacao ao Drive local atual. O usuario confirmou por print no Explorer local e no Drive web que existe uma unica pasta `projetos nao vercionados` dentro de `Arquivos Josemar`, sem duplicidade com acento.

Os backups intermediarios criados durante o portao de seguranca desta rodada foram removidos por decisao autorizada do usuario, que informou possuir copia em outro local. A remocao nao foi tratada como pendencia.

## Recomendacao antes da proxima ingestao

Antes de abrir a quarta segmentacao (`orientações direito militar.pdf`, cerca de 1,15M caracteres), recomenda-se rodar expediente real pela Despachadora envolvendo ao menos um tema coberto pelos POPs, como uso de forca, transporte de presos ou algemas. O objetivo e validar a recuperacao em campo antes de continuar empilhando novas fontes grandes.
