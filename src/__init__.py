from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config
from src.controller.generic_controller import generic_controller
from src.controller.homepage_controller import homepage
from src.controller.post_controller import api_post
from src.controller.user_profile_controller import user_profile
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    swagger_ui_blueprint = get_swaggerui_blueprint(
        '/api/docs',
        '/swagger.json',
        config={
            'app_name': "Posterr api docs"
        }
    )


    app.register_blueprint(swagger_ui_blueprint, url_prefix="/api/docs")


    app.register_blueprint(homepage)
    app.register_blueprint(api_post)
    app.register_blueprint(generic_controller)
    app.register_blueprint(user_profile)

    return app
