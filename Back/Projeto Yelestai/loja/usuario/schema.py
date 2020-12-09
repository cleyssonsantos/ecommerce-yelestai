# aqui vai ficar o schema
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


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario', 'nome', 'email', 'senha')


model = api.model('usuario',{
    'nome':fields.String('Enter Nome'),
    'email':fields.String('Enter Email'),
    'senha':fields.String('Enter Senha'),
})

model_login = api.model('mode_login',{
    'email':fields.String('Email'),
    'senha':fields.String('Senha')
})
