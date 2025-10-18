from models.user import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    days = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "destination": self.destination,
            "days": self.days,
            "customer_name": self.customer_name
        }
