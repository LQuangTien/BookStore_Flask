from flask import render_template
from flask_login import login_user
from mainapp import app, login
from mainapp.services.auth import authValidate

login.login_view = "login"


@login.user_loader
def userLoad(userId):
    return User.query.get(userId)


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def notFound(e):
    return render_template('404.html'), 404


@app.route('/login', methods=['post', 'get'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = authValidate(request)
        if user:
            login_user(user=user)
            return redirect('/')
        else:
            return redirect('/login')


@app.route('/login-admin', methods=['post', 'get'])
def login_admin():
    if request.method == 'POST':
        user = authValidate(request)
        if user:
            login_user(user=user)
    return redirect('/admin')


if __name__ == "__main__":
    from mainapp.admin_module import *

    app.run(debug=True, port=8900)
