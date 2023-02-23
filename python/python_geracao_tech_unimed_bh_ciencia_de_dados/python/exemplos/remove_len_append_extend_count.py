animais =  [ "gato","cachorro","papagaio", "periquito","burro", "macaco"]

for bichos in animais:
    print (bichos)

# Retorna quantos elementos tem em um vetor
print (len(animais))

# Remove a palavra periquito do vetor
animais.remove("periquito")


for bichos in animais:
    print (bichos)

# Retorna quantos elementos tem em um vetor
print (len(animais))

# Adiciona o valor leão no vetor
animais.append("leão")
print (animais)

# Adiciona os dois valores: burrito e 3 no vetor
animais.extend(["burrito",3])
print(animais)

# Retorna quantas vezes aparece a palavra peixe
print(animais.count("peixe"))

