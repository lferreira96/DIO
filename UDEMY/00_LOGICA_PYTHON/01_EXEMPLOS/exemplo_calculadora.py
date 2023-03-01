'''
exemplo de calculadora
'''

numero1 = int(input("Entre com o primeiro número: "))
sinal = input("Qual operador: + - * / ** %")
numero2 = int(input("Entre com o segundo número: "))

if sinal == "+":
	print(numero1+numero2)
elif sinal == "-":
	print(numero1-numero2)
elif sinal == "*":
	print(numero1*numero2)
elif sinal == "/":
	print(numero1/numero2)
elif sinal == "**":
	print(numero1**numero2)
elif sinal == "%":
	print(numero1%numero2)
else:
	print("opção inválida")

