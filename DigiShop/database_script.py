from app import db
from app import app

from app.models.model import User,Product

        
with app.app_context():
    db.create_all()
    
        