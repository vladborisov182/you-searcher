from wtforms import Form, StringField, PasswordField
from wtforms.validators import Email, Length, EqualTo, DataRequired, Email
from models import User

class RegisterForm(Form):
    username = StringField('Username', validators = [Length(min=5, max=24)])
    email = StringField('Email', validators = [Length(min=6, max=50), Email()])
    password = PasswordField('Password', 
        validators = [DataRequired(), EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm password')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValueError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValueError('Username already exists.')