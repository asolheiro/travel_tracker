from sqlite3 import Connection
from src.core.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect_database()

class EmailsToInviteRepository:
    def __init__(self, connection: Connection) -> None:
       self.__connection = connection


    def registry_email(self, email_info: dict):
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT INTO emails_to_invite
                (id, trip_id, email)
            VALUES
                (?, ?, ?)
            ''', (
                email_info["id"],
                email_info["trip_id"],
                email_info["email"],
            )
        )
        self.__connection.commit()
        
    def find_email_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__connection.cursor()
        cursor.execute(
            ''' SELECT * FROM emails_to_invite WHERE trip_id = ? ''', (trip_id,)
        )
        return cursor.fetchall()
    
    def delete_email_from_trip(self, trip_id: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''DELETE FROM emails_to_invite'''
        )
        self.__connection.commit()