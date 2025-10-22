from flask import Flask

app = Flask(__name__) #um app com flask

@app.route('/')
def index():
    return'Ola mundo'

if __name__ == '__main__':
    app.run(debug=True)