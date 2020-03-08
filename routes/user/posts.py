from flask import Blueprint, request, jsonify
from routes.auth import token_required
from models.post import Post, db
from models.user import Users
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

    new_post = Post.create(id=sf.__next__(), author=user_id.id, content=data['content'], created_at=datetime.utcnow().strftime("%Y%m%d"), updated_at=datetime.utcnow().strftime("%Y%m%d"), likes=[])

    return jsonify(success=True, message='New post was created successfully'), 200


@posts.route("/users/posts/<post_id>", methods=["DELETE"])
@token_required
def post2(user_id, post_id):

    find = Post.select().where(Post.id==post_id).get()

    if find is None:
        return jsonify(success=False, message='Unable to find that post'), 401

    if user_id.id != find.author:
        return jsonify(success=False, message='Unable to delete that post, user id\'s did not match'), 401

    Post.select().where(Post.id==post_id).get().delete_instance()

    return jsonify(success=True, message='Post was successfully deleted'), 200


@posts.route("/users/posts/<post_id>/like", methods=["PUT"])
@token_required
def post3(user_id, post_id):

    get_post = Post.select().where(Post.id==post_id).get()

    _likes = []

    if get_post.likes is None:
        likes.append(user_id.id)

    if user_id.id in get_post.likes:
        return jsonify(success=False, message='User is already in "likes"')

    _likes.append(get_post.likes)
    _likes.append(user_id.id)

    update = Post.update(likes=_likes).where(Post.id==post_id).execute()

    """
        query = (User
                .update(is_active=False)
                .where(User.registration_expired == True)
                .returning(User))

        # Send an email to every user that was deactivated.
        for deactivate_user in query.execute():
            send_deactivation_email(deactivated_user.email)
    """

    return jsonify(success=True, message=get_post.likes), 200


@posts.route("/users/posts/<post_id>", methods=["GET"])
@token_required
def post4(user_id, post_id):
    find_post = Post.select().where(Post.id==post_id).get()

    return jsonify(success=True, author=find_post.author, user=user_id.id, content=find_post.content, likes=len(find_post.likes)), 200

