from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora.forms import CreateAccount, Login
from comunidadeimpressionadora import app

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
        flash(f"Login feito com sucesso no email: {form_login.email.data}", "alert-success")
        return redirect(url_for('home'))
    if form_create_account.validate_on_submit() and 'submit_create_account' in request.form:
        flash(f"Cadastro feito com sucesso no e-mail: {form_create_account.email.data}", "alert-success")   
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_create_account=form_create_account)
