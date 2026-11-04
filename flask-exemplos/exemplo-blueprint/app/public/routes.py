from app.public import public
from flask import render_template

@public.route('/')
def inicio():
    return render_template('index.html')

@public.route('/contato')
def contato():
    return render_template('contato.html')