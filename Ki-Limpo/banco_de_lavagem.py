import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastro_lavagem():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_cliente = input("Insira o ID do cliente: ")
    urgencia = input("Insira a urgencia da lavagem: ")
    intensidade = input("Insira a intensidade da lavagem: ")
    roupa = input("Insira qual a roupa a ser lavada: ")
    pecas = input("Insira as peças de roupa: ")
    fragrancia = input("Insira a fragrancia escolhida: ")
    observacao = input("Insira uma observação (opcional): ")
    coleta_entrega = input("Haverá coleta ou entrega: ")
    data = input("Insira a data da lavagem: ")
    horario = input("Insira o horário da lavagem: ")
   
    cursor.execute(f'''
                    INSERT INTO pedidos(
                    id_cliente,
                    urgencia,
                    roupa,
                    intensidade,
                    quantidade,
                    fragrancia,
                    observacao,
                    atendimento,
                    data,
                    horario,
                    status)
                    VALUES(
                    '{id_cliente}',
                    '{urgencia}',
                    '{roupa}',
                    '{intensidade}',
                    {quantidade},
                    '{fragrancia}',
                    '{observacao}',
                    '{coleta_entrega}',
                    '{data}',
                    '{horario}',
                    '{status}'
                    )
    ''')
    
    conexao.commit()
    conexao.close()
