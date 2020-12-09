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
from .schema import model, model_login
from ..database.usuario import Usuario
from .usuario import buscar_todos_usuarios, cadastrar_usuario, usuarios_schema, deletar_usuario, atualizar_usuario, login_do_usuario


ns_usuario = api.namespace('usuario', description='Responsável pelos Usuários')

@ns_usuario.route('/buscar')
class BuscarUsuario(Resource):
    def get(self):
        resp = buscar_todos_usuarios(buscar_todos_usuarios)
        return jsonify(resp)

@ns_usuario.route('/cadastrar')
class CadastrarUsuario(Resource):
    @ns_usuario.expect(model)
    def post(self):
        resp = cadastrar_usuario(cadastrar_usuario)
        return jsonify(resp)

@ns_usuario.route('/atualizar/<int:id>')
class AtualizarUsuario(Resource):
    @ns_usuario.expect(model)
    def put(self, id):
        resp = atualizar_usuario(self, id)
        return (resp)

@ns_usuario.route('/deletar/<int:id>')
class DeletarUsuario(Resource):
    def delete(self, id):
        resp = deletar_usuario(deletar_usuario)
        return jsonify(resp)

@ns_usuario.route('/login')
class LoginUsuario(Resource):
    @ns_usuario.expect(model_login)
    def post(self):
        resp = login_do_usuario(self)
        return (resp)
