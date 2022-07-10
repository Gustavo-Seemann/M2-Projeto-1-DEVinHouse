from entities.Veiculo import Veiculo
from entities.Arrays import Motos, Veiculos

class Moto(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, potencia: int, numero_rodas: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.potencia = potencia
        self.numero_rodas = numero_rodas

    def CadastrarMoto(data_fabricado, nome, placa, valor, cor, potencia, numero_rodas):
        Motos.append(Moto(data_fabricado, nome, placa, valor, cor, potencia, numero_rodas))
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


# ------------------------------------------------------------------------
# Motos já instanciadas para exemplo:
Moto.CadastrarMoto("2019", "Harley Davidson", "39AKB1", 39000, "Vermelha", 100, 2)
Moto.CadastrarMoto("2020", "Yamaha", "399BB1", 39300, "Azul", 130, 3)
Moto.CadastrarMoto("1999", "Honda", "319AZB", 15490, "Preta", 90, 2)
# ------------------------------------------------------------------------
