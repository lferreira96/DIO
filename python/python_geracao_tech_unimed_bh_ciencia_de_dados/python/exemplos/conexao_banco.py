# Importando a biblioteca pandas responsável pela conexão com os dados
# importando a biblioteca pandas para dentro da variável pd
# instanciando os dados

import pandas as pd

# Conjunto de dados que será utilizado pelo programa (Linhas e colunas)
# Criando a ligação ao arquivo dataFrame com o arquivo de dados que será lido no caminho especificado em pd.read_csv
# sep=";" estou indicando que o separador de campos será o ;
dataFrame = pd.read_csv("D:\estudos\Dev\GitHub\DIO\geracao-tech-unimed-bh-ciencia-de-dados\python\exemplos\dados\dados.csv",sep=";")

# O Comando rename vai permitir renomear as colunas, porém, é necessário colocar inplace=True
dataFrameme = dataFrame.rename(columns = {"country" : "Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Exp_Vida", "pop":"Populacao", "gdpPercap":"PIB"},inplace = True)

# Head() vai ler as informações
dataFrame.head