@booking_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    try:
        data = request.get_json()
        print("📦 Received booking:", data)   # 👈 shows payload in Render logs
        user_id = get_jwt_identity()
        print("👤 User ID:", user_id)

        destination = data.get("destination")
        days = data.get("days")
        customer_name = data.get("customer_name")

        if not destination or not days or not customer_name:
            print("🚫 Missing field(s)")
            return jsonify({"error": "Missing required fields"}), 400

        new_booking = Booking(
            user_id=user_id,
            destination=destination,
            days=int(days),
            customer_name=customer_name
        )
        db.session.add(new_booking)
        db.session.commit()

        print("✅ Booking saved:", new_booking.destination)
        return jsonify({"message": "Booking saved successfully"}), 201

    except Exception as e:
        import traceback
        print("🔥 Full error:\n", traceback.format_exc())   # 👈 full stack trace
        return jsonify({"error": str(e)}), 500
