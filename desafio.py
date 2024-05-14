from deposito import deposito
from extrato import print_extrato
from saque import saque


MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        SALDO, EXTRATO = deposito(SALDO, valor, EXTRATO)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        SALDO, EXTRATO = saque(
            extrato=EXTRATO,
            saldo=SALDO,
            limite=LIMITE,
            limite_saques=LIMITE_SAQUES,
            numero_saques=NUMERO_SAQUES,
            valor=valor
        )
    elif opcao == "e":
        print_extrato(SALDO, extrato=EXTRATO)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a "
              "operação desejada.")
