from flask import Flask, render_template, request

app = Flask(__name__)
SENHAS_PAGINAS = {
    'dsagshdg': 'pages/page1.html',
    'wptmrqr': 'pages/page2.html',
    'sgtppr': 'pages/page3.html',
    'hgjdpm': 'pages/page4.html',
    'piggapigga': 'pages/page5.html',
    'negao': 'pages/page6.html'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/acesso', methods=['POST'])
def acesso():
    senha_digitada = request.form.get('senha', '').strip().lower()
    if senha_digitada in SENHAS_PAGINAS:
        return render_template(SENHAS_PAGINAS[senha_digitada])
    else:
        return render_template('pages/newyear.html')

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

if __name__ == '__main__':
    app.run(debug=True)