import uuid

class Veiculo:
    def __init__(self, chassi: int, data_fabricado: str, nome: str, placa: str, valor: float, cpf_comprador: str, cor: str):
        self.__chassi = uuid.uuid4() 
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


class Camionete(Veiculo):
    def init(self, chassi: int, data_fabricado: str, nome: str, placa: str, valor: float, cpf_comprador: str, total_portas: int, cap_cacamba: int, potencia: int, modo: str ):
        super().__init__(chassi, data_fabricado, nome, placa, valor, cpf_comprador)
        self.cor = "Roxa"
        self.total_portas = total_portas
        self.cap_cacamba = cap_cacamba
        self.potencia = potencia
        self.modo = modo


while True:
    print(" ")
    print("========================================================")
    print("                     DEVinCar                           ")
    print("========================================================")
    print(" [1] - Vender carro.")
    print(" [2] - Ver carros disponiveis.")
    print(" [3] - Ver carros vendidos.")
    print(" [4] - Listar todos os veiculos.")
    print(" [5] - Para sair.")
    print("========================================================")
    print(" ")
    opcaoEscolhida = input("Digite a opção escolhida: ")
    print(" ")

    if opcaoEscolhida == "1" :
        cpfComprador = input("Digite o CPF do comprador: ")
        venderCarro()

    if opcaoEscolhida == "2" :
        print(" ")
        print(" [1] - Ver Motos/Triciclos.")
        print(" [2] - Ver Carros.")
        print(" [3] - Ver Camionetes.")
        print(" [4] - Ver Todos.")
        print(" [5] - Voltar.")
        print(" ")
        opcaoEscolhida2 = input("Digite a opção escolhida: ")
        print(" ")
        if opcaoEscolhida2 == "1":
            listaMotosDisponivel()
        if opcaoEscolhida2 == "2":
            listaCarrosDisponivel()
        if opcaoEscolhida2 == "3":
            listaCamionetesDisponivel()
        if opcaoEscolhida2 == "4":
            listaVeiculosDisponivel()
        if opcaoEscolhida2 == "5":
            continue


    if opcaoEscolhida == "3" :
        listaVeiculosVendidos()

    if opcaoEscolhida == "4" :
        listaTodosVeiculos()

    if opcaoEscolhida == "5" :
        print("Você saiu!")
        break

    else: 
        print("Opção Invalida!")
        print("Tente novamente!")
        continue