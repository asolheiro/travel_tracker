from flask import jsonify, Blueprint, request

# Importação de gerenciadores de conexões
from src.core.models.settings.db_connection_handler import db_connection_handler

# Importação de controllers
from src.v1.controllers.trip_controllers.trip_creator import TripCreator
from src.v1.controllers.trip_controllers.trip_finder import TripFinder
from src.v1.controllers.trip_controllers.trip_confirmer import TripConfirmer


# Importação de repositórios
from src.core.repositories.trips_repository import TripsRepository
from src.core.repositories.emails_invite_repository import EmailsToInviteRepository


trips_routes_bp = Blueprint(
    "trip_routes", 
    __name__, 
    url_prefix="/trips"
    )

@trips_routes_bp.route("/", methods=["GET"])
def root_trip():
    return jsonify({"message": "Trips API page"}), 200


@trips_routes_bp.route("/", methods=["POST"])
def create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)
    emails_repository = EmailsToInviteRepository(connection)

    controller = TripCreator(
        trips_repository, 
        emails_repository,
    )

    response = controller.create(request.json)
        
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/<trip_id>", methods=["GET"])
def find_trip(trip_id: str):
    controller = TripFinder(
        TripsRepository(
            db_connection_handler.get_connection()
            )
    )

    response = controller.get_trip_details(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/<trip_id>/confirm/", methods=["PUT"])
def confirm_trip(trip_id: str):
    controller = TripConfirmer(
        TripsRepository(
            db_connection_handler.get_connection()
            )
        )
    
    response = controller.confirm(trip_id)
    return jsonify(response["body"]), response["status_code"]

