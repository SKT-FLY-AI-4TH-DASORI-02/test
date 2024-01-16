from flask import Flask, request, render_template, redirect, url_for, flash
import hashlib

app = Flask(__name__)
# app.secret_key = 'super_secret_key'

# 사용자 정보 DB (임시 딕셔너리)
users = {
    'admin1': hashlib.sha256('asdfghjhgfd'.encode()).hexdigest(),
    'admin2': hashlib.sha256('erthrgeggrf'.encode()).hexdigest(),
    'admin3': hashlib.sha256('vhbijdjbdkm'.encode()).hexdigest(),
    'admin4': hashlib.sha256('lp,lfpvfebb'.encode()).hexdigest(),
    'admin5': hashlib.sha256('koinjiuhhuv'.encode()).hexdigest(),
}

# 비밀번호 해시 함수
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 로그인 검증 함수
def valid_login(username, password):
    hashed_password = hash_password(password)
    return users.get(username) == hashed_password

# 사용자 로그인 함수
def log_the_user_in(username):
    return redirect(url_for('welcome', username=username))

@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome, {username}!'

# 블루프린트 등록
from signIn import signin_blueprint
from signUp import signup_blueprint

app.register_blueprint(signin_blueprint)
app.register_blueprint(signup_blueprint)

# 환영 페이지 뷰
@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
