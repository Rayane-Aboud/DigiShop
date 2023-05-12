from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email


class SelectProductForm(FlaskForm):
    
    
    # product details
    
    all_products = BooleanField('All')
    
    recommended_products = BooleanField('Recommended')
    
    on_promotion = BooleanField('On promotion')
    
    category = SelectField(choices=[('option1', 'Electronics'),
                                ('option2', 'Fashion'), 
                                ('option3', 'Home and garden'),
                                ('option4', 'Beauty and personal care'),
                                ('option5', 'Sports and outdoors'),
                                ('option6', 'Health and wellness'),
                                ('option7', 'Toys and games'),
                                ('option8', 'Food and beverage'),
                                ('option9', 'Pet supplies')], 
                       default='')
    
   
    
    clientText = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('')
