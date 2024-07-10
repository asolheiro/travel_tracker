from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def registry_participant(self, participant_infos: dict) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT 
            INTO 
                participants
                (id, trip_id, email, emails_to_invite_id, name)
            VALUES
                (? , ?, ?, ?, ?)
            ''', (
                participant_infos['id'],
                participant_infos['trip_id'],
                participant_infos['email'],
                participant_infos['emails_to_invite_id'],
                participant_infos['name'],
            )
        )
        self.__connection.commit()

    def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT
                p.id,
                p.name,
                p.is.confirmed,
                e.email                 
            from
                participants as p             
            JOIN
                emails_to_invite_ as e              
                    ON e.id = p.emails_to_invite_id             
            WHERE
                p.trip_id = ?
            ''', (trip_id, )
        )
        return cursor.fetchall()
    
    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            UPDATE
                participants
            SET
                is_confirmed = 1
            WHERE
                id = ?
            ''', (participant_id,)
        )
        self.__connection.commit()