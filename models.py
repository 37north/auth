from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Admin(db.Model):
    '''
    Admin class
    '''
    __tablename__ = 'admin'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(255))

    def __init__(self, username, pwdhash):
        '''
        Define the variables
        '''
        self.username = username.lower()
        self.set_password(pwdhash)

    def set_password(self, pwdhash):
        '''
        Set Passwords
        '''
        self.pwdhash = generate_password_hash(pwdhash)

    def check_password(self, pwdhash):
        '''
        Check the passwords
        '''
        return check_password_hash(self.pwdhash, pwdhash)