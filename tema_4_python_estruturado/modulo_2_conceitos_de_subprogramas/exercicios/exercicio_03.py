# Implementar uma solução em Python que determine se um Número é ou não Primo.

def eh_primo(n):
    if(n < 2):
        return False
    i = n // 2
    while(i > 1):
        if(n % i == 0):
            return False
        i -= 1
    return True

def imprimir_resultado(numero, resultado):
    if(resultado):
        mensagem = f'O número {numero} é primo'
    else:
        mensagem = f'O número {numero} não é primo'
    return mensagem

numero = 4
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)