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

@app.route('/page3')
def page3():
    return render_template('pages/page3.html')

@app.route('/page4')
def page4():
    return render_template('pages/page4.html')

@app.route('/page5')
def page5():
    return render_template('pages/page5.html')
