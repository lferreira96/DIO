from turtle import clearscreen


nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
Ano_atual = int(input("Ano Atual: "))
Ano_nascimento = int(input("Ano Nascimento: "))
Idade = Ano_atual - Ano_nascimento

print(f"{nome} {sobrenome} estamos no ano {Ano_atual}, você nasceu no ano de {Ano_nascimento} e por isso tem a idade {Idade} anos")# teste
print(f"{nome} {sobrenome} estamos no ano {Ano_atual}, você nasceu no ano de {Ano_nascimento} e por isso tem a idade {Idade} anos", end=".....\n")# teste
print(f"{nome} {sobrenome} estamos no ano {Ano_atual}, você nasceu no ano de {Ano_nascimento} e por isso tem a idade {Idade} anos",sep="#", end=".....\n")# teste
print(nome,Idade,sep="#")
# teste


