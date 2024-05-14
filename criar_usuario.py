lista_usuario = []


def criar_usuario(nome, data_nascimento, cpf, endereco):
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereco
    }

    for user in [*lista_usuario]:
        if usuario.get("cpf") != user.get("cpf"):
            lista_usuario.append(user)
