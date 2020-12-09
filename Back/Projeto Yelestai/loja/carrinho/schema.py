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

class CarrinhoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario','id_produto', 'quantidade', 'pedido_feito', 'id_pedido')


model = api.model('carrinho',{
    'id_usuario':fields.Integer('Enter ID User'),
    'id_produto':fields.Integer('Enter ID Preço'),
    'quantidade':fields.Integer('Enter Quantidade'),
    'pedido_feito':fields.Integer('Enter Pedido Feito'),
    'id_pedido':fields.Integer('Enter ID Pedido')
})


