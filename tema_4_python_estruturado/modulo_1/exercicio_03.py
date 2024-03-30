"""
Implementar uma solução em Python que resolva a seguinte questão:

- Calcular o valor de uma compra, sendo que o preço unitário é R$10,00

- Se for feita uma compra de até 10 unidades, não há descontos.
- Para compras entre 11 e 20 unidades é dado um desconto de 10%.
- Acima de 20 Unidades, é dado um desconto de 20%
"""

quantidade = eval(input('Digite a quantidade de produtos: '))

preco_unitario = 10
c_DESCONTO10 = 0.1
c_DESCONTO20 = 0.2

if quantidade <= 10:
    total = preco_unitario * quantidade
elif quantidade <= 20:
    total = preco_unitario * quantidade *(1-c_DESCONTO10)
else:
    total = preco_unitario * quantidade *(1-c_DESCONTO20)

print(f'O total da compra é de: R${total}')