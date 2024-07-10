import uuid

from src.core.repositories.participants_repository import ParticipantsRepository
from src.core.repositories.emails_invite_repository import EmailsToInviteRepository


class ParticipantFinder:
    def __init__(
            self,
            participants_repository: ParticipantsRepository,
            ) -> None:
        self.__participants_repository = participants_repository

    def find_participant(self, trip_id: str) -> dict:
        try:
            participants = self.__participants_repository.find_participants_from_trip(trip_id)

            participants_infos =[]
            for participant in participants:
                participants_infos.append(
                    {
                        "id": participant[0],
                        "name": participant[1],
                        "is_confirmed": participant[2],
                        "email": participant[3]
                    }
                )

            return {
                "body": {"participantsa": participants_infos},
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