from flask import Blueprint, jsonify
from routes.auth import token_required
from models.user import Users
import random
import string
import json as simplejson
import datetime
user_users = Blueprint("me", __name__, static_folder="routes")


@user_users.route("/users/<user_id>", methods=["GET"])
def user(user_id):
    user = Users.select().where(Users.id==user_id.id)
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
    user = Users.select().where(Users.id==user_id.id)
    return jsonify(
        id=user.id,
        username=user.username,
        avatar=user.avatar,
        bio=user.bio,
        vanity=user.vanity,
        created_at=user.created_at,
        updated_at=user.updated_at
    ), 

# @user_users.route("/users/2fa", methods=["POST"])
# @token_required
# def user3(user_id):
#     user = Users.query.filter_by(id=user_id).first()
#     # if user.mfa is True:
        

@user_users.route("/users/follow/<follower_id>", methods=["POST"])
@token_required
def follow_user(user_id, follower_id):
    user = Users.select().where(Users.id==user_id.id)
    return jsonify(
        id=user.id,
        follower=follower_id.id
    )


@user_users.route("/users/@me/refresh", methods=["POST"])
@token_required
def refresh(user_id, follower_id):
    user = Users.select().where(Users.id==user_id.id)
    return jsonify(
        id=user.id,
        follower=follower_id.id
    )


@user_users.route("/users/@me/forgot", methods=["POST"])
@token_required
def forgot(user_id):
    user = Users.select().where(Users.id==user_id.id)
    letters = string.ascii_lowercase+string.ascii_uppercase
    ran = ''.join(random.choice(letters) for i in range(7))
    update = (Users
              .update(Users.email_code==ran)
              .where(Users.id==user_id.id)
              .execute())
    return json.dumps({'message': 'Email Code generated https://pebblo.org/account/verify/{user.email_code}'})



@user_users.route("/users/@me/verify", methods=["POST"])
@token_required
def verify(user_id):
    user = Users.select().where(Users.id==user_id.id)
    letters = string.ascii_lowercase+string.ascii_uppercase
    ran = ''.join(random.choice(letters) for i in range(7))
    if ran != user.email_code or not user.email_code:
        return json.dumps({'error': 'Email doesn\'t exist.'})
    
    if not user:
        return json.dumps({'error': 'User doesn\'t exist.'})

    if user.verified_email is not False:
        return json.dumps({'error': 'Email already verified.'})

    update = (Users
              .update(verified_at=datetime.datetime.now())
              .where(Users.email_code==user.email_code)
              .execute())
    return json.dumps({'message': 'Email has been verified'})
              

    # print(ran)

