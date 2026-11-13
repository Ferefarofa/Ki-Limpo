import sqlite3
from login import login_cliente
from cadastros import cadastrar_cliente



def cliente_menu():
    opcao = True
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
        cadastrar_cliente()
        print("\
    \n====================================================================\
    \nVocê foi encaminhado para o login...")
        cliente = login_cliente()
    print(f"\
    \n====================================================================\
    \nBEM VINDO(A) {cliente[1]}\
    \n====================================================================")
    return cliente

def servico():

    print("\
    \n====================================================================\
    \nEscolha a opção de serviço:\
    \n1 - Lavar e secar(Valor normal)\
    \n2 - Lavar, secar e passar(Valor 1.5x do valor normal)\
    \n3 - Lavagem a seco(Valor 2x do valor normal)\
    \n4 - Sair\
    \n====================================================================")
    opcao_menu = int(input("digite a sua opção: "))

    servico = "Saindo"
    if opcao_menu == 1:
        print("Opção selecionada: lavar e secar")
        servico = "lavar e secar"
    elif opcao_menu == 2:
        print("Opção selecionada: lavar, secar e passar")
        servico = "lavar, secar e passar"
    elif opcao_menu == 3:
        print("Opção selecionada: lavagem a seco")
        servico = "lavagem a seco"
    else:
        print("Saindo...")
    return servico

def roupa_e_quantidade():
    print(f"\nEscolha as opções equivalentes às suas peças:")
    print("\n1 - Vestido")
    print("2 - Peças jeans (vestido, jaqueta, calça, etc)")
    print("3 - Camisas")
    print("4 - Camisetas")
    print("5 - Moletom (calças, casacos, etc)")
    print("6 - Peças de baixo")
    print("====================================================================")

    opcao_roupa = int(input("Digite a sua opção: "))

    # Dicionário para mapear as opções
    opcoes_roupa = {
        1: "Vestido",
        2: "Peças jeans",
        3: "Camisas",
        4: "Camisetas",
        5: "Moletom",
        6: "Peças de baixo"
    }

    # Verificar se a opção é válida
    if opcao_roupa in opcoes_roupa:
        roupa = opcoes_roupa[opcao_roupa]
        print(f"Opção selecionada: {roupa}")
    else:
        print("Opção inválida!")
        return None, None

    # Solicitar a quantidade
    quantidade = int(input("Digite a quantidade de peças: "))
    if quantidade <= 0:
        print("Quantidade inválida!")
        return None, None

    return roupa, quantidade, opcao_roupa

def intensidade():
    print(f"\
    \n====================================================================\
    \nEscolha a intensidade da lavagem:\
    \n1 - Sujeira Simples(Poeira, suor, manchas de uso leves)\
    \n2 - Bem Sujo(Manchas, resíduos, etc...)\
    \n3 - Extremamente Sujo(Cobertas de terra, encardidas, etc...)\
    \n====================================================================")
    opcao = int(input("Digite a intensidade da lavagem: "))
    if opcao == 1:
        intensidade = "Sujeira Simples"
    elif opcao == 2:
        intensidade = "Bem Sujo"
    elif opcao == 3:
        intensidade = "Extremamente Sujo"
    else:
        intensidade = "Opção inválida"
    print(f"Intensidade da lavagem: '{intensidade}'")
    return intensidade

