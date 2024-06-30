from abc import ABC, abstractmethod


class JourneyPointRepository(ABC):
    @abstractmethod
    def get_points_by_journey_id(self, journey_id: int):
        pass

    @abstractmethod
    def create(self, **kwargs):
        """
        Create a new JourneyPoint entry with the provided keyword arguments.

        Parameters:
        - journey: The Journey instance or ID to which this point belongs.
        - timestamp: The timestamp of the journey point.
        - latitude: The latitude coordinate.
        - longitude: The longitude coordinate.
        - acceleration_x: The X-axis acceleration.
        - acceleration_y: The Y-axis acceleration.
        - acceleration_z: The Z-axis acceleration.
        - rotation_x: The X-axis rotation.
        - rotation_y: The Y-axis rotation.
        - rotation_z: The Z-axis rotation.

        Any additional fields that exist on the JourneyPoint model can also be passed.

        Returns:
        - A new JourneyPoint instance.
        """
        pass
