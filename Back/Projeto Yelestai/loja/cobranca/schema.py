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

class CobrancaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario','numero_cartao', 'nome_titular', 'data_exp', 'csv')


model = api.model('cobrança',{
    'id_usuario':fields.Integer('Enter Id_User'),
    'numero_cartao':fields.String('Enter Numero do Cartão'),
    'nome_titular':fields.String('Enter Nome do Titular'),
    'data_exp':fields.String('Enter Data de Validade'),
    'csv':fields.String('Enter CSV'),
})
