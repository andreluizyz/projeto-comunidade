from flask import Flask, render_template, url_for, request, flash, redirect
from forms import CreateAccount, Login
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef11a0ceab9b58cb689d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def users():
    return render_template('users.html', list_creators=list_creators)

@app.route('/entre-em-contato')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = Login()
    form_create_account = CreateAccount()

    if form_login.validate_on_submit() and 'submit_login' in request.form:
        flash(f"Login feito com sucesso no email: {form_login.email.data}", "alert-success")
        return redirect(url_for('home'))
    if form_create_account.validate_on_submit() and 'submit_create_account' in request.form:
        flash(f"Cadastro feito com sucesso no e-mail: {form_create_account.email.data}", "alert-success")   
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_create_account=form_create_account)

if __name__ == '__main__':
    app.run(debug=True)