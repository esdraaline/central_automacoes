# Contexto de Retorno — 23/06/2026

## Estado ao encerrar o dia

- Branch: `main`.
- Despachadora endurecida para o caso de acidente com viatura e Investigação Preliminar.
- Fonte autônoma adicionada: `corpus_manual/Investigacao_Preliminar_I16.md`.
- Índice local: 729 entradas; não deve ser enviado ao git conforme D-12.
- Fase em execução: Fase 3 — Órion.
- Sprint 3.1 implementada em código, ainda não validada no sistema real.

## Próximo passo amanhã

1. Obter a URL exata da página interna do Órion.
2. Adicionar `ORION_URL=<url>` ao `segredos.env` local, sem compartilhar usuário ou senha.
3. Abrir a Central, conectar a VPN e clicar em **Abrir Órion**.
4. Confirmar se a sessão chega à tela inicial.
5. Se falhar, consultar o log: `login_orion.py` registra URL, frames e atributos estruturais dos campos, sem valores sensíveis.

## Entregas do Sprint 3.1

- `nucleo/login_orion.py`: navegação, preenchimento, envio e confirmação de sessão.
- `automacoes/orion_indicadores/manifesto.py`: botão plugável no painel.
- `automacoes/orion_indicadores/executar.py`: execução pelo contrato da Central.
- `ORION_URL` incorporada ao esquema seguro e ao template de segredos.
- `tests/test_orion_sprint31.py`: testes locais sem rede ou credenciais reais.

## Critério para encerrar o Sprint 3.1

O Sprint só será marcado como concluído quando o botão **Abrir Órion** autenticar com sucesso pela VPN e deixar a tela inicial disponível no Edge. Depois disso começa o Sprint 3.2: consulta por município e período.

## Observação Gemini

A cota gratuita diária foi atingida durante os retestes da Despachadora. O código agora distingue esgotamento diário de erro transitório e preserva o bloqueio seguro caso a chamada de autocorreção não possa ser executada.
