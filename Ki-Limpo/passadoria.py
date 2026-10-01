import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastro_passadoria():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_cliente = input("Insira o ID do cliente: ")
    prioridade = input("Insira a prioridade da passadoria: ")
    material = input("Insira o material das roupas: ")
    peso = input("Insira o peso das roupas em kg: ")
    descricao = input("Insira uma descrição (opcional): ")
    coleta_entrega = input("Haverá coleta ou entrega: ")
    data = input("Insira a data da passadoria: ")
    horario = input("Insira o horário da passadoria: ")

   
    cursor.execute(f'''INSERT INTO passadorias(id_cliente,prioridade,material,peso,descricao,coleta_entrega,data,horario,status)
                    VALUES('{id_cliente}','{prioridade}','{material}','{peso}','{descricao}','{coleta_entrega}','{data}','{horario}')
    ''')
    
    conexao.commit()
    conexao.close()
