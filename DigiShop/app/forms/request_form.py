from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired

#form that is used to create products
class RequestForm(FlaskForm):
    all_products = BooleanField('All')
    
    recommended_products = BooleanField('Recommended')
    
    on_promotion = BooleanField('On promotion')
    
    category = SelectField(choices=[('Electronics', 'Electronics'),
                                ('Fashion', 'Fashion'), 
                                ('Home and garden', 'Home and garden'),
                                ('Beauty and personal care', 'Beauty and personal care'),
                                ('Sports and outdoors', 'Sports and outdoors'),
                                ('Health and wellness', 'Health and wellness'),
                                ('Toys and games', 'Toys and games'),
                                ('Food and beverage', 'Food and beverage'),
                                ('Pet supplies', 'Pet supplies')], 
                       default='')
    clientText = TextAreaField('description',validators=[DataRequired()])
    submit=SubmitField('')