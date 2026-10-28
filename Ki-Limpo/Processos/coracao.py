import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()


from login import login_cliente, login_funcionario
from cadastros import cadastrar_cliente, cadastrar_funcionario

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
            cadastrar_cliente()
            print("\
\n====================================================================\
\nVocê foi encaminhado para o login...")
            cliente = login_cliente()
        print(f"\
\n====================================================================\
\nBEM VINDO(A) {cliente[1]}\
\n====================================================================")



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

    opcao_menu = int(input("digite a sua opção: "))

    if opcao_menu == 1:
        print("Opção selecionada: lavar e secar")
    elif opcao_menu == 2:
        print("Opção selecionada: lavar, secar e passar")
    elif opcao_menu == 3:
        print("Opção selecionada: lavagem a seco")
    else:
        print("Saindo...")
menu()

def roupa_e_quantidade():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    roupa = []
    while True:

        print(f"\
\nEscolha as opções equivalentes as suas peças:\
\n1 - Vestido\
\n2 - Peças jeans (vestido, jaqueta, calça, etc)\
\n3 - Camisas\
\n4 - Camisetas\
\n5 - Moletom (calças, casacos, etc)\
\n6 - Peças de baixo\
\n====================================================================")

        opcao = int(input("digite a sua opção: "))

        if opcao_roupa == 1:
            print("Opção selecionada: Vestido")
        elif opcao_roupa == 2:
            print("Opção selecionada: Peças jeans")
        elif opcao_roupa == 3:
            print("Opção selecionada: Camisas")
        elif opcao_roupa == 4:
            print("Opção selecionada: Camisetas")
        elif opcao_roupa == 5:
            print("Opção selecionada: Moletom")
        elif opcao_roupa == 6:
            print("Opção selecionada: Peças de baixo")
        else:
            break

        quantidade = []

        quantidade = int(input("Digite a quantidade de peças: "))
        print(f"Quantidade de peças: {quantidade}")
    roupa_e_quantidade()

def intensidade():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    intensidade = int(input("Digite a intensidade da lavagem: "))
    print(f"Intensidade da lavagem: {intensidade}")
intensidade()

def preferencia_produtos():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    while True:

        print(f"\
\nEscolha as opções de detergentes e sabões:\
\n1 - Sabão regular (em pó)\
\n2 - Sabão líquido\
\n3 - Detergente concentrado\
\n4 - Sabão neutro para roupas delicadas\
\n5 - Sabão específico para roupas infantis\
\n6 - Detergente para roupas brancas ou coloridas\
\n7 - Sair\
\n====================================================================")
        opcao = int(input("digite a sua opção: "))

        if opcao_detergente == 1:
            print("Opção selecionada: Sabão regular (en pó)")
        elif opcao_detergente == 2:
            print("Opção selecionada: Sabão líquido")
        elif opcao_detergente == 3:
            print("Opção selecionada: Detergente concentrado")
        elif opcao_detergente == 4:
            print("Opção selecionada: Sabão neutro para roupas delicadas")
        elif opcao_detergente == 5:
            print("Opção selecionada: Sabão específico para roupas infantis")
        elif opcao_detergente == 6:
            print("Opção selecionada: Detergente para roupas brancas ou coloridas")
        else:
            break
        print("\n====================================================================")

        print("\
\nEscolha as opções de Amaciantes:\
\n1 - Amaciante convencional\
\n2 - Amaciante concentrado\
\n3 - Amaciante hipoalergênico ou sem perfume\
\n4 - Sair\
\n====================================================================")

        opcao_amaciante = int(input("digite a sua opção: "))

        if opcao_amaciante == 1:
            print("Opção selecionada: Amaciante convencional")
        elif opcao_amaciante == 2:
            print("Opção selecionada: Amaciante concentrado")
        elif opcao_amaciante == 3:
            print("Opção selecionada: Amaciante hipoalergênico ou sem perfume")
        else:
            print("Saindo...")
        print("\n====================================================================")

        print(f"\
\nEscolha as opções de Produtos auxiliares de lavagem:\
\n1 - Desengorduranes têxteis\
\n2 - Reforçadores de detergência\
\n3 - Produtos para remoção de manchas difíceis\
\n4 - Sair\
\n====================================================================")

        opcao_produto_auxiliar = int(input("digite a sua opção: "))

        if opcao_produto_auxiliar == 1:
            print("Opção selecionada: Desengordurantes têxteis")
        elif opcao_produto_auxiliar == 2:
            print("Opção selecionada: Reforçadores de detergência")
        elif opcao_produto_auxiliar == 3:
            print("Opção selecionada: Produtos para remoção de manchas difíceis")
        else:
            print("Saindo...")
preferencia_produtos()

def fragrancia():
    print("\n====================================================================")

    print(f"\
\nEscolha as opções de fragrancia:\
\n1 - Algodão\
\n2 - Lavanda\
\n3 - Cítrico\
\n4 - Jasmin\
\n5 - Rosas\
\n6 - Eucalipto\
\n7 - Baunilha\
\n8 - Brisa do mar\
\n9 - Musk\
\n10 - Talco\
\n11 - Sem fragrância\
\n====================================================================")

    opcao_fragrancia = int(input("digite a sua fragrância: "))

    if opcao_fragrancia == 1:
        print("Opção selecionada: Algodão")
    elif opcao_fragrancia == 2:
        print("Opção selecionada: Lavanda")
    elif opcao_fragrancia == 3:
        print("Opção selecionada: Cítrico")
    elif opcao_fragrancia == 4:
        print("Opção selecionada: Jasmin")
    elif opcao_fragrancia == 5:
        print("Opção selecionada: Rosas")
    elif opcao_fragrancia == 6:
        print("Opção selecionada: Eucalipto")
    elif opcao_fragrancia == 7:
        print("Opção selecionada: Baunilha")
    elif opcao_fragrancia == 8:
        print("Opção selecionada: Brisa do mar")
    elif opcao_fragrancia == 9:
        print("Opção selecionada: Musk")
    elif opcao_fragrancia == 10:
        print("Opção selecionada: Talco")
    else:
        print("Opção selecionada: Sem fragrância")
fragrancia()

def funcionario():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    funcionario_op = funcionario[1] 
    print(f"Funcionário: {funcionario}")
funcionario()


def urgencia():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    
    while True:
        print("\n====================================================================")

        print(f"\
\nEscolha as opções de fragrancia:\
\n1 - Normal (prazo padrão)\
\n2 - Urgente (prioridade)\
\n3 - Expressa (máxima prioridade)\
\n4 - Sair\
\n====================================================================")

        opcao_urgencia = int(input("digite uma opção: "))
    
        if opcao_urgencia == 1:
            print("Opção selecionada: Normal (prazo padrao)")
        elif opcao_urgencia == 2:
            print("Opção selecionada: Urgente (prioridade)")
        elif opcao_urgencia == 1:
            print("Opção selecionada: Expressa (maxima prioridade)")
        else:
            print("Saindo...")
            break
urgencia()

def total():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

pecas = []




cadastro_cliente()
