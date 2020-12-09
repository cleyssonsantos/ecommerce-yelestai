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

from ..database.endereco import Endereco
from .schema import EnderecoSchema

endereco_schema = EnderecoSchema()
enderecos_schema = EnderecoSchema(many=True)

def buscar_todos_enderecos(self):
    return jsonify(enderecos_schema.dump(Endereco.query.all()))


def cadastrar_endereco(self):
    endereco = Endereco(id_usuario=request.json['id_usuario'],rua=request.json['rua'], numero=request.json['numero'], cep=request.json['cep'], bairro=request.json['bairro'], municipio=request.json['municipio'], estado=request.json['estado'], pais=request.json['pais'])
    db.session.add(endereco)
    db.session.commit()
    return {'message':'data added to database'}


def atualizar_endereco(self, id):
    endereco = Endereco.query.get(id)
    endereco.id_usuario = request.json['id_usuario']
    endereco.rua = request.json['rua']
    endereco.numero = request.json['numero']
    endereco.cep = request.json['cep']
    endereco.bairro = request.json['bairro']
    endereco.municipio = request.json['municipio']
    endereco.estado = request.json['estado']
    endereco.pais = request.json['pais']
    db.session.commit()
    return {'message':'data updated'}


def deletar_endereco(self, id):
    endereco = Endereco.query.get(id)
    db.session.delete(endereco)
    db.session.commit()
    return {'message': 'data deleted successfully'}
