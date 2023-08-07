from ..models import db
from ..models.post import Post
from ..models.user import User
from sqlalchemy import func, and_ , desc, or_
from datetime import datetime, timedelta

def get_post(id):
    post = Post.query.filter_by(id=id).first()
    return post.to_dict()

def create_post(data):
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        raise Exception('User not found')
    now = datetime.now()

    start_of_day = datetime(now.year, now.month, now.day)

    count = db.session.query(func.count(Post.id)).filter(
        and_(Post.username == user.username, Post.datetime_creation >= start_of_day)
    ).scalar()

    if count >= 5:
        raise Exception('User has exceeded daily post limit')

    post = Post(text=data['text'], username=data['username'], datetime_creation=datetime.now())
    db.session.add(post)
    db.session.commit()

    return post.to_dict()

def repost_post(data):
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        raise Exception('User not found')
    original_post = Post.query.get(data['original_post_id'])

    now = datetime.now()

    start_of_day = datetime(now.year, now.month, now.day)

    count = db.session.query(func.count(Post.id)).filter(
        and_(Post.username == user.username, Post.datetime_creation >= start_of_day)
    ).scalar()

    if count >= 5:
        raise Exception('User has exceeded daily post limit')

    if original_post.repost_from_id is not None or original_post.quote_from_id is not None:
        raise Exception('Cannot repost a repost or a quote-post')

    post = Post(text=original_post.text, username=data['username'], datetime_creation=now,
                repost_from_id=original_post.id)
    db.session.add(post)
    db.session.commit()

    return post.to_dict()

def quote_post(data):
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        raise Exception('User not found')

    now = datetime.now()
    original_post = Post.query.filter_by(id=data["original_post_id"]).first()
    start_of_day = datetime(now.year, now.month, now.day)
    count = db.session.query(func.count(Post.id)).filter(
        and_(Post.username == user.username, Post.datetime_creation >= start_of_day)
    ).scalar()

    if count >= 5:
        raise Exception('User has exceeded daily post limit')
    if original_post:
        username = user.username
        quoted_post = Post(text=data["quote_text"], username=username, datetime_creation=datetime.now(),
                           quote_from_id=original_post.id)
        db.session.add(quoted_post)
        db.session.commit()
        return quoted_post.to_dict()
    return None


def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        post.is_deleted = True
        db.session.commit()
        return True
    return False

def delete_repost(id):
    repost = Post.query.filter_by(id=id).first()
    if repost and repost.repost_from_id is not None:
        repost.is_deleted = True
        db.session.commit()
        return True
    return False

def delete_quote(id):
    repost = Post.query.filter_by(id=id).first()
    if repost and repost.quote_from_id is not None:
        repost.is_deleted = True
        db.session.commit()
        return True
    return False

def quote(quote_post_id):
    quoted_post = Post.query.filter_by(id=quote_post_id).first()
    if quoted_post:
        quoted_post.is_deleted = True
        db.session.commit()
        return True
    return False

def get_homepage(username=None, start_date=None, end_date=None, posts_per_page=10, page=1, only_mine=False):
    my_query = Post.query
    if username:
        if only_mine:
            my_query = my_query.filter(Post.username == username)
        else:
            my_query = my_query.filter(or_(Post.username == username, Post.repost_from_id != None, Post.quote_from_id != None))
    if start_date:
        my_query = my_query.filter(Post.datetime_creation >= start_date)
    if end_date:
        my_query = my_query.filter(Post.datetime_creation <= end_date)

    return my_query.order_by(desc(Post.datetime_creation)).paginate(page,posts_per_page,error_out=False).items
