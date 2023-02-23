import shutil

def escrever_arquivo(nmarquivo, texto):
    arquivo = open(nmarquivo,'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nmarquivo, texto):
    arquivo = open(nmarquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nmarquivo):
    arquivo = open(nmarquivo,'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

def media_notas(nmarquivo):
    arquivo = open(nmarquivo,'r')
    dadosarquivo = arquivo.read().split('\n')
    lista_media =[]
    for cont in dadosarquivo:
        dadosalunos = cont.split(",")
        nmaluno = dadosalunos[0]
        dadosalunos.pop(0)
        media = lambda notas: sum([int(c) for c in notas])/4
        lista_media.append({nmaluno:media(dadosalunos)})
    arquivo.close()
    return lista_media

def copia_arquivo(nmarquivo):
    shutil.copy(nmarquivo,"c:/temp/notas_alunos2.txt")

def mover_arquivo(nmarquivo):
    shutil.move(nmarquivo, "c:/temp/")

if __name__ == '__main__':
    copia_arquivo('notas_alunos.txt')
    mover_arquivo('notas_alunos2.txt')
    #escrever_arquivo('teste.txt','Este e meu primeiro teste de arquivo')

    # import os
    # os.remove('notas_alunos.txt')

    escrever_arquivo('notas_alunos.txt','Leonardo Ferreira,05,10,15,20')
    atualizar_arquivo('notas_alunos.txt', '\nAndréia Vignatti,10,15,20,25')
    atualizar_arquivo('notas_alunos.txt', '\nArthur Vignatti,15,20,25,30')
    atualizar_arquivo('notas_alunos.txt', '\nGabriel Vignatti,20,25,30,35')

    ler_arquivo('notas_alunos.txt')
    lista_media = media_notas('notas_alunos.txt')

    print(lista_media)