def fibo(n):
    'Determina o n-ésimo termo da sequência de Fibonacci'
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))


def func1(x):
    x = 10
    print(x)


x = 0
print(x)
func1(x)
print(x)