from flask import Blueprint, jsonify, request, current_app
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
@check_confirmed
@mentor_restricted
def get_user_profile():
    # Check if the user is authenticated
    if current_user.is_authenticated:
        # Access user attributes only if authenticated
        profile_data = {
            'user_id': current_user.id,
            'username': current_user.username,
            'email': current_user.email,
            'profile_image': current_user.image_file,
            'bio': current_user.bio,
            'phone_no': current_user.phone_no,
            'address': current_user.address,
        }
        return jsonify(profile_data)
    else:
        # Handle the case where the user is not authenticated
        return jsonify({'error': 'User not authenticated'}), 401


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@user.route('/profile', methods=['PUT'], strict_slashes=False)
@login_required
@check_confirmed
@mentor_restricted
def update_user_profile():
    try:
        data = request.get_json()

        current_user.email = data.get('email', current_user.email)
        current_user.username = data.get('username', current_user.username)
        current_user.bio = data.get('bio', current_user.bio)
        current_user.phone_no = data.get('phone_no', current_user.phone_no)
        current_user.address = data.get('address', current_user.address)

        # Handle image upload
        if 'profile_image' in request.files:
            profile_image = request.files['profile_image']
            if profile_image:
                picture_fn = save_picture(profile_image)
                # Delete previous image if needed
                # You may want to implement a function for this
                # delete_previous_image(current_user.profile_image)
                current_user.profile_image = picture_fn

        db.session.commit()

        return jsonify({"message": "Profile updated successfully"})

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Username already exists. Choose a different username."}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


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
