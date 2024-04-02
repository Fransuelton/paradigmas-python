"""
Implementar uma solução em Python, através do uso de Thread, que faça:

a. Inicie a execução de duas Threads;
b. Coloque a primeira e a segunda threads para esperar, respectivamente
   3 e 2 segundos.
c. Informe a ordem da execução das threads
"""

# Minha solução

from time import sleep
from threading import Thread


def tarefa1(tempo_espera, mensagem):
    print(f'⌛ - Iniciando a tarefa 1 {mensagem}')
    sleep(tempo_espera)
    print(f'🎉 - Conclusão da tarefa 1 {mensagem}')


def tarefa2(tempo_espera, mensagem):
    print(f'⌛ - Iniciando a tarefa 2 {mensagem}')
    sleep(tempo_espera)
    print(f'🎉 - Conclusão da tarefa 2 {mensagem}')


thread1 = Thread(target=tarefa1, args=(3, 'Thread 1 em execução'))
thread2 = Thread(target=tarefa2, args=(2, 'Thread 2 em execução'))
thread1.start()
thread2.start()
print(f'🚀 - Aguardando pela execução das Thread 1 e 2')
thread1.join()
thread2.join()
print(f'🥳 - Concluido')


# Solução do Exercício

def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')


t1 = Thread(target=tarefa, args=(3, 'A')) # Instanciando a thread
t2 = Thread(target=tarefa, args=(2, 'B'))
t1.start() # Fazendo a thread funcionar
t2.start()
t1.join()  # esperar até completar a execução da thread 1
t2.join()  # esperar até completar a execução da thread 2
print("A execução foi concluída!")
