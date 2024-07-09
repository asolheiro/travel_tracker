import pytest
from src.core.models.settings.db_connection_handler import db_connection_handler
from src.core.repositories.trips_repository import TripsRepository

@pytest.fixture()
def session():
    db_connection_handler.connect_database()
    
    session = TripsRepository(
        connection = db_connection_handler.get_connection()
    )
    yield session
