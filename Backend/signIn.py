from flask import Blueprint, request, render_template, redirect, url_for
from main import valid_login, log_the_user_in

signin_blueprint = Blueprint('signin_blueprint', __name__)

@signin_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('signIn.html', error=error)