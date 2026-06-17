# Relatório de Campo — Teste da Despachadora com POPs (Sprint 8.4-campo)

Este relatório apresenta os resultados da validação em campo da Despachadora de Documentos, testada com três expedientes reais operacionais da 5ª Cia, após as segmentações do Vademecum, Doutrinas PM e POPs (Sprint 8.4) e a aplicação do Prompt Hardening (Sprint 8.4-bis).

---

## 1. Informações de Execução

*   **Data da Execução:** 17 de junho de 2026
*   **SHA-256 do Índice de Corpus Utilizado:** `A31B54687E62FE0BE12AD9A3AEC00A8E1C807C2FBA864F951A359108665F7384`
    *   *Verificação local:* Confirmada a paridade exata com o arquivo canônico do Google Drive.
*   **Auditoria de Modificações no `despachadora.py` (Resolução de Ressalva):**
    *   Foi verificado o diff completo das alterações aplicadas no Sprint 8.4-bis contra `HEAD~1`.
    *   **Resultado do Diff:** Apenas as alterações mapeadas nas categorias A, B e C foram efetuadas. A trava anti-vazamento, os placeholders de escala pendente e a readequação de rótulos estáticos para `[PADRÃO]` foram os únicos trechos modificados.
    *   **Rótulo do Slogan (Linha 447):** Confirmado que o slogan institucional permaneceu como `[FUNDAMENTO]`. Trata-se de uma dívida técnica de rótulo conhecida, que será tratada em sprints de saneamento de formatação (ROADMAP).

---

## 2. Análise Qualitativa e Matriz de Resultados

A tabela abaixo consolida os critérios avaliados em cada um dos três testes de campo:

| Campo | Expediente 1 (Uso de algemas) | Expediente 2 (Transporte de preso) | Expediente 3 (Abordagem de veículo) |
|---|---|---|---|
| **Bloco 2 tem [VERIFICAR]?** | Não | Não | Não |
| **Algum [FONTE: POPs_Segmentos/...] apareceu?** | Não | Não | Não |
| **Artigo citado sem [FONTE:]?** | Sim | Sim | Sim |
| **Referência hardcoded usada fora do cenário?** | Não | Não | Não |
| **Trava anti-vazamento do 8.4-bis funcionou?** | Sim (OK) | Sim (OK) | Sim (OK) |

### Principais Diagnósticos da Matriz:

1.  **Ausência de `[FONTE:]` nas Citações:** Em nenhum dos três testes foram impressas as tags de fonte (como `[FONTE: POPs_Segmentos/...]`). Conforme o diagnóstico da ausência de proveniência (Sprint 8.4-bis), isso ocorre porque o `MASTER_SYSTEM_PROMPT` não contém instruções específicas para que a IA emita essas tags no Bloco 2, limitando-se aos rótulos `[FUNDAMENTO]`, `[PADRÃO]` e `[SUGESTÃO]`. Embora o prompt do usuário envie os trechos enriquecidos com a marcação `[FONTE: ...]`, a IA não os reproduz na saída estruturada.
2.  **Eficácia das Travas Anti-Vazamento (Categoria A):** O subitem fático `6.3.2.1` (condução em flagrante por PM), anteriormente vazado para o caso de algemas, foi contido com sucesso. Ele só foi citado no Expediente 3, onde a regra fática do bloqueio rodoviário com embriaguez exigia a sua aplicação exata. Nos Expedientes 1 e 2, a regra geral e as restrições fáticas impediram o LLM de utilizar a referência hardcoded.
3.  **Qualidade do Bloco 2:** Não houve nenhum indicador `[VERIFICAR]` no Bloco 2 dos três expedientes, indicando alta confiança na recuperação e formatação dos fundamentos.

---

## 3. Conclusão: Os POPs estão chegando no runtime?

**Sim, mas com ressalvas estruturais sobre a origem da recuperação (Poluição de Contexto).**

