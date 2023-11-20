import pytest
from movement_analysis import *
import statistics

@pytest.fixture
def movement_intensity_dataframe_with_mean_1() -> pd.DataFrame:
    acceleration_values_in_x_axis = [1.0] * 1000 # 1000 elements to make the mean close enough to 1 when a new (regular) value is added
    df = pd.DataFrame({
        'x' : acceleration_values_in_x_axis,
        'y' : [0.0] * len(acceleration_values_in_x_axis),
        'z' : [0.0] * len(acceleration_values_in_x_axis)
    })
    yield df

def test_mean_total_acceleration_when_object_is_absolutely_still():
    acceleration_data = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    df = pd.DataFrame(acceleration_data, columns=['x', 'y', 'z'])
    
    MovementAnalyser.create_total_pointwise_acceleration_column(df)
    mean_total_acceleration = MovementAnalyser.get_mean_total_acceleration(df)

    assert(mean_total_acceleration == 0.0)

def test_mean_total_acceleration_on_takeoff():
    y_acceleration_values_on_takeoff = [1.5, 2.2, 3.0, 3.8, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
    
    df = pd.DataFrame({
        'x' : [0.0] * len(y_acceleration_values_on_takeoff),
        'y' : y_acceleration_values_on_takeoff,
        'z' : [0.0] * len(y_acceleration_values_on_takeoff)
    })

    MovementAnalyser.create_total_pointwise_acceleration_column(df)
    mean_total_acceleration = MovementAnalyser.get_mean_total_acceleration(df)

    assert(mean_total_acceleration == statistics.mean(y_acceleration_values_on_takeoff))
    
def test_classifying_low_intensity_movement(movement_intensity_dataframe_with_mean_1: pd.DataFrame):
    movement_intensity_dataframe_with_mean_1.loc[0] = {'x': 0.15, 'y': 0, 'z': 0}
    MovementAnalyser.create_total_pointwise_acceleration_column(movement_intensity_dataframe_with_mean_1)
    
    intensity = MovementAnalyser.classify_by_relative_intensity(movement_intensity_dataframe_with_mean_1, 0)
    assert(intensity == MovementIntensity.LOW_INTENSITY)

def test_classifying_moderate_intensity_movement(movement_intensity_dataframe_with_mean_1: pd.DataFrame):
    movement_intensity_dataframe_with_mean_1.loc[0] = {'x': 0.5, 'y': 0, 'z': 0}
    MovementAnalyser.create_total_pointwise_acceleration_column(movement_intensity_dataframe_with_mean_1)

    intensity = MovementAnalyser.classify_by_relative_intensity(movement_intensity_dataframe_with_mean_1, 0)
    assert(intensity == MovementIntensity.MODERATE_INTENSITY)

def test_classifying_high_intensity_movement(movement_intensity_dataframe_with_mean_1: pd.DataFrame):
    movement_intensity_dataframe_with_mean_1.loc[0] = {'x': 1.5, 'y': 0, 'z': 0}
    MovementAnalyser.create_total_pointwise_acceleration_column(movement_intensity_dataframe_with_mean_1)
    
    intensity = MovementAnalyser.classify_by_relative_intensity(movement_intensity_dataframe_with_mean_1, 0)
    assert(intensity == MovementIntensity.HIGH_INTENSITY)

def test_classifying_very_high_intensity_movement(movement_intensity_dataframe_with_mean_1: pd.DataFrame):
    movement_intensity_dataframe_with_mean_1.loc[0] = {'x': 2.5, 'y': 0, 'z': 0}
    MovementAnalyser.create_total_pointwise_acceleration_column(movement_intensity_dataframe_with_mean_1)
    
    intensity = MovementAnalyser.classify_by_relative_intensity(movement_intensity_dataframe_with_mean_1, 0)
    assert(intensity == MovementIntensity.VERY_HIGH_INTENSITY)