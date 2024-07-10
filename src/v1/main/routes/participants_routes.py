from flask import jsonify, Blueprint, request

# Importação de gerenciadores de conexões
from src.core.models.settings.db_connection_handler import db_connection_handler

# Importação de controllers
from src.v1.controllers.participant_controllers.participant_creator import ParticipantCreator
from src.v1.controllers.participant_controllers.participant_finder import ParticipantFinder
from src.v1.controllers.participant_controllers.participant_confirmer import ParticipantConfirmer

# Importação de repositórios
from src.core.repositories.participants_repository import ParticipantsRepository
from src.core.repositories.emails_invite_repository import EmailsToInviteRepository


participants_routes_bp = Blueprint(
    "participants_routes", 
    __name__, 
    url_prefix="/participants"
    )


@participants_routes_bp.route("/", methods=["GET"])
def root_trip():
    return jsonify({"message": "Trip Participants API page"}), 200


@participants_routes_bp.route("/<trip_id>/invites", methods=["POST"])
def invite_trip_participants(trip_id: str):
    connection = db_connection_handler.get_connection()
    
    controller = ParticipantCreator(
        ParticipantsRepository(connection),
        EmailsToInviteRepository(connection)
    )
    response = controller.create_participant(
        body=request.json, 
        trip_id=trip_id
        )

    return jsonify(response["body"]), response["status_code"]

    
@participants_routes_bp.route("/<trip_id>", methods=["GET"])
def get_participants(trip_id: str):
    controller = ParticipantFinder(
        ParticipantsRepository(
            db_connection_handler.get_connection()
        )
    )

    response = controller.find_participant(trip_id)

    return jsonify(response["body"]), response["status_code"]

@participants_routes_bp.route("/<participant_id>/confirm", methods=["PUT"])
def confirm_participant(participant_id: str):
    controller = ParticipantConfirmer(
        ParticipantsRepository(
            db_connection_handler.get_connection()
        )
    )

    response = controller.confirm_participant(participant_id)

    return jsonify(response["body"]), response["status_code"]