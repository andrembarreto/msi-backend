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
        self.__register_journey(journey_id, bus_line)

        for point in journey_data:
            entry = { field: value for field, value in point.items() }
            entry['timestamp'] = datetime.strptime(entry['timestamp'], "%a %b %d %H:%M:%S %Y %Z")
            entry['journey_id'] = journey_id

            columns = ', '.join(entry.keys())
            params = tuple(entry.values())
            placeholders = ', '.join(['%s'] * len(entry))

            query = f"INSERT INTO mobility.ponto_jornada ({columns}) VALUES ({placeholders})"
            self.__db_connection.execute_query(query, params)

    def __retrieve_journey_id(self) -> int:
        """ Retrieves a new journey ID from the database and returns it """
        ...

    def __register_bus_line(self, bus_line: str) -> None:
        """ Creates a new entry in the bus line table using `bus_line`,
        if one does not already exist.
        """
        ...

    def __register_journey(self, journey_id: int, bus_line: str) -> None:
        """ Creates a new entry in the journey table using `journey_id`
        and linking it to a bus line identified by the `bus_line` value
        """
        ...