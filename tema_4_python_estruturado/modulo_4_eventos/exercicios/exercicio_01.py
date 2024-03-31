"""
Implementar uma solução em Python que faça o tratamento de exceção,
para verificar se uma entrada é numérica e que, além disso, insista
que o usuário digite um Número válido.
"""
while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entre com um número válido")
