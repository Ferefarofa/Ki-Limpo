import sqlite3

conexao = sqlite3.connect(Ki-Limpo/dados_lavanderia.db)
cursor = conexao.cirsor
cursor.execute("PRAGMA foreing_keys = ON")

def entrar_clube():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execcute("PRAGMA foreign_keys = ON")


    cpf_cliente = input("Digite o CPF do cliente: ")


    cursor.execute(f'''
    SELECT id nome_cliente, cpf_cliente
    FROM cliente
    WHERE cpf_clientes = '{cpf_cliente}'
    ''')
    conexao.commit()
    conexao.close()
    
