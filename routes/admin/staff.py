from flask import Blueprint, request, jsonify, make_response
from routes.auth import token_required
from models.user import User, db

app_staff = Blueprint("admin", __name__, static_folder="routes")


@app_staff.route("/staff/users/ban/<current_user>", methods=["PATCH"])
@token_required
def ban(current_user):
    if not current_user.mod or current_user.admin:
        return make_response(jsonify(result='Unauthorized'), 401)

    user = User.query.filter_by(id=current_user.id).first()
    if user.suspended is False:
        user.suspended = True
        db.session.commit()
        return make_response(jsonify(result=f"{user.username} has been suspended"), 200)
    else:
        user.suspended = False
        db.session.commit()
        return make_response(jsonify(result=f"{user.username} has been unsuspended"), 200)

@app_staff.route("/staff/users/suspend/<current_user>", methods=["PATCH"])
@token_required
def suspend(current_user):
    data = request.get_json(force=True)

    if not current_user.mod or current_user.admin:
        return make_response(jsonify(result='Unauthorized'), 401)

    if not data['time']:
        return jsonify(result='There was no time provided')

    user = User.query.filter_by(id=current_user.id).first()
    if user.suspended is False:
        user.suspended = True
        db.session.commit()
        return make_response(jsonify(result=f"{user.username} has been suspended"), 200)
    else:
        user.suspended = False
        db.session.commit()
        return make_response(jsonify(result=f"{user.username} has been unsuspended"), 200)

