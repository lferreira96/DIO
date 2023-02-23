'''
Depósito:
    - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato

Saque:
    - No máximo 03 saques diários com limite de 500 por saque
    - Informar que não será possível sacar o dinheiro por falta de saldo
    - Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato

Extrato:
    - Deve listar todas os depósitos e saques realizados na conta.
    - No fim da listagem deve ser exibido o saldo atual da conta.
    - Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
    1500.45  ->  R$ 1500.45

'''

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0

numero_saques = 0

limite = 500
extrato = ""


LIMITE_SAQUES = 3

while True:

    opc = input(menu)
    
    if opc == "d":
        valor = float(input("Valor a depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            #return extrato
        else:
            print("Valor informado inválido.\nOpecação Cancelada!")

        
    elif opc == "s":
        if (saldo == 0):
            print("Você não tem saldo para a realização desta operação.\nOperação Cancelada!")
        else:
            valor = float(input("Valor a sacar: "))
            
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Saldo insuficiente para a realização desta operação.\nVocê só pode sacar até {}\nOperação Cancelada!".format(valor-saldo))

            elif excedeu_limite:
                print("O limite desta operação é de {} por operação, limitada a {} diárias.\nOperação Cancelada!".format(limite,LIMITE_SAQUES))

            elif excedeu_saques:
                print("Limite de saques diário de {} por dia atingido.\nOperação Cancelada!".format(limite))

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Valor informado inválido.\nOperação Cancelada!")

    elif opc == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opc == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")