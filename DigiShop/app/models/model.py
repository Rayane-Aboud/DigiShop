from app import db
from datetime import datetime
from app import login_manager
from flask_login import UserMixin

# we need to build as
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model,UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True)
    firstname =db.Column(db.String(50),nullable=False)
    familyname = db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    products = db.relationship('Product',backref='seller',lazy=True)
    

    def __repr__(self) -> str:
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    

    
    
    
class Product(db.Model):
    __tablename__='product'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    product_name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.Text,nullable=False)
    price = db.Column(db.String(20),nullable=False)
    location=db.Column(db.String(20),nullable=False)
    brand = db.Column(db.String(20),nullable=False)
    picture=db.Column(db.String(20),nullable=False,default='default.png')
    category=db.Column(db.String(20),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"Post('{self.product_name}','{self.price}','{self.description}')"