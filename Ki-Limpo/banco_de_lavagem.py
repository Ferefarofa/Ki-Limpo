import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastro_lavagem():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_cliente = input("Insira o ID do cliente: ")
    prioridade = input("Insira a prioridade da lavagem: ")
    intensidade = input("Insira a intensidade da lavagem: ")
    peso = input("Insira o peso das roupas em kg: ")
    aroma = input("Insira o aroma escolhido: ")
    descricao = input("Insira uma descrição (opcional): ")
    coleta_entrega = input("Haverá coleta ou entrega: ")
    data = input("Insira a data da lavagem: ")
    horario = input("Insira o horário da lavagem: ")
   
    cursor.execute(f'''INSERT INTO lavagens(id_cliente,prioridade,intensidade,peso,aroma,descricao,coleta_entrega,data,horario)
                    VALUES('{id_cliente}','{prioridade}','{intensidade}','{peso}','{aroma}','{descricao}','{coleta_entrega}','{data}','{horario}','{status}')
    ''')
    
    conexao.commit()
    conexao.close()