Ao analisar o log de scoring e recuperação de termos em cada expediente, identificamos os seguintes comportamentos:

*   **Retenção de Arquivos Unsegmentados (Notebooklm):** O corpus do Drive mantém arquivos compilados gigantes, como `Notebooklm/Supervisor Regional/POPs.pdf`, `Notebooklm/Supervisor Regional/Vademecum.pdf` e `Doutrinas pm_compressed (1).pdf`. 
*   **Competição de Retrieval:** Devido à densidade de palavras-chave, esses arquivos de compilação da pasta `Notebooklm` obtêm scores muito elevados, consumindo as primeiras posições do pool de fundamentos (`POOL_FUNDAMENTO_N = 12`).
*   **Impacto no runtime:**
    *   No **Expediente 1 (Algemas)**, a partição específica `POPs_Segmentos/POP_5_03_00_Uso_de_Algemas.txt` obteve o score `2.2491`, terminando em 16º lugar e ficando de fora do pool de 12 documentos. A IA citou os POPs gerais de abordagem (`POP 1.01.00` e `POP 1.02.00`) que entraram no pool.
    *   No **Expediente 2 (Transporte)**, a partição `POPs_Segmentos/POP_3_03_00_Transporte_Guarda_Presos.txt` obteve o score `3.6193`, terminando em 6º lugar e entrando diretamente no contexto.
    *   No **Expediente 3 (Abordagem)**, os POPs e doutrinas específicas foram recuperados indiretamente através dos compilados gigantes da pasta `Notebooklm` que lideraram a lista de scores.
*   **Recomendação de Evolução:** Para garantir que apenas os segmentos limpos e atualizados alimentem o runtime, deve-se planejar a remoção ou arquivamento seguro dos PDFs consolidados obsoletos/duplicados da pasta `Notebooklm/` do Drive operacional, eliminando a poluição do índice de busca.

---

## 4. Pendências Identificadas

*   **[DÍVIDA TÉCNICA] Slogan (Linha 447):** Alterar de `[FUNDAMENTO]` para `[PADRÃO]`.
*   **[DÍVIDA TÉCNICA] Escala 2026 (Ronda/Categoria B):** Inserir a escala vigente de 2026 no prompt de sistema assim que estiver consolidada.
*   **[PRODUTO] Regra de Emissão de [FONTE:]:** Adicionar ao `MASTER_SYSTEM_PROMPT` no próximo sprint de prompt de sistema a instrução explícita de vinculação de fonte para que as tags `[FONTE:]` cheguem na saída final do Bloco 2.
*   **[CORPUS] Saneamento da pasta Notebooklm:** Limpar ou ignorar os PDFs consolidados duplicados no processo de indexação para evitar a concorrência desleal de busca por densidade.

---

## 5. Saídas Brutas dos Testes de Campo

Abaixo consta a reprodução literal das respostas estruturadas da Despachadora para cada um dos expedientes testados.

### 5.1. Expediente 1 (Uso de algemas)

```text
Do Sgt PM 122345-6 Comandante do CGP-5
Ao Sr. Cap PM Comandante da 5ª Cia PM
Assunto: Justificativa de uso de algemas
Referência: BOPM nº 12345/2026

1. Apraz-me cumprimentar Vossa Senhoria e, na oportunidade, relatar que em 16JUN26, por volta das 19h30min, a equipe da viatura I-05101, durante patrulhamento pela Rua Floriano Peixoto, defronte ao nº 150, Centro, Guararapes/SP, deparou-se com o indivíduo de nome J.S., o qual apresentava nervosismo incomum.
2. Ao ser dada voz de abordagem, o indivíduo desobedeceu às ordens legais e passou a proferir palavras de baixo calão contra a equipe, desferindo socos e pontapés na tentativa de se esquivar da busca pessoal.
3. Diante da ativa resistência e do perigo iminente de agressão à integridade física dos policiais militares e do próprio abordado, foi necessário o uso moderado da força física e a aplicação de algemas para contenção do indivíduo, conforme preceituam as normas vigentes. O preso foi conduzido ao plantão policial local.
4. Diante do exposto, encaminho a presente justificativa de uso de algemas para análise e deliberação de Vossa Senhoria.
```

