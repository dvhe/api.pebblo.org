from flask import Blueprint, jsonify
from routes.auth import token_required
from models.user import Users

auth = Blueprint("me", __name__, static_folder="routes")


@auth.route("/oauth/connections/twitter", methods=["GET"])
def oauth(client_id):
    