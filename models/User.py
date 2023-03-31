from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    
    def __init__(self) -> None:
        super().__init__()
        __tablename__ = 'users'
        self.id      = db.Column(db.Integer, primary_key= True)
        self.first_name    = db.Column(db.String(120))
        self.family_name   = db.Column(db.String(120))
        self.email_address = db.Column(db.String(120))
        #self.password = db.Column(db.String(120))
    
    @property
    def serialize(self):
        return {
            'id'  : self.id,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'email_address': self.email_address
        }
    