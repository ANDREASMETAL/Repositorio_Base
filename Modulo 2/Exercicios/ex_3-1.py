from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome ='Andy'
    return render_template('ex_3-1.html', nome = nome )

if __name__ == '__main__':
    app.run(debug=True)
    