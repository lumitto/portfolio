from . import main
from flask import render_template
import os


@main.route("/")
def index():
    return render_template("index.html",
                           project_names=os.listdir(os.path.join(os.getcwd(),'App', 'static', 'assets',
                                                                 'img', 'portfolio', 'thumbnails')))
