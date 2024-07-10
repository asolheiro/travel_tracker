from typing import Dict

from src.core.repositories.trips_repository import TripsRepository


class TripFinder:
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository

    def get_trip_details(self, trip_id: str) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("Trip not found")            
            
            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "start_date": trip[2],
                        "end_date": trip[3],
                        "owner_name": trip[4],
                        "owner_email": trip[5],
                        "status": trip[6]
                    }
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": {
                    "error": "Bad request",
                    "message": str(exception)
                    },
                "status_code": 400
            }