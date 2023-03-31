import os

#genereate secrete key
SECRET_KEY = '5e4489171fb4b5092a98dac26c678442'

#grab the folder where the scripte run
basedir = os.path.abspath(os.path.dirname(__file__))

#enable debug mode
DEBUG = True


#connect to the database
#SQLALCHEMY_DATABASE_URI

# Turn off the Flask-SQLAlchemy event system and warning
#SQLALCHEMY_TRACK_MODIFICATIONS = False
