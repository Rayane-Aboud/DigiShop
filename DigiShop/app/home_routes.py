from flask import Blueprint, render_template, request,redirect,url_for
from flask_login import current_user
from app.routes.user_bp import user_bp
from app.routes.product_bp import product_bp
from app.models.model import Product
from app import app,db



main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for("product_bp.get_products"))
    
    return render_template('index.html', title='Home')


@main_bp.route('/about')
def about():
    return render_template('home/about.html', title='About')




app.register_blueprint(main_bp)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)