**Saída da Despachadora:**
```text
**1. CLASSIFICAÇÃO**
[PADRÃO] Despacho Interno | Homologação de uso de algemas (BOPM nº 12345/2026) | Ordinária | CGP-5 → Cmt 5ª Cia PM | Homologação e arquivamento em SJD.

---

**2. ANÁLISE JURÍDICA**
- [FUNDAMENTO] O uso de algemas é medida excepcional regulada pela Súmula Vinculante nº 11 do Supremo Tribunal Federal (STF), a qual estabelece que o emprego do dispositivo somente é lícito em casos de resistência, fundado receio de fuga ou de perigo à integridade física própria ou alheia, por parte do preso ou de terceiros, exigindo-se a justificativa da excepcionalidade por escrito.
- [FUNDAMENTO] O artigo 292 do Código de Processo Penal (CPP) prevê expressamente que, em caso de resistência à prisão em flagrante ou à determinação legal de autoridade, poderá ser empregada a força estritamente necessária para efetuar a contenção e a condução do indivíduo.
- [FUNDAMENTO] Os Manuais de Procedimento Operacional Padrão da Instituição (POP 1.01.00 — Abordagem de Pessoas a Pé e POP 1.02.00 — Abordagem com Viatura de Quatro Rodas) preveem as algemas com chave como equipamento de uso obrigatório e indispensável para a segurança da equipe e do próprio detido em circunstâncias de risco ou hostilidade.
- [FUNDAMENTO] No caso em tela, o relatório do Comandante do CGP-5 deseja demonstrar de forma inequívoca que o indivíduo J.S. adotou conduta de resistência ativa (desobediência, investidas com socos e pontapés contra a guarnição), configurando hipótese de iminente perigo à integridade física dos militares do Estado e do próprio abordado. A justificativa por escrito foi devidamente apresentada pelo graduado responsável, cumprindo formalmente o requisito de controle administrativo.

---

**3. DECISÃO**
- [FUNDAMENTO] Face ao preenchimento inequívoco dos requisitos legais de necessidade, proporcionalidade e excepcionalidade estabelecidos pela Súmula Vinculante nº 11/STF e pelo artigo 292 do CPP, decido pelo acolhimento e homologação da justificativa de uso de algemas.
- [PADRÃO] Determino ao encarregado do SJD (Seção de Justiça e Disciplina) da 5ª Cia PM o registro da presente homologação e o arquivamento do feito junto aos arquivos da subunidade, vinculando-o ao histórico do BOPM nº 12345/2026.
- [SUGESTÃO] Cientificar os policiais militares integrantes da viatura I-05101 acerca do acerto técnico e legal de sua conduta operacional, mantendo a conformidade com as diretrizes de direitos humanos vigentes.

---

**4. TEXTO PRONTO**

```text
SECRETARIA DA SEGURANÇA PÚBLICA
POLÍCIA MILITAR DO ESTADO DE SÃO PAULO
Guararapes, [data].

DESPACHO Nº 2BPMI-[nº]/500/26

1. Trata-se de expediente encaminhado pelo Comandante do CGP-5, por meio do qual apresenta justificativa circunstanciada para o uso de algemas pela equipe da viatura I-05101, durante ocorrência capitulada em tese como resistência, registrada em 16JUN26, por volta das 19h30min, na Rua Floriano Peixoto, defronte ao nº 150, Centro, no município de Guararapes/SP, objeto do BOPM nº 12345/2026.

2. Analisando os fatos narrados, constata-se que o indivíduo abordado, J.S., adotou postura de resistência ativa à ordem legal de busca pessoal, desferindo socos e pontapés contra os integrantes da guarnição de serviço.

