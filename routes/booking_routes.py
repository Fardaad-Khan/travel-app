from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import db, Booking

booking_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@booking_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    try:
        data = request.get_json()
        user_id = get_jwt_identity()

        destination = data.get("destination")
        days = data.get("days")
        customer_name = data.get("customer_name")

        if not destination or not days or not customer_name:
            return jsonify({"error": "Missing required fields"}), 400

        booking = Booking(
            user_id=user_id,
            destination=destination,
            days=int(days),
            customer_name=customer_name
        )
        db.session.add(booking)
        db.session.commit()

        return jsonify({"message": "Booking saved successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@booking_bp.route('/', methods=['GET'])
@jwt_required()
def get_bookings():
    try:
        user_id = get_jwt_identity()
        bookings = Booking.query.filter_by(user_id=user_id).all()
        return jsonify([b.to_dict() for b in bookings]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
