def cadastrar_processos():
    conexao = sqlite3.connect("Ki-limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    pedido = input("Insira o pedido: ")
    id_cliente = input("Insira o ID do cliente: ")
    data = input("Insira a data: ")
    horario = input("Insira o horário: ")
    prioridade = input("Insira a prioridade: ")
    total = input("Insira o total: ")

    cursor.execute(f'''INSERT INTO passadoria(pedido, id_cliente, data, horario, prioridade, total)
                    VALUES('{pedido}', '{id_cliente}', '{data}', '{horario}', '{prioridade}','{total}')
                ''')

    conexao.commit()
    print("Processo cadastrado com sucesso!")

cadastrar_processos()
conexao.close()