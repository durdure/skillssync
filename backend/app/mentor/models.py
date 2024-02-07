from app import db
from app.auth.models import User


class Mentor(User):
    __tablename__ = 'mentor'

    id = db.Column(db.Integer,db.ForeignKey('user.id'), primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100))
    job_title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    skills = db.Column(db.String(200))
    availability = db.Column(db.String(200))
    languages_spoken = db.Column(db.String(200))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)