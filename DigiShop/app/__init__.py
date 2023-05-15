"""import the main app"""
from flask import Flask

"""import database library"""
from flask_sqlalchemy import SQLAlchemy

"""import lib for password in db """
from flask_bcrypt import Bcrypt

from flask_login import LoginManager #documentate about Login Manager

"""creation of the application"""
app = Flask(__name__)



"""configuration of the application using config.py"""
app.config.from_object('app.config')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
"""creation of the database instance"""
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view='user_bp.login'



from app import home_routes