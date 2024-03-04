from flask import Flask
from flask_migrate import Migrate
import os
from .models import *


def create_app():
    app = Flask(__name__)
    BASE_DIR = os.path.dirname(__file__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ORM
    from .views import main_views
    app.register_blueprint(main_views.bp)

    db.init_app(app)

    return app


app = create_app()
migrate = Migrate(app, db)
