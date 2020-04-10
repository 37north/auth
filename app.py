#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Admin


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = "development-key"

@app.route('/user', methods=['POST'])
def create_user():
    '''
    Register as a new user.
    '''
    data = request.get_json()
    hash_pwd = data['pwdhash']
    new_user = Admin(data['username'], hash_pwd)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'msg':'new user created'})


@app.route('/login', methods=['GET', 'POST'])
def admin_login():
    '''
    Login with your credentials.
    '''
    auth = request.authorization
    user = Admin.query.filter_by(username=auth.username).first()

    if not auth or not auth.username or not auth.password or not user:
        return make_response('The user or password is wrongg!')
    elif check_password_hash(user.pwdhash, auth.password):
        return make_response('Hi ' + auth.username)
    else:
        return make_response('Password is wrong for ' + user.username)

@app.route('/change_password/<uid>', methods=['GET', 'POST'])
def update_pass(uid):
    '''
    You may want to change your password.
    '''
    new_pass = request.get_json()
    hash_new_pwd = generate_password_hash(new_pass['pwdhash'])
    user = Admin.query.filter_by(uid=uid).first()
    user.pwdhash = hash_new_pwd
    db.session.commit()
    return jsonify({'msg':'pass updated'})

if __name__ == "__main__":
    app.run(debug='True', port='4000')
