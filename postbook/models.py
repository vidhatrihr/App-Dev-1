from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  name = Column(String, nullable=False)
  posts = relationship('Post', back_populates='user', cascade='all, delete')
  likes = relationship('Like', back_populates='user')


class Post(db.Model):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  body = Column(String, nullable=False)
  user = relationship('User', back_populates='posts')
  likes = relationship('Like', back_populates='post', cascade='all, delete')


class Like(db.Model):
  __tablename__ = 'likes'
  id = Column(Integer, primary_key=True, autoincrement=True)
  post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  user = relationship('User', back_populates='likes')
  post = relationship('Post', back_populates='likes')