3. O emprego de algemas para a contenção do indivíduo mostrou-se estritamente necessário e proporcional diante do cenário fático, encontrando amparo legal nos parâmetros fixados pela Súmula Vinculante nº 11 do Supremo Tribunal Federal e pelo artigo 292 do Código de Processo Penal, tendo em vista o manifesto perigo à integridade física dos policiais militares, de terceiros e do próprio abordado.

4. Diante do exposto, HOMOLOGO o uso de algemas no caso concreto e DETERMINO à Seção de Justiça e Disciplina (SJD) da 5ª Cia PM o arquivamento do presente expediente, procedendo-se às devidas anotações no sistema de controle interno da subunidade para salvaguarda institucional e eventual consulta.

5. Cientifique-se a equipe policial militar envolvida acerca deste despacho.

"Nós, Policiais Militares, sob a proteção de Deus, estamos compromissados com a Defesa da Vida, da Integridade Física e da Dignidade da Pessoa Humana."

JOSEMAR DE PAULA
Cap PM Cmt
```

---

**5. LEVANTAMENTOS**
- [SUGESTÃO] Para os auxiliares (SubTen/Sgt):
  - Verificar se o BOPM nº 12345/2026 foi devidamente encerrado e se a versão apresentada na justificativa coincide com o histórico do boletim registrado no sistema policial.
  - Verificar no sistema de gestão de evidências se a guarnição da viatura I-05101 estava equipada com Câmeras Operacionais Portáteis (COP) e se as mídias da abordagem foram devidamente salvas e vinculadas à ocorrência.

---

**6. ASSESSORIA DO ESTADO-MAIOR**
- **COMPETÊNCIA** — DECIDO. A análise e a homologação do relatório de uso de força e algemas ocorridos na área territorial da subunidade constituem atribuição direta do Comandante da 5ª Cia PM, atuando na fiscalização do policiamento.
- **PRÓXIMOS ATOS** — Encaminhar o Despacho à SJD para registro e arquivamento em pasta própria; publicar a decisão em escala de serviço ou meio de divulgação interna para ciência dos interessados.
- **PRAZO** — [VERIFICAR: data inicial]. O controle de uso de algemas deve ser processado imediatamente após a entrega do expediente pelo CG. Recomenda-se a conclusão da homologação em até 5 (cinco) dias úteis após o recebimento.
- **ALERTAS CRUZADOS** — Caso o indivíduo alegue abuso de autoridade ou tenha sofrido lesões corporais decorrentes da resistência, a homologação serve como documento de defesa institucional. Certificar-se de que foi requisitado exame de corpo de delito para o indiciado no plantão policial.
- **ANTES DE ASSINAR** — Verificar se o número de controle do Despacho foi inserido; conferir se a data foi atualizada conforme o dia de assinatura eletrônica no SEI; garantir que o slogan institucional está presente na formatação final do documento gerado para impressão ou assinatura.
```

---

### 5.2. Expediente 2 (Transporte de preso)

```text
Do Cb PM 134567-8 Encarregado da Viatura I-05102
Ao Sr. Cap PM Comandante da 5ª Cia PM
Assunto: Transporte e custódia de preso
Referência: BOPM nº 12388/2026

1. Respeitosamente, relato a Vossa Senhoria que em 16JUN26 a equipe da viatura I-05102 realizou a prisão em flagrante do civil A.B. pelo crime de furto (artigo 155 do Código Penal) no município de Valparaíso/SP.
2. Após a lavratura do Auto de Prisão em Flagrante Delito na Delegacia de Polícia de Valparaíso, o indivíduo permaneceu sob custódia desta equipe para encaminhamento à Cadeia Pública de Penápolis.
3. O deslocamento do preso foi realizado no compartimento traseiro de presos (guarda-presos) da viatura SUV prefixo I-05102, com a devida observação dos procedimentos de segurança para evitar fuga e garantir a integridade física de todos os envolvidos durante a escolta.
4. Encaminho a presente comunicação para conhecimento e registro no SJD da Subunidade.
```

