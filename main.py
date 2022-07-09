from uuid import uuid4
from datetime import datetime

Veiculos = {'motos': '', 'carros': '', 'camionetes': ''}
Motos = []
Carros = []
Camionetes = []
TransferenciasRealizadas = []


class Veiculo:
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str):
        self.__chassi = str(uuid4())
        self.data_fabricado = data_fabricado
        self.nome = nome
        self.placa = placa
        self.valor = float(valor)
        self.__cpf_comprador = 0
        self.cor = cor
        self.vendido = "Disponivel"

    @property
    def chassi(self):
        return self.__chassi

    @property
    def cpf_comprador(self):
        return self.__cpf_comprador

    @cpf_comprador.setter
    def cpf_comprador(self, cpf):
        self.__cpf_comprador = cpf

    def VenderVeiculo(self):
        cpf_cliente = input("Digite o CPF do cliente: ")
        self.vendido = "VENDIDO"
        self.cpf_comprador = cpf_cliente
        TransferenciasRealizadas.append(Transferencia(self.__dict__, cpf_cliente, self.valor))
        print("Venda concluida com sucesso!")

    def ListarInformacao(self):
        print("----------------------------")
        print("         INFORMAÇÕES")
        print("----------------------------")
        print(f"PLACA: {self.placa}      STATUS: {self.vendido}")
        print(f"MODELO: {self.nome}      ANO: {self.data_fabricado}")
        print(f"CHASSI: {self.chassi}    COR: {self.cor}")
        print(f"CPF DO COMPRADOR: {self.cpf_comprador}")
        print(f"VALOR: R${self.valor}")

    def alterarInformacao(self):
        valor = float(input("Digite o novo valor do veiculo: "))
        cor = input("Digite a nova cor do veiculo: ")
        self.valor = valor
        self.cor = cor
        print("Informações alteradas com sucesso!")



    @staticmethod
    def mostrarTodos():
        print("----------------------------------")
        print("             VEICULOS")
        print("----------------------------------")
        for motos in Veiculos['motos']:
                print(f"{motos.vendido} - PLACA: [{motos.placa}] - Moto Modelo: {motos.nome}, {motos.data_fabricado}, de {motos.numero_rodas} rodas, com a Potência de: {motos.potencia} cavalos, Cor: {motos.cor}, possui o valor de R${motos.valor}")
        for carros in Veiculos['carros']:
            print(f"{carros.vendido} - PLACA: [{carros.placa}] - Carro Modelo: {carros.nome}, {carros.data_fabricado}, de {carros.total_portas} de portas, Motor: {carros.modo} com a Potência de: {carros.potencia} cavalos, Cor: {carros.cor}, possui o valor de R${carros.valor}")
        for camionetes in Veiculos['camionetes']:
            print(f"{camionetes.vendido} - PLACA: [{camionetes.placa}] - Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R$ {camionetes.valor}")
        print("----------------------------------")

    @staticmethod
    def mostrarTodosVendidos():
        print("----------------------------------")
        print("         VEICULOS VENDIDOS")
        print("----------------------------------")
        for motos in Veiculos['motos']:
                if motos.vendido == "VENDIDO" :
                    print(f"[{motos.vendido}] PLACA: [{motos.placa}] - Moto Modelo: {motos.nome}, {motos.data_fabricado}, de {motos.numero_rodas} rodas, com a Potência de: {motos.potencia} cavalos, Cor: {motos.cor}, possui o valor de R${motos.valor}")
        for carros in Veiculos['carros']:
            if carros.vendido == "VENDIDO" :
                print(f"[{carros.vendido}] PLACA: [{carros.placa}] - Carro Modelo: {carros.nome}, {carros.data_fabricado}, de {carros.total_portas} de portas, Motor: {carros.modo} com a Potência de: {carros.potencia} cavalos, Cor: {carros.cor}, possui o valor de R${carros.valor}")
        for camionetes in Veiculos['camionetes']:
            if camionetes.vendido == "VENDIDO" :
                print(f"[{camionetes.vendido}] PLACA: [{camionetes.placa}] - Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R$ {camionetes.valor}")
        print("")
        print("----------------------------------")


