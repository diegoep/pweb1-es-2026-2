from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.auth import auth
from app.models import Usuario


@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if Usuario.buscar_por_email(email):
            flash('Este e-mail já está cadastrado.')
            return redirect(url_for('auth.cadastro'))

        Usuario.criar(nome, email, senha)
        flash('Conta criada! Agora faça login.')
        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario.buscar_por_email(request.form['email'])

        if usuario and usuario.verificar_senha(request.form['senha']):
            login_user(usuario)                  # guarda o id na sessão
            flash(f'Bem-vindo(a), {usuario.nome}!')
            return redirect(url_for('loja.index'))

        flash('E-mail ou senha inválidos.')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.')
    return redirect(url_for('loja.index'))
