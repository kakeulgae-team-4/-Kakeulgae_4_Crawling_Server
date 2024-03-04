from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello_pybo():
    return "This is flask_app"


@bp.route('/hello')
def hi():
    return "This is hello"
