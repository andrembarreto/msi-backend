from dataclasses import dataclass


@dataclass(frozen=True)
class PointAdditionalData:
    """
    This class is meant to store additional data on the collected points that
    can be calculated from the original data
    """
    transformed_x_acceleration: float
    transformed_y_acceleration: float
    transformed_z_acceleration: float
    resultant_acceleration: float
