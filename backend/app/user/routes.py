from flask import Blueprint, jsonify, request, flash, current_app, render_template, redirect, url_for
from flask_login import login_required, current_user
import os
from PIL import Image
import secrets
from app import db
from app.utils.decorators_1 import check_confirmed, mentor_restricted
from sqlalchemy.exc import IntegrityError
from app.auth.models import User
from flask_mail import Message
from app import mail
from app.config import Config
from datetime import datetime
from app.session.models import Request
from app.posts.models import Post
from sqlalchemy.exc import SQLAlchemyError


user = Blueprint('user', __name__)


@user.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    try:
        # Send email
        msg = Message(subject='New Contact Us Form Submission',
                      sender=Config.MAIL_DEFAULT_SENDER,
                      recipients=[Config.MAIL_DEFAULT_SENDER])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        return jsonify({'message': 'Your email has been sent successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@login_required
@user.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@mentor_restricted
def update_user_profile():
    if request.method == 'POST':
        try:
            data = request.form

            current_user.email = data.get('email', current_user.email)
            current_user.username = data.get('username', current_user.username)
            current_user.bio = data.get('bio', current_user.bio)
            current_user.phone_no = data.get('phone_no', current_user.phone_no)
            current_user.address = data.get('address', current_user.address)

            # Handle image upload
            if 'profile_image' in request.files:
                profile_image = request.files['profile_image']
                if profile_image.filename != '':
                    picture_fn = save_picture(profile_image)
                    current_user.image_file = picture_fn

            db.session.commit()

            flash('Profile updated successfully', 'success')

            # Redirect to the same page after processing the POST request
            return redirect(url_for('user.update_user_profile'))

        except IntegrityError as e:
            db.session.rollback()
            flash('Username already exists. Choose a different username')
            return jsonify({"error": "Username already exists. Choose a different username."}), 400

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    elif request.method == 'GET':
        # Pass user attributes to the HTML template for pre-filling the form
        user_data = {
            'profile_image': current_user.image_file,
            'email': current_user.email,
            'username': current_user.username,
            'bio': current_user.bio,
            'phone_no': current_user.phone_no,
            'address': current_user.address,
        }
        # Render HTML template for updating user profile, passing user data
        return render_template('user/account.html', user_data=user_data, user=current_user)

    # In case the request method is neither GET nor POST, return a default response
    return "Method not allowed", 405

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_images', picture_fn)

    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@user.route('/view/<int:user_id>', methods=['GET'], strict_slashes=False)
def view_user(user_id):
    try:
        # Query the user by ID
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Prepare user data to be returned in the response
        user_data = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'profile_image': user.image_file,
            'bio': user.bio,
            'phone_no': user.phone_no,
            'address': user.address
            # Add any additional user attributes here
        }

        return jsonify({'user': user_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@login_required
@user.route('/dashboard', methods=['GET', 'POST'])
@check_confirmed
def user_dashboard():
    if request.method == 'POST':
        data = request.form
        title = data.get('title')
        content = data.get('content')

        try:
            new_post = Post(title=title, content=content, author=current_user)
            db.session.add(new_post)
            db.session.commit()

            flash('You have posted a testimony', 'success')
            return redirect(url_for('user.user_dashboard'))
        except SQLAlchemyError as e:
            # Catch database-related exceptions and extract the error message
            db.session.rollback()  # Rollback the transaction in case of an exception
            error_message = str(e)
            return jsonify({'status': 'error', 'message': f'Failed to create post. Error: {error_message}'}), 500
    else:  
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%I:%M %p %b %d')

        user_id = current_user.id
        pending_requests = Request.query.filter_by(user_id=user_id, status='Pending').all()
        sessions_requests = Request.query.filter_by(user_id=user_id).all()
        return render_template('user/user_dashboard.html', pending_requests=pending_requests, 
                            user=current_user, date=formatted_datetime, sessions_requests=sessions_requests)


@user.route('/cancel_request/<int:request_id>')
def cancel_request(request_id):
    session_request = Request.query.get(request_id)
    if session_request:
        session_request.status = 'Cancelled'
        db.session.commit()
        flash('You have canceled a request', 'success')
    return redirect(url_for('user.user_dashboard'))
