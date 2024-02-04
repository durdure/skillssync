from functools import wraps

from flask import jsonify
from flask_login import current_user


def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if not current_user.confirmed:
                return jsonify({'message': 'Please confirm your account to continue!'}), 400
        else:
            # Handle the case where the user is not authenticated
            return jsonify({'error': 'User not authenticated'}), 401

        return func(*args, **kwargs)

    return decorated_function