def preferencia_produtos():
    tipo_sabao = "Não informado"
    amaciante = "Não informado"
    produto_auxiliar = "Não informado"

    print(f"\
    \nEscolha as opções de detergentes e sabões:\
    \n1 - Sabão regular (em pó)\
    \n2 - Sabão líquido\
    \n3 - Detergente concentrado\
    \n4 - Sabão neutro para roupas delicadas\
    \n5 - Sabão específico para roupas infantis\
    \n6 - Detergente para roupas brancas ou coloridas\
    \n7 - Sair\
    \n====================================================================")
    opcao = int(input("digite a sua opção: "))

    if opcao == 1:
        print("Opção selecionada: Sabão regular (em pó)")
        tipo_sabao = "Sabão regular (em pó)"
    elif opcao == 2:
        print("Opção selecionada: Sabão líquido")
        tipo_sabao = "Sabão líquido"
    elif opcao == 3:
        print("Opção selecionada: Detergente concentrado")
        tipo_sabao = "Detergente concentrado"
    elif opcao == 4:
        print("Opção selecionada: Sabão neutro para roupas delicadas")
        tipo_sabao = "Sabão neutro para roupas delicadas"
    elif opcao == 5:
        print("Opção selecionada: Sabão específico para roupas infantis")
        tipo_sabao = "Sabão específico para roupas infantis"
    elif opcao == 6:
        print("Opção selecionada: Detergente para roupas brancas ou coloridas")
        tipo_sabao = "Detergente para roupas brancas ou coloridas"
    else:
        print("Saindo...")
    print("\n====================================================================")

    print("\
    \nEscolha as opções de Amaciantes:\
    \n1 - Amaciante convencional\
    \n2 - Amaciante concentrado\
    \n3 - Amaciante hipoalergênico ou sem perfume\
    \n4 - Sair\
    \n====================================================================")

    opcao_amaciante = int(input("digite a sua opção: "))

    if opcao_amaciante == 1:
        print("Opção selecionada: Amaciante convencional")
        amaciante = "Amaciante convencional"
    elif opcao_amaciante == 2:
        print("Opção selecionada: Amaciante concentrado")
        amaciante = "Amaciante concentrado"
    elif opcao_amaciante == 3:
        print("Opção selecionada: Amaciante hipoalergênico ou sem perfume")
        amaciante = "Amaciante hipoalergênico ou sem perfume"
    else:
        print("Saindo...")
    print("\n====================================================================")
    print(f"\
    \nEscolha as opções de Produtos auxiliares de lavagem:\
    \n1 - Desengorduranes têxteis\
    \n2 - Reforçadores de detergência\
    \n3 - Produtos para remoção de manchas difíceis\
    \n4 - Sair\
    \n====================================================================")

    opcao_produto_auxiliar = int(input("digite a sua opção: "))

    if opcao_produto_auxiliar == 1:
        print("Opção selecionada: Desengordurantes têxteis")
        produto_auxiliar = "Desengordurantes têxteis"
    elif opcao_produto_auxiliar == 2:
        print("Opção selecionada: Reforçadores de detergência")
        produto_auxiliar = "Reforçadores de detergência"
    elif opcao_produto_auxiliar == 3:
        print("Opção selecionada: Produtos para remoção de manchas difíceis")
        produto_auxiliar = "Produtos para remoção de manchas difíceis"
    else:
        print("Saindo...")
    return tipo_sabao, amaciante, produto_auxiliar

def fragrancia():
    print("\n====================================================================")
    fragrancia = "Sem fragrância"

    print(f"\
    \nEscolha as opções de fragrancia:\
    \n1 - Algodão\
    \n2 - Lavanda\
    \n3 - Cítrico\
    \n4 - Jasmin\
    \n5 - Rosas\
    \n6 - Eucalipto\
    \n7 - Baunilha\
    \n8 - Brisa do mar\
    \n9 - Musk\
    \n10 - Talco\
    \n11 - Sem fragrância\
    \n====================================================================")

    opcao_fragrancia = int(input("digite a sua fragrância: "))

    if opcao_fragrancia == 1:
        print("Opção selecionada: Algodão")
        fragrancia = "Algodão"
    elif opcao_fragrancia == 2:
        print("Opção selecionada: Lavanda")
        fragrancia = "Lavanda"
    elif opcao_fragrancia == 3:
        print("Opção selecionada: Cítrico")
        fragrancia = "Cítrico"
    elif opcao_fragrancia == 4:
        print("Opção selecionada: Jasmin")
        fragrancia = "Jasmin"
    elif opcao_fragrancia == 5:
        print("Opção selecionada: Rosas")
        fragrancia = "Rosas"
    elif opcao_fragrancia == 6:
        print("Opção selecionada: Eucalipto")
        fragrancia = "Eucalipto"
    elif opcao_fragrancia == 7:
        print("Opção selecionada: Baunilha")
        fragrancia = "Baunilha"
    elif opcao_fragrancia == 8:
        print("Opção selecionada: Brisa do mar")
        fragrancia = "Brisa do mar"
    elif opcao_fragrancia == 9:
        print("Opção selecionada: Musk")
        fragrancia = "Musk"
    elif opcao_fragrancia == 10:
        print("Opção selecionada: Talco")
        fragrancia = "Talco"
    else:
        print("Opção selecionada: Sem fragrância")
    return fragrancia

def atendimento():
    print("\n====================================================================\
    \nEscolha as opções de atendimento:\
    \n1 - Coleta (o funcionário irá até o endereço do cliente para coletar as roupas)\
    \n2 - Entrega (o cliente irá até a lavanderia para entregar as roupas)\
    \n====================================================================")
    escolha = int(input("Digite a sua opção: "))
    if escolha == 1:
        print("Opção selecionada: Coleta")
        atendimento = "coleta"
    elif escolha == 2:
        print("Opção selecionada: Entrega")
        atendimento = "entrega"
    return atendimento

