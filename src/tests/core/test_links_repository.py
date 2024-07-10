import uuid

trip_id: str = str(uuid.uuid4)
link_id: str = str(uuid.uuid4)

def test_registry_link(link_session):
    link_data = {
        "id": link_id,
        "link": "www.example.com",
        "title": "Link test",
        "trip_id": trip_id,
    }
    link_session.registry_link(link_data)


def test_find_link_from_trip(link_session):
   link = link_session.find_link_by_id(trip_id)
   
   assert link[0] == link_id
   assert link[1] == trip_id


def test_delete_links(link_session):
    link = link_session.delete_links()

    assert link is None