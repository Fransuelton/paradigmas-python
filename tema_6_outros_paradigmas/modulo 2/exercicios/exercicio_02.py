"""
Implementar uma solução em Python, através do uso de Thread, que faça:

a. Inicie a execução de duas Threads;
b. A primeira Thread deve calcular o cubo de um número;
c. A segundda Thread deve calcular o quadrado de um número;
d. Coloque a primeira e a segunda threads para esperar,
   respectivamente, 3 e 2 segundos;
e. Informe a ordem da execução das threads
"""

from time import sleep
from threading import Thread


def calcular_cubo(tempo_espera, numero, mensagem):
    print(f'🚀 - Iniciando a {mensagem} para calcular o cubo de {numero}!')
    sleep(tempo_espera)
    print(f'✅ - {numero} ao cubo é: {numero ** 3}')


def calcular_quadrado(tempo_espera, numero, mensagem):
    print(f'🚀 - Iniciando a {mensagem} para calcular o quadrado de {numero}!')
    sleep(tempo_espera)
    print(f'✅ - {numero} ao quadrado é: {numero ** 2}')


thread1 = Thread(target=calcular_cubo, args=(3, 5, 'Execução da Thread'))
thread2 = Thread(target=calcular_quadrado, args=(2, 5, 'Execução da Thread'))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'🥳 - Tudo finalizado!')