from abc import ABC, abstractmethod


class BusLineRepository(ABC):
    @abstractmethod
    def create_if_not_exists(self, bus_line_id: str):
        pass
