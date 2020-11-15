from flask import render_template
from flask_login import login_user
from mainapp import app, login
from mainapp.services.auth import loginValidate, registerValidate
from os import environ
login.login_view = "login"


@login.user_loader
def userLoad(userId):
    return User.query.get(userId)


@app.route("/")
def index():
    return render_template('store/index.html')


@app.errorhandler(404)
def notFound(e):
    return render_template('store/404.html'), 404


@app.route('/register', methods=['post', 'get'])
def register():
    if request.method == 'GET':
        return render_template('store/register.html')
    if request.method == 'POST':
        user, result = registerValidate(request)
        if not user:
            return render_template('store/register.html', error=result)
        db.session.add(user)
        db.session.commit()
        return render_template('store/register.html', result=result)


@app.route('/login', methods=['post', 'get'])
def login():
    if request.method == 'GET':
        return render_template('store/login.html')
    if request.method == 'POST':
        user, error = loginValidate(request)
        if not user:
            return render_template('store/login.html', error=error)
        login_user(user=user)
        return redirect('/')


@app.route('/login-admin', methods=['post', 'get'])
def login_admin():
    if request.method == 'POST':
        user = loginValidate(request)
        if user:
            login_user(user=user)
    return redirect('/admin')


if __name__ == "__main__":
    from mainapp.admin_module import *
    app.run(debug=True, port=int(environ.get("PORT")))
