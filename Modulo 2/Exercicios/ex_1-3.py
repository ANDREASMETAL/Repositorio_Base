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

if __name__ == '__main__':
    app.run(debug=True)