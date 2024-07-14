from abc import ABC, abstractmethod

from point import Point
from point_additional_data import PointAdditionalData


class JourneyPointRepository(ABC):
    @abstractmethod
    def get_points_by_journey_id(self, journey_id: int) -> list[Point]:
        pass

    @abstractmethod
    def batch_create(self, journey_id: int, points: list[Point], points_additional_data: list[PointAdditionalData]):
        """
        Creates a new entry in the database for each point in `points`, using also
        the data provided in `points_additional_data`, in a single operation
        """
        pass
