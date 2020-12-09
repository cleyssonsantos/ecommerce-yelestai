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

from ..database.carrinho import Carrinho
from .schema import CarrinhoSchema
from ..database.produto import Produto



carrinho_schema = CarrinhoSchema() # Passar os campos de carrinho com SQLAlchemy para JSON
carrinhos_schema = CarrinhoSchema(many=True) # retorno com JSON, o parâmetro many indica que será retornado um array

def buscar_todos_carrinhos(self):
    return jsonify(carrinhos_schema.dump(Carrinho.query.all()))


def buscar_carrinho_por_id(self, id_usuario):
        carrinhos = db.session.query(Carrinho, Produto).join(Produto, Carrinho.id_produto == Produto.id_produto).filter(Carrinho.id_usuario == id_usuario).filter(Carrinho.pedido_feito == 0).all()

        produtos = []
        todos_produtos = {}
        total = 0
        for carrinho in carrinhos:
            nome_produto = carrinho[1].nome
            preco_produto = carrinho[1].preco
            id_carrinho = carrinho[0].id
            img_produto = carrinho[1].url_img
            quantidade_produto = carrinho[0].quantidade
            total += preco_produto * quantidade_produto
            produtos.append({'nome': nome_produto,
                             'preco': preco_produto * quantidade_produto, 
                             'id_carrinho': id_carrinho, 
                             'quantidade_produto': quantidade_produto,
                             'img_produto': img_produto})
        
        todos_produtos['produtos'] = produtos
        todos_produtos['total'] = total

        try:
            return {'status': True, 'message': 'carrinho_encontrado', 'info': todos_produtos}, 200
        except Exception as e: # tratar erros
            return {'status': False, 'message': 'carrinho_nao_encontrado', 'info': []}, 403


def cadastrar_carrinho(self):
    carrinhos = db.session.query(Carrinho).filter(Carrinho.id_usuario == request.json['id_usuario']).filter(Carrinho.id_produto == request.json['id_produto']).first()
    if carrinhos:
        db.session.delete(carrinhos)
        db.session.commit()

    carrinho = Carrinho(id_usuario=request.json['id_usuario'], id_produto=request.json['id_produto'], quantidade=request.json['quantidade'], pedido_feito=request.json['pedido_feito'], id_pedido=request.json['id_pedido'])
    db.session.add(carrinho)
    db.session.commit()
    return {'message':'data added to database'}


def atualizar_carrinho(self, id):
    carrinho = Carrinho.query.get(id)
    carrinho.id_usuario = request.json['id_usuario']
    carrinho.id_produto = request.json['id_produto']
    carrinho.quantidade = request.json['quantidade']
    carrinho.pedido_feito = request.json['pedido_feito']
    carrinho.id_pedido = request.json['id_pedido']
    db.session.commit()
    return {'message':'data updated'}


def deletar_carrinho(self, id):
    carrinho = Carrinho.query.get(id)
    db.session.delete(carrinho)
    db.session.commit()
    return {'message': 'data deleted successfully'}
