from dataclasses import dataclass, astuple
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

    def __getitem__(self, key):
        if isinstance(key, str):
            return getattr(self, key)
        else:
            raise KeyError(f"Invalid key: {key}")

    def __iter__(self):
        return iter(astuple(self))
