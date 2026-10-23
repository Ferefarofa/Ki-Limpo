import sqlite3

CAMINHO_BANCO = "Ki-Limpo/dados_lavanderia.db"


conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def entrar_clube():
    conexao.cursor = connect()
     
    cliente_cpf = input("Digite seu CPF")
    ID_cliente = input("Digite seu ID")

     cursor.execute(
        "SELECT id, ID_CLIENTE = ?",
        (ID_cliente,),
    )
   cliente = cursor.fetchone()

    if cliente:
        print("Cliente encontrado! Bem-vindo ao clube.")
    else:
        print("Cliente não encontrado.")
        
def pagamento_clube():
    conexao.cursor = connect()

