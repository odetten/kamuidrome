from . import db
from flask_login import UserMixin
from datetime import datetime

#creating the objects for user and messages

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(30), nullable=False, index=True)
    username = db.Column(db.String(40), nullable=False)
    text = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    
