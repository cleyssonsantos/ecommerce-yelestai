from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api, fields, Resource
# import werkzeug.security
# import bcrypt
# from functools import wraps
from flask_cors import CORS
# from sqlalchemy import func
# from pedido import enviar_email
# import yagmail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:''@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = True
CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api()
api.init_app(app)

from loja.usuario import viewer
from loja.produto import viewer
from loja.cobranca import viewer
from loja.endereco import viewer
from loja.carrinho import viewer
from loja.pedido import viewer
