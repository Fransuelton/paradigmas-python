# Disciplina - Paradigma de Linguagens de Programação em Python
# Características das variáveis em Python - Tema 3: Python Básico

# F-String

nome = "Python"

# Aqui estamos concatenando a string com a variável usando o método format
print('valor da variável = {}'.format(nome))

# Aqui estamos utilizando a f-string para concatenar usando antes das aspas a letra f
print(f'valor da variável = {nome}')

# Atribuição Múltipla

# Aqui a variável a recebe respectivamente 1 e a variável b recebe 2
a, b = 1, 2
print('Antes da troca')
print(f"O valor das variáveis: a={a}, b={b}")

# Primeira troca
temp = a
a = b
b = temp
print('Primeira troca')
print(f"O valor das variáveis: a={a}, b={b}")

# Segunda troca
a, b = b, a
print('Segunda troca')
print(f'O valor das variáveis: a={a}, b={b}')

# Operadores Compostos

# Exemplo 01
x = 10
print(f'x={x}')
x += 2
print(f'x={x}')
x -= 2
print(f'x={x}')

# Exemplo 02
y = 10
y *= 2
print(f'y={y}')
y /= 2
print(f'y={y}')
y %= 2
print(f'y={y}')

