from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pages/contato')
def contato():
    return render_template('pages/contato.html')

@app.route('/pages/sobrenos')
def sobrenos():
    return render_template('pages/sobrenos.html')