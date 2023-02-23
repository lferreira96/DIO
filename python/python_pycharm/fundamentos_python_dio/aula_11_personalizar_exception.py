'''
    Criando uma exceção com o class Error e
    InputError
'''

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x<0 or x>10:
            # o comando raise força uma exceção
            raise InputError('Favor entrar com números entre 0 e 10')
        break
    except ValueError:
        print('Valor Inválido!\nDeve-se entrar com apenas números.')
    except InputError as ex:
        print(ex)

