from flask import Blueprint, jsonify, request, current_app, render_template, url_for, flash, redirect
from flask_login import login_required, current_user
import os
from PIL import Image
import secrets
from app import db
from app.utils.decorators_1 import check_confirmed, mentor_required
from sqlalchemy.exc import IntegrityError
from .models import Mentor

mentor = Blueprint('mentor', __name__)

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


@mentor.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@login_required
@check_confirmed
@mentor_required
def update_mentor_profile():
    if request.method == 'POST':
        try:
            data = request.form

            current_user.email = data.get('email', current_user.email)
            current_user.username = data.get('username', current_user.username)
            current_user.bio = data.get('bio', current_user.bio)
            current_user.phone_no = data.get('phone_no', current_user.phone_no)
            current_user.address = data.get('address', current_user.address)
            current_user.full_name = data.get('full_name', current_user.full_name)
            current_user.profession = data.get('profession', current_user.profession)
            current_user.job_title = data.get('job_title', current_user.job_title)
            current_user.company = data.get('company', current_user.company)
            current_user.skills = data.get('skills', current_user.skills)
            current_user.availability = data.get('availability', current_user.availability)
            current_user.languages_spoken = data.get('languages_spoken', current_user.languages_spoken)

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

            flash('Profile updated successfully', 'success')

        except IntegrityError as e:
            db.session.rollback()
            flash('Username already exists. Choose a different username')
            return jsonify({"error": "Username already exists. Choose a different username."}), 400

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    elif request.method == 'GET':
        # Pass mentor attributes to the HTML template for pre-filling the form
        mentor_data = {
            'profile_image': current_user.image_file,
            'email': current_user.email,
            'username': current_user.username,
            'bio': current_user.bio,
            'phone_no': current_user.phone_no,
            'address': current_user.address,
            'full_name': current_user.full_name,
            'profession': current_user.profession,
            'job_title': current_user.job_title,
            'company': current_user.company,
            'skills': current_user.skills,
            'availability': current_user.availability,
            'languages_spoken': current_user.languages_spoken
        }
        # Render HTML template for updating mentor profile, passing mentor data
        return render_template('mentor/account.html', mentor=mentor_data)


@mentor.route('/all', methods=['GET'], strict_slashes=False)
def list_mentors():
    try:
        # Query all mentors from the database
        mentors = Mentor.query.all()

        # Prepare mentor data to be returned in the response
        mentor_data = []
        for mentor in mentors:
            mentor_info = {
                'user_id': mentor.id,
                'username': mentor.username,
                'email': mentor.email,
                'profile_image': mentor.image_file,
                'full_name': mentor.full_name,
                'profession': mentor.profession,
                'job_title': mentor.job_title,
                'company': mentor.company,
                'skills': mentor.skills,
                'availability': mentor.availability,
                'bio' : mentor.bio,
                'languages_spoken': mentor.languages_spoken
            }
            mentor_data.append(mentor_info)

        return render_template('mentors.html', mentors=mentor_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@mentor.route('/view/<int:mentor_id>', methods=['GET'], strict_slashes=False)
def view_mentor(mentor_id):
    try:
        # Query the mentor by ID
        mentor = Mentor.query.get(mentor_id)

        if not mentor:
            return jsonify({'error': 'Mentor not found'}), 404

        # Prepare mentor data to be returned in the response
        mentor_data = {
            'user_id': mentor.id,
            'username': mentor.username,
            'email': mentor.email,
            'profile_image': mentor.image_file,
            'full_name': mentor.full_name,
            'profession': mentor.profession,
            'job_title': mentor.job_title,
            'company': mentor.company,
            'skills': mentor.skills,
            'availability': mentor.availability,
            'languages_spoken': mentor.languages_spoken
        }

        return jsonify({'mentor': mentor_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
