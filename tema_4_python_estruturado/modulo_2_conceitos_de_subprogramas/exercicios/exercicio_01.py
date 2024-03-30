# Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista

# Minha resolução
def soma_elementos_pares(lista):
    total = 0
    for elemento in lista:
        if elemento % 2 == 0:
            total += elemento
    return total


lista_teste = [10, 2, 5, 7, 6, 3]

print(f"A soma total dos números pares na lista é: {soma_elementos_pares(lista_teste)}")

# Solução

def ehPar(n):
    r = (n%2==0)
    return r


def somar_par(lst):
    soma = 0
    for num in lst:
        if(ehPar(num)):
            soma=soma+num
    return soma


soma = somar_par(lista_teste)
print(f'O somatório dos elementos pares da lista é: {soma}')
