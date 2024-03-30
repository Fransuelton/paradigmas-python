"""
Implementar uma solução em Python que some todos os números pares de uma lista.

Por exemplo, se a lista for [10,2,5,7,6,3], o resultado deve ser igual a 18.
"""

# Minha resolução

lista = [10, 2, 5, 7, 6, 3]

total = 0

for valor in lista:

    if valor % 2 == 0:
        total += valor

print(f'A soma total dos números pares na lista e dé: {total}')

# Solução - Estratégia 01

lista = [10, 3, 8, 6, 9, 43]

n = len(lista) # Aqui está sendo calculado a quantidade de itens na lista utilizando o método len

soma = 0 # Variável auxiliar para acumular a soma

# Aqui estamos percorrendo os elementos dentro de um range (intervalo). Ex.: 0,1,2,3,4,5
for i in range(n):
    if lista[i] % 2 == 0:
        soma = soma + lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')

# Solução - Estratégia 02

lista = [10, 2, 5, 6, 7, 13]

soma = 0

for num in lista:
    if num % 2 == 0:
        soma = soma + num
print(f'O somatório dos elementos pares da lista é: {soma}')