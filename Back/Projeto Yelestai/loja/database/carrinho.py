from app import db, ma, api
from sqlalchemy import Integer

class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer)
    id_produto = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)
    pedido_feito = db.Column(db.Integer)
    id_pedido = db.Column(db.Integer)
