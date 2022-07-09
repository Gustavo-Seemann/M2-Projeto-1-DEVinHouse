from uuid import uuid4
from datetime import datetime

Veiculos = {'motos': '', 'carros': '', 'camionetes': ''}
Motos = []
MotosVendidas = []
Carros = []
Camionetes = []
TransferenciasRealizadas = []


class Veiculo:
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str):
        self.__chassi = str(uuid4())
        self.data_fabricado = data_fabricado
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.__cpf_comprador = 0
        self.cor = cor
        self.vendido = False

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
        self.vendido = True
        self.cpf_comprador = cpf_cliente
        MotosVendidas.append(self)
        Motos.pop(self)
        TransferenciasRealizadas.append(Transferencia(self.__dict__, cpf_cliente, self.valor))
        print("Venda concluida com sucesso!")
        print(MotosVendidas[self])
        print(Motos)


    @staticmethod
    def mostrarTodos():
        for motos in Veiculos['motos']:
                print(f"PLACA: [{motos.placa}] - Moto Modelo: {motos.nome}, {motos.data_fabricado}, de {motos.numero_rodas} rodas, com a Potência de: {motos.potencia} cavalos, Cor: {motos.cor}, possui o valor de R${motos.valor}")
        for carros in Veiculos['carros']:
            print(f"PLACA: [{carros.placa}] Carro Modelo: {carros.nome}, {carros.data_fabricado}, de {carros.total_portas} de portas, Motor: {carros.modo} com a Potência de: {carros.potencia} cavalos, Cor: {carros.cor}, possui o valor de R${carros.valor}")
        for camionetes in Veiculos['camionetes']:
            print(f"PLACA: [{camionetes.placa}] Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R$ {camionetes.valor}")

    @staticmethod
    def mostrarTodosVendidos():
        for motos in Veiculos['motos']:
                if motos.vendido == True:
                    print(f"[VENDIDO] PLACA: [{motos.placa}] - Moto Modelo: {motos.nome}, {motos.data_fabricado}, de {motos.numero_rodas} rodas, com a Potência de: {motos.potencia} cavalos, Cor: {motos.cor}, possui o valor de R${motos.valor}")
        for carros in Veiculos['carros']:
            if carros.vendido == True:
                print(f"[VENDIDO] PLACA: [{carros.placa}] - Carro Modelo: {carros.nome}, {carros.data_fabricado}, de {carros.total_portas} de portas, Motor: {carros.modo} com a Potência de: {carros.potencia} cavalos, Cor: {carros.cor}, possui o valor de R${carros.valor}")
        for camionetes in Veiculos['camionetes']:
            if camionetes.vendido == True:
                print(f"[VENDIDO] PLACA: [{camionetes.placa}] - Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R$ {camionetes.valor}")



class Moto(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, potencia: int, numero_rodas: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.potencia = potencia
        self.numero_rodas = numero_rodas
        
    def CadastrarMoto(self):
        Motos.append(self)
        Veiculos['motos'] = Motos

    @staticmethod
    def MostrarMotos():
        for motos in Veiculos['motos']:
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

    @staticmethod
    def MostrarCarros():
        for carros in Veiculos['carros']:
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

    @staticmethod
    def MostrarCamionetes():
        for camionetes in Veiculos['camionetes']:
            print(f"PLACA: [{camionetes.placa}] - Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R$ {camionetes.valor}")


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
    print(" [1] - Vender carro.")
    print(" [2] - Ver carros.")
    print(" [3] - Ver carros vendidos.")
    print(" [4] - Listar todos os veiculos.")
    print(" [5] - Para sair.")
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
            motoEscolhida = input("Insira a opção de moto escolhida: ")
            if motoEscolhida == "1" :
                Motos[0].VenderVeiculo()
            if motoEscolhida == "2" :
                Motos[1].VenderVeiculo()
            if motoEscolhida == "3" :
                Motos[2].VenderVeiculo()
            else:
                print("Modelo não encontrado!")
        if opcaoEscolhida2 == "2":
            Carro.MostrarCarros()
            carroEscolhido = input("Insira a opção de carro escolhido: ")
            if carroEscolhido == "1" :
                Carros[0].VenderVeiculo()
            if carroEscolhido == "2" :
                Carros[1].VenderVeiculo()
            if carroEscolhido == "3" :
                Carros[2].VenderVeiculo()
            else:
                print("Modelo não encontrado!")
        if opcaoEscolhida2 == "3":
            Camionete.MostrarCamionetes()
            camioneteEscolhida = input("Insira a opção de camionete escolhida: ")
            if camioneteEscolhida == "1" :
                Camionetes[0].VenderVeiculo()
            if camioneteEscolhida == "2" :
                Camionetes[1].VenderVeiculo()
            if camioneteEscolhida == "3" :
                Camionetes[2].VenderVeiculo()
            else:
                print("Modelo não encontrado!")
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
        if opcaoEscolhida2 == "2":
            Carro.MostrarCarros()
        if opcaoEscolhida2 == "3":
            Camionete.MostrarCamionetes()
        if opcaoEscolhida2 == "4":
            Veiculo.mostrarTodos()
        if opcaoEscolhida2 == "5":
            continue

    elif opcaoEscolhida == "3" :
        Veiculo.mostrarTodosVendidos()

    elif opcaoEscolhida == "4" :
        Veiculo.mostrarTodos()

    elif opcaoEscolhida == "5" :
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