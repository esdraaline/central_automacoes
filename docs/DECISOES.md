# 📌 Registro de Decisões
Decisões fechadas, com a razão de cada uma. Para não reabrir discussão depois.

---

## D-01 · Arquitetura: painel desktop + automações plugáveis ✅
Painel em customtkinter, núcleo compartilhado, e cada automação como pasta com `manifesto.py` + `executar.py`. O painel descobre as automações sozinho.
**Motivo:** as automações controlam recursos locais (VPN, Edge, Downloads); desktop é mais robusto que web e abre com duplo clique. Detalhes em PLANO.md.

---

## D-02 · Exclusão de e-mails (itens 3.1 e 4.1): triagem com confirmação ✅
Fluxo: a automação classifica os não lidos e gera relatório + lista de candidatos → no painel você revê e marca o que confirma → exclusão move para a Lixeira (recuperável). Nunca exclusão automática, nunca esvaziar lixeira, nunca exclusão permanente.
**Motivo:** apagar e-mail é irreversível; a trava de confirmação protege contra perder algo importante por bug ou classificação errada.

---

## D-03 · E-mail: Gmail via API, correio PM via navegador ✅
- **Gmail** (4 contas: josemardp@gmail.com, josemar.dp@hotmail.com, esdraaline@gmail.com, lojadares@gmail.com): API oficial (OAuth), uma autorização por conta. (Obs.: hotmail.com usará a API da Microsoft/Graph; o resto, Gmail API.)
- **Correio PM:** navegador (Playwright), atrás da VPN — provavelmente não tem API.

**Motivo:** API é muito mais estável que raspar tela.

---

## D-04 · Assinatura de PDF (item 8): certificado LOCAL, não gov.br ✅
Usar o certificado digital instalado na máquina (e-CPF local), assinando com `pyhanko`. O painel mostra o documento e você clica "assinar"; o PIN é digitado na hora, nunca armazenado.

**gov.br: NÃO automatizar com credenciais.** Motivos:
- gov.br exige 2FA a cada sessão — login salvo não passa disso de forma confiável.
- É identidade jurídica do governo; script que assina sozinho pode vincular legalmente a um documento errado se a máquina for comprometida ou der bug.

**Alternativa segura** (se um dia precisar): o painel prepara o PDF e abre o assinador gov.br; você faz o 2FA e assina. Sem senha guardada.

**Pendência para a Fase 6:** confirmar o formato do certificado local (A1 .pfx / A3 em token / ID digital do Adobe) — muda um detalhe da implementação.

---

## D-05 · Segredos abstraídos desde o início ✅
`nucleo/segredos.py` lê de `segredos.env` por padrão, mas com interface abstrata (`segredos.get("siopm")`), para trocar depois para o keyring do Windows sem reescrever nada. Senha nunca aparece no código das automações.

---

## D-06 · SEI fora da automação ✅
O SEI não será automatizado na Central de Automações. Login, acesso via gov.br, 2FA e uso do SEI serão feitos manualmente pelo operador.
**Motivo:** o fluxo gov.br/Minha Área SP envolve identidade pessoal, 2FA e risco operacional maior que o ganho de apenas abrir a sessão. Melhor manter o SEI como procedimento manual.

---

## D-07 · Despachadora: código na Central, corpus no Drive ✅
**Data:** 05/06/2026

**Contexto:** A Despachadora standalone (3 arquivos no Drive) será portada para dentro da Central como automação plugável. Precisava-se definir onde ficam os arquivos de código e onde fica o corpus documental.

**Decisão:**
- `despachadora.py`, `indexar_corpus.py` e `corpus_index.json` migram para `automacoes/despachadora/nucleo_despachadora/` (código e índice versionados no git).
- As pastas do corpus (P1–P5, JD, Notebooklm) permanecem no Google Drive e **nunca entram no git** (sigilosos + pesados; sincronizam automaticamente entre notebooks via Drive).
- O caminho do corpus é configurado por máquina via `CORPUS_PATH` em `segredos.env`.
- A chave Gemini é fornecida via `GEMINI_API_KEY` em `segredos.env` e lida por `nucleo/segredos`.

