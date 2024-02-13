from flask import Blueprint, jsonify, request, render_template
from flask_login import current_user
from app.posts.models import Post

test = Blueprint('test', __name__)

@test.route('/')
def index():
    return render_template('index.html', user=current_user)


@test.route('/about')
def about():
    posts = Post.query.all()
    return render_template('about.html', user=current_user, posts=posts)
