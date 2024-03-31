# POO no Python

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
    def set_nome(self, nome):
        self.nome=nome
    def set_ender(self, ender):
        self.ender=ender
    def get_nome(self):
        return self.nome
    def get_ender(self):
        return self.ender


# Objeto pessoa

pessoa1 = Pessoa("maria","rua 01234")
pessoa2 = Pessoa("joão","rua 56789")

# Imprimir cada um dos objetos

print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')