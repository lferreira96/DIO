#numero = int(input("Entre com um número: "))
cont = 0
while cont<101:

#for cont in range(1,101):
    vezes = 0
    for x in range(1, cont+1):
        if cont % x == 0:
            vezes += 1
            if vezes > 2:
                break
#        print(x)
    if vezes == 2:
        print("O número {} é primo" .format(cont))
    cont+=1