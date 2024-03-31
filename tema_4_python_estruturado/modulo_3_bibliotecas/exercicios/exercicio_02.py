# Implementar uma solução em Python para gerar 1000 pontos seguindo a distribuição Normal com média 20 e desvio-padrão 2.
# Além disso, exiba os dados em um histograma.

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
plt.hist(dados, color="lightblue", ec="red")
