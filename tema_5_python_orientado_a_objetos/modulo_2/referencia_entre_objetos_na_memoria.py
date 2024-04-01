class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerarextrato(self):
        print(f"numero:{self.numero}\n     cpf:{self.cpf}\n saldo:{self.saldo}")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
        return ("Transferencia Realizada")


conta1 = Conta(1, 123, 'Joao', 0)
conta2 = Conta(3, 456, 'Maria', 0)
conta1.depositar(1000)
conta1.transfereValor(conta2, 500)
print(conta1.saldo)
print(conta2.saldo)
