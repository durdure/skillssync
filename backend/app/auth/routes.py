from .models import User
from app.mentor.models import Mentor
from flask import request, Blueprint, jsonify, render_template, url_for, redirect
from app import db, bcrypt
from flask_login import current_user, login_user, logout_user, login_required
from app.utils.email import send_email
from app.utils.token_1 import confirm_token, generate_confirmation_token
import datetime


auth = Blueprint('auth', __name__)

@auth.route('/user/register', methods=['POST'], strict_slashes=False)
def register_user():

    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_pass = data.get('confirm_pass')

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({'error': 'A user with that email already exists'}), 400
    if password != confirm_pass:
        return jsonify({'error':'Passwords dont match!'}), 400
    if len(password) < 7:
        return jsonify({'error':'Password must be at least 7 characters.'}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    token = generate_confirmation_token(email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    html = render_template('email/activate.html', confirm_url=confirm_url)
    subject = "Email Confirmation Link"
    send_email(email, subject, html)

    response_data = {
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'image_file': new_user.image_file
    }

    return jsonify({'data': response_data, 'message':'User registered successfully, check your email to verify'}), 201


@auth.route('/mentor/register', methods=['POST'], strict_slashes=False)
def register_mentor():

    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_pass = data.get('confirm_pass')
    full_name = data.get("full_name")

    mentor = Mentor.query.filter_by(email=email).first()

    if mentor:
        return jsonify({'error': 'A mentor with that email already exists'}), 400
    if password != confirm_pass:
        return jsonify({'error':'Passwords dont match!'}), 400
    if len(password) < 7:
        return jsonify({'error':'Password must be at least 7 characters.'}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_mentor = Mentor(username=username, email=email, password=hashed_password, mentor=True, full_name= full_name)
    db.session.add(new_mentor)
    db.session.commit()

    token = generate_confirmation_token(email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    html = render_template('email/activate.html', confirm_url=confirm_url)
    subject = "Email Confirmation Link"
    send_email(email, subject, html)

    response_data = {
        'id': new_mentor.id,
        'username': new_mentor.username,
        'email': new_mentor.email,
        'image_file': new_mentor.image_file
    }

    return jsonify({'data': response_data, 'message':'Mentor registered successfully, check your email to verify'}), 201



@auth.route('/login', methods=['POST'], strict_slashes=False)
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    # Check if the provided credentials match a user
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'You have successfully logged in', 'user_id': user.id}), 200

    # If no matching user or mentor found, return an error
    return jsonify({'error': 'Please check your credentials and try again.'}), 401


@auth.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logout successful'}), 200
    else:
        return jsonify({'error': 'User has not logged in'}), 401



@auth.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        return jsonify({'error' : 'The confirmation link is invalid or has expired'}), 401
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        return jsonify({'message' : 'Account already confirmed. Please login.'}), 200
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        return jsonify({'message' : 'You have confirmed your account. Thanks!'}), 200



@auth.route('/resend')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    html = render_template('email/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    return jsonify({'message' : 'A new confirmation email has been sent.'})


@auth.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()

    if not data or 'email' not in data:
        return jsonify({"error": "Email is required"}), 400

    email = data['email']
    user = User.query.filter_by(email=email).first()

    if user:
        # Generate a unique token
        token = generate_confirmation_token(email)

        # Send reset password email
        reset_url = url_for('auth.reset_password', token=token, _external=True)
        template = render_template('email/reset_password.html', reset_url=reset_url)
        send_email(user.email, 'Reset Your Password', template)

        return jsonify({"message": "Check your email for a password reset link."}), 200
    else:
        return jsonify({"error": "Email address not found"}), 404

@auth.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    email = confirm_token(token)

    if not email:
        return jsonify({"error": "Invalid or expired reset password link"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    if not data or 'new_password' not in data or 'confirm_password' not in data:
        return jsonify({"error": "New password and confirm password are required"}), 400

    new_password = data['new_password']
    confirm_password = data['confirm_password']

    if new_password == confirm_password:
        # Update the user's password
        user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        db.session.commit()

        return jsonify({"message": "Password reset successfully"}), 200
    else:
        return jsonify({"error": "Passwords do not match"}), 400