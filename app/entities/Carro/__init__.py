from entities.Veiculo import Veiculo
from entities.Arrays import Carros, Veiculos

class Carro(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, total_portas: int, modo: str, potencia: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.modo = modo
        self.potencia = potencia

    def CadastrarCarro(data_fabricado, nome, placa, valor, cor, total_portas, modo, potencia):
        Carros.append(Carro(data_fabricado, nome, placa, valor, cor, total_portas, modo, potencia))
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


# ------------------------------------------------------------------------
# Carros já instanciados para exemplo.
Carro.CadastrarCarro("1969", "Ford Mustang GT", "KUT3379", 126100, "Preto", 2, "Gasolina", 130)
Carro.CadastrarCarro("2022", "Rimac Nevera", "IGM9344", 12000000, "Vermelho", 2, "Flex", 1914)
Carro.CadastrarCarro("2006", "Lamborghini Gallardo", "GIX7698", 500000, "Laranja", 2, "Gasolina", 560)
# ------------------------------------------------------------------------
