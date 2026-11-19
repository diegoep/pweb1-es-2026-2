from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    @staticmethod
    def listar():
        return db.session.scalars(db.select(Produto).order_by(Produto.nome)).all()

    @staticmethod
    def buscar_por_id(id):
        return db.session.get(Produto, int(id))


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # um usuário tem vários pedidos  →  usuario.pedidos / pedido.usuario
    pedidos = db.relationship('Pedido', backref='usuario')

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    @staticmethod
    def buscar_por_id(id):
        return db.session.get(Usuario, int(id))

    @staticmethod
    def buscar_por_email(email):
        return db.session.scalar(db.select(Usuario).filter_by(email=email))

    @staticmethod
    def criar(nome, email, senha, is_admin=False):
        usuario = Usuario(nome=nome, email=email, is_admin=is_admin,
                          senha_hash=generate_password_hash(senha))
        db.session.add(usuario)
        db.session.commit()
        return usuario


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.now)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # um pedido tem vários itens  →  pedido.itens / item.pedido
    itens = db.relationship('ItemPedido', backref='pedido')

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens)

    @staticmethod
    def salvar(usuario, itens_carrinho):
        pedido = Pedido(usuario=usuario)
        for item in itens_carrinho:
            pedido.itens.append(ItemPedido(
                produto=item['produto'],
                quantidade=item['quantidade'],
                preco_unitario=item['produto'].preco,   # preço "congelado" na compra
            ))
        db.session.add(pedido)
        db.session.commit()
        return pedido


class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)

    produto = db.relationship('Produto', backref='itens')

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario


def popular_banco():
    if db.session.scalar(db.select(Produto)) is None:
        db.session.add_all([
            Produto(nome='Caneca IFPB', preco=25.00),
            Produto(nome='Camiseta Programação Web', preco=49.90),
            Produto(nome='Adesivo Flask', preco=5.50),
            Produto(nome='Caderno de Algoritmos', preco=18.00),
        ])
        db.session.commit()

    if Usuario.buscar_por_email('admin@loja.com') is None:
        Usuario.criar('Admin', 'admin@loja.com', 'admin', is_admin=True)
