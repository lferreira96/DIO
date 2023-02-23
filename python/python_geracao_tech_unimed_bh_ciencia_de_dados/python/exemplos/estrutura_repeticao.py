# Dados de entrada
textos = input("Entre com uma palavra: ")
VOGAIS = "AEIOU"

# Inicialização das variáveis

qtd_a=0
qtd_e=0
qtd_i=0
qtd_o=0
qtd_u=0
qtd_naovogais = 0
# Processamento

for letra in textos:
    if letra.upper() in VOGAIS:
        match letra.upper():
            case "A":
                qtd_a+=1
            case "E":
                qtd_e+=1
            case "I":
                qtd_i+=1
            case "O":
                qtd_o+=1
            case "U":
                qtd_u+=1
    else:
        qtd_naovogais+=1
else:
    if len(textos) == 0:
        # Caso não seja digitado nada
        
        print("Não foi digitado nada")  

    else:
        # Saída das informações

        print("══════════════════════════════════════")
        print(f"Quantidade de letras 'A'...: {qtd_a}")
        print(f"Quantidade de letras 'E'...: {qtd_e}")
        print(f"Quantidade de letras 'I'...: {qtd_i}")
        print(f"Quantidade de letras 'O'...: {qtd_o}")
        print(f"Quantidade de letras 'U'...: {qtd_u}")
        print("══════════════════════════════════════")
        print(f"Quantidade de outras letras: {qtd_naovogais}")
        print("══════════════════════════════════════")
        print(f"Total de letras............: {len(textos)}")