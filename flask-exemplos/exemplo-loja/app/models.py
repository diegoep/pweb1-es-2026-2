import csv
from pathlib import Path

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

PASTA_DADOS = Path(__file__).parent.parent / 'data'


# ---------- funções auxiliares de CSV ----------

def ler_csv(nome_arquivo):
    caminho = PASTA_DADOS / nome_arquivo
    if not caminho.exists():
        return []
    with open(caminho, newline='', encoding='utf-8') as arquivo:
        return list(csv.DictReader(arquivo))


def adicionar_linha_csv(nome_arquivo, campos, linha):
    caminho = PASTA_DADOS / nome_arquivo
    novo = not caminho.exists()
    with open(caminho, 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        if novo:
            escritor.writeheader()
        escritor.writerow(linha)


# ---------- modelos ----------

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = float(preco)

    @staticmethod
    def listar():
        return [Produto(**linha) for linha in ler_csv('produtos.csv')]

    @staticmethod
    def buscar_por_id(id):
        for produto in Produto.listar():
            if produto.id == id:
                return produto
        return None


class Usuario(UserMixin):
    # UserMixin já fornece: is_authenticated, is_active, get_id() ...
    CAMPOS = ['id', 'nome', 'email', 'senha_hash']

    def __init__(self, id, nome, email, senha_hash):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    @staticmethod
    def listar():
        return [Usuario(**linha) for linha in ler_csv('usuarios.csv')]

    @staticmethod
    def buscar_por_id(id):
        for usuario in Usuario.listar():
            if usuario.id == id:
                return usuario
        return None

    @staticmethod
    def buscar_por_email(email):
        for usuario in Usuario.listar():
            if usuario.email == email:
                return usuario
        return None

    @staticmethod
    def criar(nome, email, senha):
        novo_id = str(len(Usuario.listar()) + 1)
        usuario = Usuario(novo_id, nome, email, generate_password_hash(senha))
        adicionar_linha_csv('usuarios.csv', Usuario.CAMPOS, vars(usuario))
        return usuario


class Pedido:
    CAMPOS = ['usuario_id', 'produto', 'quantidade', 'subtotal']

    @staticmethod
    def salvar(usuario_id, itens):
        for item in itens:
            adicionar_linha_csv('pedidos.csv', Pedido.CAMPOS, {
                'usuario_id': usuario_id,
                'produto': item['produto'].nome,
                'quantidade': item['quantidade'],
                'subtotal': f"{item['subtotal']:.2f}",
            })

    @staticmethod
    def do_usuario(usuario_id):
        return [p for p in ler_csv('pedidos.csv') if p['usuario_id'] == usuario_id]
