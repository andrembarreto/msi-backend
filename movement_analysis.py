import pandas as pd
import numpy as np
from enum import Enum


class MovementIntensity(Enum):
    LOW_INTENSITY = 0
    MODERATE_INTENSITY = 1
    HIGH_INTENSITY = 2
    VERY_HIGH_INTENSITY = 3


class MovementStability(Enum):
    STABLE = 0
    LIGHT_VIBRATION = 1
    MODERATE_VIBRATION = 2
    INTENSE_VIBRATION = 3
    UNSTABLE = 4


class MovementAnalyser:
    def __init__(self, points: pd.DataFrame):
        self.points = points
        
    @staticmethod
    def create_total_acceleration_column(df: pd.DataFrame) -> None:
        x, y, z = df['acceleration_x'], df['acceleration_y'], df['acceleration_z']
        result = np.hypot(x, y, z)
        df['total_acceleration'] = result

    @staticmethod
    def create_segment_rotation_variation_column(segment: pd.Series):
        pass

    @staticmethod
    def get_mean_total_acceleration(df: pd.DataFrame) -> float:
        return df['total_acceleration'].mean()

    @staticmethod
    def get_mean_total_rotation_variation(df: pd.DataFrame) -> float:
        return df['rotation_variation'].mean()


    # pegar valores de rotacao em cada eixo dos dois pontos que definem um trecho
    @staticmethod
    def get_segment_points_rotation_values(df: pd.DataFrame, point_id_1: int, point_id_2: int) -> list[pd.Series]:
        point_1_rotation_values = df[point_id_1, ['']]
        ...

    @staticmethod
    def classify_by_relative_intensity(df: pd.DataFrame, value_index: int) -> MovementIntensity:
        mean_total_acceleration = MovementAnalyser.get_mean_total_acceleration(df)

        relative_intensity = df.loc[value_index, 'total_acceleration'] / mean_total_acceleration

        if relative_intensity < 0.2:
            return MovementIntensity.LOW_INTENSITY
        elif relative_intensity < 1.2:
            return MovementIntensity.MODERATE_INTENSITY
        elif relative_intensity < 2.0:
            return MovementIntensity.HIGH_INTENSITY
        else:
            return MovementIntensity.VERY_HIGH_INTENSITY

    @staticmethod
    def classify_by_relative_stability(df: pd.DataFrame, value_index: int) -> MovementStability:
        mean_rotation_variation = MovementAnalyser.get_mean_total_rotation_variation(df)

        relative_variation = df.loc[value_index, 'rotation_variation'] / mean_rotation_variation

        if relative_variation < 0.01:
            return MovementStability.STABLE
        if relative_variation < 0.2:
            return MovementStability.LIGHT_VIBRATION
        elif relative_variation < 1.2:
            return MovementStability.MODERATE_VIBRATION
        elif relative_variation < 2.0:
            return MovementStability.INTENSE_VIBRATION
        else:
            return MovementStability.UNSTABLE
