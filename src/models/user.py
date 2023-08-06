# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.sql import text

from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(14), unique=True, nullable=False)
    date_joined = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username):
        self.username = username

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'date_joined': self.date_joined.strftime('%Y-%m-%d') if self.date_joined else None,
            'total_posts': len(self.posts)
        }

    def posts_to_dict(self):
        return [post.to_user_posts() for post in sorted(self.posts, key=lambda p: p.datetime_creation, reverse=True)]
