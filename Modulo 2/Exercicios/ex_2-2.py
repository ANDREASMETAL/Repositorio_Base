from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Fabrica de pitão'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá {nome}'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro de {numero} é {numero*2}'

if __name__ == '__main__':
    app.run(debug=True)
