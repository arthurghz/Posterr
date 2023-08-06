# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from src.services.post_service import get_post, delete_quote,quote_post, create_post, repost_post, delete_post, delete_repost

api_post = Blueprint('post_controller', __name__)

@api_post.route('/posts/<int:id>', methods=['GET'])
def view_post(id):
    post = get_post(id)
    return jsonify(post), 200

@api_post.route('/posts', methods=['POST'])
def new_post():
    data = request.json
    post = create_post(data)
    return jsonify(post), 201

@api_post.route('/posts/repost', methods=['POST'])
def repost():
    data = request.json
    post = repost_post(data)
    return jsonify(post), 201

@api_post.route('/posts/quote', methods=['POST'])
def api_quote():
    data = request.json
    post = quote_post(data)
    return jsonify(post), 201

@api_post.route('/posts/<int:id>', methods=['DELETE'])
def delete_single_post(id):
    result = delete_post(id)
    if result:
        return jsonify({'message': 'Post deleted successfully'}), 200
    return jsonify({'error': 'Post not found'}), 404

@api_post.route('/posts/repost/<int:id>', methods=['DELETE'])
def delete_repost_single_post(id):
    result = delete_repost(id)
    if result:
        return jsonify({'message': 'Repost deleted successfully'}), 200
    return jsonify({'error': 'Repost not found'}), 404

@api_post.route('/posts/quote/<int:id>', methods=['DELETE'])
def delete_quote_single_post(id):
    result = delete_quote(id)
    if result:
        return jsonify({'message': 'Quoted post deleted successfully'}), 200
    return jsonify({'error': 'Quoted post not found'}), 404


@api_post.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500
