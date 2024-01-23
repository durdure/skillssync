from .models import User
from flask import request, Blueprint, jsonify
from app import db, bcrypt
from flask_login import current_user, login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'], strict_slashes=False)
def register():

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

    response_data = {
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'image_file': new_user.image_file
    }

    return jsonify({'data': response_data, 'message':'User registered successfully'}), 201



@auth.route('/login', methods=['POST'], strict_slashes=False)
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'You have successfully logged in', 'user_id': user.id}), 200
    else:
        return jsonify({'error': 'Please check your credentials!! Try again.'}), 401



@auth.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logout successful'}), 200
    else:
        return jsonify({'error': 'User has not logged in'}), 401
