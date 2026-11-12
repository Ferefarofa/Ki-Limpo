
import sqlite3

def visualizar_pedidos():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, id_cliente, servico, roupa, quantidade, intensidade,
        preferencia_produtos, fragrancia, atendimento, urgencia,
        total, observacao
        FROM pedidos
    """)

    pedidos = cursor.fetchall()

    if not pedidos:
        print("\nNenhum pedido encontrado.")
    else:
        for pedido in pedidos:
            print("\n========== PEDIDO ==========")
            print(f"ID do Pedido: {pedido[0]}")
            print(f"ID do Cliente: {pedido[1]}")
            print(f"Serviço: {pedido[2]}")
            print(f"Roupa: {pedido[3]}")
            print(f"Quantidade: {pedido[4]}")
            print(f"Intensidade: {pedido[5]}")
            print(f"Produtos: {pedido[6]}")
            print(f"Fragrância: {pedido[7]}")
            print(f"Atendimento: {pedido[8]}")
            print(f"Urgência: {pedido[9]}")
            print(f"Total: R$ {pedido[10]}")
            print(f"Observação: {pedido[11]}")
            print("============================")

    conexao.close()

def menu_funcionario():
    while True:
        print("\
        \n====================================================================\
              \nÁREA DO FUNCIONÁRIO\
        \n===================================================================\
        \n1 - Visualizar pedidos\
        \n2 - Aceitar pedido\
        \n3 - Recusar pedido\
        \n4 - Sair\
        \n====================================================================\
        ")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_pedidos()

        elif opcao == "2":
            aceitar_pedido()

        elif opcao == "3":
            recusar_pedido()

        elif opcao == "4":
            print("Saindo da área do funcionário...")
            break

        else:
            print("Opção inválida!")

def aceitar_pedido():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_cliente = input("Digite o ID do pedido para aceitar: ")

    cursor.execute("SELECT * FROM pedidos WHERE id_cliente = ?", (id_cliente,))
    pedido = cursor.fetchone()

    cursor.execute("UPDATE pedidos SET status = 'aceito' WHERE id_cliente = ?", (id_cliente,))

    print(f"Pedido do cliente {id_cliente} aceito com sucesso.")

    conexao.commit()
    conexao.close()


def recusar_pedido():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_cliente = input("Digite o ID do pedido para recusar: ")

    cursor.execute("SELECT * FROM pedidos WHERE id_cliente = ?", (id_cliente,))
    pedido = cursor.fetchone()

    
    if pedido:
        observacao = input("Digite o motivo da recusa do pedido: ")
        cursor.execute("UPDATE pedidos SET status = 'recusado', observacao = ? WHERE id_cliente = ?", (observacao, id_cliente))
        conexao.commit()

        print(f"Pedido do cliente {id_cliente} recusado com sucesso.")

    else:
        print(f"Pedido do cliente {id_cliente} não encontrado.")



    conexao.close()


menu_funcionario()