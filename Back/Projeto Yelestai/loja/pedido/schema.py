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

class PedidoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'id_endereco', 'id_pedido')


model = api.model('pedido',{
    'id_usuario':fields.Integer('Enter ID User'),
    'id_endereco':fields.Integer('Enter ID Endereco'),
    'id_pedido':fields.Integer('Enter ID Pedido')
})


