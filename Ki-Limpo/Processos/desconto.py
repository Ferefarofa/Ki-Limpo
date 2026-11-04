import sqlite3

conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()


def criar_tabela_descontos():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS descontos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL UNIQUE,
            quantidade_lavagens INTEGER DEFAULT 0,
            desconto REAL DEFAULT 0.0,
            ultima_lavagem TEXT
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        )
    """)

    conexao.commit()
    conexao.close()



def atualizar_desconto():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

     cursor.execute("""
        SELECT quantidade_lavagens, desconto
        FROM descontos
        WHERE id_cliente = ?
    """, (id_cliente,))

    resultado = cursor.fetchone()








