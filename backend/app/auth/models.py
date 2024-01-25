from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user' 
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    
#session handling models
class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    availability = db.Column(db.String(200))
    user = db.relationship('User', backref=db.backref('mentor', uselist=False), lazy=True)

class Mentee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('mentee', uselist=False), lazy=True)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.String(200))
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'), nullable=False)
    mentor = db.relationship('Mentor', backref=db.backref('sessions_as_mentor', lazy=True))
    mentee_id = db.Column(db.Integer, db.ForeignKey('mentee.id'), nullable=False)
    mentee = db.relationship('Mentee', backref=db.backref('sessions_as_mentee', lazy=True))
    status = db.Column(db.String(200), default='pending')

