class Veiculo:
    def __init__(self, chassi: int, data_fabricado: str, nome: str, placa: str, valor: float, cpf_comprador: str, cor: str):
        self.__chassi = chassi
        self.data_fabricado = data_fabricado
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.__cpf_comprador = cpf_comprador
        self.cor = cor
