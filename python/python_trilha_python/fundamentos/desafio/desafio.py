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

# Constante
LIMITE_SAQUES = 3

#Variáveis

saldo = 0
saques = 0
limite = 500
extrato = ""


while True:

    opc = input(menu)
    
    match opc:
        case "d":
            valor = float(input("Valor a depositar: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                #return extrato
            else:
                print("Atenção!\n Não é possível cadastrar valor nulo ou negativo!")
        case "s":
            if (saldo == 0):
                print("Atenção!\n Saldo insuficiente para retirada")
            else:
                valor = float(input("Valor a sacar: "))
                
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = saques >= LIMITE_SAQUES
                if excedeu_saldo:
                   print("Atenção!\n Saldo insuficiente para a realização desta operação.\nVocê só pode sacar até {}".format(saldo))

                elif excedeu_limite:
                    print("Atenção!\nO limite desta operação é de {} por operação, limitada a {} diárias.".format(limite,LIMITE_SAQUES))

                elif excedeu_saques:
                    print("Atenção!\nLimite de saques diário de {} por dia atingido.".format(limite))

                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    saques += 1
                else:
                   print("Atenção!\nValor informado inválido")
        case "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
        case "q":
            break
        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")