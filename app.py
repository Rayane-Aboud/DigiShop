"""init the application, render the main page"""
from turtle import title
from flask import Flask, render_template,url_for,flash,redirect
from forms.product_form import AddProductForm

"""importing the form structures"""
from forms.user_forms import RegistrationForm,LoginForm

"""import database functionnalities"""
from flask_migrate import Migrate

"""importing the models"""
#from models.User import db

"""importing routes"""
from routes.user_bp import user_bp

"""creation of the application"""

app = Flask(__name__,static_url_path='/static')

"""configuration of the application using config.py"""
app.config.from_object('config')

"""initialisation and migration of the database"""
#migrate = Migrate(app,db)
products = [
    {
        'user':"Rayane Aboud",
        'name':"bar fix",
        #must add picture of the product
        'category':"sport and entertainment",
        'price': '2000 DA',
        'description':"Bar fix to be held on the wall perfect for new athletes new",
        'state':'new',
        'date_posted':'10-12-22',
        'location' : 'Kouba Garidi',
        'phone_number':'0611 52 12 34',
        'mail':'rayane@gmail.com',
        'facebook':'rayane@facebook.com',
        'instagram':None
    },
    {
        'user':"Karim Laouchedi",
        'name':"formation en programmation",
        'category':"teaching",
        'price': '5000 DA pour 5 mois',
        'description':"Je fais des cours de programmation pour ceux qui débute le domaine",
        'state':'null',
        'date_posted':'24-12-22',
        'location':"Borj el Bahri at Kreppon's school",
        'phone_number':'0612 34 56 78',
        'mail':'kreppon@gmail.com',
        'facebook':'kreppon@facebook.com',
        'instagram':None
    }
]



"""registering the app to the different blueprints"""
app.register_blueprint(user_bp,url_prefix='/users')






"""route to the home page"""
@app.route('/')

@app.route('/addproduct',methods=['GET','POST'])
def addproduct():
    form = AddProductForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    else:
        print(form.errors)
    return render_template('productView/addproduct.html',title='addproduct',form=form)

@app.route('/admin')
def admin():
    return render_template('admin/admin.html',title='admin')

@app.route('/products')
def home():
    return render_template('index.html',products = products)

@app.route('/homepage')
def homepage():
    return render_template('home/homepage.html',title='Homepage')
    
@app.route('/about')
def about():
    return render_template('home/about.html')

@app.route('/myAccount')
def myaccount():
    return render_template('home/myAccount.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    else:
        print(form.errors)
    return render_template('home/register.html',title='Register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password':
            return redirect('/home')
        else:
            print("rak ghalet")
    else:
        print(form.errors)
    return render_template('home/login.html',title='Login',form=form)




if __name__ =='__main__':
    app.debug = True
    app.run()