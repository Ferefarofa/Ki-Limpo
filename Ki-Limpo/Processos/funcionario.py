import sqlite3

def visualizar_pedidos():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_cliente, servico, roupa, quantidade, intensidade,
        preferencia_produtos, fragrancia, atendimento, urgencia,
        total, observacao
        FROM pedidos
    """)

    pedidos = cursor.fetchall()

    if not pedidos:
    print("\nNenhum pedido encontrado.")
        print("\nNenhum pedido encontrado.")
    else:
        for pedido in pedidos:
            print("\n========== PEDIDO ==========")
            print(f"ID do Cliente: {pedido[0]}")
            print(f"Serviço: {pedido[1]}")
            print(f"Roupa: {pedido[2]}")
            print(f"Quantidade: {pedido[3]}")
            print(f"Intensidade: {pedido[4]}")
            print(f"Produtos: {pedido[5]}")
            print(f"Fragrância: {pedido[6]}")
            print(f"Atendimento: {pedido[7]}")
            print(f"Urgência: {pedido[8]}")
            print(f"Total: R$ {pedido[9]:.2f}")
            print(f"Observação: {pedido[10]}")
            print("============================")

    conexao.close()

def menu_funcionario():
    while True:
        print("\
        ====================================================================\
              ÁREA DO FUNCIONÁRIO\
        ====================================================================\
        1 - Visualizar pedidos\
        2 - Aceitar pedido\
        3 - Recusar pedido\
        4 - Sair\
        ====================================================================\
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

    id_cliente = input("Digite o ID do cliente para aceitar o pedido: ")

    cursor.execute("SELECT * FROM pedidos WHERE id_cliente = ?", (id_cliente,))
    pedido = cursor.fetchone()

    cursor.execute("UPDATE pedidos SET status = 'aceito' WHERE id_cliente = ?", (id_cliente,))

    conexao.close()

def recusar_pedido():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_cliente = input("Digite o ID do cliente para recusar o pedido: ")

    cursor.execute("SELECT * FROM pedidos WHERE id_cliente = ?", (id_cliente,))
    pedido = cursor.fetchone()

    cursor.execute("UPDATE pedidos SET status = 'recusado' WHERE id_cliente = ?", (id_cliente,))


    conexao.close()


menu_funcionario()