**Saída da Despachadora:**
```text
**1. CLASSIFICAÇÃO**
[PADRÃO] Despacho Interno | Administrativo (Transporte e Custódia de Preso) | Ordinária |
Origem: Encarregado da Viatura I-05102 (Valparaíso/SP) → Destino: Comandante da 5ª Cia PM | Procedimento de arquivamento e registro de regularidade no SJD.

---

**2. ANÁLISE JURÍDICA**
[FUNDAMENTO] O transporte, escolta e guarda de presos no âmbito da Polícia Militar do Estado de São Paulo é regulado pelo Procedimento Operacional Padrão correspondente (POP 3.03.00 — Transporte, Escolta e Guarda de Preso). 

[FUNDAMENTO] A conduta de transportar o indivíduo preso em flagrante pelo crime de furto (artigo 155 do Código Penal) no compartimento traseiro (guarda-presos) de viatura de modelo apropriado (sport utility vehicle - SUV), sob as devidas cautelas de segurança, está em estrita consonância com as normas de preservação da integridade física dos policiais e do próprio custodiado, em observância ao princípio constitucional da dignidade da pessoa humana (Artigo 1º, III, e Artigo 5º, III, da Constituição Federal).

[FUNDAMENTO] Diante do regular encerramento da ocorrência policial-militar, com a lavratura do Auto de Prisão em Flagrante Delito (APFD) pela Polícia Civil e o devido encaminhamento do preso à Cadeia Pública de Penápolis/SP, sem registro de intercorrências, lesões ou violação de direitos, o expediente de comunicação cumpre sua finalidade informativa, restando viável o seu arquivamento e registro para salvaguarda jurídica da equipe.

---

**3. DECISÃO**
[PADRÃO] Face ao exposto na análise jurídica:
1. **TOMO CONHECIMENTO** da comunicação de transporte e custódia de preso apresentada pela equipe da Viatura I-05102, referente ao atendimento do BOPM nº 12388/2026 [FUNDAMENTO];
2. **ATESTO A REGULARIDADE** formal e operacional do procedimento adotado pelos policiais militares, que atuaram conforme os ditames do POP 3.03.00 [SUGESTÃO];
3. **DETERMINO** ao Setor de Justiça e Disciplina (SJD) da Subunidade que registre o presente expediente no sistema de controle interno e proceda ao seu arquivamento [PADRÃO].

---

**4. TEXTO PRONTO**

[PADRÃO]

SECRETARIA DA SEGURANÇA PÚBLICA
POLÍCIA MILITAR DO ESTADO DE SÃO PAULO
5ª Cia PM - Guararapes/SP

Guararapes, 17 de junho de 2026.

DESPACHO Nº 2BPMI-[nº]/500/26

1. Dou-me por ciente do teor do expediente datado de 16 de junho de 2026, subscrito pelo Cb PM 134567-8, Encarregado da Viatura I-05102, sediada no município de Valparaíso/SP, o qual relata a condução, custódia e entrega na Cadeia Pública de Penápolis/SP do civil A.B., preso em flagrante delito pela prática de furto (artigo 155 do Código Penal), conforme o BOPM nº 12388/2026.

2. Constato que a equipe policial-militar agiu em estrita observância às normas operacionais e administrativas vigentes, utilizando de forma correta e segura o compartimento de guarda-presos da viatura SUV prefixo I-05102, garantindo a integridade física de todos os envolvidos e a inviolabilidade da custódia do Estado, em conformidade com o POP 3.03.00.

3. Publique-se. Registre-se eletronicamente no Setor de Justiça e Disciplina (SJD) da 5ª Cia PM para fins de arquivo e salvaguarda jurídica dos integrantes da patrulha.


JOSEMAR DE PAULA
Cap PM Cmt


"Nós, Policiais Militares, sob a proteção de Deus, estamos compromissados com a Defesa da Vida, da Integridade Física e da Dignidade da Pessoa Humana."

---

**5. LEVANTAMENTOS**
[SUGESTÃO]
- **Para os auxiliares (Sgt Aux SJD):** Verificar se os dados do BOPM nº 12388/2026 já constam inseridos no sistema SJD da subunidade para correlação com o presente despacho de arquivamento.
- **Para verificar em normas/sistema:** Confirmar se houve preenchimento adequado do Relatório de Serviço Operacional (RSO) digital correspondente ao turno da viatura I-05102 em 16JUN26.

---

**6. ASSESSORIA DO ESTADO-MAIOR**
[SUGESTÃO]

- **COMPETÊNCIA — DECIDO:** Trata-se de competência direta do Comandante de Cia, por envolver o controle administrativo, operacional e disciplinar de seus subordinados diretos, bem como a gestão dos arquivos do SJD da subunidade.
- **PRÓXIMOS ATOS:**
  1. Remessa do despacho ao SJD para inserção no sistema e arquivamento digital;
  2. Notificação (ciência) ao Cb PM 134567-8 sobre o acolhimento de seu relatório;
  3. Atualização do banco de dados de escoltas executadas no mês pela subunidade de Valparaíso/SP.
- **PRAZO:** O registro administrativo deve ocorrer no prazo de até 05 (cinco) dias úteis a contar do recebimento do expediente na Sede da Cia.
- **ALERTAS CRUZADOS:** Caso houvesse qualquer menção a uso de força física além do estritamente necessário ou reclamação de lesões corporais pelo preso, o caso exigiria a instauração de Investigação Preliminar (IP). Como o relatório atesta a total regularidade técnica, o arquivamento direto é a medida adequada.
- **ANTES DE ASSINAR — MICROCHECKLIST:**
  - [x] Placeholder de numeração [nº] inserido para preenchimento manual;
  - [x] Nome e RE do policial militar conferidos contra o expediente de origem;
  - [x] Data e local (Guararapes/SP) corretos;
  - [x] Slogan institucional inserido ao final do documento.
```

