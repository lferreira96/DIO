contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

dados = contatos["chappie@gmail.com"]
print(dados)

for chave in contatos:
    print(chave)


for chave, valor in contatos.items():
    print(chave,valor)  

dados2 = contatos.copy()

print(dados2)

print(dados2.get("dados"))
print(dados2.get("dados",{}))
print(dados2.get("guilherme@gmail.com",{}))

for chave, valor in dados2.items():
        print(chave,valor)