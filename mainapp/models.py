from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import Enum
from mainapp import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    address = Column(String(100), nullable=True)
    sex = Column(Enum('Male', 'Female', 'Other'))
    isActive = Column(Boolean, default=True)
    isAdmin = Column(Boolean, default=False)
    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()
