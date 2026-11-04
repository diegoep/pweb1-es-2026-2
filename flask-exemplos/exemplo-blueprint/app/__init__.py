from flask import Flask
from app.admin import admin
from app.public import public

def create_app():
    app = Flask(__name__)
    app.register_blueprint(public)
    app.register_blueprint(admin)
    return app