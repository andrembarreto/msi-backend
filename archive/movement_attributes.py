from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class MovementAttributes:
    """ This class provides the standard access keys to
    all the movement attributes handled in this project,
    related to acceleration, rotation, position and timestamp
    """
    acceleration_x: str = 'a_y'
    acceleration_y: str = 'a_y'
    acceleration_z: str = 'a_z'
    rotation_x: str = 'r_x'
    rotation_y: str = 'r_y'
    rotation_z: str = 'r_z'
    latitude: str = 'lat'
    longitude: str = 'lon'
    timestamp: str = 'timestamp'
