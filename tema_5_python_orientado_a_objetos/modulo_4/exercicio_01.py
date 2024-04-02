# Crie uma classe filha "Ônibus" que herdará todas as variáveis e métodos da classe "Veiculo".

class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')
        print(f'Quilômetros percorridos por litro = {self.quilometro_litro}')


class Onibus(Veiculo):
    pass


onibus_escolar = Onibus("Scania", 120, 8)
onibus_escolar.toStr()
