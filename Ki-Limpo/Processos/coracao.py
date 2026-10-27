import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()


from login import login_cliente
from cadastro_cliente import cadastro_cliente

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
        print("\
\n====================================================================\
\nOLÁ CLIENTE, SELECIONA UMA OPÇÃO: \
\n1 - FAZER LOGIN\
\n2 - CADASTRAR\
\n====================================================================")
        opcao = int(input("Escolha: "))
        if opcao == 1:
            cliente = login_cliente()
        elif opcao == 2:
            cadastro_cliente()
            print("\
\n====================================================================\
\nVocê foi encaminhado para o login...")
            cliente = login_cliente()

    elif opcao == 2:
        print("oi")

    print(f"\
\n====================================================================\
\nBEM VINDO(A) {cliente[1]}\
\n====================================================================")
    print("====================================================================\
\nEscolha a opção de serviço:\
\n1 - Lavar e secar\
\n2 - Lavar, secar e passar\
\n3 - Lavagem a seco\
\n4 - Sair\
\n====================================================================")

inicio()

def menu():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    opcao = int(input("digite a sua opção: "))

    if opcao == 1:
        print("Opção selecionada: lavar e secar")
    elif opcao == 2:
        print("Opção selecionada: lavar, secar e passar")
    elif opcao == 3:
        print("Opção selecionada: lavagem a seco")
    else:
        print("Saindo...")
menu()