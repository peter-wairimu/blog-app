from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
import markdown2
from ..request import get_quote



@main.route("/")
def home():
    quotes = get_quote()
    return render_template("index.html",quotes=quotes)




