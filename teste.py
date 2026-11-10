def recusar():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()

    id_cliente = input("Digite o ID do cliente para recusar o pedido: ")

    cursor.execute("SELECT * FROM pedidos WHERE id_cliente = ?", (id_cliente,))
    pedido = cursor.fetchone()

    cursor.execute("UPDATE pedidos SET status = 'recusado' WHERE id_cliente = ?", (id_cliente,))
