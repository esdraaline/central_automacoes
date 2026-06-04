# 📌 Registro de Decisões

> Decisões fechadas, com a razão de cada uma. Para não reabrir discussão depois.

---

## D-01 · Arquitetura: painel desktop + automações plugáveis ✅
Painel em `customtkinter`, núcleo compartilhado, e cada automação como pasta com
`manifesto.py` + `executar.py`. O painel descobre as automações sozinho.
**Motivo:** as automações controlam recursos locais (VPN, Edge, Downloads); desktop
é mais robusto que web e abre com duplo clique. Detalhes em `PLANO.md`.

---

## D-02 · Exclusão de e-mails (itens 3.1 e 4.1): triagem com confirmação ✅
Fluxo: a automação **classifica** os não lidos e gera **relatório + lista de
candidatos** → no painel você **revê e marca** o que confirma → exclusão **move para
a Lixeira** (recuperável). **Nunca** exclusão automática, nunca esvaziar lixeira,
nunca exclusão permanente.
**Motivo:** apagar e-mail é irreversível; a trava de confirmação protege contra
perder algo importante por bug ou classificação errada.

---

## D-03 · E-mail: Gmail via API, correio PM via navegador ✅
- **Gmail (4 contas: josemardp@gmail.com, josemar.dp@hotmail.com,**
  **esdraaline@gmail.com, lojadares@gmail.com):** API oficial (OAuth), uma
  autorização por conta.
  *(Obs.: hotmail.com não é Gmail — usará a API da Microsoft/Graph; o resto, Gmail API.)*
- **Correio PM:** navegador (Playwright), atrás da VPN — provavelmente não tem API.
**Motivo:** API é muito mais estável que raspar tela.

---

## D-04 · Assinatura de PDF (item 8): certificado LOCAL, não gov.br ✅
Usar o **certificado digital instalado na máquina** (o do Adobe / e-CPF local),
assinando com `pyhanko`. O painel mostra o documento e **você clica "assinar"**;
o **PIN é digitado na hora**, nunca armazenado.

**gov.br: NÃO automatizar com credenciais.** Motivos:
1. gov.br exige 2FA a cada sessão — login salvo não passa disso de forma confiável.
2. É identidade jurídica do governo; script que assina sozinho pode te vincular
   legalmente a um documento errado se a máquina for comprometida ou der bug.
**Alternativa segura (se um dia precisar):** o painel **prepara o PDF e abre o
assinador gov.br**; você faz o 2FA e assina. Sem senha guardada.

> Pendência para a Fase 6: confirmar o formato do certificado local
> (A1 `.pfx` / A3 em token / ID digital do Adobe) — muda um detalhe da implementação.

---

## D-05 · Segredos abstraídos desde o início ✅
`nucleo/segredos.py` lê de `segredos.env` por padrão, mas com interface abstrata
(`segredos.get("siopm")`), para trocar depois para o `keyring` do Windows sem
reescrever nada. Senha nunca aparece no código das automações.
