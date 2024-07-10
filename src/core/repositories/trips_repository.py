from sqlite3 import Connection
from src.core.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect_database()

class TripsRepository:
    def __init__(self, connection: Connection) -> None:
       self.__connection = connection


    def create_trip(self, trips_info: dict):
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT 
            INTO 
                trips
                (id, destination, start_date, end_date, owner_name, owner_email, status)
            VALUES
                (?, ?, ?, ?, ?, ?, ?)
            ''',(
                trips_info["id"],
                trips_info["destination"],
                trips_info["start_date"],
                trips_info["end_date"],
                trips_info["owner_name"],
                trips_info["owner_email"],
                0
            )
        )
        self.__connection.commit()
        

    def find_trip_by_id(self, trip_id: str) -> tuple:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT 
                *
            FROM
                trips
            WHERE
                id = ?
            ''', 
            (trip_id,)
        )
        return cursor.fetchone()
    

    def update_trip_status(self, trip_id: str) -> tuple:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            UPDATE
                trips
            SET 
                status = 1
            WHERE
                id = ?
            ''', 
            (trip_id,)
        )
        self.__connection.commit()
        return self.find_trip_by_id(trip_id)


    def delete_trips(self) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            DELETE 
            FROM 
                trips
            '''
        )
        self.__connection.commit()
        