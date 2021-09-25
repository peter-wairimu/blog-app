from .import db
from flask_login import UserMixin
from sqlalchemy.sql import func

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



