from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        name = request.form['nome']
        return f'Olá{name}'
    
    return render_template('ex_4-1.html')

if __name__ == '__main__':
    app.run(debug=True)