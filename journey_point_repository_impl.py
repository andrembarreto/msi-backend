from models import JourneyPoint
from journey_point_repository import JourneyPointRepository


class JourneyPointRepositoryImpl(JourneyPointRepository):
    def get_points_by_journey_id(self, journey_id: int):
        raise NotImplementedError()

    def create(self, **kwargs):
        return JourneyPoint.create(**kwargs)
