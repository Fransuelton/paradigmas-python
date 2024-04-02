# Implementar um programa Python para criar uma classe Veiculo com atributos de instância,
# "velocidade máxima" e "quilômetros percorridos por litro".

class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro
# Aqui a solução principal já foi finalizada
    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')
        print(f'Quilômetros percorridos por litro = {self.quilometro_litro}')


modelo_carro = Veiculo("fusca", 180, 10)
modelo_carro.toStr()