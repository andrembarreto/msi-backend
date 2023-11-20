import pandas as pd
import numpy as np
from enum import Enum

class MovementIntensity(Enum):
    LOW_INTENSITY = 0
    MODERATE_INTENSITY = 1
    HIGH_INTENSITY = 2
    VERY_HIGH_INTENSITY = 3

class MovementAnalyser():
    def __init__(self, point_collection: pd.DataFrame):
        self.point_collection = point_collection
        
    @staticmethod
    def create_total_pointwise_acceleration_column(df: pd.DataFrame):
        x, y, z = df['x'], df['y'], df['z']
        result = np.hypot(x, y, z)
        df['total_acceleration'] = result

    @staticmethod
    def get_mean_total_acceleration(df: pd.DataFrame) -> float:
        return df['total_acceleration'].mean()

    @staticmethod
    def classify_by_relative_intensity(df: pd.DataFrame, value_index: int) -> MovementIntensity:
        mean_total_acceleration = MovementAnalyser.get_mean_total_acceleration(df)

        relative_intensity = df.loc[value_index, 'total_acceleration'] / mean_total_acceleration

        if relative_intensity < 0.2:
            return MovementIntensity.LOW_INTENSITY
        if 0.2 <= relative_intensity and relative_intensity < 1.2:
            return MovementIntensity.MODERATE_INTENSITY
        if 1.2 <= relative_intensity and relative_intensity < 2.0:
            return MovementIntensity.HIGH_INTENSITY
        if relative_intensity > 2.0:
            return MovementIntensity.VERY_HIGH_INTENSITY
        

    