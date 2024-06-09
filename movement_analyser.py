from enum import Enum


class MovementIntensity(Enum):
    LOW_INTENSITY = 0
    MODERATE_INTENSITY = 1
    HIGH_INTENSITY = 2
    VERY_HIGH_INTENSITY = 3


class MovementAnalyser:
    __LOW_UPPER_LIMIT: float
    __MODERATE_UPPER_LIMIT: float
    __HIGH_UPPER_LIMIT: float
    __RELATIVE_LOW_UPPER_LIMIT: float
    __RELATIVE_MODERATE_UPPER_LIMIT: float
    __RELATIVE_HIGH_UPPER_LIMIT: float

    @staticmethod
    def calculate_acceleration_intensity(acceleration: float) -> MovementIntensity:
        if abs(acceleration) < MovementAnalyser.__LOW_UPPER_LIMIT:
            return MovementIntensity.LOW_INTENSITY
        elif abs(acceleration) < MovementAnalyser.__MODERATE_UPPER_LIMIT:
            return MovementIntensity.MODERATE_INTENSITY
        elif abs(acceleration) < MovementAnalyser.__HIGH_UPPER_LIMIT:
            return MovementIntensity.HIGH_INTENSITY
        else:
            return MovementIntensity.VERY_HIGH_INTENSITY

    @staticmethod
    def calculate_acceleration_relative_intensity(acceleration: float, average_acceleration: float) -> MovementIntensity:
        relative_value = acceleration / average_acceleration
        if abs(relative_value) < MovementAnalyser.__RELATIVE_LOW_UPPER_LIMIT:
            return MovementIntensity.LOW_INTENSITY
        elif abs(relative_value) < MovementAnalyser.__RELATIVE_MODERATE_UPPER_LIMIT:
            return MovementIntensity.MODERATE_INTENSITY
        elif abs(relative_value) < MovementAnalyser.__RELATIVE_HIGH_UPPER_LIMIT:
            return MovementIntensity.HIGH_INTENSITY
        else:
            return MovementIntensity.VERY_HIGH_INTENSITY
