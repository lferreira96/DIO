class Calculadora:
# Não é necessário o init uma vez que os valores estão sendo passados direto nos métodos
#    def __init__(self):
#        pass
    def soma(self,num01, num02):
        return num01 + num02

    def subtracao(self,num01, num02):
        return num01 - num02

    def multiplicacao(self,num01, num02):
        return num01 * num02

    def divisao(self,num01, num02):
        return num01 / num02

if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(10,5))
    print(calculadora.subtracao(10,5))
    print(calculadora.multiplicacao(10,5))
    print(calculadora.divisao(10,5))