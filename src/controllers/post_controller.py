from ..models import db
from ..models.post import Post
from ..models.user import User
from sqlalchemy import func, and_
from datetime import datetime, timedelta
def get_post(id):
    post = Post.query.filter_by(id=id).first()
    return post.to_dict()

def create_post(data):
    user = User.query.get(data['user_id'])

    now = datetime.now()

    start_of_day = datetime(now.year, now.month, now.day)

    count = db.session.query(func.count(Post.id)).filter(
        and_(Post.user_id == user.id, Post.post_date >= start_of_day)
    ).scalar()

    if count >= 5:
        raise Exception('User has exceeded daily post limit')


    post = Post(content=data['content'], user_id=data['user_id'],post_date=datetime.now())
    db.session.add(post)
    db.session.commit()

    return post.to_dict()


def repost_post(data):
    user = User.query.get(data['user_id'])

    original_post = Post.query.get(data['original_post_id'])

    now = datetime.now()

    start_of_day = datetime(now.year, now.month, now.day)

    count = db.session.query(func.count(Post.id)).filter(
        and_(Post.user_id == user.id, Post.post_date >= start_of_day)
    ).scalar()

    if count >= 5:
        raise Exception('User has exceeded daily post limit')

    if original_post.original_post_id is not None:
        raise Exception('Cannot repost a repost or a quote-post')

    post = Post(content=original_post.content, user_id=data['user_id'], post_date=now,
                original_post_id=original_post.id, quote=data.get('quote'))
    db.session.add(post)
    db.session.commit()

    return post.to_dict()