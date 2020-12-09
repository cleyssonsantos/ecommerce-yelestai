from app import db, ma, api
from sqlalchemy import Integer

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer)
    id_endereco = db.Column(db.Integer)
    id_pedido = db.Column(db.Integer)