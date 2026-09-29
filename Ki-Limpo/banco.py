import sqlite3
conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def banco_cliente():
    conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS cliente(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cliente TEXT NOT NULL,
                    email_cliente TEXT NOT NULL,
                    senha_cliente TEXT NOT NULL,
                    telefone_cliente TEXT NOT NULL,
                    cpf_cliente TEXT NOT NULL,
                    endereco_cliente TEXT NOT NULL)
    ''')
    conexao.commit()
    conexao.close()


def banco_funcionario():
    conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS funcionario(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_funcionario TEXT NOT NULL,
                    email_funcionario TEXT NOT NULL,
                    senha_funcionario TEXT NOT NULL,
                    telefone_funcionario TEXT NOT NULL,
                    cpf_funcionario TEXT NOT NULL,
                    endereco_funcionario TEXT NOT NULL)
    ''')
    conexao.commit()
    conexao.close()
