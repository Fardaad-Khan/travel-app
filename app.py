from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models.user import db
from routes.auth_routes import auth_bp
from routes.destination_routes import destination_bp
from routes.booking_routes import booking_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(destination_bp)
app.register_blueprint(booking_bp)

@app.route('/')
def home():
    return {"message": "Travel App Backend Running -v6"}

if __name__ == '__main__':
    print("🗄️  Initializing database...")
    with app.app_context():
        db.create_all()
    print("✅ Database ready. Starting server...")
    app.run(host='0.0.0.0', port=5000, debug=True)

