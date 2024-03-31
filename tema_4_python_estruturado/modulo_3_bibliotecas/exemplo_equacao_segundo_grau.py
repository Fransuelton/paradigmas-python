# Implementar uma solução em python que calcule as raízes de uma equação do segundo grau.

# Exemplo: dada a equação x² + 5x + 6 = 0, as raízes são {-3,-2}.

def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente


def calc_delta(a,b,c):
    delta=b*b-4*a*c
    return delta


import numpy as np
def calcular_raizes(a,b,c,delta):
    if delta<0:
        resultado='a equação não possui raízes nos números reais'
    elif delta==0:
        x=-b/(2*a)
        resultado=f'a equação possui apenas a raiz: {x}'
    else:
        x1=(-b-np.sqrt(delta))/(2*a)
        x2=(-b+np.sqrt(delta))/(2*a)
        resultado=f'a equação possui as raízes: {x1}, {x2}'
    return resultado


#f(x)=ax^2+bx+c
a=entrada_dados()
b=entrada_dados()
c=entrada_dados()

delta=calc_delta(a,b,c)

resultado=calcular_raizes(a,b,c,delta)
print(resultado)