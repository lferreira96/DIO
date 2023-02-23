conjunto = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,101,2,3,4,5,6,7,8,9,101,2,3,4,5,6,7,8,9,101,2,3,4,5,6,7,8,9,10}
print("\n------------------------       Conjuntos      ------------------------------\n")
print("Classe........................................: {}" .format(type(conjunto)))
print("Tamanho conjunto..............................: {}" .format(len(conjunto)))
print("Conjunto......................................: {}" .format(conjunto))
conjunto.add(15)
conjunto.discard(101)
print("\n-----------------   Adicionando e removendo itens    -----------------------\n")
print("Conjunto após adicionado o 15 e retirado o 101: {}" .format(conjunto))
print("\n----------------    Unindo e Interseção de conjuntos   ----------------------\n")
# união de conjuntos
conjunto01 = {1,2,3,4,5}
conjunto02 = {5,6,7,8,9}

uniao = conjunto01.union(conjunto02)
intersecao = conjunto01.intersection(conjunto02)

print("Conjunto01........................: {}" .format(conjunto01))
print("Conjunto02........................: {}" .format(conjunto02))
print("Tamanho após a união dos conjuntos: {}" .format(len(uniao)))
print("União dos dois conjuntos..........: {}" .format(uniao))
print("Intersecao dos dois conjuntos.....: {}" .format(intersecao))

print("\n---------------------    Diferença de conjuntos   ---------------------------\n")
# união de conjuntos
diferenca01 = conjunto01.difference(conjunto02)
diferenca02 = conjunto02.difference(conjunto01)
diferenca03 = conjunto01.symmetric_difference(conjunto02)

print("Diferença Conjunto01 para o Conjunto02.....: {}" .format(diferenca01))
print("Diferença Conjunto02 para o Conjunto01.....: {}" .format(diferenca02))
print("Diferença entre os conjuntos sem interseção: {}" .format(diferenca03))


print("\n---------------------   Verifica se Está Contido   ---------------------------\n")
# união de conjuntos

conjunto03 = {1,2,3,4}
conjunto04 = {1,2,3,4,5,6,7,8,9,10}
estacontido = conjunto03.issubset(conjunto04)
contem = conjunto04.issuperset(conjunto03)

print("Conjunto03........................: {}" .format(conjunto03))
print("Conjunto04........................: {}" .format(conjunto04))

if estacontido:
    print("O conjunto {} está contido no conjunto {} " .format(conjunto03,conjunto04))
else:
    print("O conjunto {} não está contido no conjunto {} ".format(conjunto03, conjunto04))

if contem:
    print("O conjunto {} contém o conjunto {} " .format(conjunto04,conjunto03))
else:
    print("O conjunto {} não contém o conjunto {} ".format(conjunto04, conjunto03))

lista = ["cachorro","gato","cavalo","cavalo","bode"]
conjunto05 = set(lista)
print(lista)
print(type(conjunto05))
print(conjunto05)

lista = list(conjunto05)
print(lista)

print(lista[2])