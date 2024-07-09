import sqlite3
from sqlite3 import Connection


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "database.db"
        self.__connection = None

    def connect_database(self) -> None:
        connection = sqlite3.connect(
            self.__connection_string, 
            check_same_thread=False
            )
        self.__connection = connection

    def get_connection(self) -> Connection:
        return self.__connection
    
    def rollback(self):
        return self.__connection.rollback()
    

db_connection_handler = DbConnectionHandler()
