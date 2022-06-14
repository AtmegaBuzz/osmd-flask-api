from flask import request, jsonify
from models import (
    User,
    db
)


def register():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    if username is None or password is None:
        return jsonify({'username':'field is required'}),400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'username':'username already taken'}),400

    user = User(username=username,email=email)
    user.hash_password(password)
    user.generate_token()

    db.session.add(user)
    db.session.commit()

    return jsonify({ 'username': user.username , "api_key":user.api_token}), 201


def login():
    if request.method=='POST':
        username = request.json.get("username")
        password = request.json.get("password")

        user = User.query.filter_by(username=username).first() 

        if user is None:
            return jsonify({'auth_error':'invalid credentials.'})
        
        if user.verify_password(password) == False:
            return jsonify({'auth_error':'invalid credentials.'})
        
        return jsonify({'api_key':user.api_token})
        
