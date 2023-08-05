# -*- coding: utf-8 -*-
from src.models.user import User


def get_user(username):
    user = User.query.filter_by(username=username).first()
    return user.to_dict()

def get_user_posts(username):
    user = User.query.filter_by(username=username).first()
    return user.posts_to_dict()
