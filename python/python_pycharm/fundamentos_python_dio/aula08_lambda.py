contador_letras = lambda lista_palavras: [len(cont) for cont in lista_palavras]


soma = lambda a,b: a+b
subtracao = lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b

listaAnimais = ['cabra','cachorro','bode','boi','ovelha']

calculadora = {
    'soma' : lambda a, b: a + b,
    'subtracao' : lambda a, b: a - b,
    'multiplicacao' : lambda a, b: a * b,
    'divisao' : lambda a, b: a / b,
}

print (type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subracao']
multimplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

a = 10
b = 2

print(soma(a,b))
print(subtracao(a,b))
print(multiplicacao(a,b))
print(divisao(a,b))

print(contador_letras(listaAnimais))
print(soma(a,b))
print(subtracao(a,b))
print(multiplicacao(a,b))
print(divisao(a,b))

#
# def Contador_letras(lista_palavras):
#     cont = []
#     for c in lista_palavras:
#         qtd = len(c)
#         cont.append(qtd)
#     return cont