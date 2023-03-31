from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    
    firstname= StringField('First name :',validators = [DataRequired()])
    
    familyname = StringField('Family name :',validators = [DataRequired()])
    
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2, max=20)])
    
    #add the name of the shop or entreprise 
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = PasswordField('Password',validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(),EqualTo('password')])
    #see if we add facebook stuff and instagram stuff
    submit = SubmitField('Sign up')
    
    
class LoginForm(FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')

    
    