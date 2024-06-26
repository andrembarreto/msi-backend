from abc import ABC, abstractmethod


class JourneyRepository(ABC):
    @abstractmethod
    def get_by_id(self, journey_id: int):
        pass

    @abstractmethod
    def create(self, bus_line: str):
        pass
