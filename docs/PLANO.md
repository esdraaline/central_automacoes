# Central de Automações — Plano de Construção

**Autor:** Josemar de Paula · **Contexto:** produtividade do serviço (5ª Cia / 2º BPM-I / CPI-10)
**Base existente:** projeto `bopm_automation` (Python + Playwright + Edge)

---

## 1. Visão geral

Hoje existe **1 automação** (Baixar BOPMs) rodando por um `.bat` de menu. A meta é um **painel único, com botões**, onde cada botão dispara uma automação, todas vivendo na **mesma pasta** e gravando saídas num **lugar só**.

O segredo para escalar de 1 para ~12 automações sem virar bagunça é **não** acrescentar `if/else` no painel a cada nova automação. Em vez disso:

> O painel **descobre sozinho** as automações disponíveis lendo uma pasta. Adicionar uma automação nova = largar uma pasta nova. O painel passa a mostrar o botão automaticamente.

Isso é o que permite o seu fluxo: *construir uma de cada vez e ir integrando*.

---

## 2. Arquitetura recomendada

**Painel desktop em Python (`customtkinter`)** + **núcleo compartilhado** + **automações plugáveis**.

### Por que desktop e não web (FastAPI/React)?
As automações controlam recursos **locais da sua máquina**: VPN Cisco, janela do Edge visível, salvar em `Downloads`. Um painel desktop:
- abre com duplo clique (sem servidor, sem porta, sem aba de navegador para manter aberta);
- é mais robusto para esse tipo de tarefa de SO;
- mostra o log ao vivo numa janela só.

> Dá para fazer em FastAPI + HTML (mais a sua cara), e fica registrado como alternativa no fim. Mas para confiabilidade num uso diário de serviço, o desktop ganha. Recomendo começar por ele.

### Estrutura de pastas

```
central_automacoes/
├── painel.py                 # GUI principal — descobre e roda as automações
├── nucleo/                   # código compartilhado (refatorado do bopm atual)
│   ├── vpn.py                # VPNManager (movido do bopm)
│   ├── browser.py            # BrowserManager (Playwright/Edge)
│   ├── log.py                # logging padronizado
│   ├── segredos.py           # acesso seguro a credenciais (ver Seção 4)
│   ├── assinatura.py         # serviço de assinatura de PDF (item 8)
│   └── relatorio.py          # geração de relatórios padronizados
├── automacoes/
│   ├── baixar_bopm/          # 1   (a atual, adaptada)
│   │   ├── manifesto.py
│   │   └── executar.py
│   ├── validar_bopm/         # 1.1 (já existe base no gemini_submitter)
│   ├── orion_indicadores/    # 2
│   ├── correio_pm/           # 3 + 3.1
│   ├── gmail_relatorio/      # 4 + 4.1 (parametrizável p/ 4 contas)
│   ├── login_mapaforca/      # 6
│   ├── login_dejem/          # 7
│   └── assinar_pdf/          # 8
├── saidas/                   # TUDO numa pasta só: PDFs, relatórios, listas
├── logs/
├── segredos.env              # credenciais (FORA de qualquer sincronização)
└── requirements.txt
```

### O "contrato" de cada automação

Cada pasta em `automacoes/` tem dois arquivos. O painel só precisa conhecer esse contrato:

```python
# manifesto.py
MANIFESTO = {
    "id": "baixar_bopm",
    "nome": "Baixar BOPMs",
    "descricao": "Baixa do SIOPM os BOPMs pendentes de validação",
    "categoria": "SIOPM",
    "precisa_vpn": True,       # painel garante VPN antes de rodar
    "destrutivo": False,       # se True, painel pede confirmação
    "confirma_antes": False,   # botão pede "tem certeza?"
    "ordem": 10,
}
```

```python
# executar.py
def run(ctx):
    """
    ctx dá acesso ao núcleo: ctx.log, ctx.vpn, ctx.browser,
    ctx.saidas (pasta de saída), ctx.segredos.
    Retorna um dict de relatório (qtd processada, falhas, arquivos).
    """
    ...
```

O painel faz: lê todos os `manifesto.py` → desenha um cartão+botão por automação → ao clicar, garante VPN se preciso → roda `run(ctx)` numa thread → transmite o log ao vivo → mostra status (✓ / ✗ / nº processados).

**Esse é o ponto-chave do plano.** Depois que o esqueleto existe, cada item da sua lista é só uma pasta nova.

---

## 3. Roadmap por fases

A ordem prioriza **fundação primeiro**, depois **ganhos rápidos e seguros**, depois os itens mais sensíveis.