**Justificativa:** O corpus é sigiloso (expedientes da 5ª Cia) e pesa ~34 MB — não deve entrar no git. O Drive já sincroniza entre os dois notebooks. O índice (`corpus_index.json`) é derivado e seguro para versionar. Separar caminho por máquina via `segredos.env` resolve a diferença de letra de unidade entre os notebooks.

**Alternativa descartada:** Versionar o corpus no git — descartado por sigilo e tamanho.

---

## D-08 · Chave de API Gemini formato `AQ.` ✅
**Data:** 07/06/2026

**Contexto:** Durante a configuracao da Despachadora, a conta Google do projeto gerou uma chave Gemini no formato `AQ.Ab8RN6...`, associada a projeto `gen-lang-client-*`.

**Decisao:**
- Chaves Gemini no formato `AQ.` sao validas para este projeto.
- A chave deve ser copiada exatamente como exibida no AI Studio.
- Usar normalmente com `genai.Client(api_key=chave)` do SDK `google-genai`.
- Nunca adicionar prefixo `AIzaSy` nem tentar converter o formato da chave.

**Risco registrado:** Foi adicionado indevidamente o prefixo `AIzaSy` antes da chave `AQ.`, gerando `GEMINI_API_KEY=AIzaSyAQ.Ab8RN6...`, que e invalida. A chave correta e apenas `AQ.Ab8RN6...`, exatamente como fornecida pelo AI Studio.

**Motivo:** O SDK `google-genai` aceita a chave `AQ.` quando ela e passada sem alteracao. Alterar o valor causa erro `API_KEY_INVALID`.

---

## D-09 · `corpus_index.json` vai no git direto ✅
**Data:** 07/06/2026

**Contexto:** A Despachadora precisa do indice derivado do corpus para recuperar fundamentos e modelos rapidamente. O arquivo gerado tem cerca de 34 MB.

**Decisao:**
- Versionar `automacoes/despachadora/corpus_index.json` diretamente no git.
- Nao usar Git LFS por ora.
- Regenerar quando necessario com:
  `python automacoes/despachadora/nucleo_despachadora/indexar_corpus.py`
- O indexador opera em modo incremental, processando apenas arquivos novos quando possivel.

**Motivo:** O arquivo esta dentro do limite de 100 MB do GitHub e permite sincronizar os dois notebooks sem depender de reindexacao manual em cada maquina. O corpus original continua fora do git.

---

## D-10 · OCR de PDFs imagem: script separado, corpus_index.json atualizado no lugar ✅
**Data:** 08/06/2026

**Contexto:** 67 dos 714 arquivos do corpus estavam marcados como `error: "pdf_imagem_sem_ocr"` pelo `indexar_corpus.py` — PDFs escaneados que PyMuPDF e pypdf não conseguem ler. A Despachadora os ignorava completamente na busca (score = 0 por ausência de texto).

**Decisão:**
- Criar script separado `ocr_pdfs_imagem.py` em `nucleo_despachadora/` — não alterar `indexar_corpus.py`.
- O script filtra apenas entradas com `error == "pdf_imagem_sem_ocr"` e texto vazio, aplica OCR (pdf2image + pytesseract, lang=por, 300 DPI) e atualiza `corpus_index.json` no lugar (atomic write via `.tmp` + `os.replace`).
- Dependências OCR (pdf2image, pytesseract, Tesseract, Poppler) instaladas apenas na máquina que executa o OCR — não são necessárias nas demais para usar a Despachadora.
- `corpus_index.json` atualizado sincroniza para os demais notebooks via Google Drive automaticamente.

**Resultado:** 67/67 PDFs processados com sucesso; 552.992 chars adicionados ao índice. corpus_index.json atualizado em 08/06/2026.

**Fluxo para novos PDFs escaneados:**
1. `python indexar_corpus.py` — marca os novos como `pdf_imagem_sem_ocr`
2. `python ocr_pdfs_imagem.py` — extrai o texto via OCR
3. Drive sincroniza o índice atualizado para os demais notebooks

