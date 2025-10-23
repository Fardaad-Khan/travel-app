# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import time

# NEW: Import Prometheus (safe – if not installed, it skips)
try:
    from prometheus_flask_exporter import PrometheusMetrics
    METRICS_ENABLED = True
except ImportError:
    METRICS_ENABLED = False
    print("⚠️ Prometheus not available – install with pip install prometheus-flask-exporter")

from models.user import db
from routes.auth_routes import auth_bp
from routes.destination_routes import destination_bp
from routes.booking_routes import booking_bp
from config import Config

# ------------------------------------------------------------------
# 1. Flask app + config
# ------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# Add start time for uptime
app.start_time = time.time()

# ------------------------------------------------------------------
# 2. CORS – exactly the same as you had
# ------------------------------------------------------------------
CORS(
    app,
    resources={r"/*": {"origins": [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://travel-app-frontend.onrender.com",
        "https://travel-app-frontend-ten3.onrender.com"
    ]}},
    supports_credentials=True
)

# ------------------------------------------------------------------
# 3. Extensions
# ------------------------------------------------------------------
db.init_app(app)
jwt = JWTManager(app)

# NEW: Initialize metrics EARLY (before blueprints)
if METRICS_ENABLED:
    metrics = PrometheusMetrics(app, path='/metrics')
    metrics.info('app_info', 'Travel App Backend', version='v6')

# Enhanced health with optional psutil
try:
    import psutil
    @app.route('/health')
    def health():
        return jsonify({
            "status": "healthy",
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "uptime_seconds": int(time.time() - app.start_time)
        }), 200
except ImportError:
    @app.route('/health')
    def health():
        return jsonify({
            "status": "healthy",
            "uptime_seconds": int(time.time() - app.start_time)
        }), 200

# ------------------------------------------------------------------
# 4. Register Blueprints (unchanged)
# ------------------------------------------------------------------
app.register_blueprint(auth_bp)
app.register_blueprint(destination_bp)
app.register_blueprint(booking_bp)

# ------------------------------------------------------------------
# 5. Routes
# ------------------------------------------------------------------
@app.route('/')
def home():
    return {"message": "Travel App Backend Running -v6"}

# ------------------------------------------------------------------
# 6. Run only when executed directly (dev only)
# ------------------------------------------------------------------
if __name__ == '__main__':
    print("Initializing database...")
    with app.app_context():
        # Import models so they are registered before create_all()
        from models.booking import Booking
        db.create_all()
    print("Database ready. Starting server...")
    # Debug=True is fine locally, Render ignores this block
    app.run(host='0.0.0.0', port=5000, debug=True)