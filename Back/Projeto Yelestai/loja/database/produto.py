from app import db, ma, api
from sqlalchemy import Integer, String, Float

class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer)
    url_img = db.Column(db.String)
    detalhes = db.Column(db.String)
