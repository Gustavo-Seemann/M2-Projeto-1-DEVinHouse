from uuid import uuid4

Veiculos = {'motos': 'teste', 'carros': 'teste2', 'camionete': 'teste3'}
Motos = []


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

class Carro(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, cor: str, total_portas: int, modo: str, potencia: int):
        super().__init__(data_fabricado, nome, placa, valor, cor)
        self.total_portas = total_portas
        self.modo = modo
        self.potencia = potencia


class Camionete(Veiculo):
    def __init__(self, data_fabricado: str, nome: str, placa: str, valor: float, total_portas: int, cap_cacamba: int, potencia: int, modo: str ):
        super().__init__(data_fabricado, nome, placa, valor)
        self.cor = "Roxa"
        self.total_portas = total_portas
        self.cap_cacamba = cap_cacamba
        self.potencia = potencia
        self.modo = modo

def MostrarMotos():
    for motos in Veiculos['motos']:
        print(motos['nome'])


moto1 = Moto("14/04/2019", "Harley Davidson", "39AKB1", 39000, "Vermelha", 1000, 2)
moto1.CadastrarMoto()
moto2 = Moto("14/04/2020", "Yamaha", "399BB1", 39300, "Azul", 1340, 3)
moto2.CadastrarMoto()
MostrarMotos()
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
#         listaTodosVeiculos()

#     if opcaoEscolhida == "5" :
#         print("Você saiu!")
#         break

#     else: 
#         print("Opção Invalida!")
#         print("Tente novamente!")
#         continue