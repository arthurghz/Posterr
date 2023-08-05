# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from src.controllers.post_controller import get_post, create_post, repost_post

post_view = Blueprint('post_view', __name__)

@post_view.route('/posts/<id>', methods=['GET'])
def view_post(id):
    post = get_post(id)
    return jsonify(post), 200

@post_view.route('/posts', methods=['POST'])
def new_post():
    try:
        data = request.json
        post = create_post(data)
        return jsonify(post), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@post_view.route('/posts/repost', methods=['POST'])
def repost():
    try:
        data = request.json
        post = repost_post(data)
        return jsonify(post), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
