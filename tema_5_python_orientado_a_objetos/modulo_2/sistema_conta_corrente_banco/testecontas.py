from conta import Conta
from cliente import Cliente

cliente1 = Cliente(123, "João", "Rua 01")
cliente2 = Cliente(345, "Maria", "Rua 02")
cliente3 = Cliente(634, "Antonio", "Rua 83")
cliente4 = Cliente(563, "Juliana", "Rua 32")

conta1 = Conta([cliente1, cliente2], 1, 0)
conta2 = Conta([cliente3, cliente4], 2, 500)

conta1.depositar(1500)
conta1.sacar(100)
conta1.extrato.extrato(conta1.numero)
