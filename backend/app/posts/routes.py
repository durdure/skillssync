from flask import Blueprint, request, jsonify
from app import db
from flask_login import login_required, current_user
from app.posts.models import Post, Comment
from sqlalchemy.exc import SQLAlchemyError


post = Blueprint('post', __name__)


@post.route("/", methods=['GET'], strict_slashes=False)
def all_posts():
    posts = Post.query.all()

    # Convert posts to a list of dictionaries for JSON serialization
    posts_data = [
        {
            'post_id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'date_posted': post.date_posted.isoformat(),
        } for post in posts
    ]

    return jsonify({'status': 'success', 'data': posts_data})


@post.route("/user_posts", methods=['GET'], strict_slashes=False)
@login_required
def user_posts():
    user_id = current_user.id
    user_posts = Post.query.filter_by(user_id=user_id).all()

    # Convert user_posts to a list of dictionaries for JSON serialization
    user_posts_data = [
        {
            'post_id': post.id,
            'title': post.title,
            'content': post.content,
            'date_posted': post.date_posted.isoformat(),
        } for post in user_posts
    ]

    return jsonify({'status': 'success', 'data': user_posts_data})




@post.route("/new", methods=['POST'], strict_slashes=False)
@login_required
def new_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    try:
        new_post = Post(title=title, content=content, author=current_user)
        db.session.add(new_post)
        db.session.commit()

        response_data = {
            'post_id': new_post.id,
            'title': new_post.title,
            'content': new_post.content,
        }

        return jsonify({'status': 'success', 'data': response_data, 'message': 'Post created successfully'}), 201

    except SQLAlchemyError as e:
        # Catch database-related exceptions and extract the error message
        db.session.rollback()  # Rollback the transaction in case of an exception
        error_message = str(e)
        return jsonify({'status': 'error', 'message': f'Failed to create post. Error: {error_message}'}), 500
    

@post.route("/view/<int:post_id>", methods=['GET'], strict_slashes=False)
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    post_data = {
        'post_id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'date_posted': post.date_posted.isoformat(),
    }
    return jsonify({'status': 'success', 'data': post_data})


@post.route("/update/<int:post_id>", methods=['PUT'], strict_slashes=False)
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Check if the current user is the author of the post
    if current_user != post.author:
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)

    try:
        db.session.commit()

        response_data = {
            'post_id': post.id,
            'title': post.title,
            'content': post.content,
        }

        return jsonify({'status': 'success', 'data': response_data, 'message': 'Post updated successfully'})

    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = str(e)
        return jsonify({'status': 'error', 'message': f'Failed to update post. Error: {error_message}'}), 500


@post.route("/delete/<int:post_id>", methods=['DELETE'], strict_slashes=False)
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Check if the current user is the author of the post
    if current_user != post.author:
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    try:
        db.session.delete(post)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Post deleted successfully'})

    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = str(e)
        return jsonify({'status': 'error', 'message': f'Failed to delete post. Error: {error_message}'}), 500
    

@post.route("/new_comment/<int:post_id>", methods=['POST'], strict_slashes=False)
@login_required
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    content = data.get('content')

    try:
        new_comment = Comment(content=content, post=post, user=current_user)
        db.session.add(new_comment)
        db.session.commit()

        response_data = {
            'comment_id': new_comment.id,
            'content': new_comment.content,
        }

        return jsonify({'status': 'success', 'data': response_data, 'message': 'Comment added successfully'}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = str(e)
        return jsonify({'status': 'error', 'message': f'Failed to add comment. Error: {error_message}'}), 500


@post.route("/delete_comment/<int:comment_id>", methods=['DELETE'], strict_slashes=False)
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Check if the current user is the author of the comment
    if current_user != comment.user:
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    try:
        db.session.delete(comment)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Comment deleted successfully'})

    except SQLAlchemyError as e:
        db.session.rollback()
        error_message = str(e)
        return jsonify({'status': 'error', 'message': f'Failed to delete comment. Error: {error_message}'}), 500