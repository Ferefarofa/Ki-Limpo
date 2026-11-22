import sqlite3
from login import login_cliente
from cadastros import cadastrar_cliente
from pagamento import forma_pagamento, pagamento_realizado


def cliente_menu():
    opcao = True
    print("\
    \n====================================================================\
    \nOLÁ CLIENTE, SELECIONA UMA OPÇÃO: \
    \n1 - FAZER LOGIN\
    \n2 - CADASTRAR\
    \n====================================================================")
    try:
        opcao = int(input("Escolha: "))
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return cliente_menu()
    finally:
        print()
    if opcao == 1:
        cliente = login_cliente()
    elif opcao == 2:
        cadastrar_cliente()
        print("\
    \n====================================================================\
    \nVocê foi encaminhado para o login...")
        cliente = login_cliente()
    else:
        print("Opção inválida.")
        return cliente_menu()

    if cliente == None:
        print("E-mail ou senha inválidos. Tente novamente.")
        return cliente_menu()

    if cliente:
        print(f"\
    \n====================================================================\
    \nBEM VINDO(A) {cliente[1]}\
    \n====================================================================")
    return cliente


def servico():
    try:
        while True:
            print("\
            \n====================================================================\
            \nEscolha a opção de serviço:\
            \n1 - Lavar e secar(Valor normal)\
            \n2 - Lavar, secar e passar(Valor 1.5x do valor normal)\
            \n3 - Lavagem a seco(Valor 2x do valor normal)\
            \n====================================================================")
            opcao_menu = int(input("digite a sua opção: "))

            if opcao_menu == 1:
                print("Opção selecionada: lavar e secar")
                return "lavar e secar"
            elif opcao_menu == 2:
                print("Opção selecionada: lavar, secar e passar")
                return "lavar, secar e passar"
            elif opcao_menu == 3:
                print("Opção selecionada: lavagem a seco")
                return "lavagem a seco"
            else:
                print("Opção inválida.")

    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return servico()
    finally:
        print()


def roupa_e_quantidade():
    try:
        roupa = ""
        quantidade = 0
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
            6: "Peças de baixo",
        }

        # Verificar se a opção é válida
        if opcao_roupa in opcoes_roupa:
            roupa = opcoes_roupa[opcao_roupa]
            print(f"Opção selecionada: {roupa}")
        else:
            print("Opção inválida!")
        # Solicitar a quantidade
        if roupa != "":
            quantidade = int(input("Digite a quantidade de peças: "))
            if quantidade <= 0:
                print("Quantidade inválida!")

        if quantidade > 0:
            return roupa, quantidade, opcao_roupa
        else:
            return roupa_e_quantidade()
    except ValueError:
        print("Entrada inválida. Digite uma opcão valida.")
        return roupa_e_quantidade()
    finally:
        print()


