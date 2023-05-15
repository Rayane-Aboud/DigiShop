
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import bcrypt
from app.forms.user_forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.controllers.user_controller import register_user,update_user
from app.models.model import User,Product
#user blueprint
user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


#user registration
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    
    if form.validate_on_submit():
        register_user(form)#the user function is put in the controller
        return redirect(url_for('user_bp.login'))
    
    return render_template('userView/register.html', title='Register', form=form)



#user login
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('product_bp.get_products'))
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('product_bp.get_products'))
        else:
            error = 'Incorrect email or password'
    return render_template('userView/login.html', title='Login', form=form, error=error)


#user logout
@user_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


#user personal account
@user_bp.route('/account',methods=['GET','POST'])
@login_required #decorator that is ready in python
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        update_user(form)
        return redirect(url_for('user_bp.account'))#inorder to see
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    #image file has url for the current 
    image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template('userView/account.html', title='Account'
                           ,image_file=image_file,form=form)


#user personal page
@user_bp.route('/<string:username>')
def get_user_products(username):
    page = request.args.get('page', 1 ,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    
    products = Product.query.filter_by(seller=user)\
        .order_by(Product.date_posted.desc())\
        .paginate(page = page, per_page=5)
    return render_template('userView/user_products.html',products=products,user=user)
    
 

