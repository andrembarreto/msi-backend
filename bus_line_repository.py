from abc import ABC, abstractmethod


class BusLineRepository(ABC):
    @abstractmethod
    def get_by_id(self, bus_line_id: str):
        pass

    def create(self, bus_line_id: str):
        pass
