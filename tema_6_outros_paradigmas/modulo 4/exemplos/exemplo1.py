# treinamento supervisionado - classificação

from sklearn.tree import DecisionTreeClassifier

lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar = [[120, lisa], [140, lisa], [180, irregular], [200, irregular]]

resultado = [pera, pera, laranja, laranja]

# Gerar uma árvore de decisão
clf = DecisionTreeClassifier()

# Classificador
clf = clf.fit(pomar, resultado)

peso = 140
# 1 para lisa e 0 para irregular
superficie = 1

resultadousu = clf.predict([[peso, superficie]])

if resultadousu == 1:
    print('Pera')
else:
    print('Laranja')
