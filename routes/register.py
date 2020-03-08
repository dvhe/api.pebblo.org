from flask import Blueprint, request, jsonify
from models.user import Users
from models.user import db
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import Mail
import jwt, bcrypt, snowflake, time, os, re
from datetime import datetime, timezone

app_register = Blueprint("register", __name__, static_folder="routes")

@app_register.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json(force=True)
    # if is not data['email'] or is not data['password'] or is not data['username']:
    #     return make_response(jsonify(error="Invalid JSON type provided"), 400)
    
    user = Users.select().where(Users.email==data['email'])
    name = Users.select().where(Users.username==data['username'])
    if user:
        return jsonify(success=False, message='A user already exists with that email'), 409
    elif name:
        return jsonify(success=False, message='A user already exists with that username'), 409
    elif re.search('[!@#$%^&*()-+=`~{}\[\]\|;:\'"<,>/\?]+', data['username']):
        return jsonify(success=False, message='Sorry, Your username can only contain letters, numbers and \_.\'', test=data['username']), 409
    elif re.search('(admin|trending|discover|explore|login|create|register|forgot|verify|pebblo|support|help|terms|privacy|timeline|explore|groups|account|settings|me)', data['username']):
        return jsonify(success=False, message='Sorry, but you are not allowed to use that username, as it contains a blacklisted name. More information can be found at https://help.pebblo.org/'), 409
    elif len(data['password']) <= 9:
        return jsonify(success=False, message='Sorry, but your password must be longer than 9 characters')
    elif len(data['username']) <= 2:
        return jsonify(success=False, message='Sorry, but your username must be longer than 2 characters')
    elif len(data['username']) >= 16:
        return jsonify(success=False, message='Sorry, but your username cannot be longer than 16 characters')
    else:
            hashed = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt(rounds=10))
            sf = snowflake.generate(0, 0)
            new_user = Users.create(id=sf.__next__(), username=data['username'], password=hashed, email=data['email'], created_at=datetime.utcnow().strftime("%Y%m%d"))
            # send email verification
            """
            message = Mail(
                from_email='no-reply@pebblo.org',
                to_emails=data['email'],
                subject='Verification',
                html_content=f"Thanks for signing up for pebblo! You can now verify your account at https://pebblo.org/verification/{user.id}/{user.emailCode}/"
            )
            sg = SendGridAPIClient(os.environ.get('SENDGRID_KEY'))
            sg.send(message)
            """
            return jsonify(message='Successfully registered new user'), 200

            # return jsonify(message='I guess something went wrong?'), 400

