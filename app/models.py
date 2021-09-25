from .import db
from flask.app import Flask
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())



