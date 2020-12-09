# aqui vai ficar as funções
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api, fields, Resource
import werkzeug.security
import bcrypt
from functools import wraps
from flask_cors import CORS
from sqlalchemy import func
from app import db, ma, api
from .schema import CobrancaSchema
from ..database.cobranca import Cobranca

cobranca_schema = CobrancaSchema()
cobrancas_schema = CobrancaSchema(many=True)

def buscar_todas_cobrancas(self):
    return jsonify(cobrancas_schema.dump(Cobranca.query.all()))


def cadastrar_cobranca(self):
    cobranca = Cobranca(id_usuario=request.json['id_usuario'], numero_cartao=request.json['numero_cartao'], nome_titular=request.json['nome_titular'], data_exp=request.json['data_exp'], csv=request.json['csv'])
    db.session.add(cobranca)
    db.session.commit()
    return {'message':'data added to database'}


def atualizar_cobranca(self, id):
    cobranca = Cobranca.query.get(id)
    cobranca.id_usuario = request.json['id_usuario']
    cobranca.numero_cartao = request.json['numero_cartao']
    cobranca.nome_titular = request.json['nome_titular']
    cobranca.data_exp = request.json['data_exp']
    cobranca.csv = request.json['csv']
    db.session.commit()
    return {'message':'data updated'}


def deletar_cobranca(self, id):
    cobranca = Cobranca.query.get(id)
    db.session.delete(cobranca)
    db.session.commit()
    return {'message': 'data deleted successfully'}
