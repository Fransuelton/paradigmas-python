"""
Implementar uma solução em Python para visualizar dados de vendas de produtos em um gráfico de barras.

Por exemplo, utilize os seguintes dados:

x=["A","B","C","D"]
y=[3,8,1,10]

"""

# Minha solução

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [3, 8, 1, 10]

plt.bar(categorias, valores)

plt.title('Gráfico de Barras em Python')
plt.xlabel('Categorias')
plt.ylabel('Valores')

plt.show()

# Solução do Exercício

import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()