---

### 5.3. Expediente 3 (Abordagem de veículo)

```text
Do 1º Ten PM 115599-0 Comandante do 1º Pelotão
Ao Sr. Cap PM Comandante da 5ª Cia PM
Assunto: Relatório de abordagem e acompanhamento de veículo
Referência: BOPM nº 12411/2026

1. Cumprimentando-o cordialmente, levo ao conhecimento de Vossa Senhoria que no dia 16JUN26, durante a execução de ponto de bloqueio policial na Rodovia Marechal Rondon (SP-300), km 540, município de Guararapes/SP, o veículo VW Gol, cor cinza, ostentando as placas ABC-1234, desobedeceu ao sinal de parada obrigatória dado pelos policiais militares.
2. O condutor transpôs o bloqueio em alta velocidade, colocando em risco os policiais e usuários da via. Ato contínuo, iniciou-se o acompanhamento tático e cerco policial com o apoio das demais viaturas de serviço do rádio patrulhamento.
3. O veículo foi interceptado na entrada da vicinal de acesso a Rubiácea/SP. Foi realizada a abordagem policial aos três ocupantes seguindo os procedimentos de segurança operacional, sendo constatado que o condutor não possuía CNH e apresentava sinais de embriaguez. O veículo foi recolhido ao pátio credenciado.
4. Apresento o presente relatório para os devidos fins e registro de atuação operacional da equipe do Pelotão.
```

