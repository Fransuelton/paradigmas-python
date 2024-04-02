def sum(numeros):
    if not numeros:
        return 0
    primeiro = numeros[0]
    resto = numeros[1:]
    return primeiro + sum(resto)


print(sum([2, 4, 6, 8, 10]))

# segundo exemplo
print('\nsegundo exemplo')
lista = ['ferrari']
nova_lista = lista + ['porsche']
print(nova_lista)

# terceiro exemplo
print('\nterceiro exemplo')
import operator
print(operator.add(10, 20))

# quarto exemplo
print('\nquarto exemplo')
from functools import reduce
print(reduce(operator.add, [10, 20]))
print(reduce(operator.concat, ['Aprendendo reduce!']))
