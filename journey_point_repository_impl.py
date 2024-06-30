from models import JourneyPoint, Journey, db
from journey_point_repository import JourneyPointRepository
from point import Point


class JourneyPointRepositoryImpl(JourneyPointRepository):
    def get_points_by_journey_id(self, journey_id: int):
        query = JourneyPoint.select()\
                            .join(Journey)\
                            .where(JourneyPoint.journey == journey_id)
        return query

    def batch_create(self, journey_id: int, points: list[Point]):
        data = [
            {
                'journey': journey_id,
                'timestamp': point.timestamp,
                'latitude': point.latitude,
                'longitude': point.longitude,
                'acceleration_x': point.acceleration_x,
                'acceleration_y': point.acceleration_y,
                'acceleration_z': point.acceleration_z,
                'rotation_x': point.rotation_x,
                'rotation_y': point.rotation_y,
                'rotation_z': point.rotation_z
            }
            for point in points
        ]

        with db.atomic():
            JourneyPoint.insert_many(data).execute()
