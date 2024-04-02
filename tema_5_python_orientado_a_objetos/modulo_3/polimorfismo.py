class Argentina():
    def capital(self):
        print("Buenos Aires é a capital da Argentina.")

    def lingua_oficial(self):
        print("O espanhol é a língua oficial da Argentina.")


class Brasil():
    def capital(self):
        print("Brasília é a capital do Brasil.")

    def lingua_oficial(self):
        print("O português é a língua oficial do Brasil.")


obj_arg = Argentina()
obj_bra = Brasil()

for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()


# Mais um Exemplo de Polimorfismo

class Veiculo:
    def rodar(self):
        print("Reduz o consumo de combustível.")


class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veículo utiliza eletricidade.")


veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()
