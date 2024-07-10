from flask import jsonify, Blueprint, request
# Importação de gerenciadores de conexões
from src.core.models.settings.db_connection_handler import db_connection_handler
# Importação de controllers
from src.v1.controllers.activity_controllers.activity_creator import ActivityCreator
from src.v1.controllers.activity_controllers.activity_finder import ActivityFinder
# Importação de repositórios
from src.core.repositories.activities_repository import ActivitiesRepository


activities_routes_bp = Blueprint(
    "activities_routes", 
    __name__, 
    url_prefix="/activities"
    )


@activities_routes_bp.route("/", methods=["GET"])
def root_trip():
    return jsonify({"message": "Trip Activities API page"}), 200


@activities_routes_bp.route("/<trip_id>", methods=["POST"])
def create_activity(trip_id: str):
    controller = ActivityCreator(
        ActivitiesRepository(
            db_connection_handler.get_connection()
        )
    )
    response = controller.create_activity(
        body=request.json, 
        trip_id=trip_id
        )

    return jsonify(response["body"]), response["status_code"]


@activities_routes_bp.route("/<trip_id>", methods=["GET"])
def find_activity(trip_id: str):
    controller = ActivityFinder(
        ActivitiesRepository(
            db_connection_handler.get_connection()
        )
    )
    response = controller.find_from_trip(trip_id)

    return jsonify(response["body"]), response["status_code"]