def urgencia():
    print("\n====================================================================")
    print(f"\
    \nEscolha as opções de urgência:\
    \n1 - Normal (prazo padrão)\
    \n2 - Urgente (prioridade)\
    \n====================================================================")

    opcao_urgencia = int(input("digite uma opção: "))
    if opcao_urgencia == 1:
        print("Opção selecionada: Normal (prazo padrao)")
        taxa = 1.0
        urgencia = "Normal (prazo padrão)"
    elif opcao_urgencia == 2:
        print("Opção selecionada: Urgente (prioridade)")
        taxa = 1.3
        urgencia = "Urgente (prioridade)"
    else:
        print("Opção inválida. Foi selecionada a opção normal.")
        taxa = 1.0
        urgencia = "Normal (prazo padrão)"
    return taxa, urgencia  

def total(servico, opcao_roupa, quantidade, taxa):
    precos = {
        1: ("Vestido", 20.00),
        2: ("Peças jeans", 15.00),
        3: ("Camisas", 12.00),
        4: ("Camisetas", 8.00),
        5: ("Moletom", 18.00),
        6: ("Peças de baixo", 6.00),
    }

    multiplicadores = {
        "lavar e secar": 1.0,
        "lavar, secar e passar": 1.5,
        "lavagem a seco": 2.0,
    }

    multiplicador = multiplicadores[servico]
    valor_total = 0.0

    print("\n====================================================================")
    print("RESUMO DO PEDIDO")

    nome, preco = precos[opcao_roupa]
    valor = preco * quantidade * multiplicador
    valor_total = valor
    print(f"{nome} - Quantidade: {quantidade}")
    print(f"Valor: R$ {valor}")

    print(f"Subtotal: R$ {valor_total}")
    valor_total = valor_total * taxa
    print(f"Total: R$ {valor_total}")
    print("====================================================================")
    roupa = nome
    return valor_total, roupa

def observacao():
    observacao = input("Digite alguma observação sobre o pedido (opcional): ")
    return observacao

def executar():
    cliente = cliente_menu()
    print(cliente)
    servico_escolhido = servico()
    roupa, quantidade, opcao_roupa = roupa_e_quantidade()
    intensidade_escolhida = intensidade()
    selecao_sabao, amaciante, produto_auxiliar = preferencia_produtos()
    preferencias_produtos = f"{selecao_sabao}, {amaciante}, {produto_auxiliar}"
    fragrancia_escolhida = fragrancia()
    atendimento_escolhido = atendimento()
    taxa_urgencia, descricao_urgencia = urgencia()
    total_pedido, roupa = total(servico_escolhido, opcao_roupa, quantidade, taxa_urgencia)
    observacao_pedido = observacao()
    return cliente, servico_escolhido, roupa, quantidade, intensidade_escolhida, preferencias_produtos, fragrancia_escolhida, atendimento_escolhido, descricao_urgencia, total_pedido, observacao_pedido
    


def pedidos_realizados(dados_pedido):
    (
        cliente,
        servico_escolhido,
        roupa,
        quantidade,
        intensidade_escolhida,
        preferencias_produtos,
        fragrancia_escolhida,
        atendimento_escolhido,
        descricao_urgencia,
        total_pedido,
        observacao_pedido,
    ) = dados_pedido

    try:
        conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute(
            '''
            INSERT INTO pedidos (
                id_cliente, servico, roupa, quantidade, intensidade,
                preferencia_produtos, fragrancia, atendimento, urgencia,
                total, observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                cliente[0],
                servico_escolhido,
                roupa,
                quantidade,
                intensidade_escolhida,
                preferencias_produtos,
                fragrancia_escolhida,
                atendimento_escolhido,
                descricao_urgencia,
                total_pedido,
                observacao_pedido,
            ),
        )

        conexao.commit()
    except sqlite3.Error as erro:
        print(f"Não foi possível salvar o pedido: {erro}")
    finally:
        if conexao != None:
            conexao.close()





cliente_menu = cliente_menu
servico = servico
roupa_e_quantidade = roupa_e_quantidade
intensidade = intensidade
preferencia_produtos = preferencia_produtos
fragrancia = fragrancia
atendimento = atendimento
urgencia = urgencia

