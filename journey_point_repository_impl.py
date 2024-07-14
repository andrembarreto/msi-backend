from typing import Any
from models import JourneyPoint, Journey, db
from journey_point_repository import JourneyPointRepository
from point import Point
from point_additional_data import PointAdditionalData


class JourneyPointRepositoryImpl(JourneyPointRepository):
    def get_points_by_journey_id(self, journey_id: int) -> list[Point]:
        query = JourneyPoint.select()\
                            .join(Journey)\
                            .where(JourneyPoint.journey == journey_id)
        points = [
            Point(
                timestamp=point.timestamp,
                acceleration_x=point.acceleration_x,
                acceleration_y=point.acceleration_y,
                acceleration_z=point.acceleration_z,
                rotation_x=point.rotation_x,
                rotation_y=point.rotation_y,
                rotation_z=point.rotation_z,
                latitude=point.geometry.x,
                longitude=point.geometry.y
            )
            for point in query
        ]
        return points

    def batch_create(self, journey_id: int, points: list[Point], points_additional_data: list[PointAdditionalData]):
        data = [
            {
                'journey': journey_id,
                'timestamp': point.timestamp,
                'geometry': (f'POINT ({point.longitude} {point.latitude})', 4326),
                'acceleration_x': point.acceleration_x,
                'acceleration_y': point.acceleration_y,
                'acceleration_z': point.acceleration_z,
                'rotation_x': point.rotation_x,
                'rotation_y': point.rotation_y,
                'rotation_z': point.rotation_z,
                'transformed_x_acceleration': additional_data.transformed_x_acceleration,
                'transformed_y_acceleration': additional_data.transformed_y_acceleration,
                'transformed_z_acceleration': additional_data.transformed_z_acceleration,
                'resultant_acceleration': additional_data.resultant_acceleration
            }
            for point, additional_data in zip(points, points_additional_data)
        ]

        with db.atomic():
            JourneyPoint.insert_many(data).execute()
