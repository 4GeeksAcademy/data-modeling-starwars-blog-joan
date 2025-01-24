import os
import sys
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)

class Post(db.Model):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.ID), nullable=False)


class Media(db.Model):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey(Post.ID), nullable=False)

class Comment(db.Model):
    __tablename__ = 'Comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, ForeignKey(User.ID), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey(Post.ID), nullable=False)

class Follower(db.Model):
    __tablename__ = 'Follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = db.Column(db.Integer, ForeignKey(User.ID), primary_key=True, nullable=False)
    user_to_id = db.Column(db.Integer, ForeignKey(User.ID), primary_key=True, nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e