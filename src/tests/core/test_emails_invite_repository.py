import pytest
import uuid

from src.core.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect_database()

trip_id:str  = str(uuid.uuid4())

def test_registry_email(email_session):
    email_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "rmndvngrpslhr@teste.com"
    }

    email_session.registry_email(email_infos)
    
def test_get_emails_by_trip(email_session):
    
    trip = email_session.find_email_from_trip(trip_id)
    assert trip[0][1] == trip_id

def test_delete_emails_from_trips(email_session):
    email_session = email_session.delete_email_from_trip(trip_id)
    assert email_session is None