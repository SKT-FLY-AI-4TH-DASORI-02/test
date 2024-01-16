from flask import Blueprint, request, render_template, redirect, url_for, flash
from main import users, hash_password

signup_blueprint = Blueprint('signup_blueprint', __name__)

@signup_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            flash('Passwords do not match. Try again.')
            return redirect(url_for('signup_blueprint.signup'))

        if username in users:
            flash('Username already exists.')
            return redirect(url_for('signup_blueprint.signup'))

        users[username] = hash_password(password)
        flash('Account created successfully. Please login.')
        return redirect(url_for('signin_blueprint.login'))

    return render_template('signUp.html')