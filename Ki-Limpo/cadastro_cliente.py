import sqlite3
conexao = sqlite3.connect("Lavanderia/dados_lavanderia.d")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastro_cliente():
    conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")




    nome_cliente = input("Insira o nome do cliente: ")
    email_cliente = input("Insira o email do cliente: ")
    telefone_cliente = intput("Insira o telefone do cliente: ")
    cpf_cliente = input("Insira o cpf do cliente: ")
    endereco_cliente = input("Insira o endereço do cliente: ")
    senha_cliente = input("Insira uma senha com no mínimo 6 digitos: ")

    cursor.execute(f'''INSERT INTO clientes(nome_cliente, email_cliente, telefone_cliente, cpf_cliente, endereco_cliente, senha_cliente)
                    VALUES('{nome_cliente}', '{email_cliente}', '{telefone_cliente}', '{cpf_cliente}', '{endereco_cliente}', '{senha_cliente}')
    ''')
    conexao.commit()
    conexao.close()




    