lista = [1,10]
arquivo = open('teste.txt','r')
try:
    texto = arquivo.read()
    divisao = 190/1
    numero = lista[1]
    #Sx = a

except ZeroDivisionError:
    print('Não é possívl divisão por zero')
except IndexError:
    print ('Erro ao tentar acessar o índice')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
except Exception as ex:
    print('Erro: {}' .format(e))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()