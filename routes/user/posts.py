from flask import Blueprint, request, jsonify
from routes.auth import token_required
from models.post import Post, db
from models.user import User
import snowflake
from datetime import datetime, timezone

posts = Blueprint("posts", __name__, static_folder="routes")


@posts.route("/users/posts/new", methods=["POST"])
@token_required
def post(user_id):
    sf = snowflake.generate(0, 0)
    data = request.get_json(force=True)

    # if user_id.id is not user_id.id:
    #     return make_response(jsonify(message='Unable to create new post, user id\'s did not match'), 401)

    new_post = Post(id=sf.__next__(), author=user_id.id, content=data['content'], created_at=datetime.utcnow().strftime("%Y%m%d"), updated_at=datetime.utcnow().strftime("%Y%m%d"), likes=[])

    db.session.add(new_post)
    db.session.commit()

    return jsonify(success=True, message='New post was created successfully'), 200


@posts.route("/users/posts/<post_id>", methods=["DELETE"])
@token_required
def post2(user_id, post_id):

    find = Post.query.filter_by(id=post_id).first()

    if find is None:
        return jsonify(success=False, message='Unable to find that post'), 401

    if user_id.id != find.author:
        return jsonify(success=False, message='Unable to delete that post, user id\'s did not match'), 401

    db.session.delete(find)
    db.session.commit()

    return jsonify(success=True, message='Post was successfully deleted'), 200


@posts.route("/users/posts/<post_id>/like", methods=["PUT"])
@token_required
def post3(user_id, post_id):

    get_post = Post.query.filter_by(id=post_id).first()
    likes = []
    likes.append(get_post.likes)
    likes.append(user_id.id)
    get_post.likes = likes

    if likes is None:
        likes.append(user_id.id)
        get_post.likes = likes

    get_user = User.query.filter_by(id=get_post.author).first()

    return jsonify(success=True, message=f'Liked {get_user.username}\'s post'), 200

    # db.session.merge(get_post)
    # db.session.flush()
    db.session.commit()

@posts.route("/users/posts/<post_id>", methods=["GET"])
@token_required
def post4(user_id, post_id):
    find_post = Post.query.filter_by(id=post_id).first()

    return jsonify(success=True, author=find_post.author, user=user_id.id, content=find_post.content, likes=len(find_post.likes)), 200

