"""
Implementar uma solução em Python com Flask que faça:

a. Exiba a mensagem: "Página principal" no endereço raiz de uma página web
b. Exiba a mensagem: "Olá, mundo!" no endereço "ola/" de uma página web
c. Exiba a mensagem: "Olá, usuário!" no endereço "ola/nome_do_usuario" de uma página web
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Página principal."


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return "Olá, " + nome + "!"


if __name__ == '__main__':
    app.run()
