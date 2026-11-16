import sqlite3
from banco import pagamentos, pedidos





def pagamento():
    criar_tabela_pagamentos()
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT id, id_cliente, id_pedido, forma_pagamento, data_pagamento 
        FROM pagamentos
    ''')

    fazer_pagamentos = cursor.fetchall()

def forma_pagamento():
    while True:
        print(
            "\n====================================================================\n"
            "PAGAMENTO\n"
            "====================================================================\n"
            "1 - Cartão de Crédito\n"
            "2 - Cartão de Débito\n"
            "3 - Pix\n"
            "===================================================================="
        )

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            return "Cartão de Crédito"
        elif opcao == "2":
            return "Cartão de Débito"
        elif opcao == "3":
            return "Pix"
        else:
            print("Opção inválida. Tente novamente.")


def pagamento_realizado(id_cliente, id_pedido, valor, forma_pagamento_escolhida):
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO pagamentos (id_cliente, id_pedido, forma_pagamento, data_pagamento)
            VALUES (?, ?, ?, date('now'))
            """,
            (id_cliente, id_pedido, forma_pagamento_escolhida),
        )
        conexao.commit()
        print(f"Pagamento realizado com sucesso para o cliente {id_cliente}.")
        return True
    finally:
        conexao.close()
