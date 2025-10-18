from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import db, Booking

booking_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@booking_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    """Create a new booking for the logged-in user"""
    data = request.get_json()
    user_id = get_jwt_identity()

    if not all(k in data for k in ("destination", "days", "customer_name")):
        return jsonify({"error": "Missing required fields"}), 400

    booking = Booking(
        user_id=user_id,
        destination=data["destination"],
        days=data["days"],
        customer_name=data["customer_name"]
    )
    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Booking saved successfully"}), 201


@booking_bp.route('/', methods=['GET'])
@jwt_required()
def get_bookings():
    """Get all bookings for the logged-in user"""
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([b.to_dict() for b in bookings]), 200
