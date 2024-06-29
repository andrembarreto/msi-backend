from abc import ABC, abstractmethod


class JourneyPointRepository(ABC):
    @abstractmethod
    def get_points_by_journey_id(self, jourey_id: int):
        pass

    @abstractmethod
    def create(self, **journey_point_data):
        pass
