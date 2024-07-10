import uuid
from typing import Dict

from src.core.repositories.trips_repository import TripsRepository
from src.core.repositories.emails_invite_repository import EmailsToInviteRepository


class TripCreator:
    def __init__(self, trips_repository: TripsRepository, emails_repository: EmailsToInviteRepository) -> None:
        self.__trips_repository = trips_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:
            trip_infos = { 
                "id": str(uuid.uuid4()),
                **body
                }
            self.__trips_repository.create_trip(trip_infos)
            
            emails = body.get("emails_to_invite")
            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "id": str(uuid.uuid4()),
                        "email": email,
                        "trip_id": trip_infos['id'],
                    })
                
            return {
                "body": {
                    "id": trip_infos['id'],
                },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad request",
                    "message": str(exception)
                    },
                "status_code": 400
            }