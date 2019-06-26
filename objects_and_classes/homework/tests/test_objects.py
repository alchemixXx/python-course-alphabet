# from homework.homework import Car, Garage, Cesar
import homework.homework as hw
from homework.constants import CARS_TYPES, CARS_PRODUCER
import unittest


class CarTest(unittest.TestCase):

    def test_car_type_checking_valid_values(self):
        """Testing car checking function (if car type in CAR_TYPE file)"""
        for car_type in CARS_TYPES:
            self.assertEqual(hw.Car.type_checking(car_type), car_type)





class GarageTest(unittest.TestCase):
    pass


class CesarTest(unittest.TestCase):
    pass

