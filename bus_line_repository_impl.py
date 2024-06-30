from models import BusLine
from bus_line_repository import BusLineRepository


class BusLineRepositoryImpl(BusLineRepository):
    def create_if_not_exists(self, bus_line_id: str):
        BusLine.get_or_create(id=bus_line_id)
