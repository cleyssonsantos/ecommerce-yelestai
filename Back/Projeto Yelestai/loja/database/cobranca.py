from app import db, ma, api
from sqlalchemy import Integer, String

class Cobranca(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer)
    numero_cartao = db.Column(db.String)
    nome_titular = db.Column(db.String)
    data_exp = db.Column(db.String)
    csv = db.Column(db.String)