class Moto(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, potencia: int, numero_rodas: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.potencia = potencia
        self.numero_rodas = numero_rodas
        
    def CadastrarMoto(self):
        Motos.append(self)
        Veiculos['motos'] = Motos

    def ListarInformacao(self):
        super().ListarInformacao()
        print(f"POTÊNCIA (CV): {self.potencia}")
        print(f"NÚMERO DE RODAS: {self.numero_rodas}")
        print("----------------------------")

    @staticmethod
    def MostrarMotos():
        for motos in Veiculos['motos']:
            if motos.vendido == "Disponivel" :
                print(f"PLACA: [{motos.placa}]  - Moto Modelo: {motos.nome}, {motos.data_fabricado}, de {motos.numero_rodas} rodas, com a Potência de: {motos.potencia} cavalos, Cor: {motos.cor}, possui o valor de R${motos.valor}")



class Carro(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, total_portas: int, modo: str, potencia: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.modo = modo
        self.potencia = potencia

    def CadastrarCarro(self):
        Carros.append(self)
        Veiculos['carros'] = Carros

    def ListarInformacao(self):
        super().ListarInformacao()
        print(f"NÚMERO DE PORTAS: {self.total_portas}")
        print(f"MOTOR: {self.modo}  POTÊNCIA (CV): {self.potencia}")
        print("----------------------------")

    @staticmethod
    def MostrarCarros():
        for carros in Veiculos['carros']:
            if carros.vendido == "Disponivel" :
                print(f"PLACA: [{carros.placa}] - Carro Modelo: {carros.nome}, {carros.data_fabricado}, de {carros.total_portas} de portas, Motor: {carros.modo} com a Potência de: {carros.potencia} cavalos, Cor: {carros.cor}, possui o valor de R${carros.valor}")



class Camionete(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, total_portas: int, cap_cacamba: int, potencia: int, modo: str, cor = "Roxa"):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.cap_cacamba = cap_cacamba
        self.potencia = potencia
        self.modo = modo

    def CadastrarCamionetes(self):
        Camionetes.append(self)
        Veiculos['camionetes'] = Camionetes

    def ListarInformacao(self):
        super().ListarInformacao()
        print(f"NÚMERO DE PORTAS: {self.total_portas}")
        print(f"CAPACIDADE DA CAÇAMBA (L): {self.cap_cacamba}")
        print(f"MOTOR: {self.modo}  POTÊNCIA (CV): {self.potencia}")
        print("----------------------------")

    def alterarInformacao(self):
        valor = float(input("Digite o novo valor do veiculo: "))
        self.valor = valor
        print("Informações alteradas com sucesso!")

    @staticmethod
    def MostrarCamionetes():
        for camionetes in Veiculos['camionetes']:
            if camionetes.vendido == "Disponivel":
                print(f"PLACA: [{camionetes.placa}] - Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R${camionetes.valor}")


class Transferencia:
    def __init__(self, dados_veiculo, cpf_comprador, valor):
        self.dados_veiculo = dados_veiculo
        self.cpf_comprador = cpf_comprador
        self.valor = valor
        self.data =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")



moto1 = Moto("2019", "Harley Davidson", "39AKB1", 39000, "Vermelha", 100, 2)
moto1.CadastrarMoto()
moto2 = Moto("2020", "Yamaha", "399BB1", 39300, "Azul", 130, 3)
moto2.CadastrarMoto()
moto3 = Moto("1999", "Honda", "319AZB", 15490, "Preta", 90, 2)
moto3.CadastrarMoto()

carro1 = Carro("1969", "Ford Mustang", "B9318C", 278000, "Preto", 2, "Gasolina", 483)
carro1.CadastrarCarro()
carro2 = Carro("1990", "Ford Mustang GT", "LC319C", 385000, "Cinza", 2, "Gasolina", 490)
carro2.CadastrarCarro()
carro3 = Carro("2010", "Lamborghini", "C1C9LK", 560000, "Laranja", 2, "Flex", 433)
carro3.CadastrarCarro()

camionete1 = Camionete("2020", "Mitsubishi L200 Triton", "KCZ1CL", 145000, 4, 6000, 400, "Diesel")
camionete1.CadastrarCamionetes()
camionete2 = Camionete("2021", "Chevrolet S10 Z71", "L3Z1MC", 185000, 4, 4000, 410, "Gasolina")
camionete2.CadastrarCamionetes()
camionete3 = Camionete("2018", "Fiat Toro", "Z351CL", 193200, 4, 5500, 390, "Diesel")
camionete3.CadastrarCamionetes()

print("RODOU!")

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
    print(" [7] - Para sair.")
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

        if opcaoEscolhida2 == "2":
            Carro.MostrarCarros()
            carroEscolhido = input("Insira a placa do carro escolhido: ")
            carroEscolhido = carroEscolhido.upper()
            try:
                resultIndice = next(i for i,obj in enumerate(Veiculos['carros']) if obj.placa == carroEscolhido)
            except:
                print("Veiculo não encontrado!")
            else:
                Carros[resultIndice].VenderVeiculo()

        if opcaoEscolhida2 == "3":
            Camionete.MostrarCamionetes()
            camioneteEscolhida = input("Insira a placa da camionete escolhida: ")
            camioneteEscolhida = camioneteEscolhida.upper()
            try:
                resultIndice = next(i for i,obj in enumerate(Veiculos['camionetes']) if obj.placa == camioneteEscolhida)
            except:
                print("Veiculo não encontrado!")
            else:
                Camionetes[resultIndice].VenderVeiculo()

        if opcaoEscolhida2 == "4":
            continue


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
            Veiculo.mostrarTodos()
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
        print("Você saiu!")
        break

    else: 
        print("Opção Invalida!")
        print("Tente novamente!")
        continue
    
    while True:
        resposta = input("\nDeseja continuar?\n [S] para SIM \n [N] para NÃO \n")
        if resposta.lower() == "s" :
            continuar = True
            break
        elif resposta.lower() == "n" :
            print("\nVocê saiu!")
            continuar = False
            break
        else:
            print("\nOpcao Invalida!")