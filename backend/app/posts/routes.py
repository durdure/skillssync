from flask import Blueprint, request, jsonify
from app import db
from flask_login import login_required, current_user
from app.posts.models import Post


post = Blueprint('post', __name__)

@post.route("/new", methods=['POST'], strict_slashes=False)
# @login_required
def new_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    new_post = Post(title, content, author=current_user)
    db.session.add(new_post)
    db.session.commit()

    data = {
        'post_id' : new_post.id,
        'title' : new_post.title,
        'content' : new_post.content
    }

    return jsonify({'data':data, 'message':"Post created succefully"}), 201