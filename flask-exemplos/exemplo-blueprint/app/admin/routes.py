from app.admin import admin
from flask import render_template
from app.admin.service import recuperar_usuarios

@admin.route('/')
def inicio_admin():
    usuarios = recuperar_usuarios()
    return render_template('admin/index.html', usuarios=usuarios)