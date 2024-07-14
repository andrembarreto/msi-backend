from unittest import TestCase, mock
from datetime import datetime

from point import Point
from point_additional_data import PointAdditionalData
from journey_service_impl import JourneyServiceImpl
from journey_repository import JourneyRepository
from journey_point_repository import JourneyPointRepository
from bus_line_repository import BusLineRepository
from acceleration_data_handler import AccelerationDataHandler

class TestJourneyService(TestCase):
    def setUp(self):
        self.bus_lines = set()
        self.journeys: list[str] = []
        self.journey_points_data: dict[str, list] = {'ids': [], 'points': [], 'additional_data': []}

        bus_line_repo = mock.MagicMock(spec=BusLineRepository)
        bus_line_repo.create_if_not_exists.side_effect = lambda id: self.bus_lines.add(id)

        journey_repo = mock.MagicMock(spec=JourneyRepository)
        def create_journey_mock(bus_line):
            self.journeys.append(bus_line)
            return len(self.journeys)
        journey_repo.create.side_effect = create_journey_mock

        journey_point_repo = mock.MagicMock(spec=JourneyPointRepository)
        def batch_create_mock(journey_id, points, points_add_data):
            self.journey_points_data['ids'].append(journey_id)
            self.journey_points_data['points'].append(points)
            self.journey_points_data['additional_data'].append(points_add_data)
        journey_point_repo.batch_create.side_effect = batch_create_mock

        self.journey_service = JourneyServiceImpl(bus_line_repository=bus_line_repo,
                                                  journey_points_repository=journey_point_repo,
                                                  journey_repository=journey_repo)

    def test_creates_bus_line_if_none_exists(self):
        bus_line = 'line 1'
        points = [
            Point(datetime.now(), x, x, x, x, x, x, 10+x/100, 11+x/100) for x in range(100)
        ]
        self.journey_service.register_journey(bus_line=bus_line, journey_points=points)

        self.assertTrue(bus_line in self.bus_lines)

    def test_creates_journey(self):
        self.journey_service.register_journey(bus_line='line 1', journey_points=[])
        self.assertEqual(len(self.journeys), 1)

    def test_passes_additional_points_data_to_repository(self):
        points = [
            Point(datetime.now(), x, x, x, x, x, x, 10+x/100, 11+x/100) for x in range(100)
        ]
        self.journey_service.register_journey(bus_line='line 1', journey_points=points)
        additional_points_data = self.journey_points_data['additional_data'].pop()
        stored_points = self.journey_points_data['points'].pop()

        self.assertEqual(len(additional_points_data), len(stored_points))

    def test_gravity_influence_is_removed(self):
        points = [
            Point(datetime.now(), x, x, x, x, x, x, 10+x/100, 11+x/100) for x in range(100)
        ]

        self.journey_service.register_journey(bus_line='line 1', journey_points=points)
        additional_points_data = self.journey_points_data['additional_data'].pop()
        stored_points = self.journey_points_data['points'].pop()

        point_of_interest: Point = stored_points.pop()
        _, _, transformed_z_acceleration = AccelerationDataHandler.get_transformed_acceleration_values(
            acceleration_values=(point_of_interest.acceleration_x, point_of_interest.acceleration_y, point_of_interest.acceleration_z),
            rotation_values=(point_of_interest.rotation_x, point_of_interest.rotation_y, point_of_interest.rotation_z)
        )

        additional_data_on_point_of_interest: PointAdditionalData = additional_points_data.pop()
        self.assertEqual(round(additional_data_on_point_of_interest.transformed_z_acceleration, 2),
                         round(transformed_z_acceleration, 2) - 9.8)
