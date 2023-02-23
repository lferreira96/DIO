from turtle import screensize


frase = input("Entre com a frase: ")
frase2 = input("Entre com a segunda frase: ")
frase3 = frase + frase2

# ════════════════════════════════════════
# coloca todas as letras em maiúsculas
print(frase.upper())

# coloca todas as letras em minúsculas
print(frase.lower())

# coloca a primeira letra de cada palavra em maiúsculo e o restante em minúsculo
print(frase.title())

# ════════════════════════════════════════
# retira todos os espaços das extremidades
print(frase2, frase.strip(), frase2)

# retira os espaços à esquerda
print(frase2, frase.lstrip(), frase2)

# retira os espaços à direita
print(frase2, frase.rstrip(), frase2)

# ════════════════════════════════════════
# insere nas extremidades um determinado caracter para completar uma frase até atingir um determinado tamanho
print(frase.center(len(frase3)+10, "#"))

# Se não adicionarmos nada, simplesmente completará com espaços em branco
print(frase.center(len(frase3)))


#insere na frase um caracter especificado entre as letras
print(".".join(frase3))
