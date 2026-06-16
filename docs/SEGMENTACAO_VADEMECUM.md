# Segmentacao do Vademecum

Executado em 16/06/2026, como parte do Sprint 8.4 - Curadoria de fontes oficiais.

## Problema original

O `Vademecum.pdf` estava indexado como um unico documento de 7.374.439 caracteres. A recuperacao da Despachadora usa densidade:

`score = ocorrencias / (len(texto) ** 0.5)`

Com esse tamanho, o denominador do Vademecum fica perto de 2.715. Na pratica, ele precisava ter cerca de 27 vezes mais ocorrencias de um termo para competir com um documento de 10k caracteres. Embora estivesse classificado como `NORMA`, quase nunca subia no top 12 do pool Fundamento.

## Segmentos criados

Origem:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs\Notebooklm\Supervisor Regional\Vademecum.pdf`

Destino:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs\Normas\Vademecum_Segmentos\`

| Arquivo | Artigos cobertos | Caracteres |
|---|---|---:|
| `Vademecum_CTB.txt` | Arts. 162-175, 269-272, 291-308 | 30.383 |
| `Vademecum_ECA.txt` | Arts. 98-130, 171-190 | 39.103 |
| `Vademecum_CP_Militar.txt` | Arts. 149-166, 175-176, 187-203, 240-250 | 21.287 |
| `Vademecum_CPP_Flagrante.txt` | Arts. 282-350 | 39.123 |
| `Vademecum_Lei_Maria_da_Penha.txt` | Arts. 1-7, 10-12, 18-24 | 22.171 |
| `Vademecum_Drogas_11343.txt` | Arts. 28-59 | 22.123 |

Todos os segmentos foram indexados com:

- `natureza=NORMA`
- `classificacao_origem=humana`
- `classificacao_confianca=alta`
- `error=None`
- tamanho entre 20k e 150k caracteres

Proveniencia registrada via reimport CSV:

`Segmento extraído de Vademecum.pdf (Notebooklm/Supervisor Regional). Captura: 16/06/2026.`

## Backup

- Backup local: `C:\projetos\central_automacoes\automacoes\despachadora\corpus_index.backup.20260616-170608.json`
- Backup Drive: `G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\backups_corpus_index_despachadora\corpus_index.backup.20260616-170608.json`
- SHA-256 do backup: `7f5982f3c4acf763d8f7b09848317c949a599d96cb00ad04b12d9aeecf5f4ebf`

## SHA-256 final

`12c29eec5983347e6b20e973c140030bb905c1ec728a5c8fc5b23d45e83f0705`

O `corpus_index.json` final foi copiado para:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs\corpus_index.json`

## Prova de aditividade

```text
total_backup: 605
total_final: 611
incremento_final: 6
chaves_originais_intactas: true
chaves_originais_ausentes: []
novas_chaves:
- Normas/Vademecum_Segmentos/Vademecum_CPP_Flagrante.txt
- Normas/Vademecum_Segmentos/Vademecum_CP_Militar.txt
- Normas/Vademecum_Segmentos/Vademecum_CTB.txt
- Normas/Vademecum_Segmentos/Vademecum_Drogas_11343.txt
- Normas/Vademecum_Segmentos/Vademecum_ECA.txt
- Normas/Vademecum_Segmentos/Vademecum_Lei_Maria_da_Penha.txt
qtd_novas_chaves: 6
campos_originais_inalterados: true
alteracoes_campos_originais: []
entradas_existentes_totalmente_inalteradas: true
entradas_existentes_alteradas: []
passou: true
```

## Observacoes operacionais

O `CORPUS_PATH` desta maquina foi corrigido em `segredos.env` para:

`G:\Meu Drive\Arquivos Josemar\Projetos não vercionados\5 Cia\Skill despachadora de Docs`

Nenhum `git commit`, `git push` ou deploy foi executado.
