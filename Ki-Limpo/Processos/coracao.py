import sqlite3

from login import login_cliente, login_funcionario
from cadastros import cadastrar_cliente, cadastrar_funcionario
from banco import banco_cliente, banco_funcionario,pedidos
from cliente import cliente_menu, servico, roupa_e_quantidade, intensidade, preferencia_produtos, fragrancia, atendimento, urgencia, total, observacao, executar, pedidos_realizados
from funcionario import funcionario_menu, menu_funcionario, visualizar_pedidos, visualizar_pedidos_andamento, visualizar_pedidos_finalizados, aceitar_pedido, recusar_pedido, finalizar_pedido

pedidos()

def inicio():
    try:
        print(f"\
\n====================================================================\
\nBEM VINDO AO KI-LIMPO SYSTEM\
\nSELECIONA UMA DAS OPÇÕES:\
\n1 - SOU CLIENTE\
\n2 - SOU FUNCIONÁRIO\
\n====================================================================")
        tipo = int(input("Escolha: "))

        if tipo == 1:
            dados_pedido = executar()
            if dados_pedido == None:
                print("Nenhum pedido realizado.")
            else:
                pedidos_realizados(dados_pedido)

        elif tipo == 2:
            funcionario = funcionario_menu()
            menu_funcionario(funcionario)
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        inicio()
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    finally:
        print("Programa finalizado.")

inicio()
