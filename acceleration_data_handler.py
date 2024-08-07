import numpy as np
import math


class AccelerationDataHandler:
    @staticmethod
    def get_resultant_acceleration(ax: float, ay: float, az: float) -> float:
        """ Calculates and returns the resultant acceleration from `acceleration_values` """
        return math.sqrt(ax*ax + ay*ay + az*az)

    @staticmethod
    def get_transformed_acceleration_values(acceleration_values, rotation_values) -> tuple[float, float, float]:
        """
        Performs an active transformation of the `acceleration_values` for a fixed coordinate system,
        using the `rotation_values` based on the right-hand cartesian system
        """
        roll, pitch, yaw = rotation_values
        R_x, R_y, R_z = AccelerationDataHandler.get_rotation_matrices(roll, pitch, yaw)

        combined_rotation_matrix = R_z @ R_y @ R_x
        transformed_acceleration = combined_rotation_matrix @ acceleration_values

        return transformed_acceleration

    @staticmethod
    def get_rotation_matrices(roll, pitch, yaw):
        roll_rad = np.deg2rad(roll)
        pitch_rad = np.deg2rad(pitch)
        yaw_rad = np.deg2rad(yaw)

        # Roll rotation matrix (around x-axis)
        R_x = np.array([
            [1, 0, 0],
            [0, np.cos(roll_rad), -np.sin(roll_rad)],
            [0, np.sin(roll_rad), np.cos(roll_rad)]
        ])

        # Pitch rotation matrix (around y-axis)
        R_y = np.array([
            [np.cos(pitch_rad), 0, np.sin(pitch_rad)],
            [0, 1, 0],
            [-np.sin(pitch_rad), 0, np.cos(pitch_rad)]
        ])

        # Yaw rotation matrix (around z-axis)
        R_z = np.array([
            [np.cos(yaw_rad), -np.sin(yaw_rad), 0],
            [np.sin(yaw_rad), np.cos(yaw_rad), 0],
            [0, 0, 1]
        ])

        return R_x, R_y, R_z
