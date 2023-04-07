from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SelectField,DecimalField
from wtforms.validators import DataRequired,Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename


class AddProductForm(FlaskForm):
    
    # seller informations
    
    sellername = StringField('Name :',validators = [DataRequired()])
    
    location = StringField('Location', validators=[DataRequired()])

    phone = StringField('Phone number', validators=[DataRequired()])
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    productName = StringField('Product Name',validators=[DataRequired()])

    brand = StringField('Brand',validators=[DataRequired()])

    description = StringField('Description',validators=[DataRequired()])
    
    category = SelectField('Category', choices=[('option1', 'Electronics'),
                                                ('option2', 'Fashion'), 
                                                ('option3', 'Home and garden'),
                                                ('option4', 'Beauty and personal care'),
                                                ('option5', 'Sports and outdoors'),
                                                ('option6', 'Health and wellnes'),
                                                ('option7', 'Toys and games'),
                                                ('option8', 'Food and beverage'),
                                                ('option9', 'Pet supplies')])

    price = DecimalField('Price', validators=[DataRequired()], places=2)


    image = FileField('Upload an image',description='Upload image',validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])


    submit = SubmitField('Submit')