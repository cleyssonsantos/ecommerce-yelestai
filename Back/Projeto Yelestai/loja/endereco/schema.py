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

"""Definindo o Schema do Marshmallow para facilitar utilização do JSON"""
class EnderecoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario', 'rua', 'numero', 'cep', 'bairro', 'municipio', 'estado', 'pais')


model = api.model('endereco',{
    'id_usuario':fields.Integer('Enter Id_User'),
    'rua':fields.String('Enter Rua'),
    'numero':fields.String('Enter Numero'),
    'cep':fields.String('Enter CEP'),
    'bairro':fields.String('Enter Bairro'),
    'municipio':fields.String('Enter Municipio'),
    'estado':fields.String('Enter Estado'),
    'pais':fields.String('Enter Pais'),
})
