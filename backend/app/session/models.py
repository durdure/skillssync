from datetime import datetime
from app import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    mentor = db.relationship('Mentor', foreign_keys=[mentor_id], backref=db.backref('requested_sessions', lazy=True))
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('mentee_sessions', lazy=True))


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    meeting_url = db.Column(db.String(255), nullable=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='Pending')

    mentor = db.relationship('Mentor', foreign_keys=[mentor_id], backref=db.backref('mentored_sessions', lazy=True))
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('attended_sessions', lazy=True))
