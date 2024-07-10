import uuid

from src.core.repositories.participants_repository import ParticipantsRepository
from src.core.repositories.emails_invite_repository import EmailsToInviteRepository


class ParticipantCreator:
    def __init__(
            self,
            participants_repository: ParticipantsRepository,
            emails_repository: EmailsToInviteRepository
            ) -> None:
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create_participant(self, body: any, trip_id: str) -> dict:
        try:
            emails_info = {
                "id": str(uuid.uuid4()),
                "email": body["email"],
                "trip_id": trip_id,
            }

            participant_infos = {
                "id": str(uuid.uuid4()),
                "trip_id": trip_id,
                "emails_to_invite_id": emails_info['id'],
                "name": body["name"]
            }

            self.__emails_repository.registry_email(emails_info)
            self.__participants_repository.registry_participant(participant_infos)

            return {
                "body": {"participant_id": participant_infos['id']},
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