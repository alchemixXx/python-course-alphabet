# from homework.homework import Car, Garage, Cesar
import homework as hw
from constants import CARS_TYPES, CARS_PRODUCER
import unittest


class CarTest(unittest.TestCase):

    def setUp(self) -> None:
        self.fake_car_type = ['bolid', 'Hatchback', 'Convertible', [], (), {}, '', "some fake phrase"]
        self.fake_producers = []  # а ты правда продюсер?

    def test_car_type_checking_valid_values(self):
        """Testing car checking function (if car type in CAR_TYPE file)"""
        for car_type in CARS_TYPES:
            self.assertEqual(hw.Car.type_checking(car_type), car_type)

    def test_car_type_checking_bad_values(self):
        """This function will test car_type func on wrong values"""
        for car_type in self.fake_car_type:
            with self.assertRaises(ValueError, msg="Type should be instance of CAR_TYPES!") as context:
                hw.Car.type_checking(car_type)
            self.assertTrue("Type should be instance of CAR_TYPES!" in context.exception.args)






class GarageTest(unittest.TestCase):
    pass


class CesarTest(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()