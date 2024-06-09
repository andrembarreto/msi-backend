from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class Point:
    timestamp: datetime
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    rotation_x: float
    rotation_y: float
    rotation_z: float
    latitude: float
    longitude: float
