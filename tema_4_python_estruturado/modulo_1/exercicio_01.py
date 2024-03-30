# Implementar uma solução em Python que verifique se um Número é par ou ímpar

numero = eval(input('Digite um número: '))

if numero % 2 == 0:
    resultado = "Par"
else:
    resultado = "ímpar"

print(f'O número {numero} é {resultado}')