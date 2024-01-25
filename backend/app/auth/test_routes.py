import json
from flask import url_for
from .models import User

def test_register(client, db):
    # Create a test user
    test_user = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password',
        'confirm_pass': 'password'
    }

    # Send a POST request to the register route
    response = client.post(url_for('auth.register'), json=test_user)

    # Check the response status code
    assert response.status_code == 201

    # Check the response data
    data = json.loads(response.data)
    assert 'data' in data
    assert 'message' in data
    assert 'id' in data['data']
    assert 'username' in data['data']
    assert 'email' in data['data']
    assert 'image_file' in data['data']
    assert data['message'] == 'User registered successfully'

    # Check if the user is added to the database
    user = User.query.filter_by(email=test_user['email']).first()
    assert user is not None
    assert user.username == test_user['username']
    assert user.email == test_user['email']
    assert user.check_password(test_user['password'])  # Assuming you have a check_password method in your User model