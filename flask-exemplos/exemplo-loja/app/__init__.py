from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'   # para onde mandar quem não está logado
login_manager.login_message = 'Faça login para acessar esta página.'


def create_app():
    app = Flask(__name__)
    app.secret_key = 'troque-esta-chave-em-producao'

    login_manager.init_app(app)

    from app.auth import auth
    from app.loja import loja
    app.register_blueprint(auth)
    app.register_blueprint(loja)

    return app


# Flask-Login chama esta função a cada requisição para
# "recarregar" o usuário a partir do id guardado na sessão
@login_manager.user_loader
def carregar_usuario(user_id):
    from app.models import Usuario
    return Usuario.buscar_por_id(user_id)
