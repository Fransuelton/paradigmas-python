# Implementar uma solução em Python que retorne o menor elemento de uma lista

def encontar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo


lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontar_minimo(lista_teste)
print("O menor elemento da lista é: [{}]".format(menor))