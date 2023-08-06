# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, abort

from src.services import get_user, get_user_posts

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/profile/<username>', methods=['GET'])
def view_user(username):
    user = get_user(username)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user), 200

@user_profile.route('/profile/<username>/posts', methods=['GET'])
def view_user_posts(username):
    posts = get_user_posts(username)
    if posts is None:
        abort(404, description="User has no posts")
    return jsonify(posts), 200
