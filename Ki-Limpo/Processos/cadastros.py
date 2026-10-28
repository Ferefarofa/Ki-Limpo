import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

from banco import banco_cliente
from banco import banco_funcionario

banco_funcionario()
banco_cliente()


def cadastrar_cliente():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")




    nome_cliente = input("Insira o nome do cliente: ")
    email_cliente = input("Insira o email do cliente: ")
    telefone_cliente = input("Insira o telefone do cliente: ")
    cpf_cliente = input("Insira o cpf do cliente: ")
    endereco_cliente = input("Insira o endereço do cliente: ")
    senha_cliente = input("Insira uma senha com no mínimo 6 digitos: ")

    cursor.execute(f'''INSERT INTO clientes(nome_cliente, email_cliente, telefone_cliente, cpf_cliente, endereco_cliente, senha_cliente)
                    VALUES('{nome_cliente}', '{email_cliente}', '{telefone_cliente}', '{cpf_cliente}', '{endereco_cliente}', '{senha_cliente}')
    ''')
    conexao.commit()
    conexao.close()

def cadastrar_funcionario():
    conexao = sqlite3.connect("Ki-limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    senha_gerente = "gerente123"
    senha = input("Insira a senha do gerente: ")
    if senha == senha_gerente:
        nome_funcionario = input("Insira o nome do funcionario: ")
        email_funcionario = input("Insira o email do funcionario: ")
        telefone_funcionario = input("Insira o telefone do funcionario: ")
        cpf_funcionario = input("Insira o CPF do funcionario: ")
        senha_funcionario = input("Insira a senha do funcionario: ")
    else:
        print("Senha do gerente incorreta. ")

    cursor.execute(f'''INSERT INTO funcionarios(nome_funcionario, email_funcionario, telefone_funcionario, cpf_funcionario, senha_funcionario)
                    VALUES('{nome_funcionario}', '{email_funcionario}', '{telefone_funcionario}', '{cpf_funcionario}','{senha_funcionario}')
            ''')
    conexao.commit()
    print("Funcionario cadastrado com sucesso!")
    conexao.close()
    