from enum import Enum
import numpy as np
from typing import Iterable


class MovementIntensity(Enum):
    LOW_INTENSITY = 0
    MODERATE_INTENSITY = 1
    HIGH_INTENSITY = 2
    VERY_HIGH_INTENSITY = 3


class MovementAnalyser:
    @staticmethod
    def calculate_acceleration_intensity(acceleration_values: Iterable[float]) -> Iterable[MovementIntensity]:
        ...

    @staticmethod
    def get_relative_intensity_from_acceleration_values(acceleration_values: Iterable[float]) -> Iterable[MovementIntensity]:
        np_acceleration_values = np.abs(np.array(acceleration_values))

        mean_acceleration_value = np.mean(np_acceleration_values)
        acceleration_standard_deviation = np.std(np_acceleration_values)

        def _calculate_acceleration_relative_intensity(acc, mean, std) -> MovementIntensity:
            if acc < mean + std:
                return MovementIntensity.LOW_INTENSITY
            elif acc < mean + 2 * std:
                return MovementIntensity.HIGH_INTENSITY
            else:
                return MovementIntensity.VERY_HIGH_INTENSITY

        calculate_acceleration_relative_intensity = np.vectorize(
            lambda acceleration: _calculate_acceleration_relative_intensity(acc=acceleration,
                                                                            mean=mean_acceleration_value,
                                                                            std=acceleration_standard_deviation)
        )
        acceleration_relative_intensities = calculate_acceleration_relative_intensity(np_acceleration_values)

        return acceleration_relative_intensities
