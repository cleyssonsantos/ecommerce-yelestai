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
from .schema import model, CobrancaSchema
from .cobranca import cobranca_schema, cobrancas_schema
from ..database.cobranca import Cobranca
from .cobranca import buscar_todas_cobrancas, cadastrar_cobranca, atualizar_cobranca, deletar_cobranca


ns_cobranca = api.namespace('cobranca', description='Responsável pelas Cobranças')


@ns_cobranca.route('/buscar')
class BuscarCobranca(Resource):
    def get(self):
        resp = buscar_todas_cobrancas(self)
        return (resp)

@ns_cobranca.route('/cadastrar')
class CadastrarCobranca(Resource):
    @ns_cobranca.expect(model)
    def post(self):
        resp = cadastrar_cobranca(self)
        return (resp)

@ns_cobranca.route('/atualizar/<int:id>')
class AtualizarCobranca(Resource):
    @ns_cobranca.expect(model)
    def put(self, id):
        resp = atualizar_cobranca(self, id)
        return (resp)

@ns_cobranca.route('/deletar/<int:id>')
class DeletarCobranca(Resource):
    def delete(self, id):
        resp = deletar_cobranca(self, id)
        return (resp)
