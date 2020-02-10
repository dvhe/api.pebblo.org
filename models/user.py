from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    name = db.Column(db.String(40), unique=True, nullable=True)
    avatar = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.LargeBinary(500), unique=True, nullable=False)
    vanity = db.Column(db.String(80), unique=True, nullable=True)
    verified = db.Column(db.Boolean, unique=True, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    verified_email = db.Column(db.Boolean, unique=True, nullable=True)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    email_code = db.Column(db.String(80), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    updated_at = db.Column(db.DateTime, unique=False, nullable=True)
    verified_at = db.Column(db.DateTime, unique=False, nullable=True)
    admin = db.Column(db.Boolean, unique=False, nullable=True)
    mod = db.Column(db.Boolean, unique=False, nullable=True)
    suspended = db.Column(db.Boolean, unique=False, nullable=True)
    suspended_date = db.Column(db.DateTime, unique=False, nullable=True)