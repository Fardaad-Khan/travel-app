from models.user import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    days = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(120), nullable=False)

    # New fields
    travel_date = db.Column(db.Date, nullable=True)
    travelers = db.Column(db.Integer, default=1)
    special_requests = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "destination": self.destination,
            "days": self.days,
            "customer_name": self.customer_name,
            "travel_date": self.travel_date.isoformat() if self.travel_date else None,
            "travelers": self.travelers,
            "special_requests": self.special_requests,
            "created_at": self.created_at.isoformat()
        }
