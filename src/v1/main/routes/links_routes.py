from flask import jsonify, Blueprint, request

# Importação de gerenciadores de conexões
from src.core.models.settings.db_connection_handler import db_connection_handler

# Importação de controllers
from src.v1.controllers.link_controllers.link_creator import LinkCreator
from src.v1.controllers.link_controllers.link_finder import LinkFinder

# Importação de repositórios
from src.core.repositories.links_repository import LinksRepository


links_routes_bp = Blueprint(
    "link_routes", 
    __name__, 
    url_prefix="/links"
    )


@links_routes_bp.route("/", methods=["GET"])
def root_trip():
    return jsonify({"message": "Trip Links API page"}), 200


@links_routes_bp.route("/<trip_id>", methods=["POST"])
def create_link(trip_id: str):
    controller = LinkCreator(
        LinksRepository(
            db_connection_handler.get_connection()
        )
    )
    response = controller.create(trip_id, request.json)

    return jsonify(response["body"]), response["status_code"]


@links_routes_bp.route("/<trip_id>", methods=["GET"])
def find_links(trip_id: str):
    controller = LinkFinder(
        LinksRepository(
            db_connection_handler.get_connection()
        )
    )
    response = controller.find_link_by_trip_id(trip_id)

    return jsonify(response["body"]), response["status_code"]
    