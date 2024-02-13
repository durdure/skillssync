from app import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'user' 
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(255), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.String(1000), nullable=True)
    phone_no = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    mentor = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')


