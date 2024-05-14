lista_contas = []


def criar_conta_corrente(agencia, usuario):
    conta = {
        "agencia": agencia,
        "numero": "{:04d}".format(len(lista_contas) + 1),
        "usuario": usuario,
    }

    for element in [*lista_contas]:
        if usuario != element.get("usuario"):
            lista_contas.append(conta)
