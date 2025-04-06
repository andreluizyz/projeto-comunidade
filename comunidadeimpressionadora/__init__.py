from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef11a0ceab9b58cb689d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

list_creators = ["Clarissa", "Lucas", "Marcos", "Ana", "Juliana", "Pedro", "Fernanda", "Roberto", "Carla", "Thiago"]

database = SQLAlchemy(app)

from comunidadeimpressionadora import routes