from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = Blueprint('auth', __name__)

# Route for user registration
@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data["password"])
    new_user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password,
        location=data["location"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
