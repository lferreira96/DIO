nome = input("Nome: ")
idade = int(input("Idade: "))
sexo = input("Sexo: ")
estado_civil = input("Estado Civil: ")

msg_idade = " maior de idade " if idade >= 18 else " menor de idade "

#if idade >= 18:
#    msg_idade = " maior de idade "
#else:
#    msg_idade = " menor de idade "

match estado_civil.upper():
    case "C":
        msg_ec = " é casad"
    case "S":
        msg_ec = " é solteir"
    case "V":
        msg_ec = " é viúv"
    case "D":
        msg_ec = " é divorciad"
    case _:
        msg_ec = " não definiu seu estado civil "

match sexo.upper():
    case "M":
        msg_sexo = " do sexo masculino "
        msg_ec+="o "
    case "F":
        msg_sexo = " do sexo feminino "
        msg_ec+="a "
    case _:
        msg_sexo = " não definiu seu sexo "

mensagem_final = f"{nome} você é {msg_idade}, {msg_sexo} e {msg_ec}"

print(mensagem_final)