# comandos
# >  - maior que
# >= - maior ou igual a
# <  - menor que
# <= - menor ou igual a
# == - igual a
# if <condição> : - se

# if <condição> : - se....senão
# else:

# if <condição> : - se....senão se
# elif:

# and
# or
# not





# utilizando os comandos if, else, elif e os operadores and, or e not

# declarando variáveis para nome, ano atual, ano de nascimento, sexo e idade
# nome = input("Entre com o seu Nome: ")
# anoAtual = int(input("Entre com o Ano Atual: "))
# anoNascimento = int(input("Entre com o Ano em que Nasceu: "))
# sexo = input("Entre com o seu Sexo: ")
#
# idade = anoAtual - anoNascimento
#
# if (idade >= 18):
#     msgIdade = "maior"
# else:
#     msgIdade = "menor"
#
# if ((sexo == "masculino") or (sexo == "Masculino")):
#     msgSexo = "homem"
# else :
#     msgSexo = "mulher"
#
# print("{} você é {} e é {} de idade" .format(nome,msgSexo,msgIdade))


# ENTRANDO COM 03 VALORES

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if a > b and a > c:
    print("o valor a {} é maior que b {} e c {}" .format(a,b,c))
elif b > a and b > c:
    print("o valor b {} é maior que a {} e c {}".format(b, a, c))
elif c > a and c > b:
    print("o valo r c {} é maior que a {} e b {}".format(c, a, b))