from typing import Any
from datetime import datetime

from db_connection import DBConnection


class MobilityDBController:
    def __init__(self, db_connection: DBConnection) -> None:
        self.__db_connection = db_connection
        self.__db_connection.connect()

    def register_journey_data(self, journey_data: list[dict[str, Any]]):
        bus_line: str = journey_data[0]['bus_line']
        self.__register_bus_line(bus_line)
        journey_id = self.__register_journey(bus_line)

        for point in journey_data:
            entry = { field: value for field, value in point.items() }
            entry['timestamp'] = datetime.strptime(entry['timestamp'], "%a %b %d %H:%M:%S %Y %Z")
            entry['journey_id'] = journey_id

            columns = ', '.join(entry.keys())
            params = tuple(entry.values())
            placeholders = ', '.join(['%s'] * len(entry))

            query = f"INSERT INTO mobility.ponto_jornada ({columns}) VALUES ({placeholders})"
            self.__db_connection.execute_query(query, params)
            self.__db_connection.commit()

    def __register_bus_line(self, bus_line: str) -> None:
        """ Creates a new entry in the bus line table using `bus_line`,
        if one does not already exist.
        """
        bus_line_query = "SELECT id from mobility.linha_onibus WHERE id = %s"
        result = self.__db_connection.fetch_one(bus_line_query, params=(bus_line,))

        if not result:
            insert_query = "INSERT INTO mobility.linha_onibus (id) VALUES (%s)"
            self.__db_connection.execute_query(insert_query, params=(bus_line,))

    def __register_journey(self, bus_line: str) -> int:
        """ Creates a new entry in the journey table, linking it to a bus line
        identified by the `bus_line` value. Returns the newly added journey's id
        """
        insert_query = "INSERT INTO mobility.jornada (bus_line) VALUES (%s) RETURNING id"
        result = self.__db_connection.fetch_one(insert_query, params=(bus_line,))
        return list(result.values())[0]
