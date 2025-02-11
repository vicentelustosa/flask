from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Usuário')
    password = PasswordField('Senha')
    profile_pic = FileField('Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    username = StringField('Usuário')
    password = PasswordField('Senha')
    submit = SubmitField('Entrar')

class PostForm(FlaskForm):
    content = TextAreaField('Escreva seu aviso')
    submit = SubmitField('Publicar')
