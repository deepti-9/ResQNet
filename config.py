import os

# Configuration for Flask application
SQLALCHEMY_DATABASE_URI = 'sqlite:///resqnet.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)  # Secret key for sessions, cookies, etc.
