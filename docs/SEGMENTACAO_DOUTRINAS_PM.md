# Segmentacao das Doutrinas PM

Executado em 16/06/2026, como parte do Sprint 8.4 - Curadoria de fontes oficiais.

## Origem

Arquivo original:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs\Notebooklm\Supervisor Regional\Doutrinas pm_compressed (1).pdf`

O PDF reunia 24 normas e manuais PMESP em 1.643 paginas e cerca de 3,09 milhoes de caracteres. Como a recuperacao da Despachadora usa densidade (`ocorrencias / len(texto)^0.5`), o compilado unico ficava prejudicado no pool Fundamento. A solucao foi segmentar o material em arquivos tematicos menores.

Destino dos segmentos:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs\Normas\Doutrinas_PM_Segmentos\`

## Segmentos criados

| Arquivo | Paginas | Caracteres |
|---|---:|---:|
| `Doutrinas_D88777_R200.txt` | 1-16 | 45.797 |
| `Doutrinas_I16PM_Pt1.txt` | 17-50 | 76.400 |
| `Doutrinas_I16PM_Pt2.txt` | 51-87 | 78.026 |
| `Doutrinas_I40PM.txt` | 88-123 | 95.142 |
| `Doutrinas_M03PM_DefesaPessoal.txt` | 124-199 | 114.417 |
| `Doutrinas_M04PM_CmtCia.txt` | 200-219 | 31.320 |
| `Doutrinas_M10PM_Eventos_Pt1.txt` | 220-291 | 120.290 |
| `Doutrinas_M10PM_Eventos_Pt2.txt` | 292-363 | 119.354 |
| `Doutrinas_M19PM_Tiro_Pt1.txt` | 364-401 | 121.279 |
| `Doutrinas_M19PM_Tiro_Pt2.txt` | 402-441 | 120.522 |
| `Doutrinas_M19PM_Tiro_Pt3.txt` | 442-476 | 120.666 |
| `Doutrinas_M19PM_Tiro_Pt4.txt` | 477-512 | 121.604 |
| `Doutrinas_M19PM_Tiro_Pt5.txt` | 513-562 | 123.767 |
| `Doutrinas_M19PM_Tiro_Pt6.txt` | 563-602 | 120.378 |
| `Doutrinas_DireitosHumanos_Pt1.txt` | 603-662 | 95.057 |
| `Doutrinas_DireitosHumanos_Pt2.txt` | 663-730 | 95.535 |
| `Doutrinas_Fundamentos_Pt1.txt` | 731-807 | 116.390 |
| `Doutrinas_Fundamentos_Pt2.txt` | 808-892 | 117.529 |
| `Doutrinas_NORSOP_Pt1.txt` | 893-923 | 82.809 |
| `Doutrinas_NORSOP_Pt2.txt` | 924-960 | 85.464 |
| `Doutrinas_PM3_RadioForca.txt` | 961-975 | 32.654 |
| `Doutrinas_PM3_Escolar_Comunitario.txt` | 976-1003 | 59.844 |
| `Doutrinas_PM3_EscoltaTransito.txt` | 1004-1025 | 48.785 |
| `Doutrinas_PM3_VistoriaEventos.txt` | 1026-1078 | 113.194 |
| `Doutrinas_PM3_Rural_Reintegracao.txt` | 1079-1111 | 68.470 |
| `Doutrinas_PM3_AtivDelegada.txt` | 1112-1131 | 45.562 |
| `Doutrinas_R5PM_Uniformes_Pt1.txt` | 1132-1262 | 109.408 |
| `Doutrinas_R5PM_Uniformes_Pt2.txt` | 1263-1417 | 109.232 |
| `Doutrinas_R5PM_Uniformes_Pt3.txt` | 1418-1545 | 109.231 |
| `Doutrinas_RDPM.txt` | 1546-1599 | 135.324 |
| `Doutrinas_RegGeral_SSP57.txt` | 1600-1643 | 134.909 |

Todos os 31 segmentos ficaram entre 20k e 150k caracteres.

## Indexacao

Resultado final dos 31 segmentos no indice:

- `natureza=NORMA`
- `classificacao_origem=humana`
- `classificacao_confianca=alta`
- `error=None`

Proveniencia registrada via reimport CSV:

`Segmento extraído de Doutrinas_pm_compressed.pdf. Captura: 16/06/2026.`

CSV usado no reimport:

`saidas/reimport_doutrinas_pm_segmentos.csv`

## Backup

- Backup local: `C:\projetos\central_automacoes\automacoes\despachadora\corpus_index.backup.20260616-173711.json`
- Backup Drive: `G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\backups_corpus_index_despachadora\corpus_index.backup.20260616-173711.json`
- SHA-256 do backup: `12c29eec5983347e6b20e973c140030bb905c1ec728a5c8fc5b23d45e83f0705`

## Prova de aditividade

```text
total_antes: 611
total_depois: 642
incremento: 31
total_nao_diminuiu: true
chaves_originais_intactas: true
chaves_originais_ausentes: []
qtd_novas_chaves: 31
novas_chaves_doutrinas: 31
outras_novas_chaves: []
campos_originais_inalterados: true
alteracoes_campos_originais: []
entradas_existentes_totalmente_inalteradas: true
entradas_existentes_alteradas: []
passou: true
```

## SHA-256 final

`0c7f59568d53d6d7708f1f720a36d718f8b51933e79d0b90fe4799896691f149`

O `corpus_index.json` final foi copiado para:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs\corpus_index.json`

Hash local e hash do Drive conferidos com `Get-FileHash`; ambos retornaram:

```text
0C7F59568D53D6D7708F1F720A36D718F8B51933E79D0B90FE4799896691F149
```

Nenhum `git commit`, `git push` ou deploy foi executado.
