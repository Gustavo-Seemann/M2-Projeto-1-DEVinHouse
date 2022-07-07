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

    def mostrarTodos():
        for motos in Veiculos['motos']:
                print(f"Moto Modelo: {motos['nome']}, {motos['data_fabricado']}, de {motos['numero_rodas']} rodas, com a Potência de: {motos['potencia']} cavalos, Placa: {motos['placa']}, Cor: {motos['cor']}, possui o valor de R${motos['valor']}")
        for carros in Veiculos['carros']:
            print(f"Carro Modelo: {carros['nome']}, {carros['data_fabricado']}, de {carros['total_portas']} de portas, Motor: {carros['modo']} com a Potência de: {carros['potencia']} cavalos, Placa: {carros['placa']}, Cor: {carros['cor']}, possui o valor de R${carros['valor']}")
        for camionetes in Veiculos['camionetes']:
            print(f"Camionete Modelo: {camionetes['nome']}, {camionetes['data_fabricado']}, Motor: {camionetes['modo']} com a Potência de: {camionetes['potencia']} cavalos, Caçamba com capacidade de {camionetes['cap_cacamba']} litros, Placa: {camionetes['placa']}, Cor: {camionetes['cor']}, possui o valor de R$ {camionetes['valor']}")



class Moto(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, potencia: int, numero_rodas: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.potencia = potencia
        self.numero_rodas = numero_rodas
        
    def CadastrarMoto(self):
        moto = {
            'data_fabricado': self.data_fabricado,
            'nome': self.nome,
            'placa': self.placa,
            'valor': self.valor,
            'cor': self.cor,
            'potencia': self.potencia,
            'numero_rodas': self.numero_rodas,
            'chassi': self.chassi,
            'cpf_comprador': self.cpf_comprador,
            'vendido': self.vendido
        }
        Motos.append(moto)
        Veiculos['motos'] = Motos

    @staticmethod
    def MostrarMotos():
        for motos in Veiculos['motos']:
            print(f"Moto Modelo: {motos['nome']}, {motos['data_fabricado']}, de {motos['numero_rodas']} rodas, com a Potência de: {motos['potencia']} cavalos, Placa: {motos['placa']}, Cor: {motos['cor']}, possui o valor de R${motos['valor']}")



class Carro(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, total_portas: int, modo: str, potencia: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.modo = modo
        self.potencia = potencia

    def CadastrarCarro(self):
        carro = {
            'data_fabricado': self.data_fabricado,
            'nome': self.nome,
            'placa': self.placa,
            'valor': self.valor,
            'cor': self.cor,
            'total_portas': self.total_portas,
            'modo': self.modo,
            'potencia': self.potencia,
            'chassi': self.chassi,
            'cpf_comprador': self.cpf_comprador,
            'vendido': self.vendido
        }
        Carros.append(carro)
        Veiculos['carros'] = Carros

    @staticmethod
    def MostrarCarros():
        for carros in Veiculos['carros']:
            print(f"Carro Modelo: {carros['nome']}, {carros['data_fabricado']}, de {carros['total_portas']} de portas, Motor: {carros['modo']} com a Potência de: {carros['potencia']} cavalos, Placa: {carros['placa']}, Cor: {carros['cor']}, possui o valor de R${carros['valor']}")



class Camionete(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, total_portas: int, cap_cacamba: int, potencia: int, modo: str, cor = "Roxa"):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.cap_cacamba = cap_cacamba
        self.potencia = potencia
        self.modo = modo

    def CadastrarCamionetes(self):
        camionete = {
            'data_fabricado': self.data_fabricado,
            'nome': self.nome,
            'placa': self.placa,
            'valor': self.valor,
            'cor': self.cor,
            'total_portas': self.total_portas,
            'modo': self.modo,
            'cap_cacamba': self.cap_cacamba,
            'potencia': self.potencia,
            'chassi': self.chassi,
            'cpf_comprador': self.cpf_comprador,
            'vendido': self.vendido
        }
        Camionetes.append(camionete)
        Veiculos['camionetes'] = Camionetes

    @staticmethod
    def MostrarCamionetes():
        for camionetes in Veiculos['camionetes']:
            print(f"Camionete Modelo: {camionetes['nome']}, {camionetes['data_fabricado']}, Motor: {camionetes['modo']} com a Potência de: {camionetes['potencia']} cavalos, Caçamba com capacidade de {camionetes['cap_cacamba']} litros, Placa: {camionetes['placa']}, Cor: {camionetes['cor']}, possui o valor de R$ {camionetes['valor']}")




moto1 = Moto("2019", "Harley Davidson", "39AKB1", 39000, "Vermelha", 100, 2)
moto1.CadastrarMoto()
moto2 = Moto("2020", "Yamaha", "399BB1", 39300, "Azul", 130, 3)
moto2.CadastrarMoto()
moto3 = Moto("1999", "Honda", "319AZB", 15490, "Preta", 90, 2)
moto3.CadastrarMoto()
Moto.MostrarMotos()

carro1 = Carro("1969", "Ford Mustang", "B9318C", 278000, "Preto", 2, "Gasolina", 483)
carro1.CadastrarCarro()
carro2 = Carro("1990", "Ford Mustang GT", "LC319C", 385000, "Cinza", 2, "Gasolina", 490)
carro2.CadastrarCarro()
carro3 = Carro("2010", "Lamborghini", "C1C9LK", 560000, "Laranja", 2, "Flex", 433)
carro3.CadastrarCarro()
Carro.MostrarCarros()

camionete1 = Camionete("2020", "Mitsubishi L200 Triton", "KCZ1CL", 145000, 4, 6000, 400, "Diesel")
camionete1.CadastrarCamionetes()
camionete2 = Camionete("2021", "Chevrolet S10 Z71", "L3Z1MC", 185000, 4, 4000, 410, "Gasolina")
camionete2.CadastrarCamionetes()
camionete3 = Camionete("2018", "Fiat Toro", "Z351CL", 193200, 4, 5500, 390, "Diesel")
camionete3.CadastrarCamionetes()
Camionete.MostrarCamionetes()

print("RODOU!")


# while True:
#     print(" ")
#     print("========================================================")
#     print("                     DEVinCar                           ")
#     print("========================================================")
#     print(" [1] - Vender carro.")
#     print(" [2] - Ver carros disponiveis.")
#     print(" [3] - Ver carros vendidos.")
#     print(" [4] - Listar todos os veiculos.")
#     print(" [5] - Para sair.")
#     print("========================================================")
#     print(" ")
#     opcaoEscolhida = input("Digite a opção escolhida: ")
#     print(" ")

#     if opcaoEscolhida == "1" :
#         cpfComprador = input("Digite o CPF do comprador: ")
#         venderCarro()

#     if opcaoEscolhida == "2" :
#         print(" ")
#         print(" [1] - Ver Motos/Triciclos.")
#         print(" [2] - Ver Carros.")
#         print(" [3] - Ver Camionetes.")
#         print(" [4] - Ver Todos.")
#         print(" [5] - Voltar.")
#         print(" ")
#         opcaoEscolhida2 = input("Digite a opção escolhida: ")
#         print(" ")
#         if opcaoEscolhida2 == "1":
#             listaMotosDisponivel()
#         if opcaoEscolhida2 == "2":
#             listaCarrosDisponivel()
#         if opcaoEscolhida2 == "3":
#             listaCamionetesDisponivel()
#         if opcaoEscolhida2 == "4":
#             listaVeiculosDisponivel()
#         if opcaoEscolhida2 == "5":
#             continue


#     if opcaoEscolhida == "3" :
#         listaVeiculosVendidos()

#     if opcaoEscolhida == "4" :
#         Veiculo.MostrarTodos()

#     if opcaoEscolhida == "5" :
#         print("Você saiu!")
#         break

#     else: 
#         print("Opção Invalida!")
#         print("Tente novamente!")
#         continue