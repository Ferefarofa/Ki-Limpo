import sqlite3

conexao = sqlite3.connect()
cursor = conexao.cirsor
cursor.execute("PRAGMA foreing_keys = ON")

def clube()
    conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clube(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT NOT NULL,
                    cpf_cliente TEXT NOT NULL
                    id_cliente INTEGER NOT NULL,
                    FOREIGN KEY id_cliente REFERENCES clientes(id)  
                    )
    ''')
    conexao.commit()
    conexao.close()


def entrar_clube(cpf):
    conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execcute("PRAGMA foreign_keys = ON")

    cursor.execute('''
    SELECT id nome_cliente, cpf_cliente
    FROM cliente
    WHERE cpf_clientes = ?
    """,)
    
