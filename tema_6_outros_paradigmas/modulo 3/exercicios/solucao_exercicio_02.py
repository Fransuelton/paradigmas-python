"""
Implementar uma solução em Python com Flask que faça:

a. Exiba a mensagem: "Olá, programadores!" no endereço raiz de uma página web e apareça a mensagem "Entre com dois números"
b. Exiba a mensagem: "0.0" no endereço "/somar/"
c. Exiba a mensagem: "30.0" no endereço "/somar/10/20" de uma página web
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    instr = '<p>Entre com dois números</p>'
    return boas_vindas + instr


@app.route('/somar/')
@app.route('/somar/<num01>/<num02>')
def soma(num01=0, num02=0):
    resultado = float(num01) + float(num02)
    return str(resultado)


if __name__ == '__main__':
    app.run(debug=True)
