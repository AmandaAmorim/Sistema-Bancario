menu = """
    Bem vindo ao Sistema Bancário!
    Digite o número da opção desejada: 
    1. Depositar
    2. Sacar
    3. Extrato 
    4. Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = 0  

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            depositos += 1
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if 0 < valor <= saldo and numero_saques < LIMITE_SAQUES and valor <= limite:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saque inválido. Verifique o saldo, limite ou número de saques.")

    elif opcao == "3":
        print("Extrato:")
        print(extrato if extrato else "Nenhuma transação realizada.")
        print("Saldo atual: R$ {:.2f}".format(saldo))
        print("Número de saques realizados: {}".format(numero_saques))
        print("Número de depósitos realizados: {}".format(depositos))
       
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        print("\n" + menu)  # Reexibir o menu após cada operação