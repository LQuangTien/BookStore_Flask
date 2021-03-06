from flask import url_for, request
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from werkzeug.utils import redirect

from mainapp import admin, db
from mainapp.models import User
from flask_admin.contrib.sqla import ModelView


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_admin', next=request.url))


class CustomAuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_admin', next=request.url))


class aboutUsView(CustomAuthenticatedView):
    @expose('/')
    def index(self):
        return self.render('admin/aboutus.html')


class logoutView(CustomAuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return self.render('admin/index.html')


class userView(AuthenticatedView):
    column_exclude_list = ['password', ]


admin.add_view(userView(User, db.session))
admin.add_view(aboutUsView(name='About us'))
admin.add_view(logoutView(name='Logout'))
