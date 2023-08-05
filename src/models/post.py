# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import ForeignKey

from . import db
from .user import User

class Post(db.Model):
    '''Post Model'''
    __tablename__ = 'post'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    repost_from_id = db.Column(db.BigInteger, ForeignKey('post.id'), nullable=True)
    quote_from_id = db.Column(db.BigInteger, ForeignKey('post.id'), nullable=True)
    user_id = db.Column(db.BigInteger, ForeignKey('user.id'), nullable=False)
    datetime_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    text = db.Column(db.String(777), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref='posts')
    repost = db.relationship('Post', remote_side=[id], foreign_keys=[repost_from_id], backref='reposts')
    quote = db.relationship('Post', remote_side=[id], foreign_keys=[quote_from_id], backref='quotes')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'repost_from_id': self.repost_from_id,
            'quote_from_id': self.quote_from_id,
            'datetime_creation': self.datetime_creation.strftime('%Y-%m-%d %H:%M:%S') if self.datetime_creation else None,
            'text': self.text,
            'is_deleted': self.is_deleted,
        }
