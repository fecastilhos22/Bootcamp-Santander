menu = """
============== MENU ============

D - Depositar
S - Sacar
E - Extrato
O - Sair
      
 ================================

 Obrigada por usar nosso sistema!!

=> """

saldo = 0
estrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUE_DIARIO = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Digite o valor que você deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Não foi possível realizar o depósito. O valor informado não é válido.Tente novamente!")
            
    elif opcao == "S":
        valor = float(input("Digite o valor que você deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE_DIARIO

        if excedeu_saldo:
            print("Não foi possível realizar o saque!Saldo insuficiente!")
        elif excedeu_limite:
            print(
                "Não foi possível realizar o saque!Você excedeu o limite do valor de saque diário!"
            )
        elif excedeu_saques:
            print(
                "Não foi possível realizar o saque!Você excedeu o limite de saques diário!"
            )
        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print(
                "Não foi possível realizar o saque. O valor informado não é válido.Tente novamente!"
            )
    elif opcao == "E":
        print("\n================ EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "O":
        print("Obrigada por usar nosso sistema bancário, até logo!")
        break
else:
    print("Opção inválida, selecione novamente a opção desejada!")

