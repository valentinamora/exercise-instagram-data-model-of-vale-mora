import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er # type: ignore

Base = declarative_base()

class User(Base):
     __tablename__ = 'users'
     id=Column(Integer,primary_key=True)
     username=Column(String(50),unique=True,nullable=False)
     firstname = Column(String(50))
     lastname = Column(String(50))
     email = Column (String(30), unique=True,nullable=False)
     follower = relationship('Follower')
     posts = relationship('post')

class Follower(Base):
     __tablename__ = 'follower'
     id=Column(Integer,primary_key=True)
     user_from_id = Column (Integer, ForeignKey('user.id'))
     user_to_id = Column (Integer, ForeignKey('user.id'))
       

class Comment(Base):
    __tablename__ = 'comment'
    id = Column (Integer,primary_key=True)
    comment_text = Column (String(100))
    author_id = Column (Integer, ForeignKey('user.id'))
    post_id = Column (Integer, ForeignKey('post.id'))
    posts= relationship('Post')
    
class Post(Base):
    __tablename__ = 'post'
    id= Column (Integer,primary_key=True)
    user_id= Column (Integer, ForeignKey('user.id'))
    users = relationship('User')

class Media(Base):
    __tablename__ = 'media'
    id = Column (Integer,primary_key=True)
    # type = Column (enumerate(50))
    url = Column (String (100))
    post_id = Column (Integer, ForeignKey('post.id'))



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
