import pytest
from src.core.models.settings.db_connection_handler import db_connection_handler
from src.core.repositories import trips_repository, emails_invite_repository


@pytest.fixture()
def trip_session():
    db_connection_handler.connect_database()
    
    session = trips_repository.TripsRepository(
        connection = db_connection_handler.get_connection()
    )
    yield session


@pytest.fixture()
def email_session():
    db_connection_handler.connect_database()
    
    session = emails_invite_repository.EmailsToInviteRepository(
        connection = db_connection_handler.get_connection()
    )
    
    yield session
