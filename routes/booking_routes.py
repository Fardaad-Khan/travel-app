from flask import Blueprint, jsonify, request

booking_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

bookings = []  # In-memory list for demo (replace with DB later)

@booking_bp.route('/', methods=['POST'])
def create_booking():
    data = request.get_json()
    bookings.append(data)
    return jsonify({'message': 'Booking confirmed', 'booking': data}), 201

@booking_bp.route('/', methods=['GET'])
def get_bookings():
    return jsonify(bookings)
