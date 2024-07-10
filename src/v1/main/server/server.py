from flask import Flask, jsonify, Blueprint

from src.v1.main.routes.trips_routes import trips_routes_bp
from src.v1.main.routes.links_routes import links_routes_bp


app = Flask(__name__)

root_bp = Blueprint("Root", __name__)

@root_bp.route("/", methods=["GET"])
def get_root():
    return jsonify({"message": "Welcome to TravelTracker v1"}), 200

app.register_blueprint(root_bp)
app.register_blueprint(trips_routes_bp)
app.register_blueprint(links_routes_bp)