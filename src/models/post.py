from . import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    content = db.Column(db.String(777))
    post_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    original_post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)
    quote = db.Column(db.String(777))
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'post_date': self.post_date.isoformat() if self.post_date else None,
            'original_post_id': self.original_post_id,
            'quote': self.quote
        }