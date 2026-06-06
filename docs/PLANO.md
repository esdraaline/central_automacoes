# Central de Automações — Plano de Construção
**Autor:** Josemar de Paula · **Contexto:** produtividade do serviço (5ª Cia / 2º BPM-I / CPI-10)
**Base existente:** projeto `bopm_automation` (Python + Playwright + Edge)

---

## 1. Visão geral

Hoje existe 1 automação (Baixar BOPMs) rodando por um `.bat` de menu. A meta é um painel único, com botões, onde cada botão dispara uma automação, todas vivendo na mesma pasta e gravando saídas num lugar só.

O segredo para escalar de 1 para ~12 automações sem virar bagunça é **não acrescentar if/else no painel a cada nova automação**. Em vez disso:

- O painel descobre sozinho as automações disponíveis lendo uma pasta.
- Adicionar uma automação nova = largar uma pasta nova. O painel passa a mostrar o botão automaticamente.

Isso é o que permite o seu fluxo: construir uma de cada vez e ir integrando.

---

## 2. Arquitetura

Painel desktop em Python (customtkinter) + núcleo compartilhado + automações plugáveis.

**Por que desktop e não web (FastAPI/React)?**
As automações controlam recursos locais da sua máquina: VPN Cisco, janela do Edge visível, salvar em saídas/. Um painel desktop abre com duplo clique (sem servidor, sem porta, sem aba de navegador para manter aberta), é mais robusto para esse tipo de tarefa de SO e mostra o log ao vivo numa janela só.
*(Alternativa FastAPI + HTML registrada na Seção 7.)*

### Estrutura de pastas

```
central_automacoes/
├── painel.py                 # GUI principal — descobre e roda as automações
├── nucleo/                   # código compartilhado (refatorado do bopm atual)
│   ├── vpn.py                # VPNManager
│   ├── browser.py            # BrowserManager (Playwright/Edge)
│   ├── log.py                # logging padronizado
│   ├── segredos.py           # acesso seguro a credenciais
│   ├── login_mapa_forca.py   # login reutilizável SIOPM/Mapa Força
│   ├── login_dejem.py        # login reutilizável Dejem/Delegada
│   ├── assinatura.py         # serviço de assinatura de PDF (Fase 6)
│   └── relatorio.py          # geração de relatórios padronizados
├── automacoes/
│   ├── baixar_bopm/          # 1   (a atual, adaptada)
│   ├── validar_bopm/         # 1.1 (Fase 2)
│   ├── orion_indicadores/    # 2   (Fase 3)
│   ├── correio_pm/           # 3 + 3.1 (Fase 4/5)
│   ├── gmail_relatorio/      # 4 + 4.1 (Fase 4/5)
│   ├── abrir_mapa_forca/     # 6   (uso real, Edge aberto)
│   ├── abrir_dejem/          # 7   (uso real, Edge aberto)
│   ├── teste_logins/         # diagnóstico (valida e fecha)
│   ├── assinar_pdf/          # 8   (Fase 6)
│   └── despachadora/         # Fase 7 — ver seção abaixo
├── saidas/                   # TUDO numa pasta só: PDFs, relatórios, listas
├── logs/
├── docs/                     # README, PLANO, DECISOES, ROADMAP, STATUS, PROMPT_*
├── segredos.env              # credenciais — NUNCA no git, criar manualmente em cada notebook
├── segredos.env.exemplo      # template sem valores reais — versionado no git
└── requirements.txt
```

### O contrato de cada automação

```python
# manifesto.py
MANIFESTO = {
    "id": "baixar_bopm",
    "nome": "Baixar BOPMs",
    "descricao": "Baixa do SIOPM os BOPMs pendentes de validação",
    "categoria": "SIOPM",
    "precisa_vpn": True,       # painel garante VPN antes de rodar
    "destrutivo": False,       # se True, painel pede confirmação
    "confirma_antes": False,
    "ordem": 10,
}

# executar.py
def run(ctx):
    # ctx.log, ctx.vpn, ctx.browser, ctx.saidas, ctx.segredos
    return {"status": "ok", "detalhes": "..."}
```