**Saída da Despachadora:**
```text
---

### **1. CLASSIFICAÇÃO**
[PADRÃO] 
*   **Tipo de documento:** Despacho Interno (da Cia para o Pelotão)
*   **Assunto:** Fiscalização procedimental de ocorrência de trânsito com condicionante legal (acompanhamento, embriaguez ao volante e falta de CNH)
*   **Urgência:** Ordinária
*   **Origem → Destino:** Comandante da 5ª Cia PM → Comandante do 1º Pelotão PM
*   **Procedimento cabível:** Instrução e determinação de saneamento de ato procedimental policial-militar

---

### **2. ANÁLISE JURÍDICA**
[FUNDAMENTO] 
1.  **Condicionante Legal de Trânsito:** O Código de Trânsito Brasileiro (CTB), em seu artigo 291, § 1º, estabelece as condicionantes graves aplicadas aos crimes de trânsito (notadamente a influência de álcool ou substância psicoativa e a ausência de permissão para dirigir ou CNH).
2.  **Obrigatoriedade de Apresentação Pessoal:** Conforme regulado pela **norma interna PMESP, subitem 6.4.1.4**, em ocorrências de trânsito que envolvam as referidas condicionantes legais, o procedimento simplificado de registro é expressamente vedado. É compulsória a condução e apresentação pessoal dos envolvidos e do veículo perante o plantão de Polícia Judiciária para a elaboração do Boletim de Ocorrência da Polícia Civil (BOPC) e demais providências correlatas.
3.  **Doutrina de Padronização Operacional:** A conduta da equipe militar deve estar balizada nos procedimentos operacionais vigentes, em especial o POP 4.01.01 (Acompanhamento de Veículo), revisado pelo Bol G PM nº 103, de 02JUN22, e o POP 1.02.01 (Abordagem de Pessoa em Automóvel). O relatório apresentado pelo Comandante do 1º Pelotão é omisso quanto à efetiva apresentação dos infratores na Delegacia de Polícia local após a abordagem.

---

### **3. DECISÃO**
[PADRÃO] 
1.  **Acolho temporariamente** o relatório de abordagem e acompanhamento de veículo referente ao BOPM nº 12411/2026 apresentado pelo Comandante do 1º Pelotão.
2.  [FUNDAMENTO] **Determino** ao Comandante do 1º Pelotão que proceda ao saneamento e complementação do presente expediente, certificando formalmente se os policiais militares de serviço realizaram a apresentação pessoal do condutor embriagado e sem habilitação à Delegacia de Polícia de Guararapes ou Rubiácea, em estrita obediência ao previsto no artigo 291, § 1º do CTB e na **norma interna PMESP, subitem 6.4.1.4**.
3.  [SUGESTÃO] **Determino** a juntada, no prazo estabelecido, de cópia do Boletim de Ocorrência da Polícia Civil (BOPC) ou documento correlato que comprove o registro cartorário da autuação criminal.
4.  [PADRÃO] **Determino** à Seção de Justiça e Disciplina (SJD) da 5ª Cia PM o controle do prazo de retorno desta instrução.

---

### **4. TEXTO PRONTO**
[PADRÃO]

```text
SECRETARIA DA SEGURANÇA PÚBLICA
POLÍCIA MILITAR DO ESTADO DE SÃO PAULO
Guararapes, [data].

DESPACHO Nº 2BPMI-[nº]/500/26

1. Trata-se de relatório de atuação operacional exarado pelo Comandante do 1º Pelotão PM, que noticia ocorrência de desobediência a bloqueio policial na Rodovia Marechal Rondon (SP-300), km 540, seguida de acompanhamento tático e abordagem policial na vicinal de Rubiácea/SP, onde restou constatado que o condutor do veículo VW Gol (placas ABC-1234) não possuía CNH e apresentava visíveis sinais de embriaguez.

2. Compulsando o expediente recebido, verifica-se que o relatório operacional é omisso no tocante ao desdobramento de polícia judiciária que o caso impõe, indicando unicamente que o veículo foi removido ao pátio credenciado.

