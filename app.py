from flask import Flask, send_from_directory
import os
from flask_cors import CORS
from models import db
from routes import api_routes
from auth import auth_routes

# Initialize the Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing
CORS(app)

# Load configurations
app.config.from_pyfile('config.py')


# Initialize the database
db.init_app(app)

# Register Blueprints
app.register_blueprint(api_routes,url_prefix ="/api")
app.register_blueprint(auth_routes,url_prefix ="/auth")


# Root route to handle / request
@app.route('/')
def home():
    print("Home route accessed")  # Check if this gets printed in the terminal
    return "Welcome to ResQNet!"  # This should return the message when you visit the root URL

# Route for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/test')
def test_route():
    return "This is a test route!"


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
