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
Moto.CadastrarMoto("2019", "Yamaha YZF-R3", "HVG9437", 23990, "Vermelha", 42, 2)
Moto.CadastrarMoto("2020", "Kawasaki Ninja ZX-6R 636", "IGO1606", 49900, "Verde", 130, 2)
Moto.CadastrarMoto("2018", "BMW R 1200 GS", "JNQ3477", 73300, "Preta", 125, 2)
# ------------------------------------------------------------------------
