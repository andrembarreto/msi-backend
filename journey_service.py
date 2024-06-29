from abc import ABC, abstractmethod
from typing import Any


class JourneyService(ABC):
    @abstractmethod
    def register_journey(self, bus_line: str, journey_points: list[dict[str, Any]]) -> None:
        """ Registers a new journey, composed by `journey_points` and set in `bus_line`,
        into the database """
        pass
