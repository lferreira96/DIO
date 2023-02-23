listNum = [1,4,87,32,11,16,-10,35,0,3,5,6,45]
listNumTupla = (1,4,87,32,11,16,-10,35,0,3,5,6,45)
listAnimais = ["jacaré","avestruz","tamanduá", "boto","guelpardo"]
listTuplaConvertida = tuple(listAnimais)
listAlfabeto = ["Aa","AA","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","az","Y"]

print(type(listNumTupla))
print(type(listTuplaConvertida))
print(listAnimais)
print (len(listAlfabeto))
print(sum(listNum))
print(max(listNum))
print(min(listNum))
print("minimo:",min(listAlfabeto))
print("máximo:",max(listAlfabeto))
listAnimais2 = listAnimais * 2
print(listAnimais2)
if "lobo" in listAnimais:
    print("já cadastrado")
else:
    listAnimais.append("lobo")

print(listAnimais)
listAnimais.pop(3)
print(listAnimais)
listAnimais.remove("avestruz")
print(listAnimais)
listAnimais.sort()
listAnimais.reverse()
print(listAnimais)

print(listNum)
listNum.reverse()
#listNum.reverse()
print(listNum)

# frutas = ["melancia", "laranja", "uva"]
# numeros = [1, 2, 3]
# lista_heterogenea = ["melancia", 1, [frutas, numeros], frutas]
#
# print(frutas)
# print(numeros)
# print(lista_heterogenea)
# print(lista_heterogenea[2])
#
#
# valores_dobrados = []
# for valor in range(20):
#    valores_dobrados.append(valor*2)
# print(valores_dobrados)
#
# # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# #Com list comprehension esta operação é simplificada ao seguinte:
#
# valores_dobrados = [valor * 2 for valor in range(20)]
# print(valores_dobrados)
# # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
#
