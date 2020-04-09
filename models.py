from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import datetime
db = SQLAlchemy()

class Admin(db.Model):
	__tablename__ = 'admin'
	uid = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(120), unique = True)
	pwdhash = db.Column(db.String(255))
	
	def __init__(self, username, pwdhash):
		self.username = username.lower()
		self.set_password(pwdhash)
	
	
	def set_password(self, pwdhash):
		self.pwdhash = generate_password_hash(pwdhash)
		
	def check_password(self, password):
		return check_password_hash(self.pwdhash, pwdhash)
		
		
