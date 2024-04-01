import datetime
from extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()  # Corrigido o atributo de data de abertura
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ["DEPOSITO", valor, datetime.datetime.today()])  # Corrigido a adição de transação

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["SAQUE", valor, datetime.datetime.today()])  # Corrigido a adição de transação
            return True

    def transfereValor(self, conta_destino, valor):  # Corrigido o nome do parâmetro
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            conta_destino.depositar(valor)  # Corrigido o nome do método e o acesso ao saldo
            self.saldo -= valor
            self.extrato.transacoes.append(
                ["TRANSFERENCIA", valor, datetime.datetime.today()])  # Corrigido a adição de transação
            return "Transferência Realizada"

    def gerar_saldo(self):  # Corrigido o nome do método e o acesso ao atributo "numero"
        print(f"Número: {self.numero}\nSaldo: {self.saldo}")
