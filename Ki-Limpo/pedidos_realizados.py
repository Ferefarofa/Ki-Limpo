import sqlite3

conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def peiddos_realizados()
    conexao = sqlite3.connect("Lavanderia/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    
    servico = input("Insira o serviço realizado: ")
    id_cliente = int(input("Insira o id do cliente efetuador do pedido: "))
    cpf_cliente = input("Insira o cpf do cliente efetuador do pedido: ")
    id_fucnionário = int(input("Insira o id do funcionário responsavel pelo pedido: "))
    data = input("Insira a data do pedido: ")
    horario = input("Insira o horáiro do pedido: ")

    cursor.execute(f'''
                    INSERT INTO realizados(servico, id_cliente, cpf_cliente, id_funcionario, data, horario)
                    VALUES(servico, id_cliente, cpf_cliente, id_funcionario, data, horario)

    ''')
    conexao.commit()
    conexao.close()