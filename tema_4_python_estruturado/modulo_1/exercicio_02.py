"""
Implementar uma solução em Python que resolva a seguinte questão:

- Se a nota for maior ou igual a 7, o estudante foi aprovado.
- Se a nota for menor que 7 e maior ou igual a 5, o estudante está em recuperação.
- Se a nota for menor que 5, o estudante está reprovado.
"""

nota = eval(input("Informe a nota do estudante: "))

if nota >= 7:
    situacao = "Aprovado"
elif nota >= 5:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

print(f'O estudante com a nota {nota} está: {situacao}')
