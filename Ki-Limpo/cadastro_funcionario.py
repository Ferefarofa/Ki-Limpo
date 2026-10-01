import sqlite3 
conexao = sqlite3.connect("Ki-limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def cadastrar_funcionario():
    conexao = sqlite3.connect("Ki-limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    nome_funcionario = input("Insira o nome do funcionario: ")
    email_funcionario = input("Insira o email do funcionario: ")
    senha_funcionario = input("Insira a senha do funcionario: ")
    telefone_funcionario = input("Insira o telefone do funcionario: ")
    cpf_funcionario = input("Insira o CPF do funcionario: ")

    cursor.execute(f'''INSERT INTO funcionarios(nome_funcionario, email_funcionario, senha_funcionario, telefone_funcionario, cpf_funcionario)
                    VALUES('{nome_funcionario}', '{email_funcionario}', '{senha_funcionario}', '{telefone_funcionario}', '{cpf_funcionario}')
            ''')
    conexao.commit()
    print("Funcionario cadastrado com sucesso!")
cadastrar_funcionario()
conexao.close()