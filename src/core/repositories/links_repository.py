from sqlite3 import Connection
from src.core.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect_database()

class LinksRepository:
    def __init__(self, connection: Connection) -> None:
       self.__connection = connection


    def registry_link(self, link_info: dict):
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT INTO links
                (id, trip_id, link, title)
            VALUES
                (?, ?, ?, ?)
            ''',(
                link_info["id"],
                link_info["trip_id"],
                link_info["link"],
                link_info["title"],
            )
        )
        self.__connection.commit()
        
    def get_link_by_trip_id(self, trip_id: str) -> tuple:
        cursor = self.__connection.cursor()
        cursor.execute(
            ''' SELECT * FROM links WHERE trip_id = ? ''', (trip_id,)
        )
        return cursor.fetchall()
    
    def delete_links(self) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''DELETE FROM links'''
        )
        self.__connection.commit()