# Os dicionários são compostos por <chaves>:<valores>
# podendo as chaves serem numéricas ou alfanuméricas

dc = {3:"Leonardo",4:"Arthur",1:"Gabriel",2:"Andréia"}
print(dc)
dc[3] = "Leonardo Ferreira"
print(dc)

# Retornando as chaves do dicionário
print (dc.keys())

# Retornando os vamores do dicionário
print (dc.values())

# Inserindo uma nova chave e valor para o dicionário

dc.setdefault(5,"Lavinia")
print (dc)
