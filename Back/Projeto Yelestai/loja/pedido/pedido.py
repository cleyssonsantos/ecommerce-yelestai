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

from .schema import PedidoSchema
from ..database.pedido import Pedido
from ..database.produto import Produto
from ..database.carrinho import Carrinho
from ..database.usuario import Usuario
import yagmail



pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)


def buscar_todos_pedidos(self):
    return jsonify(pedidos_schema.dump(Pedido.query.all()))


def buscar_pedido_por_id(id_usuario):
    carrinhos = db.session.query(Carrinho, Pedido, Produto).join(Pedido, Carrinho.id_usuario == Pedido.id_usuario)\
                    .join(Produto, Carrinho.id_produto == Produto.id_produto).filter(Carrinho.id_usuario == id_usuario)\
                    .filter(Carrinho.pedido_feito == 1).group_by(Carrinho).all()
    produtos = []
    todos_produtos = {}
    total = 0
    for carrinho in carrinhos:
        nome_produto = carrinho[2].nome
        preco_produto = carrinho[2].preco
        id_carrinho = carrinho[0].id
        img_produto = carrinho[2].url_img
        quantidade_produto = carrinho[0].quantidade
        total += preco_produto * quantidade_produto
        produtos.append({'nome': nome_produto,
                         'id_pedido': carrinho[0].id_pedido,
                         'preco': preco_produto * quantidade_produto, 
                         'id_carrinho': id_carrinho, 
                         'quantidade_produto': quantidade_produto,
                         'img_produto': img_produto})
        todos_produtos['produtos'] = produtos
        todos_produtos['total'] = total


    try:
        return {'status': True, 'message': 'pedido_encontrado', 'info': todos_produtos}, 200
    except Exception as e: # tratar erros
        return {'status': False, 'message': 'pedido_nao_encontrado', 'info': []}, 403


def cadastrar_pedido(self):
    pedido = Pedido(id_usuario=request.json['id_usuario'], id_endereco=request.json['id_endereco'], id_pedido=request.json['id_pedido'])
    db.session.add(pedido)


    base = db.session.query(Carrinho).filter(Carrinho.id_usuario == request.json['id_usuario']).\
        filter(Carrinho.pedido_feito == 0).update({"id_pedido": request.json['id_pedido'], "pedido_feito": 1})

    db.session.add(pedido)
    db.session.commit()
    # Envio do email
    aqui_esta_o_usuario = db.session.query(Usuario).filter(Usuario.id_usuario == request.json['id_usuario']).all() #Verificar depois
    email = []
    todos_emails = {}


    for i in aqui_esta_o_usuario:
        email = aqui_esta_o_usuario[0].email 

        try:
            #Envio do email
            de = "cleyssonssilva@gmail.com"
            senha = "rccparasempre15"
            para = email
                    
            subject = 'Parabéns pela compra - Yelestai !!' # Título do email
                    
            yag = yagmail.SMTP(user=de, password=senha)
            contents = [
            "Se você está recebendo esse email é porque acabou de efetuar uma compra em nosso site :D",
            "Para verificar sua compra acesse nossa loja em 'www.lojayelestai.com.br' na aba Pedidos Realizados.",
            "Estamos muito felizes e esperamos lhe ver em breve, abraços! :)",
            ]

            yag.send(to=para, subject=subject, contents=contents)
            return {'message': 'email enviado'}
            
        except:
            print('Email não enviado.')
    return {'message':'data added to database'}


def atualizar_pedido(self, id):
    pedido = Pedido.query.get(id)
    pedido.id_usuario = request.json['id_usuario']
    pedido.id_endereco = request.json['id_endereco']
    pedido.id_pedido = request.json['id_pedido']
    db.session.commit()
    return {'message':'data updated'}


def deletar_pedido(self, id):
    pedido = Pedido.query.get(id)
    db.session.delete(pedido)
    db.session.commit()
    return {'message': 'data deleted successfully'}

