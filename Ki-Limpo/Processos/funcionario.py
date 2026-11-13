import sqlite3
from login import login_funcionario
from cadastros import cadastrar_funcionario

def funcionario_menu():
    print("\
    \n====================================================================\
    \nOLÁ FUNCIONÁRIO, SELECIONA UMA OPÇÃO: \
    \n1 - FAZER LOGIN\
    \n2 - CADASTRAR\
    \n====================================================================")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        funcionario = login_funcionario()
    elif opcao == 2:
        cadastrar_funcionario()
        print("\
    \n====================================================================\
    \nVocê foi encaminhado para o login...")
        funcionario = login_funcionario()
    else:
        print("Opção inválida.")
        return
    print(f"\
    \n====================================================================\
    \nBEM VINDO(A) {funcionario[1]}\
    \n====================================================================")
    return funcionario

def visualizar_pedidos():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT id, id_cliente, servico, roupa, quantidade, intensidade,
        preferencia_produtos, fragrancia,funcionario, atendimento, urgencia,
        total, observacao, status, horario, data
        FROM pedidos WHERE status =?
    ''', ('pendente',))

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
            print(f"Atendimento: {pedido[9]}")
            print(f"Urgência: {pedido[10]}")
            print(f"Total: R$ {pedido[11]}")
            print(f"Observação: {pedido[12]}")
            print(f"Status: {pedido[13]}")
            print(f"Horário: {pedido[14]}")
            print(f"Data: {pedido[15]}")
            print(f"Funcionário: {pedido[8]}")
            print("============================")

    conexao.close()

def menu_funcionario(funcionario):
    while True:
        print("\
        \n====================================================================\
              \nÁREA DO FUNCIONÁRIO\
        \n===================================================================\
        \n1 - Visualizar pedidos pendentes\
        \n2 - Visualizar pedidos em andamento\
        \n3 - Visualizar pedidos finalizados\
        \n4 - Aceitar pedido\
        \n5 - Recusar pedido\
        \n6 - Finalizar pedido\
        \n7 - Sair\
        \n====================================================================\
        ")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_pedidos()

        elif opcao == "2":
            visualizar_pedidos_andamento()

        elif opcao == "3":
            visualizar_pedidos_finalizados()

        elif opcao == "4":
            aceitar_pedido(funcionario[1])  # Passando o nome do funcionário para a função aceitar_pedido

        elif opcao == "5":
            recusar_pedido()

        elif opcao == "6":
            finalizar_pedido()

        elif opcao == "7":
            print("Saindo da área do funcionário...")
            break

        else:
            print("Opção inválida!")

def aceitar_pedido(funcionario):
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_pedido = input("Digite o ID do pedido para aceitar: ")

    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (id_pedido,))
    pedido = cursor.fetchone()

    cursor.execute("UPDATE pedidos SET status = 'aceito' WHERE id = ?", (id_pedido,))

    cursor.execute(
    "UPDATE pedidos SET funcionario = ? WHERE id = ?",
    (funcionario, id_pedido)
    )
    conexao.commit()

    print(f"Pedido {id_pedido} aceito com sucesso.")

    conexao.close()

def finalizar_pedido():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_pedido = input("Digite o ID do pedido para finalizar: ")

    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (id_pedido,))
    pedido = cursor.fetchone()

    if pedido:
        cursor.execute("UPDATE pedidos SET status = 'finalizado' WHERE id = ?", (id_pedido,))
        conexao.commit()
        print(f"Pedido {id_pedido} finalizado com sucesso.")
    else:
        print(f"Pedido {id_pedido} não encontrado.")

    conexao.close()

def recusar_pedido():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_pedido = input("Digite o ID do pedido para recusar: ")

    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (id_pedido,))
    pedido = cursor.fetchone()

    
    if pedido:
        observacao = input("Digite o motivo da recusa do pedido: ")
        cursor.execute("UPDATE pedidos SET status = 'recusado', observacao = ? WHERE id = ?", (observacao, id_pedido))
        conexao.commit()

        print(f"Pedido {id_pedido} recusado com sucesso.")

    else:
        print(f"Pedido {id_pedido} não encontrado.")



    conexao.close()

def visualizar_pedidos_andamento():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT id, id_cliente, servico, roupa, quantidade, intensidade,
        preferencia_produtos, fragrancia,funcionario, atendimento, urgencia,
        total, observacao, status, horario, data
        FROM pedidos WHERE status = ?''',
        ('aceito',)
    )

    pedidos = cursor.fetchall()

    if not pedidos:
        print("\nNenhum pedido em andamento encontrado.")
    else:
        for pedido in pedidos:
            print("\n========== PEDIDOS EM ANDAMENTO ==========")
            print(f"ID do Pedido: {pedido[0]}")
            print(f"ID do Cliente: {pedido[1]}")
            print(f"Serviço: {pedido[2]}")
            print(f"Roupa: {pedido[3]}")
            print(f"Quantidade: {pedido[4]}")
            print(f"Intensidade: {pedido[5]}")
            print(f"Produtos: {pedido[6]}")
            print(f"Fragrância: {pedido[7]}")
            print(f"Atendimento: {pedido[9]}")
            print(f"Urgência: {pedido[10]}")
            print(f"Total: R$ {pedido[11]}")
            print(f"Observação: {pedido[12]}")
            print(f"Status: {pedido[13]}")
            print(f"Horário: {pedido[14]}")
            print(f"Data: {pedido[15]}")
            print(f"Funcionário: {pedido[8]}")
            print("=========================================")

    conexao.close()

def visualizar_pedidos_finalizados():

    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT id, id_cliente, servico, roupa, quantidade, intensidade,
        preferencia_produtos, fragrancia,funcionario, atendimento, urgencia,
        total, observacao, status, horario, data
        FROM pedidos WHERE status = ?''',
        ('finalizado',)
    )

    pedidos = cursor.fetchall()

    if not pedidos:
        print("\nNenhum pedido finalizado encontrado.")
    else:
        for pedido in pedidos:
            print("\n========== PEDIDOS FINALIZADOS ==========")
            print(f"ID do Pedido: {pedido[0]}")
            print(f"ID do Cliente: {pedido[1]}")
            print(f"Serviço: {pedido[2]}")
            print(f"Roupa: {pedido[3]}")
            print(f"Quantidade: {pedido[4]}")
            print(f"Intensidade: {pedido[5]}")
            print(f"Produtos: {pedido[6]}")
            print(f"Fragrância: {pedido[7]}")
            print(f"Atendimento: {pedido[9]}")
            print(f"Urgência: {pedido[10]}")
            print(f"Total: R$ {pedido[11]}")
            print(f"Observação: {pedido[12]}")
            print(f"Status: {pedido[13]}")
            print(f"Horário: {pedido[14]}")
            print(f"Data: {pedido[15]}")
            print(f"Funcionário: {pedido[8]}")
            print("=========================================")

    conexao.close()
