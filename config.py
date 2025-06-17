import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '247804eb1bdc277b1679bc079f4f3c5f8e5378744eb0ad6d2d07aa19609eca72'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'orders.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
