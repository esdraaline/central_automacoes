# automacoes/

Uma pasta por automação. O painel descobre todas sozinho — você nunca edita o
painel para adicionar uma automação nova.

## Como criar uma automação nova

1. Crie uma pasta aqui (ex.: `login_dejem/`).
2. Coloque dois arquivos:

```python
# manifesto.py
MANIFESTO = {
    "id": "login_dejem",
    "nome": "Logar no Dejem",
    "descricao": "Abre o Dejem e autentica na minha área",
    "categoria": "Logins",
    "precisa_vpn": False,
    "destrutivo": False,
    "confirma_antes": False,
    "ordem": 50,
}
```

```python
# executar.py
def run(ctx):
    # ctx.log, ctx.vpn, ctx.browser, ctx.saidas, ctx.segredos
    ...
    return {"status": "ok", "detalhes": "..."}
```

3. Abra o painel: o botão já aparece.

## Pastas atuais
- `baixar_bopm/` — automação 1 (código original; será adaptada ao contrato na Fase 0).
