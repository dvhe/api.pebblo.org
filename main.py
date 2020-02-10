from flask import Flask, jsonify, make_response
from flask_cors import CORS
from routes.login import app_login
from routes.register import app_register
from routes.test import test
from routes.user.posts import posts
from routes.user.user import user_users
from flask_sqlalchemy import SQLAlchemy
from models.user import db
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_login)
app.register_blueprint(app_register)
app.register_blueprint(test)
app.register_blueprint(posts)
app.register_blueprint(user_users)

app.config['SECRET'] = 'pebblo'
app.config['JSON_SORT_KEYS'] = False

postgres = {
    'user': 'postgres',
    'pw': 'djshawn1',
    'db': 'pebblo_production',
    'host': 'localhost',
    'port': '5432'
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % postgres

# db.init_app(app)

db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.BIGINT, primary_key=True)
#     username = db.Column(db.String(16), unique=True, nullable=False)
#     name = db.Column(db.String(40), unique=True, nullable=True)
#     avatar = db.Column(db.String(80), unique=True, nullable=True)
#     password = db.Column(db.LargeBinary(500), unique=True, nullable=False)
#     vanity = db.Column(db.String(80), unique=True, nullable=True)
#     verified = db.Column(db.Boolean, unique=True, nullable=True)
#     email = db.Column(db.String(80), unique=True, nullable=True)
#     verified_email = db.Column(db.Boolean, unique=True, nullable=True)
#     bio = db.Column(db.String(2000), unique=False, nullable=True)
#     email_code = db.Column(db.String(80), unique=True, nullable=True)
#     created_at = db.Column(db.DateTime, unique=False, nullable=False)
#     updated_at = db.Column(db.DateTime, unique=False, nullable=True)
#     verified_at = db.Column(db.DateTime, unique=False, nullable=True)
#     admin = db.Column(db.Boolean, unique=False, nullable=True)
#     mod = db.Column(db.Boolean, unique=False, nullable=True)
#     suspended = db.Column(db.Boolean, unique=False, nullable=True)
#     suspended_date = db.Column(db.DateTime, unique=False, nullable=True)


# class Post(db.Model):
#     id = db.Column(db.BIGINT, primary_key=True)
#     author = db.Column(db.BIGINT, unique=False, nullable=False)
#     content = db.Column(db.String(2000), unique=False, nullable=False)
#     likes = db.Column(db.ARRAY(db.String(5000)), unique=False, nullable=False)
#     # likes = db.Column(db.JSON(), unique=False, nullable=False)
#     # other_content = db.Column(db.JSON(), unique=False, nullable=False)
#     created_at = db.Column(db.DateTime, unique=True, nullable=False)
#     updated_at = db.Column(db.DateTime, unique=True, nullable=True)


# db.create_all()


@app.route("/", methods=["GET"])
def default():
    return jsonify(
        message='Hello world'
    )


@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify(
        message='Request error',
        error='Unknown'
    )


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(
        message='Invalid endpoint',
        error='Not found'
    )


"""
@app.errorhandler(3468)
def email_in_use():
    return jsonify(message='A user already exists with that email')
"""

app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, page_not_found)
# app.register_error_handler(3468, email_in_use)

"""
requests.post(
    'https://canary.discordapp.com/api/webhooks/672121210628210691/v__5o35r-DCmyVjSiTqMc2PcydmGymqvCOE55SW4vSsQfG3Q8OIEcgbKaN4tBEA3cYHb',
    json={
        "embeds": [{
            "description": "<:p_ToggleON:649803139431792649> API is now online",
            "color": "8576870"
        }]
    })
"""

if __name__ == 'main':
    app.run(host='0.0.0.0', port='3000', debug=True)
