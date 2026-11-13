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
        print("\
        \n====================================================================\
        \nPAGAMENTO\
        \n===================================================================\
        \n1 - Cartão de Crédito\
        \n2 - Cartão de Débito\
        \n3 - Pix\\
        \n====================================================================\
        ")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        return "Cartão de Crédito"

    elif opcao == "2":
        return "Cartão de Débito"

    elif opcao == "3":
        return "Pix"

    else:
        print("Opção inválida. Tente novamente.")



def pagamento_realizado(id_cliente, id_pedido, valor):
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pagamentos WHERE id_cliente = ?", (id_cliente,))
    pedido = cursor.fetchone()

    cursor.execute("UPDATE pagamentos SET total = ? WHERE id_cliente = ?", (valor, id_cliente))

    print(f"valor pago pelo cliente {id_cliente} aceito com sucesso.")

    conexao.commit()
    conexao.close()
