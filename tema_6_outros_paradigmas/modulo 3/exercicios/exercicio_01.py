"""
Implementar uma solução em Python com Flask que faça:

a. Exiba a mensagem: "Olá, programadores!" no endereço raiz de uma
   página web e apareça o link "/user/Usuário"
b. Exiba a mensagem: "Olá, Usuário!" no endereço "/user/" e exiba
   a mensagem "Altere o endereço do browser e recarregue a página"
c. Exiba a mensagem: "Olá, nome_usuário!" no endereço "/user/nome_do_usuario"
   de uma página web
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Olá, programadores!"


@app.route('/user/')
@app.route('/user/<name>')
def user(name="Usuário"):
    if (name == "Usuário"):
        return "Altere o endereço do browser e recarregue a página"
    else:
        return "Olá, " + name + "!"


if __name__ == '__main__':
    app.run()
