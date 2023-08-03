import os
from flask import Flask
from src.models import db
from src.views import user_view, post_view


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)

    app.register_blueprint(user_view)
    app.register_blueprint(post_view)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8080)
