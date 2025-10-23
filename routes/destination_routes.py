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
        {"name": "New York", "lat": 40.7128, "lng": -74.0060},
        {"name": "London", "lat": 51.5074, "lng": -0.1278},
        {"name": "Rome", "lat": 41.9028, "lng": 12.4964},
        {"name": "Barcelona", "lat": 41.3851, "lng": 2.1734},
        {"name": "Rio de Janeiro", "lat": -22.9068, "lng": -43.1729},
        {"name": "Cape Town", "lat": -33.9249, "lng": 18.4241},
        {"name": "Bangkok", "lat": 13.7563, "lng": 100.5018},
        {"name": "Istanbul", "lat": 41.0082, "lng": 28.9784},
        {"name": "Hong Kong", "lat": 22.3964, "lng": 114.1095},
        {"name": "Singapore", "lat": 1.3521, "lng": 103.8198},
        {"name": "Amsterdam", "lat": 52.3676, "lng": 4.9041},
        {"name": "Prague", "lat": 50.0755, "lng": 14.4378},
        {"name": "Vienna", "lat": 48.2082, "lng": 16.3738},
        {"name": "Berlin", "lat": 52.5200, "lng": 13.4050},
        {"name": "Moscow", "lat": 55.7558, "lng": 37.6173},
        {"name": "Cairo", "lat": 30.0444, "lng": 31.2357},
        {"name": "Machu Picchu", "lat": -13.1631, "lng": -72.5450},
        {"name": "Great Wall of China", "lat": 40.4319, "lng": 116.5704},
        {"name": "Taj Mahal", "lat": 27.1751, "lng": 78.0421},
        {"name": "Bora Bora", "lat": -16.5004, "lng": -151.7415},
        {"name": "Grand Canyon", "lat": 36.1069, "lng": -112.1129},
        {"name": "Santorini", "lat": 36.3932, "lng": 25.4615},
        {"name": "Kyoto", "lat": 35.0116, "lng": 135.7681},
        {"name": "Venice", "lat": 45.4408, "lng": 12.3155},
        {"name": "Seoul", "lat": 37.5665, "lng": 126.9780},
        {"name": "Mexico City", "lat": 19.4326, "lng": -99.1332},
    ]
    return jsonify(destinations)

@destination_bp.route('/map', methods=['GET'])
def get_map():
    city = request.args.get('city', 'Paris')
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())