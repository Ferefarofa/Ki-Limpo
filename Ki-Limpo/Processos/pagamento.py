import sqlite3
from banco import pagamentos


def forma_pagamento():
    while True:
        print("\
        \n====================================================================\
        \nPAGAMENTO\
        \n1 - Cartão de Crédito\
        \n2 - Cartão de Débito\
        \n3 - Pix\
        \n====================================================================")

        opcao = input("Escolha: ")

        if opcao == "1":
            return "Cartão de Crédito"
        elif opcao == "2":
            return "Cartão de Débito"
        elif opcao == "3":
            return "Pix"
        else:
            print("Opção inválida!")


def pagamento_realizado(id_cliente, id_pedido):
    pagamentos()
    forma = forma_pagamento()

    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pagamentos (id_cliente, id_pedido, forma_pagamento, data_pagamento) VALUES (?, ?, ?, ?)",
        (id_cliente, id_pedido, forma, "hoje"),
    )

    conexao.commit()
    conexao.close()

    print("Pagamento realizado com sucesso!")
