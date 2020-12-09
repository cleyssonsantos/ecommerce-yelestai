# aqui fica o schema
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

class ProdutoSchema(ma.Schema):
    class Meta:
        fields = ('id_produto', 'nome','preco', 'estoque', 'url_img', 'detalhes')


model = api.model('produto',{
    'nome':fields.String('Enter Nome'),
    'preco':fields.String('Enter Preço'),
    'estoque':fields.String('Enter Estoque'),
    'url_img':fields.String('Insira Url da IMG'),
    'detalhes':fields.String('Insira os detalhes do produto')
})


