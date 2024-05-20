from . import main
from flask import render_template
import os
# TODO 1 - Send emails (currently mailgun)
# TODO 2 - os.listdir path problem


@main.route("/")
def index():
    return render_template("index.html",
                           project_names=os.listdir("D:\\Python\\Problems & Projects\\Portfolio Projects Alpha\\Portfolio\\App\\static\\assets\\img\\portfolio\\thumbnails"))
