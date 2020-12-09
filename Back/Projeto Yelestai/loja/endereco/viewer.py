# aqui vai ficar as rotas
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
from .schema import model, EnderecoSchema
from .endereco import endereco_schema, enderecos_schema
from ..database.endereco import Endereco
from .endereco import buscar_todos_enderecos, cadastrar_endereco, atualizar_endereco, deletar_endereco


ns_endereco = api.namespace('endereco', description='Responsável pelos Endereços')

@ns_endereco.route('/buscar')
class BuscarEndereco(Resource):
    def get(self):
        resp = buscar_todos_enderecos(self)
        return (resp)

@ns_endereco.route('/cadastrar')
class CadastrarEndereco(Resource):
    @ns_endereco.expect(model)
    def post(self):
        resp = cadastrar_endereco(self)
        return (resp)

@ns_endereco.route('/atualizar/<int:id>')
class AtualizarEndereco(Resource):
    @ns_endereco.expect(model)
    def put(self, id):
        resp = atualizar_endereco(self, id)
        return (resp)

@ns_endereco.route('/deletar/<int:id>')
class DeletarEndereco(Resource):
    def delete(self, id):
        resp = deletar_endereco(self, id)
        return (resp)
