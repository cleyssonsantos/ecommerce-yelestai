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
from ..database.usuario import Usuario
from .schema import UsuarioSchema


não tem nada salvo em outro lugar não? nao .-.  o projeto era só isso ta faltando oq?
eu lembro que vc tinha tirado esses pontos

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


def buscar_todos_usuarios(buscar_todos_usuarios):
    return usuarios_schema.dump(Usuario.query.all())


def cadastrar_usuario(cadastrar_usuario):
    senha_hash = bcrypt.hashpw(request.json['senha'].encode(), bcrypt.gensalt(12))
    usuario = Usuario(nome=request.json['nome'], email=request.json['email'], senha=senha_hash)
    db.session.add(usuario)
    db.session.commit()
    return {'message':'data added to database'}


def atualizar_usuario(self, id):
    
    usuario = Usuario.query.get(id)
    usuario.nome = request.json['nome']
    usuario.email = request.json['email']
    usuario.senha = request.json['senha']
    db.session.commit()
    return {'message':'data updated'}


def deletar_usuario(deletar_usuario):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return {'message': 'data deleted successfully'}


def login_do_usuario(self):
    dados_user =usuarios_schema.dump(Usuario.query.filter(Usuario.email == request.json['email']).all())
    try:
        senha = dados_user[0]['senha']
        isvalid = bcrypt.checkpw(request.json['senha'].encode(), senha.encode())
        if isvalid:
            nome = dados_user[0]['nome']
            email = dados_user[0]['email']
            id_user = dados_user[0]['id_usuario']
            dados = {'nome': nome, 'email': email, 'id_usuario': id_user}
            return {'status': True, 'message': dados}, 200
        return {'status': False, 'message': 'senha_invalida'}, 403 
    except Exception as e: # tratar erros
        return {'status': False, 'message': 'senha_invalida'}, 403 
