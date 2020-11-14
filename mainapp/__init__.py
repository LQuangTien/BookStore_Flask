from flask import Flask
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


# settings.py
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ str(os.environ.get('DATABASE_USERNAME')) +':'+ str(os.environ.get('DATABASE_PASSWORD')) + '@localhost/bookstore?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
admin = Admin(app=app, name='BAN SACH',
              template_mode='bootstrap3')
login = LoginManager(app=app)