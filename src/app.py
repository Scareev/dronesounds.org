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

@app.route('/pages/content')
def content():
    return render_template('pages/content.html')

@app.route('/pages/newyear')
def newyear():
    return render_template('pages/newyear.html')


@app.route('/page1')
def page1():
    return render_template('pages/page1.html')


@app.route('/page2')
def page2():
    return render_template('pages/page2.html')