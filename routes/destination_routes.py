from flask import Blueprint, jsonify, request
import requests
import os

destination_bp = Blueprint('destinations', __name__, url_prefix='/destinations')

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', 'YOUR_API_KEY_HERE')

@destination_bp.route('/', methods=['GET'])
def get_destinations():
    destinations = [
        {"name": "Paris", "lat": 48.8566, "lng": 2.3522},
        {"name": "Tokyo", "lat": 35.6895, "lng": 139.6917},
        {"name": "Sydney", "lat": -33.8688, "lng": 151.2093},
        {"name": "Dubai", "lat": 25.2048, "lng": 55.2708},
    ]
    return jsonify(destinations)

@destination_bp.route('/map', methods=['GET'])
def get_map():
    city = request.args.get('city', 'Paris')
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())
