import uuid

from src.core.repositories.participants_repository import ParticipantsRepository


class ParticipantConfirmer:
    def __init__(
            self,
            participants_repository: ParticipantsRepository,
            ) -> None:
        self.__participants_repository = participants_repository
    

    def confirm_participant(self, participant_id) -> dict:
            try:
                self.__participants_repository.update_participant_status(participant_id)
                return {
                    "body": None,
                    "status_code": 204
                    }
            except Exception as exc:
                return{
                    "body": {
                        "error": "Bad request",
                        "message": str(exc)
                        },
                    "status_code": 400
                }