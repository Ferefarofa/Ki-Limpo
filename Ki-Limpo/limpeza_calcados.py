import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def pedido_limpeza_calcado()
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    id_cliente = int(input("Insira o id do cliente: "))
    tipo_limpeza = input("Digite o tipo de limpeza de calçado: ")
    pares = int(input("Insira a quantidade de pares: "))
    coleta_entrega = int(input("1 - Coleta\n2 - Entrega\nColeta ou entrega: "))
    data = input("Insira a data: ")
    horario = input("Insira o horário: ")
    prioridade = int(input("1 = Normal\n2 = Urgente\nInsira a prioridade da lavagem: "))
    descricao = input("Insira a descrição da lavagem(opcional): ")


    cursor.execute(f'''
                INSERT INTO limpeza_calcados(id_cliente, tipo_limpeza, pares, coleta_entrega, data, horario, prioridade, descricao)
                VALUES({id_cliente}, '{tipo_limpeza}', {pares}, {coleta_entrega}, '{data}', '{horario}', {prioridade}, '{descricao}')
    '''
    )

    conexao.commit()
    conexao.close()


    
