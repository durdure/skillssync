from functools import wraps

from flask import jsonify, render_template
from flask_login import current_user


def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if not current_user.confirmed:
                return render_template('error/confirm_account.html', user=current_user)
        else:
            # Handle the case where the user is not authenticated
            return jsonify({'error': 'User not authenticated'}), 401

        return func(*args, **kwargs)

    return decorated_function


def mentor_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({'error': 'Unauthorized'}), 401
        if not current_user.mentor:
            return jsonify({'error': 'Access denied. User is not a mentor.'}), 403
        return func(*args, **kwargs)
    return decorated_function


def mentor_restricted(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        # Check if the current user is a mentor
        if current_user.is_authenticated and current_user.mentor:
            return jsonify({'error': 'Mentors are not allowed to access this route.'}), 403
        return route_function(*args, **kwargs)
    return decorated_function
