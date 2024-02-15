from flask import Blueprint, flash, url_for, redirect, render_template
from .models import Request
from app import db
from app.mentor.models import Mentor
from datetime import datetime
from flask_login import current_user, login_required


session = Blueprint('session', __name__)

@session.route('/request_session/<int:mentor_id>')
@login_required
def request_session(mentor_id):
    user_id = current_user.id
    mentor = Mentor.query.get(mentor_id)
    if mentor:
        session = Request(mentor_id=mentor_id, user_id=user_id, date=datetime.now())
        db.session.add(session)
        db.session.commit()
    flash('You have requested a session, check your dashboard for more info', 'success')
    return redirect(url_for('mentor.list_mentors'))

