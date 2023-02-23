class Calculadora:
    def __init__(self, numero01, numero02):
        self.num01 = numero01
        self.num02 = numero02

    def soma(self):
        return self.num01 + self.num02

    def subtracao(self):
        return self.num01 - self.num02

    def multiplicacao(self):
        return self.num01 * self.num02

    def divisao(self):
        return self.num01 / self.num02

calculadora = Calculadora(10,5)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())