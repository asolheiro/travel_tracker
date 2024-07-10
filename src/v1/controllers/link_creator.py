import uuid
from src.core.repositories.links_repository import LinksRepository


class LinkCreator:
    def __init__(self, link_repository: LinksRepository) -> None:
        self.__link_repository = link_repository

    def create(self, trip_id: str, body: any,) -> dict:
        try:
            link_info = {
                "id": str(uuid.uuid4()),
                "trip_id": trip_id,
                **body,
            }
            self.__link_repository.registry_link(link_info)
            return {
                "body": {
                    "id": link_info['id'],
                },
                "status_code": 201
            }
        
        except Exception as exc:
            return {
                "body": {
                    "error": "Bad request",
                    "message": str(exc)
                },
                "status_code": 400
            }