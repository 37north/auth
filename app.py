from flask import Flask, url_for, redirect, render_template, request, session, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from models import db, Admin
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = "development-key"


	
	
	
@app.route('/adminLogin', methods = ['GET', 'POST'])
def adminLogin():
	AUTH = request.authorization
	user = Admin.query.filter_by(username = AUTH.username).first()

	if not AUTH or not AUTH.username or not AUTH.password or not user:
		return make_response('The user or password is wrong!')

	
	elif check_password_hash(user.pwdhash, AUTH.password):

		return make_response('Hi ' + AUTH.username)
	else:
		return make_response('The user or password is wrong!')
			


@app.route('/change_password/<uid>', methods = ['GET', 'POST'])
def updatePass(uid):
	new_pass = request.get_json()
	hash_new_pwd = generate_password_hash(new_pass['pwdhash'])
	user = Admin.query.filter_by(uid = uid).first()
	user.pwdhash = hash_new_pwd
	db.session.commit()
	return jsonify({'msg':'pass updated'})
	
	



	
@app.route('/user', methods = ['POST'])
def create_user():
	data = request.get_json()
	hash_psw = generate_password_hash(data['pwdhash'])
	newUser = Admin(data['username'], hash_psw)
	db.session.add(newUser)
	db.session.commit()
	return jsonify({'msg':'new user created'})
	


	



if __name__ == "__main__":
    app.run(debug='True', port='4000')
