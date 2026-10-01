import sqlite3

CAMINHO_BANCO = "Ki-Limpo/dados_lavanderia.db"


def conectar():
    # Abre o banco e devolve a conexão e o cursor
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    return conexao, cursor


def entrar_clube():
    conexao, cursor = conectar()

    cpf_cliente = input("Digite o CPF do cliente: ")

    cursor.execute(
        "SELECT id, nome_cliente, cpf_cliente, clube FROM clientes WHERE cpf_cliente = ?",
        (cpf_cliente,),
    )
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        conexao.close()
        return

    id_cliente, nome_cliente, cpf, clube = cliente

    if clube == 1:
        print(nome_cliente, "já faz parte do clube!")
        conexao.close()
        return

    cursor.execute(
        "INSERT INTO clube (cliente, cpf_cliente, id_cliente) VALUES (?, ?, ?)",
        (nome_cliente, cpf, id_cliente),
    )

    cursor.execute("UPDATE clientes SET clube = 1 WHERE id = ?", (id_cliente,))

    conexao.commit()
    conexao.close()
    print(nome_cliente, "entrou no clube com sucesso!")


def sair_clube():
    conexao, cursor = conectar()

    cpf_cliente = input("Digite o CPF do cliente: ")

    cursor.execute(
        "SELECT id, nome_cliente, clube FROM clientes WHERE cpf_cliente = ?",
        (cpf_cliente,),
    )
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado.")
        conexao.close()
        return

    id_cliente, nome_cliente, clube = cliente

    if clube != 1:
        print(nome_cliente, "não faz parte do clube.")
        conexao.close()
        return

    cursor.execute("DELETE FROM clube WHERE id_cliente = ?", (id_cliente,))
    cursor.execute("UPDATE clientes SET clube = 2 WHERE id = ?", (id_cliente,))

    conexao.commit()
    conexao.close()
    print(nome_cliente, "saiu do clube.")


def verificar_clube():

    conexao, cursor = conectar()

    cpf_cliente = input("Digite o CPF do cliente: ")

    cursor.execute(
        "SELECT nome_cliente, clube FROM clientes WHERE cpf_cliente = ?", (cpf_cliente,)
    )
    cliente = cursor.fetchone()
    conexao.close()

    if cliente is None:
        print("Cliente não encontrado.")
    elif cliente[1] == 1:
        print(cliente[0], "é membro do clube.")
    else:
        print(cliente[0], "não é membro do clube.")


def listar_membros():
    conexao, cursor = conectar()

    cursor.execute("SELECT cliente, cpf_cliente FROM clube")
    membros = cursor.fetchall()
    conexao.close()

    if len(membros) == 0:
        print("Nenhum membro no clube ainda.")
        return

    print("--- Membros do clube ---")
    for membro in membros:
        print("Nome:", membro[0], "| CPF:", membro[1])


def menu_clube():
    while True:
        print()
        print("=== CLUBE DA LAVANDERIA ===")
        print("1 - Entrar no clube")
        print("2 - Sair do clube")
        print("3 - Verificar se é membro")
        print("4 - Listar membros")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            entrar_clube()
        elif opcao == "2":
            sair_clube()
        elif opcao == "3":
            verificar_clube()
        elif opcao == "4":
            listar_membros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente de novo.")


if __name__ == "__main__":
    menu_clube()
