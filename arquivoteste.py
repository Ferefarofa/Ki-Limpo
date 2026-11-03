def calcular_total():
    precos = {
        1: ("Camiseta", 8.00),
        2: ("Camisa social", 12.00),
        3: ("Calça", 13.00),
        4: ("Vestido", 20.00),
        5: ("Toalha de banho", 9.00),
        6: ("Lençol de casal", 16.50),
        7: ("Cobertor", 30.00),
        8: ("Edredom", 40.00),
        9: ("Cortina", 35.00),
    }

    print("\n====================================================================")
    print("Escolha o tipo de serviço:")
    print("1 - Lavar e secar")
    print("2 - Lavar, secar e passar")
    print("3 - Lavagem a seco")
    print("====================================================================")
    servico = int(input("Digite o número do serviço: "))


    multiplicadores = {
        1: 1.0,  #lavar e secar 
        2: 1.5,   #lavar, secar e passar
        3: 2.2   #lavagem a seco
    }

    total = 0.0
    pecas = []

    total = 0.0
    while True:
        print("\n====================================================================")
        print("Escolha a peça de roupa:")
        print("1 - Camiseta")
        print("2 - Camisa social")
        print("3 - Calça")
        print("4 - Vestido")
        print("5 - Toalha de banho")
        print("6 - Lençol de casal")
        print("7 - Cobertor")
        print("8 - Edredom")
        print("9 - Cortina")
        print("10 - Sair")
        print("====================================================================")

        opcao_roupa = int(input("Digite o número da peça de roupa: "))


        pecas = []

        if opcao_roupa == 1:
            pecas.append("Camiseta")

        elif opcao_roupa == 2:
            pecas.append("Camisa social")

        elif opcao_roupa == 3:
            pecas.append("Calça")

        elif opcao_roupa == 4:
            pecas.append("Vestido")

        elif opcao_roupa == 5:
            pecas.append("Toalha de banho")

        elif opcao_roupa == 6:
            pecas.append("Lençol de casal")

        elif opcao_roupa == 7:
            pecas.append("Cobertor")

        elif opcao_roupa == 8:
            pecas.append("Edredom")

        elif opcao_roupa == 9:
            pecas.append("Cortina")

        elif opcao_roupa == 10:
            break

        else:
            print("Opção inválida!")
            continue
        
            break
calcular_total()