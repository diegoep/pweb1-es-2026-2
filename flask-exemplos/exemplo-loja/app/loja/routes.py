from flask import render_template, redirect, url_for, flash, session
from flask_login import login_required, current_user

from app.loja import loja
from app.models import Produto, Pedido


# O carrinho fica na sessão como um dicionário {id_do_produto: quantidade}
# Ex.: session['carrinho'] = {'1': 2, '3': 1}

def itens_do_carrinho():
    carrinho = session.get('carrinho', {})
    itens = []
    for produto_id, quantidade in carrinho.items():
        produto = Produto.buscar_por_id(produto_id)
        itens.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': produto.preco * quantidade,
        })
    return itens


@loja.route('/')
def index():
    return render_template('index.html', produtos=Produto.listar())


@loja.route('/carrinho/adicionar/<produto_id>', methods=['POST'])
def adicionar(produto_id):
    carrinho = session.get('carrinho', {})
    carrinho[produto_id] = carrinho.get(produto_id, 0) + 1
    session['carrinho'] = carrinho        # reatribuir avisa o Flask que mudou
    flash('Produto adicionado ao carrinho.')
    return redirect(url_for('loja.index'))


@loja.route('/carrinho/remover/<produto_id>', methods=['POST'])
def remover(produto_id):
    carrinho = session.get('carrinho', {})
    carrinho.pop(produto_id, None)
    session['carrinho'] = carrinho
    return redirect(url_for('loja.carrinho'))


@loja.route('/carrinho')
def carrinho():
    itens = itens_do_carrinho()
    total = sum(item['subtotal'] for item in itens)
    return render_template('carrinho.html', itens=itens, total=total)


@loja.route('/carrinho/finalizar', methods=['POST'])
@login_required                           # só usuário logado finaliza compra
def finalizar():
    itens = itens_do_carrinho()
    if not itens:
        flash('Seu carrinho está vazio.')
        return redirect(url_for('loja.carrinho'))

    Pedido.salvar(current_user.id, itens)
    session.pop('carrinho')
    flash('Pedido realizado com sucesso!')
    return redirect(url_for('loja.pedidos'))


@loja.route('/pedidos')
@login_required
def pedidos():
    return render_template('pedidos.html', pedidos=Pedido.do_usuario(current_user.id))
