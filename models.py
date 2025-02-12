from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    location = db.Column(db.String(200))

# Define Disaster Model
class Disaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    type = db.Column(db.String(50))
    needs = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    urgency = db.Column(db.String(20))
    reported_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
