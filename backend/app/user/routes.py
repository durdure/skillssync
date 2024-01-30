from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required, current_user
import os
from PIL import Image
import secrets
from app import db
from app.utils.decorators_1 import check_confirmed

user = Blueprint('user', __name__)

@user.route('/profile', methods=['GET'], strict_slashes=False)
@login_required
@check_confirmed
def get_profile():
    profile_data = {
        'user_id': current_user.user_id,
        'username': current_user.username,
        'email': current_user.email,
        'profile_image': current_user.profile_image,
        'bio': current_user.bio,
        'phone_no': current_user.phone_no,
        'address': current_user.address
    }

    return jsonify(profile_data)

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
def update_profile():
    try:
        data = request.get_json()

        current_user.username = data.get('username', current_user.username)
        current_user.email = data.get('email', current_user.email)
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

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
