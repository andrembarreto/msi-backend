from typing import Any
from datetime import datetime

from db_connection import DBConnection


class MobilityDBController:
    def __init__(self, db_connection: DBConnection) -> None:
        self.__db_connection = db_connection
        self.__db_connection.connect()

    def register_journey_data(self, journey_data: list[dict[str, Any]]):
        journey_id: int = self.__retrieve_journey_id()
        bus_line: str = journey_data[0]['bus_line']
        self.__register_bus_line(bus_line)
        # TODO: create a journey_id - bus_line link in the database

        for point in journey_data:
            entry = { field: value for field, value in point.items() }
            entry['timestamp'] = datetime.strptime(entry['timestamp'], "%a %b %d %H:%M:%S %Y %Z")
            entry['journey_id'] = journey_id

            # TODO: add entry to the database

    def __retrieve_journey_id(self) -> int:
        """ Retrieves a new journey ID from the database and returns it """
        ...

    def __register_bus_line(self, bus_line: str) -> None:
        """ Registers `bus_line` to the bus lines table in the database, if not yet registered """
        ...