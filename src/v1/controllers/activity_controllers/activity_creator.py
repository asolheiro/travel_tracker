import uuid

from src.core.repositories.activities_repository import ActivitiesRepository


class ActivityCreator:
    def __init__(
            self,
            activities_repository: ActivitiesRepository,
            ) -> None:
        self.__activities_repository = activities_repository

    def create_activity(self, body: any, trip_id: str) -> dict:
        try:
            activities_infos = {
                "id": str(uuid.uuid4()),
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"]
            }
            self.__activities_repository.registry_activity(activities_infos)
            
            return {
                "body": {"activity_id": activities_infos['id']},
                "status_code": 201
            }
        except Exception as exc:
            return {
                "body": {
                    "error": "Bad request",
                    "message": str(exc),
                    },
                "status_code": 400
            }