# Implementar uma solução em Python que faça o tratamento de exceção para verificar se a entrada é, de um fato, um número.

try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Entre com um número válido")