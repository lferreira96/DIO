table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone, in table.items():
    print(f'{name:10} ==> {phone:10d}')

#══════════════════════════════════════════════════
nome = "Leonardo Ferreira"
idade = 46
profissao = "Progamador"
linguagem = "Python"

pessoa = {"nome": "Leonardo Ferreira","idade" : 46,"profissao" : "Progamador","linguagem" : "Python"}



# não é mais utilizado
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#══════════════════════════════════════════════════
#pouco utilizado ou não utilizado
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))


#══════════════════════════════════════════════════
#foram criados os identificadores inome, iidade, iprofissao, ilinguagem para receber o valor das variáveis e ser colocado no local que precisa
print("Olá, me chamo {inome}. Eu tenho {iidade} anos de idade, trabalho como {iprofissao} e estou matriculado no curso de {ilinguagem}.".format(inome=nome, iidade=idade, iprofissao=profissao, ilinguagem=linguagem))


#
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

#══════════════════════════════════════════════════

# Este é o método usado hoje, uma vez que não é necessário especificar nada no final, somente no local correto
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

#══════════════════════════════════════════════════

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")


#══════════════════════════════════════════════════
#══════════════════════════════════════════════════
#══════════════════════════════════════════════════