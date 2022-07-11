from entities import Veiculo, Veiculos, Carro, Carros, Camionete, Camionetes, Moto, Motos

continuar = True
while continuar == True:
    print(" ")
    print("========================================================")
    print("                     DEVinCar                           ")
    print("========================================================")
    print(" [1] - Vender veículo.")
    print(" [2] - Ver veículos disponiveis.")
    print(" [3] - Ver veículos vendidos.")
    print(" [4] - Listar todos os veículos.")
    print(" [5] - Pesquisar informação do veículo.")
    print(" [6] - Alterar informação do veículo.")
    print(" [7] - Para Cadastrar um novo veiculo.")
    print(" [8] - Para sair.")
    print("========================================================")
    print(" ")
    opcaoEscolhida = input("Digite a opção escolhida: ")
    print(" ")

    if opcaoEscolhida == "1" :
        print("Escolha o modelo: ")
        print(" [1] - Ver Motos/Triciclos.")
        print(" [2] - Ver Carros.")
        print(" [3] - Ver Camionetes.\n")
        print(" [4] - Voltar")
        print(" ")
        opcaoEscolhida2 = input("Digite a opção escolhida: ")
        print(" ")
        if opcaoEscolhida2 == "1":
            Moto.MostrarMotos()
            motoEscolhida = input("Insira a placa da moto escolhida: ")
            motoEscolhida = motoEscolhida.upper()
            try:
                resultIndice = next(i for i,obj in enumerate(Veiculos['motos']) if obj.placa == motoEscolhida)
            except:
                print("Veiculo não encontrado!")
            else:
                Motos[resultIndice].VenderVeiculo()

        elif opcaoEscolhida2 == "2":
            Carro.MostrarCarros()
            carroEscolhido = input("Insira a placa do carro escolhido: ")
            carroEscolhido = carroEscolhido.upper()
            try:
                resultIndice = next(i for i,obj in enumerate(Veiculos['carros']) if obj.placa == carroEscolhido)
            except:
                print("Veiculo não encontrado!")
            else:
                Carros[resultIndice].VenderVeiculo()

        elif opcaoEscolhida2 == "3":
            Camionete.MostrarCamionetes()
            camioneteEscolhida = input("Insira a placa da camionete escolhida: ")
            camioneteEscolhida = camioneteEscolhida.upper()
            try:
                resultIndice = next(i for i,obj in enumerate(Veiculos['camionetes']) if obj.placa == camioneteEscolhida)
            except:
                print("Veiculo não encontrado!")
            else:
                Camionetes[resultIndice].VenderVeiculo()

        elif opcaoEscolhida2 == "4":
            continue

        else:
            print("Opção Invalida!")


    elif opcaoEscolhida == "2" :
        print(" ")
        print(" [1] - Ver Motos/Triciclos.")
        print(" [2] - Ver Carros.")
        print(" [3] - Ver Camionetes.")
        print(" [4] - Ver Todos.")
        print(" [5] - Voltar.")
        print(" ")
        opcaoEscolhida2 = input("Digite a opção escolhida: ")
        print(" ")
        if opcaoEscolhida2 == "1":
            Moto.MostrarMotos()
        elif opcaoEscolhida2 == "2":
            Carro.MostrarCarros()
        elif opcaoEscolhida2 == "3":
            Camionete.MostrarCamionetes()
        elif opcaoEscolhida2 == "4":
            Veiculo.mostrarTodosDisponiveis()
        elif opcaoEscolhida2 == "5":
            continue
        else:
            print("Opção Invalida!")


    elif opcaoEscolhida == "3" :
        Veiculo.mostrarTodosVendidos()


    elif opcaoEscolhida == "4" :
        Veiculo.mostrarTodos()

    elif opcaoEscolhida == "5" :
        VeiculoPesquisado = input("Insira a placa do veiculo a ser procurado: ")
        VeiculoPesquisado = VeiculoPesquisado.upper()
        VeiculosTodos = Motos + Carros + Camionetes
        try:
            resultIndice = next(i for i,obj in enumerate(VeiculosTodos) if obj.placa == VeiculoPesquisado)
        except:
            print("Veiculo não encontrado!")
        else:
            VeiculosTodos[resultIndice].ListarInformacao()

    elif opcaoEscolhida == "6" :
        VeiculoPesquisado = input("Insira a placa do veiculo a ter informações alteradas: ")
        VeiculoPesquisado = VeiculoPesquisado.upper()
        VeiculosTodos = Motos + Carros + Camionetes
        try:
            resultIndice = next(i for i,obj in enumerate(VeiculosTodos) if obj.placa == VeiculoPesquisado)
        except:
            print("Veiculo não encontrado!")
        else:
            VeiculosTodos[resultIndice].alterarInformacao()


    elif opcaoEscolhida == "7" :
        print("------------------------------------")
        print("      CADASTRO DE VEICULO")
        print("------------------------------------")
        print("Selecione o tipo de veículo: ")
        print(" [1] - Moto/Triciclo.")
        print(" [2] - Carro.")
        print(" [3] - Camionete.")
        print("")
        print(" [4] - Cancelar")
        opcaoEscolhida2 = input("Digite a opção: ")
        if opcaoEscolhida2 == "1" :
            nome = input("Digite o nome do modelo da motocicleta: ")
            data_fabricado = input("Digite o ano de fabricação do modelo: ")
            placa = input("Digite a placa da motocicleta: ")
            valor = float(input("Insira o valor da motocicleta: R$"))
            cor = input("Digite a cor da motocicleta: ")
            potencia = int(input("Digite a potência da motocicleta: "))
            numero_rodas = int(input("Digite o número de rodas da motocicleta: "))
            Moto.CadastrarMoto(data_fabricado, nome, placa, valor, cor, potencia, numero_rodas)
            print("Motocicleta cadastrada com sucesso!")

        elif opcaoEscolhida2 == "2" :
            nome = input("Digite o nome do modelo do veículo: ")
            data_fabricado = input("Digite o ano de fabricação do modelo: ")
            placa = input("Digite a placa do veículo: ")
            valor = float(input("Insira o valor do veículo: R$"))
            cor = input("Digite a cor do veículo: ")
            potencia = int(input("Digite a potência do veículo: "))
            total_portas = int(input("Digite o número de portas do veículo: "))
            modo = input("O motor do veículo é a Gasolina ou Flex? ")
            Carro.CadastrarCarro(data_fabricado, nome, placa, valor, cor, total_portas, modo, potencia)
            print("Carro cadastrado com sucesso!")

        elif opcaoEscolhida2 == "3" :
            nome = input("Digite o nome do modelo da camionete: ")
            data_fabricado = input("Digite o ano de fabricação do modelo: ")
            placa = input("Digite a placa da camionete: ")
            valor = float(input("Insira o valor da camionete: R$"))
            cap_cacamba = int(input("Digite a capacidade da caçamba da camionete (em litros): "))
            potencia = int(input("Digite a potência da camionete: "))
            total_portas = int(input("Digite o número de portas da camionete: "))
            modo = input("O motor da camionete é a Gasolina ou Diesel? ")
            Camionete.CadastrarCamionetes(data_fabricado, nome, placa, valor, total_portas, cap_cacamba, potencia, modo)
            print("Camionete Cadastrada com sucesso!")

        elif opcaoEscolhida2 == "4":
            continue

        else:
            print("Opção Invalida!")

    elif opcaoEscolhida == "8" :
        print("Você saiu!")
        break

    else: 
        print("Opção Invalida!")
        print("Tente novamente!")
        continue
    
    while True:
        resposta = input("\nDeseja continuar?\n [S] para SIM \n [N] para NÃO \n Digite a opção: ")
        if resposta.lower() == "s" :
            continuar = True
            break
        elif resposta.lower() == "n" :
            print("\nVocê saiu!")
            continuar = False
            break
        else:
            print("\nOpcao Invalida!")

