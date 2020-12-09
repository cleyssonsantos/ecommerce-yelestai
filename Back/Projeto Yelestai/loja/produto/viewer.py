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
from .schema import model, ProdutoSchema
# from .schema import produto_schema, produtos_schema
from ..database.produto import Produto
from .produto import buscar_todos_produtos, buscar_produto_pelo_id, cadastrar_produto, atualizar_produto, deletar_produto
from .produto import produto_schema, produtos_schema


ns_produto = api.namespace('produto', description='Responsável pelos Produtos')


@ns_produto.route('/buscar')
class BuscarProduto(Resource):
    def get(self):
        resp = buscar_todos_produtos(buscar_todos_produtos)
        return (resp)

@ns_produto.route('/buscar/<string:id>')
class BuscarProdutoID(Resource):
    def get(self, id):
        resp = buscar_produto_pelo_id(self, id)
        return (resp)

@ns_produto.route('/cadastrar')
class CadastrarProduto(Resource):
    @ns_produto.expect(model)
    def post(self):
        resp = cadastrar_produto(cadastrar_produto)
        return (resp)

@ns_produto.route('/atualizar/<int:id>')
class AtualizarProduto(Resource):
    @ns_produto.expect(model)
    def put(self, id):
        resp = atualizar_produto(self, id)
        return (resp)

@ns_produto.route('/deletar/<int:id>')
class DeletarProduto(Resource):
    def delete(self, id):
        resp = deletar_produto(self, id)
        return (resp)
