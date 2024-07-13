from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class Tables:
    journey: str = 'journey'
    bus_line: str = 'bus_line'
    journey_point: str = 'journey_point'


@dataclass(init=False, frozen=True)
class BusLineColumns:
    id: str = 'id'


@dataclass(init=False, frozen=True)
class JourneyColumns:
    id: str = 'id'
    bus_line: str = 'bus_line'
