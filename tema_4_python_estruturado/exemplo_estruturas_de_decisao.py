numero1 = eval(input("Digite um número: "))
numero2 = eval(input("Digite outro número: "))

if numero1 > numero2:
    print(f'O número {numero1} é o maior')
else:
    print(f'O número {numero2} é o maior')

# Estratégia 01
a = 10
b = 20
if (a > b):
    maior = a
else:
    maior = b
print(f'O maior número é: {maior}')

# Estratégia 02
c = 10
d = 20
maior = a
if (b > maior):
    maior = b
print(f'O maior número é: {maior}')