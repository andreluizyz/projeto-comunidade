from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(20), nullable=False)
    profile_picture = database.Column(database.String, default='default.jpg')
    post = database.relationship('Post', backref='author', lazy=True)
    cousers = database.Column(database.String, nullable=False, default='Não informado')

    def count_posts(self):
        return len(self.post)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    data_create = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_user =  database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)