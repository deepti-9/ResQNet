from flask import Blueprint, jsonify, request
from models import db, Disaster

api_routes = Blueprint('api_routes', __name__)

# Route to fetch all disasters
@api_routes.route('/disasters', methods=['GET'])
def get_disasters():
    disasters = Disaster.query.all()
    return jsonify([{
        "id": d.id,
        "location": d.location,
        "type": d.type,
        "needs": d.needs.split(','),
        "image_url": d.image_url,
        "urgency": d.urgency,
        "reported_on": d.reported_on.strftime('%Y-%m-%d')
    } for d in disasters])

# Route to report a disaster
@api_routes.route('/disaster', methods=['POST'])
def add_disaster():
    data = request.json
    new_disaster = Disaster(
        location=data["location"],
        type=data["type"],
        needs=','.join(data["needs"]),
        image_url=data["image_url"],
        urgency=data["urgency"]
    )
    db.session.add(new_disaster)
    db.session.commit()
    return jsonify({"message": "Disaster reported successfully"}), 201
