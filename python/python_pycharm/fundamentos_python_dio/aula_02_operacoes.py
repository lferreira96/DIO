# Operadores matemáticos:
# +, -, *, /, %,
# ctrl + / - comenta as linhas selecionadas
# ctrl + F10 - compila e executa o código
# outra forma de se escrever valores também é utilizando {} e .format
# print('soma: {}'.format(soma))
#conversão de tipos:
#int()
#str()

# O Python já coloca espaço quando mandamos imprimir algo, não sendo necessário adicionar o espaço
# para retornar o tipo de uma variável, utilizamos a função: type()
# a formatação segue o mesmo padrão de javascript. Exemplo: \n

#a = 10
#b = 5
a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
texto = "teste"
IntParaTexto = str(soma)

print(type(resto))
print(type(divisao))
print(type(texto))
print(type(IntParaTexto))

print('A soma dos valores {a} e {b} é: {s}'.format(a=a,b=b,s=soma))
print('A subtração dos valores {} e {} é: {}'.format(a,b,subtracao))
print('A multiplicação entre os valores {} e {} é: {}'.format(a,b,multiplicacao))
print('A divisão entre os valores {} e {} é: {}'.format(a,b,divisao))
print('O resto da divisão de {} por {} é: {}'.format(a,b,resto))

# outra forma de se escrever
print("")
print("A soma dos valores",a,"e",b,"é:",soma)
print("A subtração dos valores",a,"e",b,"é:",subtracao)
print("A multiplicação dos valores",a,"e",b,"é:",multiplicacao)
print("A divisão de",a,"por",b,"é:",divisao)
print("O resto da divisão de",a,"e",b,"é:",resto)