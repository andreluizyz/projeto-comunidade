from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class CreateAccount(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit_create_account = SubmitField('Criar Conta')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    remind_data = BooleanField('Lembrar Dados?')
    submit_login = SubmitField('Fazer Login')

class FormEditProfile(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    profile_picture = FileField('Edit Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    course_python = BooleanField('Python com a Lê')
    course_sql = BooleanField('SQL com o pai')
    course_html = BooleanField('Front Ender Impressionador')
    course_design = BooleanField('Van Gogh Impressionador')
    course_github = BooleanField('Git Impressionador')
    submit_edit_profile = SubmitField('Edit Profile')

    def validate_email(self, email):
        if current_user.email != email.data:
            user = Usuario.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email já cadastrado. Cadastre-se com outro e-mail para continuar.')