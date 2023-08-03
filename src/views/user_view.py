from flask import Blueprint, jsonify, abort

from src.controllers import get_user, get_user_posts

user_view = Blueprint('user_view', __name__)

@user_view.route('/users/<username>', methods=['GET'])
def view_user(username):
    user = get_user(username)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user), 200

@user_view.route('/users/<username>/posts', methods=['GET'])
def view_user_posts(username):
    posts = get_user_posts(username)
    if posts is None:
        abort(404, description="User has no posts")
    return jsonify(posts), 200
