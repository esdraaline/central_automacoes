# Regra Mestre de Armazenamento — Central de Automações

**Regra inviolável: nenhum arquivo do projeto pode existir apenas em pasta local.**
Todo arquivo criado ou modificado deve ir imediatamente para o GitHub ou para o
Google Drive — conforme a categoria abaixo. Nunca para um terceiro lugar.

---

## GitHub — código e documentação

Vai para o git tudo que for:
- Código Python (.py)
- Documentação do projeto (docs/)
- Configuração de ambiente não-sigilosa (requirements.txt, .gitignore)
- Exemplos de configuração sem valores reais (segredos.env.exemplo)
- Manifestos e contratos das automações (manifesto.py, executar.py)

## Google Drive — corpus e dados sigilosos

Vai para o Drive tudo que for:
- Corpus físico da Despachadora (pastas P1, P2, P3, P4, P5, JD, Notebooklm)
- corpus_index.json — índice gerado do corpus (sigiloso + pesado)
- Qualquer arquivo que contenha dados pessoais, expedientes, CPF, nomes do efetivo,
  contatos de autoridades ou documentos internos da PMESP

## .gitignore — último recurso

O .gitignore só recebe entradas novas quando não há alternativa.
A regra é: se o arquivo é sigiloso, vai ao Drive. Só entra no .gitignore se
precisar existir dentro da pasta do projeto mas não puder ir ao git.
O que já está no .gitignore hoje permanece — não rever entradas existentes.

## segredos.env

Fica apenas local em cada máquina. Nunca vai ao git, nunca vai ao Drive.
Sincronização manual entre máquinas, usando segredos.env.exemplo como guia.

## Regra de sincronização

Sempre que uma sessão de trabalho (Codex, Claude Code ou qualquer IA) criar ou
modificar um arquivo, ela DEVE confirmar ao encerrar:
- Arquivos de código: commitados e pushed ao GitHub?
- corpus_index.json: copiado/atualizado no Drive?
- segredos.env: Josemar foi alertado para replicar manualmente no outro notebook?
- Nada ficou apenas em pasta local?
