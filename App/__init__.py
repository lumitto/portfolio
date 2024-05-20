from flask import Flask
from .main import main as main_blueprint
# TODO Add 3 or 6 more works


def init_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    return app
