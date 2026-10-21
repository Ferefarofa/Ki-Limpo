import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()



def tela_login():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    print("====================================================================\
    \n Bem-Vindo ao Ki-Limpo SYSTEM\n Escolha a opção de login:\
    \n 1 - Login cliente\n 2 - Login funcionário\n\
====================================================================")

    opcao = int(input("Insira a opção: "))
    if opcao == 1:
        email = input("E-mail: ")
        senha = input("Senha: ")

        cursor.execute(f'''
        SELECT FROM clientes WHERE email_cliente = '{email}'
        AND senha_cliente = '{senha}'
        ''')

        cliente = cursor.fetchone()


















tela_login()