**Alternativa descartada:** Integrar OCR diretamente no `indexar_corpus.py` — descartado para não adicionar dependências pesadas (pdf2image, Tesseract) ao fluxo principal de indexação, que roda com frequência.

---

## D-11 · MODELO_PRECEDENTE como terceira natureza da base da Despachadora ✅
**Data:** 09/06/2026

**Contexto:** Na base documental da 5ª Cia, muitos modelos de redação são documentos reais antigos reutilizados como espelho. Em vários casos, o texto tem forma I-7-PM clara, mas não há sinal seguro para dizer se nasceu como molde ou como caso real.

**Decisão:**
- Criar a natureza `MODELO_PRECEDENTE`.
- `MODELO_PRECEDENTE` significa: documento-espelho da casa, com forma I-7-PM reconhecível, cujo tipo exato — molde ou caso real — não pôde ser cravado por sinal.
- `MODELO_DE_REDACAO` e `PRECEDENTE` continuam válidos quando houver sinal claro.
- A segunda passada só pode promover entradas de baixa confiança para `MODELO_PRECEDENTE`; não pode renomear nem migrar entradas já classificadas em alta confiança.

**Motivo:** O rótulo preserva honestidade classificatória sem desperdiçar documentos úteis para a recuperação. Ele evita chute entre "modelo" e "precedente" quando a função prática é a mesma: servir de espelho de redação.

---

## D-12 · `corpus_index.json` sincroniza pelo Drive, não pelo git ✅
**Data:** 09/06/2026

**Contexto:** A decisão D-09 previa versionar `automacoes/despachadora/corpus_index.json` diretamente no git. Na prática, após OCR e enriquecimento do corpus, o fluxo operacional passou a tratar o índice como artefato derivado/sigiloso sincronizado pelo Google Drive, e o arquivo está protegido no `.gitignore`.

**Decisão:**
- `automacoes/despachadora/corpus_index.json` não deve ser commitado.
- O índice atualizado deve ser copiado para `CORPUS_PATH/corpus_index.json` no Google Drive.
- Backups do índice devem ficar em `G:\Meu Drive\Arquivos Josemar\Trabalho\backups_corpus_index_despachadora\`, fora do `CORPUS_PATH`.
- Artefatos de saída ignorados pelo git que precisem migrar entre máquinas devem ser copiados para uma pasta de sincronização no Drive fora do corpus físico.
- A decisão D-12 substitui o fluxo operacional descrito na D-09 para o índice.

**Motivo:** O índice contém texto extraído de documentos sensíveis e muda por operações locais de OCR/classificação. O Drive já sincroniza os notebooks e evita expor esse artefato no repositório remoto.

---

## D-13 · Reimportador pode remover entradas via EXCLUIR (operação humana) ✅
**Data:** 16/06/2026

**Contexto:** As regras invioláveis dos sprints 8.2 e 8.3 diziam explicitamente "nenhuma entrada existente pode ser removida" e o fluxo era estritamente aditivo. Na revisão humana das 199 entradas (16/06/2026), 124 documentos foram marcados como `natureza_correta=EXCLUIR` na planilha de triagem, e o reimportador precisava suportá-los.

**Decisão:**
- O `classificar_corpus.py` foi estendido: quando `natureza_correta=EXCLUIR`, a entrada é removida do índice em vez de atualizada.
- A regra "nenhuma remoção" valia para operações automáticas de IA — a IA não pode excluir. O humano pode, via planilha revisada linha a linha.
- Entradas com `classificacao_origem=humana` continuam protegidas mesmo contra EXCLUIR.
- A operação é sempre precedida de backup automático com timestamp.
- Resultado do primeiro uso: corpus passou de 729 para 605 entradas; 124 documentos sem valor documental removidos.

**Motivo:** Aditividade é regra para a IA, não para o humano. O portão de verificação (planilha revisada linha a linha) garante que nenhuma remoção acontece sem decisão consciente do operador.

---
