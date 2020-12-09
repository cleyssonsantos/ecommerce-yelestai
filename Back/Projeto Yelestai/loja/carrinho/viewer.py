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
from .schema import model, CarrinhoSchema
from .carrinho import carrinho_schema, carrinhos_schema
from ..database.carrinho import Carrinho
from ..database.produto import Produto
from .carrinho import buscar_todos_carrinhos, buscar_carrinho_por_id, cadastrar_carrinho, atualizar_carrinho, deletar_carrinho


ns_carrinho = api.namespace('carrinho', description='Responsável pelo Carrinho')


@ns_carrinho.route('/buscar')
class BuscarCarrinho(Resource):
    def get(self):
        resp = buscar_todos_carrinhos(self)
        return (resp)

@ns_carrinho.route('/buscar/<string:id_usuario>')
class BuscarCarrinhoID(Resource):
    def get(self, id_usuario):
        resp = buscar_carrinho_por_id(self, id_usuario)
        return (resp)

@ns_carrinho.route('/cadastrar')
class CadastrarCarrinho(Resource):
    @ns_carrinho.expect(model)
    def post(self):
        resp = cadastrar_carrinho(self)
        return (resp)

@ns_carrinho.route('/atualizar/<int:id>')
class AtualizarCarrinho(Resource):
    @ns_carrinho.expect(model)
    def put(self, id):
        resp = atualizar_carrinho(self, id)
        return (resp)

@ns_carrinho.route('/deletar/<int:id>')
class DeletarCarrinho(Resource):
    def delete(self, id):
        resp = deletar_carrinho(self, id)
        return (resp)
