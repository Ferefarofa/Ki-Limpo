import sqlite3
conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def banco_cliente():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cliente TEXT NOT NULL,
                    email_cliente TEXT NOT NULL,
                    senha_cliente TEXT NOT NULL,
                    telefone_cliente TEXT NOT NULL,
                    cpf_cliente TEXT NOT NULL,
                    endereco_cliente TEXT NOT NULL,
                    sequencia INTEGER,
                    clube INTEGER)
    ''')#O clube esta em integer por possuir 2 opções sim ou nao que vao ser caracterizada entre 1 ou 2, demais outras opções estao sujeitas a tal metodo de seleção também(Integer especial)
    conexao.commit()
    conexao.close()


def banco_funcionario():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS funcionarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_funcionario TEXT NOT NULL,
                    email_funcionario TEXT NOT NULL,
                    senha_funcionario TEXT NOT NULL,
                    telefone_funcionario TEXT NOT NULL,
                    cpf_funcionario TEXT NOT NULL,
                    trabalhos INTEGER,
                    comissao REAL)
    ''')#
    conexao.commit()
    conexao.close()


def lavagens():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS lavagens(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    prioridade INTEGER NOT NULL,
                    intensidade TEXT NOT NULL,
                    peso REAL NOT NULL,
                    aroma TEXT NOT NULL,
                    descricao TEXT,
                    coleta_entrega TEXT NOT NULL,
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    status TEXT
                    )
    ''')# prioridade, coleta entrega, status (Integer especial)
    conexao.commit()
    conexao.close()


def passadorias():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS passadorias(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    prioridade INTEGER NOT NULL,
                    material TEXT NOT NULL,
                    peso REAL NOT NULL,
                    descricao TEXT,
                    coleta_entrega TEXT NOT NULL,
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    status TEXT
                    )
    ''')# prioridade, coleta entrega, status (Integer especial)
    conexao.commit()
    conexao.close()

def limpeza_calçados():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS limpeza_calcados(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    prioridade INTEGER NOT NULL,
                    tipo_limpeza TEXT NOT NULL,
                    pares INTEGER NOT NULL,
                    descricao TEXT,
                    coleta_entrega TEXT NOT NULL,
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    status TEXT
                    )
    ''')# prioridade, coleta entrega, status (Integer especial)
    conexao.commit()
    conexao.close()



def processos():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS passadoria(
                    id INTEGER PRIMARY KEY,
                    pedido TEXT NOT NULL,
                    id_cliente INTEGER NOT NULL
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    prioridade INTEGER NOT NULL,
                    total TEXT NOT NULL
                    )
    ''')# prioridade,(Integer especial)
    conexao.commit()
    conexao.close()

def realizados():
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS realizados(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    servico TEXT NOT NULL,
                    id_cliente INTEGER NOT NULL,
                    cpf_cliente TEXT NOT NULL,
                    id_fucnionário INTEGER NOT NULL,
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    FOREIGN KEY id_cliente REFERENCES clientes(id),
                    FOREIGN KEY id_funcionario REFERENCES funcionarios(id)
                    )
    ''')
    conexao.commit()
    conexao.close()

def clube()
    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clube(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT NOT NULL,
                    cpf_cliente TEXT NOT NULL
                    id_cliente INTEGER NOT NULL,
                    FOREIGN KEY id_cliente REFERENCES clientes(id)  
                    )
    ''')
    conexao.commit()
    conexao.close()