O painel faz: lê todos os `manifesto.py` → desenha um cartão+botão por automação → ao clicar, garante VPN se preciso → roda `run(ctx)` numa thread → transmite o log ao vivo → mostra status (✓ / ✗ / nº processados).

---

## 3. Roadmap por fases

| Fase | Entrega | Itens | Status |
|---|---|---|---|
| 0 | Fundação: nucleo/ + painel-esqueleto com BOPM | (fundação) | ✅ |
| 1 | Logins: Mapa Força · Dejem/Delegada | 6 · 7 | ✅ |
| 2 | Validar BOPM (formalizar o gemini_submitter) | 1.1 | ⏳ |
| 3 | Consultar indicadores criminais no Órion | 2 | ⏳ |
| 4 | Relatório de e-mails não lidos (só leitura) | 3 correio PM · 4 Gmail | ⏳ |
| 5 | Triagem/exclusão de e-mails (com trava) | 3.1 · 4.1 | ⏳ ⚠ |
| 6 | Assinatura de PDF com certificado local | 8 | ⏳ ⚠ |
| 7 | Despachadora do Comandante (redação assistida) | — | ⏳ (paralela) |

---

## 4. Segurança das credenciais

Centralizado em `nucleo/segredos.py`, lendo de `segredos.env` (via `python-dotenv`). Interface abstrata `segredos.get("siopm")` — permite trocar para `keyring` do Windows sem reescrever quem chama. Senha nunca aparece no código das automações.

`segredos.env` fora de qualquer sincronização/backup/git. `segredos.env.exemplo` versionado sem valores reais.

---

## 5. Decisões fechadas (resumo — detalhe em DECISOES.md)

- **D-01:** Arquitetura desktop + automações plugáveis.
- **D-02:** Exclusão de e-mail: triagem → confirmação → Lixeira. Nunca automático, nunca permanente.
- **D-03:** Gmail via API (OAuth); correio PM via navegador (Playwright).
- **D-04:** Assinatura com certificado LOCAL (e-CPF/pyhanko), PIN na hora, por documento. gov.br não se automatiza.
- **D-05:** Segredos abstraídos desde o início via `nucleo/segredos`.
- **D-06:** SEI fora do escopo — acesso manual.
- **D-07:** Despachadora — código na Central, corpus no Drive. `CORPUS_PATH` e `GEMINI_API_KEY` via `segredos.env`.

---

## 6. Fase 7 — Despachadora do Comandante (detalhe)

### O que é

Assessora de Estado-Maior do Cmt da 5ª Cia PM. Recebe um expediente (parte, ofício, despacho, denúncia, BO, laudo — arquivo ou texto colado), busca contexto num corpus indexado da 5ª Cia e devolve **6 blocos fixos:** Classificação, Análise Jurídica, Decisão, Texto Pronto (padrão I-7-PM), Levantamentos, Assessoria do Estado-Maior.

### Estado de partida

Versão standalone **pronta e testada** em caso real. Hoje em:
`G:\Meu Drive\Arquivos Josemar\Trabalho\Skill despachadora de Docs\`

Arquivos: `indexar_corpus.py`, `despachadora.py`, `corpus_index.json`, `README.md`.
`MASTER_SYSTEM_PROMPT v1.2` (10 blocos) embutido inline em `despachadora.py`.

### Estrutura alvo (D-07)

```
automacoes/despachadora/
├── manifesto.py              # precisa_vpn=False, destrutivo=False, categoria="Redação"
├── executar.py               # run(ctx) — chama o núcleo; lê CORPUS_PATH de ctx.segredos
├── corpus_index.json         # versionado no git (~34 MB); gerado pelo indexar_corpus
└── nucleo_despachadora/
    ├── despachadora.py       # MOVIDO do Drive — vira função chamável (main() → def processar())
    └── indexar_corpus.py     # MOVIDO do Drive — mantido junto para reindexações
