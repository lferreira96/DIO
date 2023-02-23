def Contador_letras(lista_palavras):
    # cria uma lista vazia
    cont = []

    # vai rodar toda a lista
    for c in lista_palavras:

        # guarda o tamanho da lista na posição c dentro de qtd
        qtd = len(c)

        # adiciona a quantidade na lista
        cont.append(qtd)

    # retorna a lista de contadores preenchida
    return cont

def teste():
    return "teste"


if __name__ == '__main__':
    lAnimais = ['cachorro', 'gato', 'coelho']
    print (Contador_letras(lAnimais))

# aula08_conta_letras