3. Face ao teor do art. 291, § 1º da Lei Federal nº 9.503/97 (Código de Trânsito Brasileiro), que fixa as condicionantes de excepcionalidade em crimes de trânsito (condução sob efeito de álcool e ausência de CNH), e de acordo com o subitem 6.4.1.4 da norma interna PMESP, as ocorrências desta natureza exigem, obrigatoriamente, a apresentação pessoal e física dos infratores e dos fatos perante a autoridade de Polícia Judiciária (Delegacia de Polícia), sendo vedada a adoção de rito simplificado.

4. Posto isto, determino ao Sr. 1º Ten PM Comandante do 1º Pelotão PM que, no prazo de 02 (dois) dias úteis:
a) Informe e certifique se houve a devida apresentação pessoal do condutor e dos demais envolvidos à Delegacia de Polícia Civil de Guararapes ou Rubiácea/SP;
b) Junte ao presente expediente cópia do Boletim de Ocorrência da Polícia Civil (BOPC) lavrado ou certidão que comprove o recebimento da ocorrência pelo Delegado de Polícia de plantão;
c) Se o caso, justifique eventual óbice procedimentado pela guarnição.

5. Registre-se e intime-se o Oficial subalterno para o cumprimento.


JOSEMAR DE PAULA
Cap PM Cmt


"Nós, Policiais Militares, sob a proteção de Deus, estamos compromissados com a Defesa da Vida, da Integridade Física e da Dignidade da Pessoa Humana."
```

---

### **5. LEVANTAMENTOS**
[SUGESTÃO] 

*   **Para mim mesmo (Cmt):** 
    *   Monitorar os índices de ocorrências envolvendo acompanhamento tático na Rodovia Marechal Rondon (SP-300) para avaliar a necessidade de reforço doutrinário de bloqueio e cerco na área da Cia.
*   **Para os auxiliares (Sgt/SubTen Aux SJD):** 
    *   Autuar o presente Despacho no sistema eletrônico de gestão documental (SEI/SJD) e criar alerta de prazo para cobrança de retorno em 48 horas úteis.
*   **Para verificar em normas/sistema:** 
    *   Consultar diretamente no sistema Prodesp/Copom o teor do BOPM nº 12411/2026 para certificar a inserção dos dados de embriaguez no histórico.

---

### **6. ASSESSORIA DO ESTADO-MAIOR**
[SUGESTÃO]

*   **COMPETÊNCIA:** **DECIDO** — Trata-se de competência direta do Comandante de Cia na fiscalização e orientação corretiva/preventiva do policiamento e das atividades administrativas de seus pelotões subordinados.
*   **PRÓXIMOS ATOS:** 
    *   Retorno do expediente saneado pelo 1º Pelotão;
    *   Verificação do alinhamento da conduta da equipe ao POP 4.01.01 (Acompanhamento de Veículo);
    *   Havendo inobservância injustificada da apresentação obrigatória em DP, instauração de Investigação Preliminar (IP) por parte desta subunidade;
    *   Sendo regular o procedimento, arquivamento na SJD para fins de cadastro de produtividade.
*   **PRAZO:** **02 (dois) dias úteis**, com base na urgência de controle de legalidade procedimental. [VERIFICAR: data inicial do recebimento do expediente físico/digital para início da contagem].
*   **ALERTAS CRUZADOS:** O acompanhamento de veículo com transposição violenta de bloqueio e direção perigosa sob efeito de álcool exige que, além dos trâmites penais (DP), as autuações de trânsito de natureza administrativa (multas, apreensão e medidas do CTB) tenham sido devidamente inseridas no sistema informatizado, evitando prejuízos à regularidade do processo de trânsito.
*   **ANTES DE ASSINAR:** 
    *   [nº] do Despacho devidamente preenchido pelo auxiliar;
    *   Confirmação de que o RE e nome do 1º Ten PM Comandante do Pelotão estão em conformidade com o cadastro funcional;
    *   Inclusão obrigatória do Slogan Institucional da PMESP ao final da folha.
```
