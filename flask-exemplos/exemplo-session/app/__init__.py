from flask import Flask
from app.main import main

def create_app():
    app = Flask(__name__)
    app.secret_key = 'LBoweEU15idyZLe7b5d4asRkccHTo55qG32m77amCbBvsTjvHdwa9DVRGqiL56Ui'
    app.register_blueprint(main)
    return app
