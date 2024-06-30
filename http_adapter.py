from flask import jsonify, Response

from point import Point
from journey_service import JourneyService
from http_status_code import HTTPStatusCode


class HTTPAdapter:
    def __init__(self, journey_service: JourneyService):
        self.__journey_service = journey_service

    @staticmethod
    def point_from_json(point_data: dict) -> Point:
        return Point(
            timestamp=point_data['timestamp'],
            latitude=point_data['latitude'],
            longitude=point_data['longitude'],
            acceleration_x=point_data['acceleration_x'],
            acceleration_y=point_data['acceleration_y'],
            acceleration_z=point_data['acceleration_z'],
            rotation_x=point_data['rotation_x'],
            rotation_y=point_data['rotation_y'],
            rotation_z=point_data['rotation_z']
        )

    def receive_mobility_data(self, mobility_data) -> Response:
        try:
            bus_line = mobility_data['bus_line']
        except KeyError:
            return jsonify({'status': HTTPStatusCode.MISSING_BUS_LINE})
        try:
            points_data = mobility_data['points']
        except KeyError:
            return jsonify({'status': HTTPStatusCode.MISSING_POINTS})

        try:
            points = [self.point_from_json(point) for point in points_data]
        except KeyError:
            return jsonify({'status': HTTPStatusCode.BAD_FORMAT})

        self.__journey_service.register_journey(bus_line, points)
        return jsonify({'status': HTTPStatusCode.SUCCESS})
