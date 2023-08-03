from datetime import datetime

from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(14), unique=True)
    joined_date = db.Column(db.DateTime)
    posts = db.relationship('Post', backref='User', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'joined_date': self.joined_date.strftime('%Y-%m-%d %H:%M:%S') if self.joined_date else None,
            'posts': [post.to_dict() for post in sorted(self.posts, key=lambda p: p.post_date, reverse=True)[:5]],
            'total_posts': len(self.posts)
        }

    def posts_to_dict(self):
        return [post.to_dict() for post in sorted(self.posts, key=lambda p: p.post_date, reverse=True)]