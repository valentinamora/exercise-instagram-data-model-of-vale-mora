import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er  # type: ignore 

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    
    # Relationships
    followers = relationship('Follower', foreign_keys='Follower.user_to_id')
    following = relationship('Follower', foreign_keys='Follower.user_from_id')
    posts = relationship('Post')

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    caption = Column(String(2000)) 
    created_at = Column(DateTime)
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment')
    media = relationship('Media')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    author = relationship('User')
    post = relationship('Post')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(50)) 
    url = Column(String(255))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post')


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

