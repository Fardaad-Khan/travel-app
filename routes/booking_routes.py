from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import db, Booking

booking_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@booking_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    """Create a new booking for the logged-in user."""
    try:
        data = request.get_json()
        print("📦 Received booking data:", data)

        user_id = get_jwt_identity()
        print("👤 Current user ID:", user_id)

        destination = data.get("destination")
        days = data.get("days")
        customer_name = data.get("customer_name")

        # Safety check
        if not destination or not days or not customer_name:
            print("❌ Missing one or more fields!")
            return jsonify({"error": "Missing required fields"}), 400

        new_booking = Booking(
            user_id=user_id,
            destination=destination,
            days=int(days),
            customer_name=customer_name
        )
        db.session.add(new_booking)
        db.session.commit()

        print("✅ Booking saved successfully!")
        return jsonify({"message": "Booking saved successfully"}), 201

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


@booking_bp.route('/', methods=['GET'])
@jwt_required()
def get_bookings():
    """Get all bookings for the logged-in user."""
    try:
        user_id = get_jwt_identity()
        bookings = Booking.query.filter_by(user_id=user_id).all()
        return jsonify([b.to_dict() for b in bookings]), 200
    except Exception as e:
        print("🔥 ERROR fetching bookings:", str(e))
        return jsonify({"error": str(e)}), 500
