from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora.forms import CreateAccount, Login
from comunidadeimpressionadora import app, database, bycrypt
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user

list_creators= ["Clarissa", "Lucas", "Marcos", "Ana", "Juliana", "Pedro", "Fernanda", "Roberto", "Carla", "Thiago"]

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
        user = Usuario.query.filter_by(email=form_login.email.data).first()
        if user and bycrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=form_login.remind_data.data)
            flash(f"Login feito com sucesso no email: {form_login.email.data}", "alert-success")
            return redirect(url_for('home'))
        else:
            flash("Falha no login. Email ou senha incorretos", "alert-danger")
            return redirect(url_for('login'))
    
    if form_create_account.validate_on_submit() and 'submit_create_account' in request.form:
        password_bcrypt = bycrypt.generate_password_hash(form_create_account.password.data).decode('utf-8')
        user = Usuario(username= form_create_account.username.data, email= form_create_account.email.data, password= password_bcrypt)
        database.session.add(user)
        database.session.commit()
        flash(f"Cadastro feito com sucesso no e-mail: {form_create_account.email.data}", "alert-success")   
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_create_account=form_create_account)
