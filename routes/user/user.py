from flask import Blueprint, jsonify
from routes.auth import token_required
from models.user import User

user_users = Blueprint("me", __name__, static_folder="routes")


@user_users.route("/users/<user_id>", methods=["GET"])
def user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(
        id=user.id,
        username=user.username,
        avatar=user.avatar,
        bio=user.bio,
        vanity=user.vanity
    ), 200

@user_users.route("/users/@me", methods=["GET"])
@token_required
def user2(user_id):
    user = User.query.filter_by(id=user_id.id).first()
    return jsonify(
        id=user.id,
        username=user.username,
        avatar=user.avatar,
        bio=user.bio,
        vanity=user.vanity,
        created_at=user.created_at,
        updated_at=user.updated_at
    ), 200


"""
@user_users.route("/users/follow/<user_id>", methods=["POST"])
@token_required
def user(user_id):
    user = User.query.filter_by(id=user_id.id).first()


"""