from app.main import main
from flask import request, session, render_template

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form["nome"]
        session["nome"] = nome
    return render_template('index.html')

@main.route('/carrinho', methods=['GET', 'POST'])
def carrinho():
    if request.method == 'POST':
        if "produtos" not in session:
            session["produtos"] = []
        produto = request.form["produto"]
        session["produtos"] = session["produtos"] + [produto]
    return render_template('carrinho.html')