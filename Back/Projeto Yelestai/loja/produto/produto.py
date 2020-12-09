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

from .schema import ProdutoSchema
from ..database.produto import Produto 

produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)

def buscar_todos_produtos(buscar_todos_produtos):
    return jsonify(produtos_schema.dump(Produto.query.all()))


def buscar_produto_pelo_id(self, id):
    produto = produtos_schema.dump(Produto.query.filter(Produto.id_produto == id).all())
    try:
        produto = produto[0]
        return {'status': True, 'message': 'produto_encontrado', 'info': produto}, 200
    except Exception as e: # tratar erros
        return {'status': False, 'message': 'produto_nao_encontrato', 'info': []}, 403


def cadastrar_produto(cadastrar_produto):
    produto = Produto(nome=request.json['nome'], preco=request.json['preco'], estoque=request.json['estoque'], url_img=request.json['url_img'], detalhes=request.json['detalhes'])
    db.session.add(produto)
    db.session.commit()
    return {'message':'data added to database'}


def atualizar_produto (self, id):
    produto = Produto.query.get(id)
    produto.nome = request.json['nome']
    produto.preco = request.json['preco']
    produto.estoque = request.json['estoque']
    produto.url_img = request.json['url_img']
    produto.detalhes = request.json['detalhes']
    db.session.commit()
    return {'message':'data updated'}


def deletar_produto(self, id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return {'message': 'data deleted successfully'}
