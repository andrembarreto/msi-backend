from typing import Any

from journey_service import JourneyService
from journey_repository import JourneyRepository
from journey_point_repository import JourneyPointRepository
from bus_line_repository import BusLineRepository
from point import Point


class JourneyServiceImpl(JourneyService):
    def __init__(self,
                 journey_repository: JourneyRepository,
                 journey_points_repository: JourneyPointRepository,
                 bus_line_repository: BusLineRepository) -> None:
        self.__journey_repository = journey_repository
        self.__journey_points_repository = journey_points_repository
        self.__bus_line_repository = bus_line_repository

    def register_journey(self, bus_line: str, journey_points: list[Point]) -> None:
        self.__bus_line_repository.create_if_not_exists(bus_line)
        journey_id = self.__journey_repository.create(bus_line)

        self.__journey_points_repository.batch_create(journey_id, journey_points)
