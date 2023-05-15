from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,SubmitField,TextAreaField,HiddenField,SelectField
from wtforms.validators import DataRequired, ValidationError



#form that is used to create products
class ProductForm(FlaskForm):
    product_name = StringField('product name',validators=[DataRequired()])
    price = StringField('price :',validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    brand = StringField('Brand',validators=[DataRequired()])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','jpeg','png'])])
    description = TextAreaField('description',validators=[DataRequired()])
    category = SelectField('Category', choices=[('option1', 'Electronics'),
                                                ('option2', 'Fashion'), 
                                                ('option3', 'Home and garden'),
                                                ('option4', 'Beauty and personal care'),
                                                ('option5', 'Sports and outdoors'),
                                                ('option6', 'Health and wellnes'),
                                                ('option7', 'Toys and games'),
                                                ('option8', 'Food and beverage'),
                                                ('option9', 'Pet supplies')])
    submit=SubmitField('Add product to the market')
    
    def validate_price(self,price):
        if not price.data.isdigit():
            raise ValidationError('invalid price input')
        if float (price.data) < 0:
            raise ValidationError('invalid price input')
        


#delete the product
class DeleteProductForm(FlaskForm):
    product_id = HiddenField('Product ID')
    submit = SubmitField('Delete for good')