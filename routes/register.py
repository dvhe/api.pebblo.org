from flask import Blueprint, request, jsonify, make_response
from models.user import User
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

    user = User.query.filter_by(email=data['email']).first()
    name = User.query.filter_by(username=data['username']).first()
    if user:
        return make_response(jsonify(message='A user already exists with that email'), 409)
    elif name:
        return make_response(jsonify(message='A user already exists with that username'), 409)
    # elif data['username'].startswith('-') or data['username'].startswith('.') or data['username'].startswith('_') or re.match('^([A-Za-z0-9._](?:(?:[A-Za-z0-9._]|(?:\.(?!\.))){2,28}(?:[A-Za-z0-9._]))?)$', data['username']) or re.match('(admin|mod|pebblo|administrator|moderator)', data['username']):
    #     return make_response(jsonify(message='Invalid username format'), 409)
    else:
            hashed = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt(rounds=10))
            sf = snowflake.generate(0, 0)
            new_user = User(id=sf.__next__(), username=data['username'], password=hashed, email=data['email'], created_at=datetime.utcnow().strftime("%Y%m%d"))
            db.session.add(new_user)
            db.session.commit()
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
            return make_response(jsonify(message='Successfully registered new user'), 200)

            return make_response(jsonify(message='I guess something went wrong?'), 400)

#createdAt=int(round(time.time() * 1000))