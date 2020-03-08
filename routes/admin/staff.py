from flask import Blueprint, request, jsonify, make_response
from routes.auth import token_required
from models.user import Users, db
import json as simplejson
import datetime

app_staff = Blueprint("admin", __name__, static_folder="routes")

def timestamp(time):
    dmh = time[-1]
    period = time.replace(dmh, '')
    try:
        if dmh == 'd' or dmh == 'm' or dmh == 'h':
            days = 0
            minutes = 0
            hours = 0
            if dmh == 'd':
                days = int(period)
            elif dmh == 'h':
                hours = int(period)
            return datetime.datetime.now() + datetime.timedelta(days, 0, 0, 0, minutes, hours, 0)
        else:
            return 'error'
    except:
        return 'error'

epoch = datetime.datetime.utcfromtimestamp(0)

def convert(dt):
    return (timestamp(dt) - datetime.datetime.now()).total_seconds() * 1000.0

# date = timestamp('7d') - datetime.datetime.now()
# print(convert('7d'))

@app_staff.route("/staff/users/suspend/<current_user>", methods=["PATCH"])
@token_required
def suspend(current_user, param):
    data = request.get_json(force=True)

    if not current_user.mod or current_user.admin:
        return json.dumps({'result': 'Unauthorized'})

    if not data['time']:
        return json.dumps({'result': 'There was no time provided'})

    user = User.select().where(User.id=current_user.id)
    if user.suspended is False:
        query = (Users
        .update(suspended=True, suspended_date=convert(data['time']))
        .where(Users.id==user.id)
        .execute())
        return json.dumps({'result': f"{user.username} has been unsuspended"})
    else:
        query = (Users
              .update(supsended=False, suspended_date=convert(data['time']))
              .where(Users.id==user.id)
              .execute())
        return json.dumps({'result': f"{user.username} has been unsuspended"})