def intensidade():
    print(f"\
    \n====================================================================\
    \nEscolha a intensidade da lavagem:\
    \n1 - Sujeira Simples(Poeira, suor, manchas de uso leves)\
    \n2 - Bem Sujo(Manchas, resíduos, etc...)\
    \n3 - Extremamente Sujo(Cobertas de terra, encardidas, etc...)\
    \n====================================================================")
    try:
        opcao = int(input("Digite a intensidade da lavagem: "))
        if opcao == 1:
            return "Sujeira Simples"
        elif opcao == 2:
            return "Bem Sujo"
        elif opcao == 3:
            return "Extremamente Sujo"
        else:
            print("Opção inválida.")
            return intensidade()
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return intensidade()
    finally:
        print()


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
    \n====================================================================")
    try:
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
            print("Opção inválida.")
            return preferencia_produtos()
        print("\n====================================================================")

        print("\
        \nEscolha as opções de Amaciantes:\
        \n1 - Amaciante convencional\
        \n2 - Amaciante concentrado\
        \n3 - Amaciante hipoalergênico ou sem perfume\
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
            print("Opção inválida. Saindo...")
            return preferencia_produtos()
        print("\n====================================================================")
        print(f"\
        \nEscolha as opções de Produtos auxiliares de lavagem:\
        \n1 - Desengorduranes têxteis\
        \n2 - Reforçadores de detergência\
        \n3 - Produtos para remoção de manchas difíceis\
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
            print("Opção inválida.")
            return preferencia_produtos()
        if (tipo_sabao and amaciante and produto_auxiliar) != "Não informado":
            return tipo_sabao, amaciante, produto_auxiliar
        else:
            print("Informações faltando")
            return preferencia_produtos()
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return preferencia_produtos()
    finally:
        print()


def fragrancia():
    print("\n====================================================================")

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

    try:
        opcao_fragrancia = int(input("digite a sua fragrância: "))

        if opcao_fragrancia == 1:
            print("Opção selecionada: Algodão")
            return "Algodão"
        elif opcao_fragrancia == 2:
            print("Opção selecionada: Lavanda")
            return "Lavanda"
        elif opcao_fragrancia == 3:
            print("Opção selecionada: Cítrico")
            return "Cítrico"
        elif opcao_fragrancia == 4:
            print("Opção selecionada: Jasmin")
            return "Jasmin"
        elif opcao_fragrancia == 5:
            print("Opção selecionada:returnsas")
            return "Rosas"
        elif opcao_fragrancia == 6:
            print("Opção selecionada: Eucalipto")
            return "Eucalipto"
        elif opcao_fragrancia == 7:
            print("Opção selecionada: Baunilha")
            return "Baunilha"
        elif opcao_fragrancia == 8:
            print("Opção selecionada: Brisa do mar")
            return "Brisa do mar"
        elif opcao_fragrancia == 9:
            print("Opção selecionada: Musk")
            return "Musk"
        elif opcao_fragrancia == 10:
            print("Opção selecionada: Talco")
            return "Talco"
        elif opcao_fragrancia == 11:
            print("Opção selecionada: Sem fragrância")
            return "Sem fragrância"
        else:
            print("Opção inválida.")
            return fragrancia()
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return fragrancia()
    finally:
        print()


def atendimento():
    print("\n====================================================================\
    \nEscolha as opções de atendimento:\
    \n1 - Coleta (o funcionário irá até o endereço do cliente para coletar as roupas)\
    \n2 - Entrega (o cliente irá até a lavanderia para entregar as roupas)\
    \n====================================================================")
    try:
        escolha = int(input("Digite a sua opção: "))
        if escolha == 1:
            print("Opção selecionada: Coleta")
            return "coleta"
        elif escolha == 2:
            print("Opção selecionada: Entrega")
            return "entrega"
        else:
            print("Opção inválida.")
            return atendimento()
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return atendimento()
    finally:
        print()


def urgencia():
    print("\n====================================================================")
    print(f"\
    \nEscolha as opções de urgência:\
    \n1 - Normal (prazo padrão)\
    \n2 - Urgente (prioridade)\
    \n====================================================================")
    taxa = 0.0
    descricao_urgencia = "Não definido"
    try:
        opcao_urgencia = int(input("digite uma opção: "))

        if opcao_urgencia == 1:
            print("Opção selecionada: Normal (prazo padrao)")
            taxa = 1.0
            descricao_urgencia = "Normal (prazo padrão)"
        elif opcao_urgencia == 2:
            print("Opção selecionada: Urgente (prioridade)")
            taxa = 1.3
            descricao_urgencia = "Urgente (prioridade)"
        else:
            print("Opção inválida.")
            return urgencia()
        if (taxa != 0.0) and (descricao_urgencia != "Não definido"):
            return taxa, descricao_urgencia
    except ValueError:
        print("Entrada inválida. Digite o número de uma opção.")
        return urgencia()
    finally:
        print()


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

    try:
        multiplicador = multiplicadores[servico]

        print("\n====================================================================")
        print("RESUMO DO PEDIDO")

        nome, preco = precos[opcao_roupa]
        valor = preco * quantidade * multiplicador
        valor_total = valor * taxa
        print(f"{nome} - Quantidade: {quantidade}")
        print(f"Valor: R$ {valor}")

        print(f"Subtotal: R$ {valor}")
        print(f"Total: R$ {valor_total}")
        print("====================================================================")
        roupa = nome
        return valor_total, roupa
    except KeyError as erro:
        print(f"Erro nas informações do pedido")
        return None, None
    finally:
        print()


def observacao():
    try:
        observacao = input("Digite alguma observação sobre o pedido (opcional): ")
        return observacao
    except ValueError:
        print("Entrada inválida. Tente novamente")
        return observacao()
    finally:
        print()


def executar_cliente():
    cliente = None
    if cliente == None:
        cliente = cliente_menu()
    opcao = 0
    while opcao != 4:
        print("\n====================================================================\
            \nVocê pode:\
            \n1 - Fazer um pedido\
            \n2 - Visualizar pedidos realizados\
            \n3 - Ver pedidos finalizados\
            \n4 - Sair\
            \n====================================================================")
        try:
            opcao = int(input("Escolha: "))
            if opcao == 1:
                if cliente is None:
                    return None
                servico_escolhido = servico()
                if servico_escolhido is None:
                    return None
                roupa, quantidade, opcao_roupa = roupa_e_quantidade()
                if roupa is None:
                    return None
                intensidade_escolhida = intensidade()
                if intensidade_escolhida is None:
                    return None
                selecao_sabao, amaciante, produto_auxiliar = preferencia_produtos()
                if selecao_sabao is None:
                    return None
                preferencias_produtos = (
                    f"{selecao_sabao}, {amaciante}, {produto_auxiliar}"
                )
                fragrancia_escolhida = fragrancia()
                if fragrancia_escolhida is None:
                    return None
                atendimento_escolhido = atendimento()
                if atendimento_escolhido is None:
                    return None
                taxa_urgencia, descricao_urgencia = urgencia()
                if taxa_urgencia is None:
                    return None
                total_pedido, roupa = total(
                    servico_escolhido, opcao_roupa, quantidade, taxa_urgencia
                )
                if total_pedido is None:
                    return None
                observacao_pedido = observacao()
                dados_pedido = (
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
                )
                pedidos_realizados(dados_pedido)
            elif opcao == 2:
                conexao = None
                try:
                    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
                    cursor = conexao.cursor()
                    cursor.execute(
                        "SELECT * FROM pedidos WHERE id_cliente = ? AND status = ?",
                        (cliente[0], "pendente" or "aceito"),
                    )
                    pedidos = cursor.fetchall()

                    if not pedidos:
                        print("\nNenhum pedido encontrado.")
                    else:
                        for pedido in pedidos:
                            print("\n========== PEDIDO ==========")
                            print(f"ID do Pedido: {pedido[0]}")
                            print(f"ID do Cliente: {pedido[1]}")
                            print(f"Serviço: {pedido[2]}")
                            print(f"Roupa: {pedido[3]}")
                            print(f"Quantidade: {pedido[4]}")
                            print(f"Intensidade: {pedido[5]}")
                            print(f"Produtos: {pedido[6]}")
                            print(f"Fragrância: {pedido[7]}")
                            print(f"Atendimento: {pedido[9]}")
                            print(f"Urgência: {pedido[10]}")
                            print(f"Total: R$ {pedido[11]}")
                            print(f"Observação: {pedido[12]}")
                            print(f"Status: {pedido[13]}")
                            print(f"Horário: {pedido[14]}")
                            print(f"Data: {pedido[15]}")
                            cursor.execute(
                                "SELECT * FROM pagamentos WHERE id_pedido = ?",
                                (pedido[0],),
                            )

                            pagamentos_pedido = cursor.fetchall()

                            if pagamentos_pedido:
                                for pagamento in pagamentos_pedido:
                                    print(f"Pagamento: Pago - {pagamento[3]}")
                            else:
                                print("Pagamento: Pendente")
                            print("============================")

                except sqlite3.Error as erro:
                    print(f"Erro no banco de dados: {erro}")
                finally:
                    if conexao != None:
                        conexao.close()
            elif opcao == 3:
                conexao = None
                try:
                    conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
                    cursor = conexao.cursor()
                    cursor.execute(
                        "SELECT * FROM pedidos WHERE id_cliente = ? AND status = ?",
                        (cliente[0], "finalizado"),
                    )
                    pedidos = cursor.fetchall()

                    if not pedidos:
                        print("\nNenhum pedido encontrado.")
                    else:
                        for pedido in pedidos:
                            print("\n========== PEDIDO ==========")
                            print(f"ID do Pedido: {pedido[0]}")
                            print(f"ID do Cliente: {pedido[1]}")
                            print(f"Serviço: {pedido[2]}")
                            print(f"Roupa: {pedido[3]}")
                            print(f"Quantidade: {pedido[4]}")
                            print(f"Intensidade: {pedido[5]}")
                            print(f"Produtos: {pedido[6]}")
                            print(f"Fragrância: {pedido[7]}")
                            print(f"Atendimento: {pedido[9]}")
                            print(f"Urgência: {pedido[10]}")
                            print(f"Total: R$ {pedido[11]}")
                            print(f"Observação: {pedido[12]}")
                            print(f"Status: {pedido[13]}")
                            print(f"Horário: {pedido[14]}")
                            print(f"Data: {pedido[15]}")
                            print("============================")

                except sqlite3.Error as erro:
                    print(f"Erro no banco de dados: {erro}")
                finally:
                    if conexao != None:
                        conexao.close()
            elif opcao == 4:
                print("Saindo...")
                return None
            else:
                print("Opção inválida")
        except ValueError:
            print("Entrada inválida. Digite o número de uma opção.")
            continue


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

    conexao = None
    try:
        conexao = sqlite3.connect("Ki-Limpo/dados_lavanderia.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute(
            """
            INSERT INTO pedidos (
                id_cliente, servico, roupa, quantidade, intensidade,
                preferencia_produtos, fragrancia, atendimento, urgencia,
                total, observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
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
        cursor.execute("SELECT * FROM pedidos WHERE id_cliente = ?", (cliente[0],))

        pedidos = cursor.fetchall()

        for pedido in pedidos:
            id_pedido = pedido[0]

        pagamento_realizado(cliente[0], id_pedido, total_pedido, forma_pagamento())

    except sqlite3.Error as erro:
        print(f"Não foi possível salvar o pedido: {erro}")
    finally:
        if conexao != None:
            conexao.close()
