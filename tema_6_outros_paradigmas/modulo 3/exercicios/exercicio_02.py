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
    mensagem = '<p>Entre com dois números</p>'
    return boas_vindas + mensagem


@app.route('/somar/')
@app.route('/somar/<n1>/<n2>')
def user(n1=0, n2=0):
    personalizar = f'<h1>{int(n1) + int(n2)}</h1>'
    return personalizar


if __name__ == '__main__':
    app.run(debug=True)
