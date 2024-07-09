import pytest
import uuid
from datetime import datetime, timedelta

from src.core.repositories.trips_repository import TripsRepository
from src.core.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect_database()

trip_id:str  = str(uuid.uuid4())

@pytest.mark.skip(reason="Teste de interação com o banco")
def test_create_trip(session):
        
    trips_infos = {
        "id": trip_id,
        "destination": "Belém",
        "start_date": datetime.strptime("12-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("12-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Armando Solheiro",
        "owner_email": "rmndvngrpslhr@test.com"
    }

    session.create_trip(trips_info=trips_infos)
    
@pytest.mark.skip(reason="Teste de interação com o banco")
def test_get_trip_by(session):
    
    trip = session.find_trip_by_id(trip_id)
    assert trip[0] == trip_id

@pytest.mark.skip(reason="Teste de interação com o banco")
def test_update_trip_status(session):
    
    trip = session.update_trip_status(trip_id)
    assert trip[6] == 1

