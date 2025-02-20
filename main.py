from flask import Flask, render_template, url_for 
from forms import CreateAccount, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef11a0ceab9b58cb689d'

list_creators = ['Andre', 'João', 'Maria', 'Pedro', 'Ana']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def users():
    return render_template('users.html', list_creators=list_creators)

@app.route('/entre-em-contato')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    form_login = Login()
    form_create_account = CreateAccount()
    
    return render_template('login.html', form_login=form_login, form_create_account=form_create_account)

if __name__ == '__main__':
    app.run(debug=True)