from flask import Blueprint, jsonify, request, render_template

test = Blueprint('test', __name__)

@test.route('/')
def index():
    return render_template('index.html')


@test.route('/about')
def about():
    return render_template('about.html')


# @test.route('/account')
# def account():
#     return render_template('mentor/account.html')

