from flask import Blueprint, jsonify, request, render_template
from flask_login import current_user
from app.posts.models import Post
from app.session.models import Session
from app.mentor.models import Mentor
from app.auth.models import User
from app import db

nav = Blueprint('nav', __name__)

@nav.route('/')
def index():
    # Query to find the top 3 mentors with the most sessions
    top_mentors = Mentor.query.limit(3)
    
    return render_template('index.html', user=current_user, top_mentors=top_mentors)



@nav.route('/about')
def about():
    session_count = len(Session.query.all())
    mentor_count = len(Mentor.query.all())
    user_count = len(User.query.all())
    mentee_count = user_count - mentor_count
    posts = Post.query.all()
    return render_template('about.html', user=current_user, posts=posts, session_count=session_count,
                           mentor_count=mentor_count, mentee_count=mentee_count)


@nav.route('/team')
def team():
    return render_template('team.html', user=current_user)
