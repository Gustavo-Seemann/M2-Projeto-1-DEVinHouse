from datetime import datetime
from entities.Arrays import TransferenciasRealizadas

class Transferencia:
    def __init__(self, dados_veiculo, cpf_comprador, valor):
        self.dados_veiculo = dados_veiculo
        self.cpf_comprador = cpf_comprador
        self.valor = valor
        self.data =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @staticmethod
    def MaiorMenorVenda():
        print("----------------------------")
        print("    MAIOR VALOR DE VENDA")
        print("----------------------------")
        maiorPreco = 0
        for preco in TransferenciasRealizadas:
            if preco.valor >= maiorPreco:
                maiorPreco = preco.valor
        print(f"O maior valor de venda realizado foi R${maiorPreco}!")
        result = [x for x in TransferenciasRealizadas if x.valor == maiorPreco]
        for transferencia in result:
            print(f"VEÍCULO: {transferencia.dados_veiculo['nome']}, PLACA: {transferencia.dados_veiculo['placa']}, CPF DO COMPRADOR: {transferencia.cpf_comprador}, REALIZADA EM: {transferencia.data}")
        print("----------------------------")
        print("    MENOR VALOR DE VENDA")
        print("----------------------------")
        menorPreco = maiorPreco
        for preco in TransferenciasRealizadas:
            if preco.valor < menorPreco:
                menorPreco = preco.valor
        print(f"E o menor valor de venda realizado foi R${menorPreco}!")
        result2 = [x for x in TransferenciasRealizadas if x.valor == menorPreco]
        for transferencia in result2:
            print(f"VEÍCULO: {transferencia.dados_veiculo['nome']}, PLACA: {transferencia.dados_veiculo['placa']}, CPF DO COMPRADOR: {transferencia.cpf_comprador}, REALIZADA EM: {transferencia.data}")