import sqlite3

from login import login_cliente, login_funcionario
from cadastros import cadastrar_cliente, cadastrar_funcionario
from banco import banco_cliente, banco_funcionario,pedidos
from cliente import cliente_menu, servico, roupa_e_quantidade, intensidade, preferencia_produtos, fragrancia, atendimento, urgencia, total, observacao, executar, pedidos_realizados

def inicio():
    try:
        pedidos()
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
            pedidos_realizados(dados_pedido)

        elif tipo == 2:
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
