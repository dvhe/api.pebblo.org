from flask import Blueprint, request, jsonify, make_response
from models.user import Users
import jwt
import bcrypt
import os
import datetime

app_login = Blueprint("login", __name__, static_folder="routes")


@app_login.route("/auth/login", methods=["POST"])
def login():
    # auth = request.authorization
    # if not auth or not auth.username or not auth.password:
    #     return jsonify(error="Invalid username or password was provided"), 200

    # user = Users.query.filter_by(username=auth.username).first()
    # if user is None:
    #     return jsonify(error='User does not exist'), 400
    # if user.suspended is True:
    #     return jsonify(message='Unable to login due to your account being suspended'), 401
    # if user:
    #     if bcrypt.checkpw(auth.password.encode('utf-8'), bytes(user.password)):
    #         token = jwt.encode({'id': user.id, 'email': user.email}, os.getenv('JWT_KEY'))
    #         return jsonify(message='Login successful', token=token.decode('UTF-8')), 200

    #     return jsonify(message='Unable to login, passwords did not match'), 400
    data = request.get_json(force=True)
    if not data['username'] or not data['password']:
        return jsonify(message="The username or password you entered did not match our records. Are you sure you typed the correct credentials?"), 401

    user = Users.select().where(Users.username==data['username']).get()

    if user is None:
        return jsonify(message='The username or password you entered did not match our records. Are you sure you typed the correct credentials?'), 401
    if user.suspended is True:
        return jsonify(message='Unable to login due to your account being suspended. Learn more information at https://help.pebblo.org/accounts'), 401
    if user:
        if bcrypt.checkpw(data['password'].encode('utf-8'), bytes(user.password)):
            token = jwt.encode({'id': user.id, 'email': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)}, os.getenv('JWT_KEY'))
            return jsonify(message='Login successful', token=token.decode('UTF-8')), 200

        return jsonify(message='Unable to login, passwords did not match'), 401

