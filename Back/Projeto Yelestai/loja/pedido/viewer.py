# aqui vai ficar as rotas
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api, fields, Resource
import werkzeug.security
import bcrypt
import yagmail
from functools import wraps
from flask_cors import CORS
from sqlalchemy import func
from app import db, ma, api
from .schema import model, PedidoSchema
# from .schema import pedido_schema, pedidos_schema
from ..database.pedido import Pedido
from ..database.produto import Produto
from ..database.carrinho import Carrinho
from ..database.usuario import Usuario
from .pedido import pedido_schema, pedidos_schema
from .pedido import buscar_todos_pedidos, cadastrar_pedido, atualizar_pedido, deletar_pedido, buscar_pedido_por_id


ns_pedido = api.namespace('pedido', description='Responsável pelos Pedidos')

@ns_pedido.route('/buscar')
class BuscarPedido(Resource):
    def get(self):
        resp = buscar_todos_pedidos(self)
        return (resp)

@ns_pedido.route('/buscar/<string:id_usuario>')
class BuscarPedidoID(Resource):
    def get(self, id_usuario):
        resp = buscar_pedido_por_id(id_usuario)
        return (resp)

@ns_pedido.route('/cadastrar')
class CadastrarPedido(Resource):
    @ns_pedido.expect(model)
    def post(self):
        resp = cadastrar_pedido(self)
        return (resp)
        

@ns_pedido.route('/atualizar/<int:id>')
class AtualizarPedido(Resource):
    @ns_pedido.expect(model)
    def put(self, id):
        resp = atualizar_pedido(self, id)
        return (resp)

@ns_pedido.route('/deletar/<int:id>')
class DeletarPedido(Resource):
    def delete(self, id):
        resp = deletar_pedido(self, id)
        return (resp)
