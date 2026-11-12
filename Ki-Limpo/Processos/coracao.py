import sqlite3

conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()


from login import login_cliente, login_funcionario
from cadastros import cadastrar_cliente, cadastrar_funcionario
from banco import banco_cliente, banco_funcionario,pedidos
from cliente import cliente_menu, servico, roupa_e_quantidade, intensidade, preferencia_produtos, fragrancia, atendimento, urgencia, total, observacao, executar, pedidos_realizados
pedidos()
def inicio():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    print(f"\
\n====================================================================\
\nBEM VINDO AO KI-LIMPO SYSTEM\
\nSELECIONA UMA DAS OPÇÕES:\
\n1 - SOU CLIENTE\
\n2 - SOU FUNCIONÁRIO\
\n====================================================================")
    tipo = int(input("Escolha: "))

    if tipo == 1:
        executar()
        pedidos_realizados()

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
        print(f"\
\n====================================================================\
\nBEM VINDO(A) {funcionario[1]}\
\n====================================================================")


inicio()
