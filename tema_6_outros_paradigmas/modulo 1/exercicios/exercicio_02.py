"""
Considere as listas abaixo:

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2,2,3,3]

Implementar uma solução através de programação funcional
para arredondar os valores da lista de números na mesma ordem da lista de precisão.
"""

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2, 2, 3, 3]

arredondamento = lambda x, y: round(x, y)

resultado = list(map(arredondamento, lista_numeros, lista_precisao))

print(resultado)
