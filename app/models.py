from .import db
from flask.app import Flask
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,check_password_hash
from .import login_manager
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy





class Quote(db.Model):
  '''
  Comments data
  '''
  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key=True)
  comment = db.Column(db.String(255))
  title = db.Column(db.Integer,db.ForeignKey('pitches.id'))
  poster = db.Column(db.Integer,db.ForeignKey('users.id'))
  def save_comment(self):
    db.session.add(self)
    db.session.commit()
  def __repr__(self):
    return f'{self.comment}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    



