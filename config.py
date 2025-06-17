import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'you_own_random_value'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'orders.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
