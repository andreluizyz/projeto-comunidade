from comunidadeimpressionadora import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(20), nullable=False)
    profile_picture = database.Column(database.String, default='default.jpg')
    post = database.relationship('Post', backref='autor', lazy=True)
    cousers = database.Column(database.String, nullable=False, default='Não informado')

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    data_create = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_user =  database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)