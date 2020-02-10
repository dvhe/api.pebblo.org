from flask import Blueprint, request, jsonify, make_response
from models.user import User
import jwt
import bcrypt
import os

app_login = Blueprint("login", __name__, static_folder="routes")


@app_login.route("/auth/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(jsonify(error="Invalid username or password was provided"), 200)

    user = User.query.filter_by(username=auth.username).first()
    if user is None:
        return make_response(jsonify(error='User does not exist'), 400)
    if user.suspended is True:
        return make_response(jsonify(message='Unable to login due to your account being suspended'), 401)
    if user:
        if bcrypt.checkpw(auth.password.encode('utf-8'), bytes(user.password)):
            token = jwt.encode({'id': user.id, 'email': user.email}, os.getenv('JWT_KEY'))
            return make_response(jsonify(message='Login successful', token=token.decode('UTF-8')), 200)

        return make_response(jsonify(message='Unable to login, passwords did not match'), 400)

