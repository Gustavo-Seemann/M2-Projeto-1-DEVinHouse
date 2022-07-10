from entities.Veiculo import Veiculo
from entities.Arrays import Camionetes, Veiculos


class Camionete(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, total_portas: int, cap_cacamba: int, potencia: int, modo: str, cor = "Roxa"):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.cap_cacamba = cap_cacamba
        self.potencia = potencia
        self.modo = modo

    def CadastrarCamionetes(data_fabricado, nome, placa, valor, total_portas, cap_cacamba, potencia, modo):
        Camionetes.append(Camionete(data_fabricado, nome, placa, valor, total_portas, cap_cacamba, potencia, modo))
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


# ------------------------------------------------------------------------
# Camionetes já instaciadas para exemplo.
Camionete.CadastrarCamionetes("2020", "Mitsubishi L200 Triton", "KCZ1CL", 145000, 4, 6000, 400, "Diesel")
Camionete.CadastrarCamionetes("2021", "Chevrolet S10 Z71", "L3Z1MC", 185000, 4, 4000, 410, "Gasolina")
Camionete.CadastrarCamionetes("2018", "Fiat Toro", "Z351CL", 193200, 4, 5500, 390, "Diesel")
# ------------------------------------------------------------------------
