from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef11a0ceab9b58cb689d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bycrypt = Bcrypt(app)
login_manager =  LoginManager(app)

from comunidadeimpressionadora import routes

with app.app_context():
    database.create_all()
