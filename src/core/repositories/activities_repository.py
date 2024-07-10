from sqlite3 import Connection
from src.core.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect_database()

class ActivitiesRepository:
    def __init__(self, connection: Connection) -> None:
       self.__connection = connection


    def registry_activity(self, activity_info: dict):
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT 
            INTO 
                activities
                (id, trip_id, title, occurs_at)
            VALUES
                (?, ?, ?, ?)
            ''', 
            (
                activity_info["id"],
                activity_info["trip_id"],
                activity_info["title"],
                activity_info["occurs_at"],
            )
        )
        self.__connection.commit()
        

    def find_activities_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT 
                * 
            FROM 
                emails_to_invite 
            WHERE 
                trip_id = ?
            ''', 
            (trip_id,)
        )
        return cursor.fetchall()
    

    def delete_email_from_trip(self, trip_id: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            DELETE 
            FROM 
                emails_to_invite
            '''
        )
        self.__connection.commit()