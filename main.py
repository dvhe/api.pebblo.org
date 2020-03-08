from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from routes.login import app_login
from routes.register import app_register
from routes.test import test
from routes.user.posts import posts
from routes.user.user import user_users
from models.user import db, Users
from models.post import Post
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

db.create_tables([Users, Post])

@app.route("/", methods=["GET"])
def default():
    return jsonify(
        message='Hello world'
    )

@app.route("/test", methods=["POST"])
def testing():
    data = request.get_json(force=True)
    return jsonify(
        email=data['email'],
        username=data['username'],
        password=data['password']
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

app.register_error_handler(400, handle_bad_request)
app.register_error_handler(404, page_not_found)

# requests.post(
#     'https://canary.discordapp.com/api/webhooks/672121210628210691/v__5o35r-DCmyVjSiTqMc2PcydmGymqvCOE55SW4vSsQfG3Q8OIEcgbKaN4tBEA3cYHb',
#     json={
#         "embeds": [{
#             "description": "<:p_ToggleON:649803139431792649> API is now online",
#             "color": "8576870"
#         }]
#     })

def run_app():
    app.run(host='0.0.0.0', port='3000', debug=True)

run_app()