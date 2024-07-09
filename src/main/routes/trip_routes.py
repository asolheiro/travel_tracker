from flask import jsonify, Blueprint


trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/", methods=["GET"])
def root_trip():
    return jsonify({"message": "Welcome to TravelTracker v1"}), 200


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"message": "Welcome to TravelTracker v1"}), 200