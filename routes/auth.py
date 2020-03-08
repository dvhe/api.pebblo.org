from flask import request, make_response,  jsonify
from models.user import Users
from functools import wraps
import jwt
import os


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "userToken" in request.headers:
            token = request.headers["userToken"]

        if not token:
            return make_response(jsonify(message="Authorization token is required for this action"), 401)

        try:
            data = jwt.decode(token, os.environ.get('JWT_KEY'))
            user = Users.select().where(Users.id==data['id']).get()
        except:
            return make_response(jsonify(message="Unable to authenticate due to token being invalid"), 401)

        return f(user, *args, **kwargs)

    return decorated

