# Mutabilidade
def sum(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(sum([2, 4, 6, 8, 10]))

# segundo exemplo
print('\nsegundo exemplo')
lista = ['ferrari']
lista.append('porsche')
print(lista)
