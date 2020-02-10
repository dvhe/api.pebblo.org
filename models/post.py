from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    author = db.Column(db.BIGINT, unique=False, nullable=False)
    content = db.Column(db.String(2000), unique=False, nullable=False)
    likes = db.Column(db.ARRAY(db.String(5000)), unique=False, nullable=False)
    # likes = db.Column(db.JSON(), unique=False, nullable=False)
    # other_content = db.Column(db.JSON(), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=True, nullable=False)
    updated_at = db.Column(db.DateTime, unique=True, nullable=True)