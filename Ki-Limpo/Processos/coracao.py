import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()


from login import login_cliente
from cadastro_cliente import cadastro_cliente

def inicio():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    print(f"\
\n====================================================================\
\nBEM VINDO AO KI-LIMPO SYSTEM\
\nSELECIONA UMA DAS OPÇÕES:\
\n1 - SOU CLIENTE\
\n2 - SOU FUNCIONÁRIO\
\n====================================================================")
    tipo = int(input("Escolha: "))
    return tipo

tipo = inicio()
if tipo == 1:
    print("\
\n====================================================================\
\nOLÁ CLIENTE, SELECIONA UMA OPÇÃO: \
\n1 - FAZER LOGIN\
\n2 - CADASTRAR\
\n====================================================================")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        cliente = login_cliente()
    elif opcao == 2:
        cadastro_cliente()

elif opcao == 2:
    print("oi")

print(f"\
\n====================================================================\
\nBEM VINDO {cliente[1]}\
\n====================================================================")