| Fase | Entrega | Itens da sua lista | Esforço | Risco |
|------|---------|--------------------|---------|-------|
| **0** | Refatorar `bopm` em `nucleo/` + painel-esqueleto rodando a automação 1 | (fundação) | Médio | Baixo |
| **1** | Automações de login (abrir sistema + autenticar) | 6 Mapa Força · 7 Dejem/Delegada | Baixo | Baixo |
| **2** | Validar BOPM (formalizar o que o Gemini já faz) | 1.1 | Baixo | Baixo |
| **3** | Consultar indicadores criminais no Órion | 2 | Médio | Médio |
| **4** | Relatório de e-mails **não lidos** (só leitura) | 3 correio PM · 4 Gmail (4 contas) | Médio | Médio |
| **5** | Triagem/exclusão de e-mails (com trava de confirmação) | 3.1 · 4.1 | Médio | **Alto** ⚠ |
| **6** | Assinatura de PDF | 8 | Médio | **Alto** ⚠ |

Os itens marcados ⚠ exigem decisão sua antes (Seção 5).

---

## 4. Segurança das credenciais (importante)

Hoje o `config.py` guarda senhas em **texto puro** (VPN, SIOPM). Para 1 automação numa máquina sua, tudo bem. Mas você vai passar a guardar **VPN + SIOPM + Órion + Mapa Força + Dejem + 4 contas de e-mail** no mesmo lugar. Texto puro fica arriscado — principalmente se a pasta um dia for parar num pen drive, num backup, ou (Deus me livre) num repositório.

**Recomendação:** centralizar tudo em `nucleo/segredos.py`, lendo de **uma destas opções**, em ordem de preferência:

1. **Windows Credential Manager** via biblioteca `keyring` — as senhas ficam no cofre do próprio Windows, nunca em arquivo.
2. **Arquivo `.env` cifrado** com uma senha-mestra que você digita ao abrir o painel.
3. No mínimo: um único `segredos.env`, **fora de qualquer sincronização/backup automático**, com aviso no topo.

O resto do código (núcleo e automações) nunca vê senha — só chama `ctx.segredos.get("siopm")`.

---

## 5. Decisões que preciso de você

### Decisão A — Exclusão de e-mails (itens 3.1 e 4.1)
Apagar e-mail automaticamente é **irreversível**. Não vou construir um script que sai deletando sozinho — o risco de apagar algo importante é real. Proposta de desenho seguro:

1. A automação **classifica** os não lidos e gera um **relatório + lista de candidatos a excluir** (ex.: newsletters, promoções, remetentes já marcados por você).
2. No painel, você **revê e marca** o que confirma.
3. A exclusão **move para a Lixeira** (recuperável) — **nunca** esvazia a lixeira nem faz exclusão permanente.

Você concorda com esse desenho (triagem → você confirma → vai pra lixeira)? Ou quer regras de exclusão automática para categorias específicas bem definidas (ex.: "tudo de remetente X")?

### Decisão B — Assinatura do PDF (item 8)
"Assinatura digital" tem dois significados bem diferentes:

- **(a) Carimbo visual** — colar a imagem da sua assinatura no campo "JOSEMAR DE PAULA" do PDF. Simples, rápido, **sem valor jurídico de certificado**.
- **(b) Assinatura digital com certificado (e-CPF / ICP-Brasil)** — válida juridicamente, exige seu certificado e PIN, feita com bibliotecas tipo `pyhanko`/`endesive`.

Qual você quer? (Pode ser as duas: carimbo para rascunhos, certificado para o documento final.)

Importante: se for a opção (b), **não** faço o script assinar vários documentos em lote sozinho — cada assinatura jurídica é um ato seu. O painel mostra o documento e **você clica "assinar"** em cada um. Carimbo visual (a) pode ser em lote sem problema.

### Decisão C — E-mail por API ou por navegador?
- **Gmail (4 contas):** o ideal é a **API oficial do Gmail (OAuth)** — muito mais estável que abrir o navegador e raspar a tela. Exige autorizar o acesso uma vez por conta.
- **Correio PM:** provavelmente é webmail na intranet (atrás da VPN). Aí normalmente **não tem API** e a automação vai por navegador (Playwright), como o SIOPM.

Topa o Gmail via API e o correio PM via navegador?

---

## 6. Primeiro passo sugerido

Não construir nenhuma automação nova ainda. Construir a **Fase 0**:

1. Reorganizar o `bopm_automation` atual dentro da estrutura `central_automacoes/` (núcleo + 1ª automação no novo formato).
2. Subir o **painel-esqueleto** com **1 botão** ("Baixar BOPMs") que roda o que você já tem, agora pela interface gráfica, com log ao vivo.

Quando esse esqueleto estiver de pé e rodando a automação que você já confia, o resto é repetição: uma pasta de cada vez.

---

## 7. Alternativa registrada (FastAPI + HTML)

Se em algum momento você quiser o painel acessível pelo navegador/celular (como fez no app de Relatório de Ronda), dá para trocar a camada de interface por **FastAPI + uma página HTML**, mantendo **o mesmo núcleo e as mesmas automações** intactos. O contrato `manifesto.py` + `run(ctx)` não muda. É só outra "casca" por cima. Por isso vale começar pelo desktop sem medo de retrabalho.
