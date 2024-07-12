from abc import ABC, abstractmethod


class AccelerationDataHandler(ABC):
    @abstractmethod
    @staticmethod
    def get_resultant_acceleration(acceleration_values):
        """ Calculates and returns the resultant acceleration from `acceleration_values` """
        ...

    @abstractmethod
    @staticmethod
    def get_transformed_acceleration_values(acceleration_values, rotation_values):
        """
        Performs an active transformation of the `acceleration_values` for a fixed coordinate system,
        using the `rotation_values` based on the right-hand cartesian system
        """
        ...
