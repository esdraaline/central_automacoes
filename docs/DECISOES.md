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
