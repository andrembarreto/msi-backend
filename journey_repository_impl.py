from models import Journey
from journey_repository import JourneyRepository

class JourneyRepositoryImpl(JourneyRepository):
    def get_by_id(self, journey_id: int):
        return Journey.get_by_id(journey_id)

    def create(self, bus_line_id: str):
        return Journey.create(bus_line=bus_line_id)
