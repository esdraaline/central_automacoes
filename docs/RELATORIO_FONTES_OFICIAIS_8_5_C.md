# Relatório de Fontes Oficiais do Corpus — Sprint 8.5-c

Este relatório registra a curadoria e criação das fontes autônomas oficiais de fundamentos jurídicos críticos para a Despachadora, realizadas durante a Sprint 8.5-c.

## A. Estado inicial
- Repositório local limpo, sem alterações pendentes antes do início dos trabalhos.
- Último commit local registrado: `cc37300 chore(despachadora): ajusta manifesto de curadoria do corpus`.
- As 4 primeiras fontes autônomas oficiais haviam sido pré-redigidas, mas faltava a 5ª fonte de acidente com viatura e a indexação apropriada respeitando a natureza de cada arquivo Markdown via frontmatter.

## B. Fontes oficiais localizadas
Após busca literal no corpus físico e no índice, foram validadas as seguintes origens oficiais para cada tema:
1. **Súmula Vinculante nº 11 (Uso de Algemas)**: Localizada no documento [Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/P3/POPs/Processo-3.03.00-transporte-e-Guarda-de-Presos.pdf).
2. **Súmula 473 (Autotutela)**: Localizada no documento [orientações direito militar.pdf](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/Notebooklm/Supervisor%20Regional/orientações%20direito%20militar.pdf).
3. **Competência de IPM**: Localizada no [CPPM](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/JD/PPJM/Manuais,%20Leis,%20Regulamentos/CPPM.htm) (Artigos 7º e 8º) e na instrução [I-40-PM](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/Normas/Doutrinas_PM_Segmentos/Doutrinas_I40PM.txt) (Artigos 2º e 3º).
4. **Competência e Prazos de Sindicância**: Localizada no manual [I-16-PM](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/JD/PPJM/Manuais,%20Leis,%20Regulamentos/I-16-PM.pdf) (Artigos 7º, 9º, 65 e 76).
5. **Acidente com Viatura (Providências)**: Localizada nas instruções [I-16-PM](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/JD/PPJM/Manuais,%20Leis,%20Regulamentos/I-16-PM.pdf) (Artigos 65, 82, 84, 91, 94, 100 e 101), no [POP 3.01.00 - Acidente de Trânsito](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/Normas/POPs_Segmentos/POP_3_01_00_Acidente_Transito.txt) e na Resolução PGE nº 9/2024 (transcrita e validada do [Despacho para não instauração de Sindicância.pdf](file:///G:/Meu%20Drive/Arquivos%20Josemar/projetos%20nao%20vercionados/5%20Cia/Skill%20despachadora%20de%20Docs/JD/Despacho%20para%20não%20instauração%20de%20Sindicância.pdf)).

## C. Fontes autônomas criadas
Foram criados 5 arquivos de fontes autônomas oficiais sob a pasta [automacoes/despachadora/corpus_manual/](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/):
1. [Sumula_Vinculante_11_Algemas.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Sumula_Vinculante_11_Algemas.md): Súmula Vinculante nº 11 do STF e Decreto Federal nº 8.858/16. Natureza: `JURISPRUDENCIA`.
2. [Sumula_473_Autotutela.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Sumula_473_Autotutela.md): Súmula nº 473 do STF. Natureza: `JURISPRUDENCIA`.
3. [Competencia_IPM.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Competencia_IPM.md): Código de Processo Penal Militar (Artigos 7º e 8º) e I-40-PM (Artigos 2º e 3º). Natureza: `NORMA`.
4. [Competencia_Prazos_Sindicancia.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Competencia_Prazos_Sindicancia.md): Instruções I-16-PM (Artigos 7º, 9º, 65 e 76). Natureza: `NORMA`.
5. [Acidente_Viatura_Providencias.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Acidente_Viatura_Providencias.md): I-16-PM (Artigos 65, 82, 84, 91, 94, 100, 101), POP 3.01.00 e Resolução PGE nº 9/2024. Natureza: `NORMA`.

Todos estes arquivos possuem metadados YAML de frontmatter, incluindo o caminho real da fonte oficial no corpus físico (`fonte_origem`) e o `status_fonte: "VALIDADA"`.

## D. Fontes não criadas por falta de origem oficial
- Não há nenhuma. Todos os 5 temas críticos puderam ser criados devido à presença dos textos oficiais autênticos e limpos no corpus físico ou documentos locais citados.

## E. Riscos reduzidos
- **Eliminação de invenção normativa (alucinação)**: A Despachadora agora recupera trechos normativos oficiais integrais e validados, em vez de depender de texto normativo gerado de memória pelo LLM ou retirado de modelos de peças históricas.
- **Isolamento de Heurísticas de Classificação**: O indexador oficial atribui `classificacao_origem = "humana"` para as entradas do `corpus_manual`, garantindo que eventuais execuções do classificador automático baseado em heurísticas (`classificar_corpus.py`) não sobrescrevam a natureza declarada e validada.
- **Pontaria nas buscas**: Foram adicionadas palavras-chave específicas nas descrições de uso esperado de cada arquivo Markdown (ex.: "prazo de sindicância" e "dano ao erário") para garantir que as buscas literais e lexicais capturem esses fundamentos com máxima precisão.

## F. Pendências para o usuário fornecer arquivo oficial
- Nenhuma pendência imediata para estes 5 temas. Contudo, se houver novas portarias, resoluções estaduais ou manuais operacionais atualizados (por exemplo, regulamentos pós-2026), estes devem ser depositados pelo usuário na pasta de corpus físico e reindexados.

## G. Próxima etapa recomendada
- Integrar as novas fontes autônomas ao fluxo completo de execução e realizar testes de campo (Sprint 8.6) para avaliar a taxa de acerto e mitigação de flags `[VERIFICAR]` geradas pelo validador pós-Gemini.

## Auditoria de fidelidade 8.5-c.1

| arquivo | fonte_origem existe? | texto oficial íntegro? | interpretação separada? | status | observação |
| ------- | -------------------- | ---------------------- | ----------------------- | ------ | ---------- |
| [Sumula_Vinculante_11_Algemas.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Sumula_Vinculante_11_Algemas.md) | Sim (corpus físico) | Sim | Sim | VALIDADO_SEM_AJUSTES | Texto literal da SV 11 e Dec. Fed. 8.858/16 íntegro e fiel. Termos de busca estão na transcrição oficial. |
| [Sumula_473_Autotutela.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Sumula_473_Autotutela.md) | Sim (compilada local) | Sim | Sim | VALIDADO_SEM_AJUSTES | A fonte no corpus é local/compilada (`orientações direito militar.pdf`). O termo `autotutela` está corretamente isolado no uso esperado. |
| [Competencia_IPM.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Competencia_IPM.md) | Sim (corpus físico) | Sim | Sim | VALIDADO_SEM_AJUSTES | Trechos do CPPM e I-40-PM fiéis. Interpretações operacionais e limites estritamente separados. |
| [Competencia_Prazos_Sindicancia.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Competencia_Prazos_Sindicancia.md) | Sim (corpus físico) | Sim | Sim | VALIDADO_SEM_AJUSTES | Prazos e prorrogações fiéis às I-16-PM. A expressão `prazo de sindicância` está devidamente isolada na seção de uso esperado. |
| [Acidente_Viatura_Providencias.md](file:///c:/projetos/central_automacoes/automacoes/despachadora/corpus_manual/Acidente_Viatura_Providencias.md) | Sim (corpus físico/local) | Sim | Sim | VALIDADO_SEM_AJUSTES | Fundamentos da I-16-PM, POP 3.01.00 e Resolução PGE nº 9/2024 fiéis. A expressão `dano ao erário` está devidamente isolada no uso esperado. |

