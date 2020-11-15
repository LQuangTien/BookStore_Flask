from flask import Flask
from os import environ, urandom
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


# settings.py
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ str(environ.get('DATABASE_USERNAME')) +':'+ str(environ.get('DATABASE_PASSWORD')) + '@localhost/bookstore?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
admin = Admin(app=app, name='BAN SACH',
              template_mode='bootstrap3')
login = LoginManager(app=app)