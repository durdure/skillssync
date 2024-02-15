from .models import User
from app.mentor.models import Mentor
from flask import request, Blueprint, flash, render_template, url_for, redirect, jsonify
from app import db, bcrypt
from flask_login import current_user, login_user, logout_user, login_required
from app.utils.email import send_email
from app.utils.token_1 import confirm_token, generate_confirmation_token
import datetime


auth = Blueprint('auth', __name__)

@auth.route('/user/register', methods=['GET','POST'], strict_slashes=False)
def register_user():

    data = request.form

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_pass = data.get('confirm_pass')

    user = User.query.filter_by(email=email).first()

    if request.method == 'POST':
        if user:
            flash('A user with that email already exists.', 'danger')
        elif password != confirm_pass:
            flash('Paswords dont match!', 'danger')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            token = generate_confirmation_token(email)
            confirm_url = url_for('auth.confirm_email', token=token, _external=True)
            html = render_template('email/activate.html', confirm_url=confirm_url)
            subject = "Email Confirmation Link"
            send_email(email, subject, html)

            return render_template('error/confirm_account.html', user=current_user)
        
    return render_template('auth/signup_user.html', title='Sign up', user=current_user)
    


@auth.route('/mentor/register', methods=['POST', 'GET'], strict_slashes=False)
def register_mentor():

    data = request.form

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_pass = data.get('confirm_pass')
    full_name = data.get("full_name")

    mentor = Mentor.query.filter_by(email=email).first()

    if request.method  == 'POST':
        if mentor:
            flash('A mentor with that email already exists', 'danger')
        elif password != confirm_pass:
            flash('Passwords dont match!', 'danger')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_mentor = Mentor(username=username, email=email, password=hashed_password, mentor=True, full_name= full_name)
            db.session.add(new_mentor)
            db.session.commit()

            token = generate_confirmation_token(email)
            confirm_url = url_for('auth.confirm_email', token=token, _external=True)
            html = render_template('email/activate.html', confirm_url=confirm_url)
            subject = "Email Confirmation Link"
            send_email(email, subject, html)

            return render_template('error/confirm_account.html', user=current_user)


    return render_template('auth/signup_mentor.html', title='Sign up', user=current_user)



@auth.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        # Check if the provided credentials match a user
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('You have logged in successfully!', 'success')
            login_user(user)
            if user.mentor:
                next_page = request.args.get('next')
                if user.confirmed:
                    return redirect(next_page) if next_page else redirect(url_for('mentor.mentor_dashboard'))
                else:
                    return redirect(next_page) if next_page else redirect(url_for('mentor.update_mentor_profile'))
            else:
                next_page = request.args.get('next')
                if user.confirmed:
                    return redirect(next_page) if next_page else redirect(url_for('user.user_dashboard'))
                else:
                    return redirect(next_page) if next_page else redirect(url_for('user.update_user_profile'))
        else:
            flash('Please check your username and password!', 'danger')

    return render_template('auth/login.html', title='Log In', user=current_user)







@auth.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out of Skillsync', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired', 'success')
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
        return redirect(url_for('auth.login'))
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
        return redirect(url_for('auth.login'))



@auth.route('/resend')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    html = render_template('email/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/forgot-password', methods=['POST', 'GET'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        
        if user:
            # Generate a unique token
            token = generate_confirmation_token(email)

            # Send reset password email
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            template = render_template('email/reset_password.html', reset_url=reset_url)
            send_email(user.email, 'Reset Your Password', template)

            flash('If your email exists in our database, a password reset link will be sent to your email.', 'success')
            return redirect(url_for('auth.forgot_password'))
        else:
            flash('If your email exists in our database, a password reset link will be sent to your email.', 'success')
            return redirect(url_for('auth.forgot_password'))
    else:
        return render_template('auth/forgot_password.html', user=current_user)

    

@auth.route('/reset-password/<token>', methods=['POST', 'GET'])
def reset_password(token):
    if request.method == 'POST':
        # Confirm the validity of the token
        email = confirm_token(token)

        if not email:
            flash('Invalid or expired reset password link', 'danger')
            return redirect(url_for('auth.login'))

        # Find the user by email
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User not found', 'danger')
            return redirect(url_for('auth.login'))

        # Get data from the form
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        # Check if passwords match
        if new_password == confirm_password:
            # Update the user's password
            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            db.session.commit()
            flash('Password reset successfully', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.reset_password', token=token))
    else:
        return render_template('auth/reset_password.html', user=current_user)
