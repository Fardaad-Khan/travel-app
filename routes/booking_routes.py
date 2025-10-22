from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import db, Booking
from datetime import datetime

booking_bp = Blueprint('bookings', __name__, url_prefix='/bookings')


# 🟢 Create a new booking
@booking_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    try:
        data = request.get_json()
        print("📦 Received booking data:", data)

        # Get user from JWT
        user_id = get_jwt_identity()
        print("👤 Current user ID:", user_id)

        # Required fields
        destination = data.get("destination")
        days = data.get("days")
        customer_name = data.get("customer_name")

        if not destination or not days or not customer_name:
            print("🚫 Missing one or more required fields")
            return jsonify({"error": "Missing required fields"}), 400

        # Optional fields
        travel_date_str = data.get("travel_date")
        travel_date = datetime.strptime(travel_date_str, "%Y-%m-%d").date() if travel_date_str else None
        travelers = int(data.get("travelers", 1))
        special_requests = data.get("special_requests", "")

        # Create booking
        new_booking = Booking(
            user_id=user_id,
            destination=destination,
            days=int(days),
            customer_name=customer_name,
            travel_date=travel_date,
            travelers=travelers,
            special_requests=special_requests
        )

        db.session.add(new_booking)
        db.session.commit()

        print(f"✅ Booking saved for {customer_name} → {destination}")
        return jsonify({"message": "Booking saved successfully"}), 201

    except Exception as e:
        import traceback
        print("🔥 Full error traceback:\n", traceback.format_exc())
        return jsonify({"error": str(e)}), 500


# 🟡 Get all bookings for the logged-in user
@booking_bp.route('/', methods=['GET'])
@jwt_required()
def get_bookings():
    try:
        user_id = get_jwt_identity()
        print("📋 Fetching bookings for user ID:", user_id)

        bookings = Booking.query.filter_by(user_id=user_id).all()
        booking_list = [b.to_dict() for b in bookings]

        print(f"✅ {len(booking_list)} bookings found.")
        return jsonify(booking_list), 200

    except Exception as e:
        import traceback
        print("🔥 Error fetching bookings:\n", traceback.format_exc())
        return jsonify({"error": str(e)}), 500
