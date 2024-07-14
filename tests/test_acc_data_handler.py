from unittest import TestCase
from acceleration_data_handler import AccelerationDataHandler


class TestAccelerationDataHandler(TestCase):
    def test_resultant_acceleration_should_be_0_if_all_values_are_0(self):
        result = AccelerationDataHandler.get_resultant_acceleration(0, 0, 0)
        self.assertEqual(result, 0)

    def test_transformed_acceleration_values_should_have_same_resultant_as_original_ones(self):
        ax, ay, az = 10.0, 20.0, 30.0
        resultant_before_transforming = AccelerationDataHandler.get_resultant_acceleration(ax, ay, az)
        f_x, f_y, f_z = AccelerationDataHandler.get_transformed_acceleration_values(acceleration_values=(ax, ay, az),
                                                                                        rotation_values=(20.0, 5.0, -10.0))
        resultant_after_transforming = AccelerationDataHandler.get_resultant_acceleration(f_x, f_y, f_z)
        self.assertEqual(resultant_after_transforming, resultant_before_transforming)

    def test_transformed_acceleration_values_should_be_the_same_if_there_is_no_rotation(self):
        ax, ay, az = 10.0, 20.0, 30.0
        f_x, f_y, f_z = AccelerationDataHandler.get_transformed_acceleration_values(
            acceleration_values=(ax, ay, az),
            rotation_values=(0.0, 0.0, 0.0)
        )
        self.assertEqual(ax, f_x)
        self.assertEqual(ay, f_y)
        self.assertEqual(az, f_z)
