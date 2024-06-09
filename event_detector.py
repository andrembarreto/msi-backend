from abc import ABC
from datetime import datetime

from point import Point

class EventDetector(ABC):
    @staticmethod
    def detect(points: list[Point]) -> list[tuple[datetime, datetime]]:
        """ Returns a list of detected occurrences of the target event
        as a list of pairs of timestamps that define the interval of
        that event (initial timestamp, final timestamp)
        """
        ...


class BumpDetector(EventDetector):
    ...


class PotholeDetector(EventDetector):
    ...


class SuddenBrakingDetector(EventDetector):
    ...


class SuddenAccelerationDetector(EventDetector):
    ...


class SharpCurveDetector(EventDetector):
    ...
