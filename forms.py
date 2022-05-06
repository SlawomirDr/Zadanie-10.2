from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email

class TodoForm(FlaskForm):
    title = StringField('Tytuł')
    description = TextAreaField('Opis')
    done = BooleanField('Czy zrobione')
