import uuid

from src.core.repositories.activities_repository import ActivitiesRepository


class ActivityFinder:
    def __init__(
            self,
            activities_repository: ActivitiesRepository,
            ) -> None:
        self.__activities_repository = activities_repository

    def find_from_trip(self, trip_id: str) -> dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)
            formatted_activities = []
            for activity in activities:
                formatted_activities.append({
                    "id": activity[0], 
                    "trip_id": activity[1], 
                    "title": activity[2], 
                    "occurs_at": activity[3]
                    })
                
            return {
                "body": {"activities": formatted_activities,
                "status_code": 201
                }
            }
        except Exception as exc:
            return {
                "body": {
                    "error": "Bad request",
                    "message": str(exc),
                    },
                "status_code": 400
            }
        