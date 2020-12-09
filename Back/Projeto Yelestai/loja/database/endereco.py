from app import db, ma, api
from sqlalchemy import Integer, String

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer)
    rua = db.Column(db.String)
    numero = db.Column(db.String)
    cep = db.Column(db.String)
    bairro = db.Column(db.String)
    municipio = db.Column(db.String)
    estado = db.Column(db.String)
    pais = db.Column(db.String)