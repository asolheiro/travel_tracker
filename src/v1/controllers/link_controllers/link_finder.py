from src.core.repositories.links_repository import LinksRepository
class LinkFinder:
    def __init__(self, link_repository: LinksRepository) -> None:
        self.__link_repository = link_repository

    def find_link_by_trip_id(self, trip_id: str) -> list:
        try:
            links = self.__link_repository.get_link_by_trip_id(trip_id)
            if links:    
                formatted_links = []
                for link in links:
                    formatted_links.append({
                        "id": link[0],
                        "url": link[2],
                        "title": link[3],
                        }
                    )

                return {
                    "body": {
                        "links": formatted_links
                        },
                    "status_code": 200
                }

        except Exception as exc:
            return {
                "body": {
                    "error": "Bad request",
                    "message": str(exc)
                    },
                "status_code": 400
            }