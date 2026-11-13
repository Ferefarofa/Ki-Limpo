import sqlite3

def login_cliente():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    try:
        cursor = conexao.cursor()
        email = input("E-mail: ")
        senha = input("Senha: ")
        cursor.execute(
            "SELECT * FROM clientes WHERE email_cliente = ? AND senha_cliente = ?",
            (email, senha),
        )
        return cursor.fetchone()
    finally:
        conexao.close()

def login_funcionario():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    try:
        cursor = conexao.cursor()
        email = input("E-mail: ")
        senha = input("Senha: ")
        cursor.execute(
            "SELECT * FROM funcionarios WHERE email_funcionario = ? AND senha_funcionario = ?",
            (email, senha),
        )
        funcionario = cursor.fetchone()
        print(funcionario)
        return funcionario
    finally:
        conexao.close()

