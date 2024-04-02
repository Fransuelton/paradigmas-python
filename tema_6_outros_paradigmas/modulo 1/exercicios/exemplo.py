# Considere a lista abaixo:

# veiculos = ['aviao', 'carro', 'navio', 'onibus']

# Implementar uma solução através de programação funcional para transformar todos os nomes em maiusculos.

veiculos = ['aviao', 'carro', 'navio', 'onibus']

f_maiuscula = lambda x: str.upper(x)

nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(f'nomes maiusculos = {nomes_maiusculos}')
