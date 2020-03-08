from flask import Blueprint, request, jsonify, make_response
from routes.auth import token_required
import json as simplejson

test = Blueprint("test", __name__, static_folder="routes")


@test.route("/test", methods=["GET"])
@token_required
def testing(user_id):
    if not user_id.admin:
        return jsonify(message='lol not admin')

    return jsonify(message='nice you are an admin!')