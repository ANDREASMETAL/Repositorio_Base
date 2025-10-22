from flask import Flask

app = Flask(__name__) #um app com flask

@app.route('/')
def index():
    return'Ola mundo'

@app.route('/sobre')
def sobre():
    return'Meu nome e andreas. sou aprendiz python'

@app.route('/cumprimentar/<nome>')
def cumprimentar(nome):
    return f'Ola {nome}'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'o dobro do {numero} é {numero*2}'

if __name__ == '__main__':
    app.run(debug=True)