import numpy as np

from acceleration_data_handler import AccelerationDataHandler


class AccelerationDataHandlerImpl(AccelerationDataHandler):
    @staticmethod
    def get_resultant_acceleration(acceleration_values):
        return np.hypot(*acceleration_values)


    @staticmethod
    def get_transformed_acceleration_values(acceleration_values, rotation_values):
        roll, pitch, yaw = rotation_values
        R_x, R_y, R_z = AccelerationDataHandlerImpl.get_rotation_matrices(roll, pitch, yaw)

        # Combined rotation matrix R
        R = R_z @ R_y @ R_x

        # Transform the acceleration vector the rotation matrix
        transformed_acceleration = R @ acceleration_values

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
