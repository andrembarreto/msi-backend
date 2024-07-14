from journey_service import JourneyService
from journey_repository import JourneyRepository
from journey_point_repository import JourneyPointRepository
from bus_line_repository import BusLineRepository
from acceleration_data_handler import AccelerationDataHandler

from point import Point
from point_additional_data import PointAdditionalData


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
        points_additional_data = self._get_points_additional_data(journey_points)

        self.__journey_points_repository.batch_create(journey_id, journey_points, points_additional_data) # type: ignore

    def _get_points_additional_data(self, points: list[Point]) -> list[PointAdditionalData]:
        points_additional_data: list[PointAdditionalData] = []

        for point in points:
            t_x_acceleration, t_y_acceleration, t_z_acceleration = \
                AccelerationDataHandler.get_transformed_acceleration_values(
                    acceleration_values=(point.acceleration_x, point.acceleration_y, point.acceleration_z),
                    rotation_values=(point.rotation_x, point.rotation_y, point.rotation_z)
                )
            # remove gravity influence
            t_z_acceleration -= 9.8

            resultant_acceleration = \
                AccelerationDataHandler.get_resultant_acceleration(
                    ax=t_x_acceleration,
                    ay=t_y_acceleration,
                    az=t_z_acceleration
                )

            points_additional_data.append(
                PointAdditionalData(
                    transformed_x_acceleration=t_x_acceleration,
                    transformed_y_acceleration=t_y_acceleration,
                    transformed_z_acceleration=t_z_acceleration,
                    resultant_acceleration=resultant_acceleration
                )
            )

        return points_additional_data
