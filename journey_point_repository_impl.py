from models import JourneyPoint, Journey
from journey_point_repository import JourneyPointRepository


class JourneyPointRepositoryImpl(JourneyPointRepository):
    def get_points_by_journey_id(self, journey_id: int):
        query = JourneyPoint.select()\
                            .join(Journey)\
                            .where(JourneyPoint.journey == journey_id)
        return query

    def create(self, **kwargs):
        return JourneyPoint.create(**kwargs)
