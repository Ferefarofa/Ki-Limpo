import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()



def login_cliente():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    email = input("E-mail: ")
    senha = input("Senha: ")

    cursor.execute(f'''
    SELECT * FROM clientes WHERE email_cliente = '{email}'
    AND senha_cliente = '{senha}'
    ''')

    cliente = cursor.fetchone()
    
    return cliente
    conexao.close()

def login_funcionario():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    email = input("E-mail: ")
    senha = input("Senha: ")

    cursor.execute(f'''
    SELECT * FROM funcionarios WHERE email_funcionario = '{email}'
    AND senha_funcionario = '{senha}'
    ''')

    funcionario = cursor.fetchone()
    print(funcionario)
    
    return funcionario
    conexao.close()

