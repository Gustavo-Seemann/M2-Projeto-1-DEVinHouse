from uuid import uuid4
from entities.Transferencia import Transferencia
from entities.Arrays import Veiculos, TransferenciasRealizadas


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
        self.transferencia = "Ainda não vendido."

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
        self.transferencia = Transferencia(self.__dict__, cpf_cliente, self.valor)
        TransferenciasRealizadas.append(self.transferencia)
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
        if self.vendido == "VENDIDO":
            print(f"VENDIDO NA DATA DE: {self.transferencia.data}")

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
        Transferencia.MaiorMenorVenda()
        print("----------------------------------")

    @staticmethod
    def mostrarTodosDisponiveis():
        print("---------------------------------------")
        print("         VEICULOS DISPONIVEIS")
        print("---------------------------------------")
        for motos in Veiculos['motos']:
                if motos.vendido == "Disponivel" :
                    print(f"[{motos.vendido}] PLACA: [{motos.placa}] - Moto Modelo: {motos.nome}, {motos.data_fabricado}, de {motos.numero_rodas} rodas, com a Potência de: {motos.potencia} cavalos, Cor: {motos.cor}, possui o valor de R${motos.valor}")
        for carros in Veiculos['carros']:
            if carros.vendido == "Disponivel" :
                print(f"[{carros.vendido}] PLACA: [{carros.placa}] - Carro Modelo: {carros.nome}, {carros.data_fabricado}, de {carros.total_portas} de portas, Motor: {carros.modo} com a Potência de: {carros.potencia} cavalos, Cor: {carros.cor}, possui o valor de R${carros.valor}")
        for camionetes in Veiculos['camionetes']:
            if camionetes.vendido == "Disponivel" :
                print(f"[{camionetes.vendido}] PLACA: [{camionetes.placa}] - Camionete Modelo: {camionetes.nome}, {camionetes.data_fabricado}, Motor: {camionetes.modo} com a Potência de: {camionetes.potencia} cavalos, Caçamba com capacidade de {camionetes.cap_cacamba} litros, Cor: {camionetes.cor}, possui o valor de R$ {camionetes.valor}")
        print("")
        print("---------------------------------------")
