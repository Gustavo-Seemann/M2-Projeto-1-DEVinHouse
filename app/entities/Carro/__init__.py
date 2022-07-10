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
Carro.CadastrarCarro("1969", "Ford Mustang", "B9318C", 278000, "Preto", 2, "Gasolina", 483)
Carro.CadastrarCarro("1990", "Ford Mustang GT", "LC319C", 385000, "Cinza", 2, "Gasolina", 490)
Carro.CadastrarCarro("2010", "Lamborghini", "C1C9LK", 560000, "Laranja", 2, "Flex", 433)
# ------------------------------------------------------------------------
