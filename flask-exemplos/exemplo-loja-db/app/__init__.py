from flask import Flask
from flask_login import LoginManager

from app.models import db, Usuario, popular_banco

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Faça login para acessar esta página.'


def create_app():
    app = Flask(__name__)
    app.secret_key = 'troque-esta-chave-em-producao'
    # O arquivo loja.db é criado dentro da pasta instance/
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'

    db.init_app(app)
    login_manager.init_app(app)

    from app.auth import auth
    from app.loja import loja
    from app.admin import admin
    app.register_blueprint(auth)
    app.register_blueprint(loja)
    app.register_blueprint(admin)

    with app.app_context():
        db.create_all()      # cria as tabelas que ainda não existem
        popular_banco()      # dados iniciais (só se o banco estiver vazio)

    return app


@login_manager.user_loader
def carregar_usuario(user_id):
    return Usuario.buscar_por_id(user_id)
