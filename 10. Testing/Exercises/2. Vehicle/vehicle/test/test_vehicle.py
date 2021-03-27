import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(fuel=2.5, horse_power=240.25)

    def test_vehicle_check_instance_attributes_are_set(self):
        self.assertEqual(2.5, self.vehicle.fuel)
        self.assertEqual(240.25, self.vehicle.horse_power)
        self.assertEqual(2.5, self.vehicle.capacity)

    def test_capacity_unchanged_if_fuel_is_changed(self):
        self.assertEqual(2.5, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(2.5, self.vehicle.capacity)

    def test_vehicle__drive_if_has_fuel_go(self):
        self.vehicle.drive(kilometers=1)
        actual_fuel = self.vehicle.fuel
        expected_fuel = 1.25
        self.assertEqual(expected_fuel, actual_fuel)

    def test_vehicle__drive__if_doesnt_have_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers=100)
        self.assertEqual(2.5, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle__refuel_if_fuel_is_equal_or_less_than_capacity(self):
        self.vehicle.drive(1)
        self.vehicle.refuel(1.25)
        actual_fuel = self.vehicle.fuel
        expected_fuel = 2.5
        self.assertEqual(expected_fuel, actual_fuel)

    def test_vehicle__refuel__if_fuel_is_bigger_than_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual('Too much fuel', str(ex.exception))
        self.assertEqual(2.5, self.vehicle.fuel)

    def test_vehicle__printing_result(self):
        result = self.vehicle.__str__()
        expected_result = f"The vehicle has 240.25 horse power with 2.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
