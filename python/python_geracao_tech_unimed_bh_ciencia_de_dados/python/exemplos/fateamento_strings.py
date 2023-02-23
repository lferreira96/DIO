nome = "Leonardo Ferreira"

#═════════════════════════════════
# Exibe a letra que está na posição 0
print(nome[0])

# Exibe todas as letras até atingir a posição 7, considerando começando de 1
print(nome[:7])

# Exibe todas as letras a partir da posição 8
print(nome[7:])
# Exibe todas as letras entre as posições delimitadas, inclusive com as extremidades
print(nome[9:17])

# Vai pegar todas as letras entre 9 e 17, pulando de 2 em 2 (step - passo)
# Ferreira - F r e r  - Letras que pegará
#             e r i a - Letras que não pegará
print(nome[9:17:2])

# Pega o nome por completo
print(nome[:])

# Exibe o nome espelhado (ao contrário)
print(nome[::-1])
