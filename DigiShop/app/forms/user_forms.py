from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo,ValidationError
from app.models.model import User
from flask_login import current_user


#user registration form
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
    
    """creation of custom validators"""
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken please choose a different one')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('e-mail already existing.. log in ?')
    
    
#user login form
class LoginForm(FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')
    
    """using the login manager"""

#user update form
class UpdateAccountForm(FlaskForm):
    
    
    username = StringField('',
                           validators=[DataRequired(),Length(min=2, max=20)])
    
    #add the name of the shop or entreprise 
    email = StringField('',validators=[DataRequired(),Email()])
    
    #update the profile picture
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','jpeg','png'])])
    
    #see if we add facebook stuff and instagram stuff
    update = SubmitField('Submit')
    
    
    """creation of custom validators"""
    #username validation function
    def validate_username(self,username):
        # if the user renamed him self a name that is different than his 
        if username.data != current_user.username:
            #check if the different name already exist
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken please choose a different one')
    
    #email validation function
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already taken.. choose another one')
        
    
    