```

**Corpus documental (P1–P5, JD, Notebooklm) permanece no Drive. Nunca entra no git.**

### Contrato técnico herdado do standalone

- **Índice** `corpus_index.json`: lista de `{section, arquivo, tipo, texto, error}`.
- **Recuperação** por densidade: `score = ocorrências ÷ (len(texto) ** 0.5)`. Dois pools: **Fundamento** (top 12, todas as seções) + **Modelo de redação** (top 8, excluindo seção `Notebooklm`). Dedup por chave.
- **Modelo:** `gemini-2.5-flash` via SDK `google-genai` (não o legado `google-generativeai`).
- **Extratores:** PDF (PyMuPDF→pypdf→`pdf_imagem_sem_ocr`); DOCX (parágrafos+tabelas); DOC/RTF (Word COM via pywin32, batch, ReadOnly); XLSX (openpyxl); TXT/MD/HTML.

### Restrições técnicas a investigar no Sprint 7.1

| Ponto | Detalhe | Impacto |
|---|---|---|
| Input de arquivo no painel | `_on_run` passa apenas `ctx` sem argumento de arquivo. Extensão necessária. | ⚠ investigar |
| Exibição de saída longa | `_run_thread` exibe resultado como string curta hardcoded. Os 6 blocos precisam de mecanismo próprio. | ⚠ investigar |
| `SKILL_ROOT` hardcoded | `indexar_corpus.py` linha 38: `Path("G:/Meu Drive/...")`. Adaptar para `CORPUS_PATH`. | Mínima |
| `CORPUS_FILE` relativo ao script | Ao mover para `nucleo_despachadora/`, apontar um nível acima. | Mínima |
| `.gitignore` e corpus | Cobrir P1–P5, JD, Notebooklm antes do Sprint 7.2. | Antes do 7.2 |

### Regras invioláveis herdadas do standalone

1. **Nada de FUNDAMENTO inventado** — norma/artigo/número/prazo/valor só do corpus ou de lei pública estável. Sem lastro → `[VERIFICAR: ...]`.
2. **Três tiers de proveniência:** `[FUNDAMENTO]` (rastreável) · `[PADRÃO]` (forma) · `[SUGESTÃO]` (antecipação). Inventar FUNDAMENTO é falha grave.
3. **Proveniência não se fabrica** — `[FONTE: section/arquivo]` só para chunk efetivamente recuperado em runtime.
4. **TEXTO PRONTO nunca é omitido** — sem fundamento, entrega com `[VERIFICAR]` e leva a dúvida ao Bloco 5.
5. NI PM3-001/02/15 = SECRETO (citar como "norma interna PMESP"); DEJEM nunca citar artigo; Bol G PM 49/16MAR11 REVOGADO.
6. **Reaproveitar, não reescrever** — preservar extração + recuperação dois-pools + chamada Gemini. Reimplementar é regressão.
7. **SDK:** `google-genai` (não o legado `google-generativeai`); modelo: `gemini-2.5-flash`.

### Sequenciamento

- **Sprint 7.1 (investigação):** Claude Code lê a Central e propõe o plano de port. Nenhum código escrito.
- **Sprint 7.2 (port do núcleo):** mover e adaptar arquivos conforme plano aprovado.
- **Sprint 7.3 (integração UI):** extensão do painel para input de arquivo e exibição dos 6 blocos.
- **Sprint 7.4 (testes e system prompt v1.3):** testar com casos reais; promover `[VERIFICAR]` confirmados.

---

## 7. Alternativa registrada (FastAPI + HTML)

Se em algum momento você quiser o painel acessível pelo navegador/celular, dá para trocar a camada de interface por FastAPI + uma página HTML, mantendo o mesmo núcleo e as mesmas automações intactos. O contrato `manifesto.py` + `run(ctx)` não muda. É só outra "casca" por cima.
