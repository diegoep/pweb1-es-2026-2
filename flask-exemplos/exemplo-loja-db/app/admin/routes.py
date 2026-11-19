from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from app.admin import admin
from app.models import db, Produto


# Roda antes de TODAS as rotas deste blueprint
@admin.before_request
@login_required
def exigir_admin():
    if not current_user.is_admin:
        abort(403)   # 403 = Proibido


@admin.route('/produtos')
def produtos():
    return render_template('admin/produtos.html', produtos=Produto.listar())


@admin.route('/produtos/novo', methods=['GET', 'POST'])
def novo_produto():
    if request.method == 'POST':
        produto = Produto(nome=request.form['nome'],
                          preco=float(request.form['preco']))
        db.session.add(produto)                    # INSERT
        db.session.commit()
        flash('Produto cadastrado.')
        return redirect(url_for('admin.produtos'))
    return render_template('admin/produto_form.html', produto=None)


@admin.route('/produtos/<int:id>/editar', methods=['GET', 'POST'])
def editar_produto(id):
    produto = db.get_or_404(Produto, id)
    if request.method == 'POST':
        produto.nome = request.form['nome']        # UPDATE: basta alterar
        produto.preco = float(request.form['preco'])
        db.session.commit()
        flash('Produto atualizado.')
        return redirect(url_for('admin.produtos'))
    return render_template('admin/produto_form.html', produto=produto)


@admin.route('/produtos/<int:id>/excluir', methods=['POST'])
def excluir_produto(id):
    produto = db.get_or_404(Produto, id)
    if produto.itens:
        flash('Este produto já foi vendido e não pode ser excluído.')
    else:
        db.session.delete(produto)                 # DELETE
        db.session.commit()
        flash('Produto excluído.')
    return redirect(url_for('admin.produtos'))
