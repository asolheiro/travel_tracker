from sqlite3 import Connection
from typing import Dict


class TripsRepository:
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def create_trip(self, trips_info: Dict)  -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
                INSERT INTO trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''', (
                trips_info["id"],
                trips_info["destination"],
                trips_info["start_date"],
                trips_info["end_date"],
                trips_info["owner_name"],
                trips_info["owner_email"],
                )
        )
        self.__connection.commit()

    def find_trip_by_id(self, trip_id: str):
        cursor = self.__connection.cursor()
        cursor.execute(
            '''SELECT * FROM trips WHERE id = ?''', (trip_id,)
        )
        return cursor.fetchone()
    
    def update_trips_status(self, trip_id: str):
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            UPDATE trips
                SET status = 1
            WHERE
                id = ?
            ''', (trip_id,)
        )
        self.__connection.commit()
        
        