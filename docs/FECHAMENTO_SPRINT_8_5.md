# Checkpoint Técnico — Fechamento da Sprint 8.5
## Estabilização do Corpus e Recuperação Local

Este documento registra o fechamento técnico e documental da **Sprint 8.5** do projeto da Despachadora da 5ª Cia PM.

---

### A. Linha do tempo de commits

A Sprint 8.5 foi desenvolvida localmente por meio da seguinte sequência cronológica de commits git:

1. `839cee8` — `docs(despachadora): registra auditoria e varredura do corpus`
2. `df01226` — `chore(despachadora): aplica curadoria inicial do corpus normativo`
3. `cc37300` — `chore(despachadora): ajusta manifesto de curadoria do corpus`
4. `7ff1a04` — `chore(despachadora): adiciona fontes oficiais autônomas ao corpus`
5. `6ec981c` — `docs(despachadora): audita fidelidade das fontes autonomas`
6. `dcd4eb3` — `chore(despachadora): segmenta orientacoes de direito militar`
7. `0554bcf` — `chore(despachadora): ajusta recuperacao apos segmentacao`

---

### B. Estado técnico final

O sistema encontra-se estabilizado e refinado localmente para futuras fases de testes reais:
* **Corpus Curado**: Exclusão de arquivos fáticos, holerites, escalas de serviço e duplicatas.
* **Fontes Oficiais Autônomas**: Ingestão de 5 arquivos sob `corpus_manual/` contendo a transcrição oficial e auditada das regras de Súmulas e Competências.
* **PDF Segmentado**: Desmembramento de `orientações direito militar.pdf` em 15 arquivos Markdown literals de natureza `DOUTRINA`.
* **Recuperação Calibrada**: Lógica de pontuação de chunks com boost condicional de domínio ativo no script de produção para prevenir falsos positivos em acidentes.

---

### C. Corpus e índice

* **Total de Chunks Indexados**: `731`
* **Naturezas Ativas**: `NORMA`, `PROCEDIMENTAL`, `DOUTRINA`, `JURISPRUDENCIA`, `MODELO_DE_REDACAO`, `MODELO_PRECEDENTE`, `PRECEDENTE` e `OUTRO`.
* **Manifesto de Curadoria**: Ativo em `curadoria_corpus.json`. Excluiu 87 arquivos e determinou a remoção do PDF bruto original do índice para evitar redundâncias.
* **Novos Segmentos**: 15 seções em `Normas/Orientacoes_Direito_Militar_Segmentos/` com classificação de natureza `DOUTRINA` via metadados de frontmatter.

---

### D. Recuperação dos 3 casos

A simulação local da busca híbrida nos 3 cenários de teste produziu os seguintes rankings:

1. **Caso 1 — Algemas / condução / espera na DP**:
   * *Rank 1*: `Sumula_Vinculante_11_Algemas.md` (Score: 18.37 | JURISPRUDENCIA)
   * *Ranks Seguintes*: POP de transporte de preso (`Processo-3.03.00`) e POP de uso de algemas (`Processo-5.03.00`).
   * *Status*: Excelente (fonte autônoma lidera com folga).

2. **Caso 2 — Acidente com viatura e vítima**:
   * *Rank 1*: `Processo-3.01.00-Acidente-de-Transito.pdf` (Score: 8.12 | PROCEDIMENTAL)
   * *Ranks Seguintes*: NIs de acidentes com viatura (`NI Nº PM3-002-02-17`) e `Acidente_Viatura_Providencias.md` (Score: 7.25 | NORMA).
   * *Status*: Excelente (boost de +3.5 ativado pelo par "acidente"/"viatura" eliminou o falso positivo de abordagem de pedestres).

3. **Caso 3 — IPM / autotutela / competência**:
   * *Rank 1*: `corpus_manual/Sumula_473_Autotutela.md` (Score: 10.41 | JURISPRUDENCIA)
   * *Ranks Seguintes*: DPRD Jurisprudências (Segmentos 08C e 08A | DOUTRINA) e I-40-PM (NORMA).
   * *Status*: Excelente (autotutela lidera e jurisprudências dão suporte interpretativo controladamente).

---

### E. O que não foi feito

* **Sem OCR em lote**: Os 51 PDFs imagem com erro de extração não foram processados.
* **Sem push para Git Remoto**: Todos os commits permanecem apenas localmente.
* **Sem deploy**: A Central de Automações não foi distribuída para homologação de produção.
* **Sem homologação jurídica plena**: A validade dos textos gerados em campo pelo painel não foi assinada formalmente por assessores jurídicos.
* **Sem teste manual ampliado**: Não foram geradas respostas do Gemini em painel para o novo índice.

---

### F. Pendências

1. Execução de OCR em lote nos 51 PDFs imagem que permanecem com erro de indexação.
2. Realização de teste manual real no painel CTk com operador para aferir a qualidade final dos 6 blocos.
3. Decisão estratégica sobre a execução de git push e deploy da ferramenta.
4. Monitoramento contínuo de eventuais alarmes ou bloqueios falsos disparados pelas 7 regras do validador pós-Gemini.
5. Calibração e ajuste fino diante de novos falsos positivos.

---

### G. Recomendação

```
Próxima ação preferencial: 8.6-a — teste manual real no painel com corpus novo.
```
*Justificativa*: Antes de rodar processamentos pesados (como OCR em lote) ou efetuar push/deploy, deve-se validar o comportamento interativo end-to-end do LLM no painel da Central com o novo corpus estabilizado da Sprint 8.5.
