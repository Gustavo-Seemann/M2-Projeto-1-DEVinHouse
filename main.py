class Veiculo:
    def __init__(self, chassi: int, data_fabricado: str, nome: str, placa: str, valor: float, cpf_comprador: str, cor: str):
        self.__chassi = chassi
        self.data_fabricado = data_fabricado
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.__cpf_comprador = 0
        self.cor = cor

class Moto(Veiculo):
    def init(self, chassi: int, data_fabricado: str, nome: str, placa: str, valor: float, cpf_comprador: str, cor: str, potencia: int, numero_rodas: int):
        super().__init__(chassi, data_fabricado, nome, placa, valor, cpf_comprador, cor)
        self.potencia = potencia
        self.numero_rodas = numero_rodas

class Carro(Veiculo):
    def init(self, chassi: int, data_fabricado: str, nome: str, placa: str, valor: float, cpf_comprador: str, cor: str, total_portas: int, modo: str, potencia: int):
        super().__init__(chassi, data_fabricado, nome, placa, valor, cpf_comprador, cor)
        self.total_portas = total_portas
        self.modo = modo
        self.potencia = potencia