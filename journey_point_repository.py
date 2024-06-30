from abc import ABC, abstractmethod

from point import Point


class JourneyPointRepository(ABC):
    @abstractmethod
    def get_points_by_journey_id(self, journey_id: int):
        pass

    @abstractmethod
    def batch_create(self, journey_id: int, points: list[Point]):
        pass
