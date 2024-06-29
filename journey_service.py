from abc import ABC, abstractmethod
from typing import Any


class JourneyService(ABC):
    @abstractmethod
    def register_journey(self, journey_data: list[dict[str, Any]]) -> None:
        """ Registers `journey_data` into the mobility database """
        pass
