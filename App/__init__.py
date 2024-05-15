from flask import Flask
from .main import main as main_blueprint
# TODO Use logging


def init_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    return app
