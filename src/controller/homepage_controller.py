# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request

from src.services.post_service import get_homepage

homepage = Blueprint('homepage_controller', __name__)


@homepage.route('/homepage', methods=['GET'])
def api_get_homepage():
    username = request.args.get('username', None)
    page = int(request.args.get('page', 1))
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    only_mine = request.args.get('only_mine', 'false').lower() == 'true'

    posts = get_homepage(username, start_date, end_date, 10, page, only_mine)
    return jsonify([post.to_dict() for post in posts])
