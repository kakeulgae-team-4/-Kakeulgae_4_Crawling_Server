from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # flask_app.config.from_object(config)
    BASE_DIR = os.path.dirname(__file__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    with app.app_context():
        posts = models.Post.query.all()
        for post in posts:
            print(post)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
