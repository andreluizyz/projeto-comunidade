from main import app, database
from comunidadeimpressionadora.models import Usuario, Post

with app.app_context():
    # database.drop_all()  # Apaga todas as tabelas
    # database.create_all()  # Recria as tabelas
    
    # usuario1 = Usuario(username="André", email="andre@gmail.com", password="andre123")
    # usuario2 = Usuario(username="João", email="joao@gmail.com", password="joao123")
    # usuario3 = Usuario(username="Paulo", email="paulo@gmail.com", password="paulo123")
    # usuario4 = Usuario(username="José", email="jose@gmail.com", password="jose123")

    # database.session.add(usuario1)
    # database.session.add(usuario2)
    # database.session.add(usuario3)
    # database.session.add(usuario4)
    # database.session.commit()
    print(database.session.query(Usuario.username, Usuario.email).all())
   

   