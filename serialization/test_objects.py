import homework as hw
from constants import CARS_TYPES, CARS_PRODUCER
# from fixtures import car1, car2, car3, car4, car5, garage1, garage2, garage3, cesar_1, cesar_2
from fixtures import car4, car5, garage1, garage2, garage3, cesar_1, cesar_2
import uuid
import unittest


class CarTest(unittest.TestCase):
    #
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.price="683.0",
    #     cls.producer="Lamborghini"
    #     cls.car_type="Truck",
    #     cls.number="ce80e01a-af46-43c3-9e9e-83c324ba2c63",
    #     cls.mileage="1523.0",
    #     cls.garage_numb = "0"

    def setUp(self) -> None:
        self.fake_car_type = ['bolid', 'Hatchback', 'Convertible', '', "some fake phrase", 12553, 1258964.65465421,
                              ["element_one", "element_two"], ("element_one", "element_two",),
                              {"element_one": "value_one", "element_two": "value_two"},
                              [], (), {}, None, True, False]

        self.fake_producers = ["DaeWoo", "McLaren", "just a string", "", 12553, 1258964.65465421,
                               ["element_one", "element_two"], ("element_one", "element_two",),
                               {"element_one": "value_one", "element_two": "value_two"},
                               [], (), {}, None, True, False]  # а ты правда продюсер?

        self.number = 'c4595999-28b9-4a98-bd85-9d59ada33efe'

        self.new_uuid_number = str(uuid.uuid4())

        self.bad_uuid_values_1 = ['35461654651-sadasd-szdfsf', '%4595999-28b9-4a98-bd85-9d59ada33efe',
                                  'c4595999-28b9-4a98-bd85-d59ada33efe', '', "some fake phrase"]

        self.bad_uuid_values_2 = [["element_one", "element_two"], ("element_one", "element_two",),
                                  {"element_one": "value_one", "element_two": "value_two"},
                                  [], (), {}, 12553, 1258964.65465421, uuid.uuid4(), True, False]

        self.bad_uuid_values_3 = [None]

        self.price_values = [12553, 1258964.65465421,"12553"]

        self.price_bad_values = [["element_one", "element_two"], ("element_one", "element_two",),
                               {"element_one": "value_one", "element_two": "value_two"},
                               [], (), {}, None, True, False]
        self.comparison = [1.0025, 100, 1000, 0, -1, 0.0, 100000000000000000, 10000000000000.0, 0.00000001, -1.0025]

        self.car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                      producer="Ford")
        self.car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                      producer="Ford")
        self.car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                      producer="Ford", garage_numb=0)

    def tearDown(self) -> None:
        self.number = 'c4595999-28b9-4a98-bd85-9d59ada33efe'
        self.car1 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                      producer="Ford")
        self.car2 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f53', car_type="Diesel",
                      producer="Ford")
        self.car3 = hw.Car(price=1, mileage=1, number='65c11813-3eb5-4d48-b62b-3da6ef951f55', car_type="Diesel",
                      producer="Ford", garage_numb=0)

    def test_car_type_checking_valid_values(self):
        """This function will test  car type checking (if car type in CAR_TYPE list)"""
        for car_type in CARS_TYPES:
            self.assertEqual(hw.Car.type_checking(car_type), car_type)

    def test_car_type_checking_bad_values(self):
        """This function will test car type checking on wrong values"""
        for car_type in self.fake_car_type:
            with self.assertRaises(ValueError, msg="Type should be instance of CAR_TYPES!") as context:
                hw.Car.type_checking(car_type)
            self.assertTrue("Type should be instance of CAR_TYPES!" in context.exception.args)

    def test_car_producer_valid_data(self):
        """This function will test  car producer checking (if car producer in CARS_PRODUCER list)"""
        for producer in CARS_PRODUCER:
            self.assertEqual(hw.Car.producer_checking(producer), producer)

    def test_car_producer_checking_bad_values(self):
        """This function will test car type checking on wrong values"""
        for producer in self.fake_producers:
            with self.assertRaises(ValueError, msg="Producer should be instance of CARS_PRODUCER!") as context:
                hw.Car.producer_checking(producer)
            self.assertTrue("Producer should be instance of CARS_PRODUCER!" in context.exception.args)

    def change_number(self, new_number):
        try:
            uuid.UUID(new_number, version=4)
            self.number = new_number
            return "Number has been changed"
        except ValueError or AttributeError or TypeError:
            return 'Sorry, you have entered wrong number'

    def test_change_number_valid_data(self):
        """This function will test changing uuid-number of car function """
        expected_res = "Number has been changed"
        self.assertEqual(hw.Car.change_number(self, new_number=self.new_uuid_number), expected_res)
        self.assertEqual(self.number, self.new_uuid_number)

    def test_change_number_bad_data_attribute_error(self):
        """This function will test changing uuid-number of car function on wrong values: list, tuple, dict, float, int.
        Should be AttributeError"""
        expected_res = 'Sorry, you have entered wrong number. It should be a string, not list, tuple, set, dict, int or float'
        with self.assertRaises(AttributeError) as context:
            for value in self.bad_uuid_values_2:
                process = hw.Car.change_number(self, new_number=value)
                self.assertEqual(process, expected_res)
            self.assertTrue(
                'Sorry, you have entered wrong number. It should be a string, not list, tuple, set, dict, int or float'
                in context.exception.args)

    def test_change_number_bad_data_value_error(self):
        """This function will test changing uuid-number of car function on wrong values: bad string.
        Should be AttributeError"""
        expected_res = 'Sorry, you have entered bad format of string'
        with self.assertRaises(AttributeError) as context:
            for value in self.bad_uuid_values_1:
                process = hw.Car.change_number(self, new_number=value)
                self.assertEqual(process, expected_res)
            self.assertTrue("Sorry, you have entered bad format of string" in context.exception.args)


    def test_change_number_bad_data_type_error(self):
        """This function will test changing uuid-number of car function on wrong values: bad string.
        Should be AttributeError"""
        expected_res = 'Sorry, you have entered bad type of argument. ' \
                       'One of the hex, bytes, bytes_le, fields, or int arguments must be given'
        with self.assertRaises(AttributeError) as context:
            for value in self.bad_uuid_values_3:
                process = hw.Car.change_number(self, new_number=value)
                self.assertEqual(process, expected_res)
            self.assertTrue("Sorry, you have entered bad type of argument. "
                            "One of the hex, bytes, bytes_le, fields, or int arguments must be given"
                            in context.exception.args)

    def test_convert_to_float_valid_data(self):
        """ This function will test convert to float function """
        for value in self.price_values:
            self.assertIsInstance(hw.Car._convert_to_float(value), float)
            self.assertEqual(hw.Car._convert_to_float(value), float(value))

    def test_convert_to_float_bad_data(self):
        """ This function will test convert to float function on bad data: str, list, dict, tuple, None, Bool"""
        for value in self.price_bad_values:
            self.assertEqual(hw.Car._convert_to_float(value), None)

    #
    # def test_repr(self):
    #     """This func will test __repr__ of Car class"""
    #     self.assertIsInstance(hw.Car.__repr__(self), str)

    def test_less_equal(self):
        """This func will test __le__ of Car"""
        for value in self.comparison:
            self.car1.price = value
            if value <= 1:
                self.assertEqual(self.car1 <= self.car2, True)
            else:
                self.assertEqual(self.car1 <= self.car2, False)

    def test_less(self):
        """This func will test __lt__ of Car"""
        for value in self.comparison:
            self.car1.price = value
            if value < 1:
                self.assertEqual(self.car1 < self.car2, True)
            else:
                self.assertEqual(self.car1 < self.car2, False)

    def test_equality_equal(self):
        """This test will pass if two objects have the same attributes"""
        self.assertTrue(self.car1.equality(self.car2))

    def test_equality_not_equal_price(self):
        """This test will pass if two objects have NOT the same attribute price"""
        for value in self.comparison:
            self.car1.price = value
            self.assertFalse(self.car1.equality(self.car3))

    def test_equality_not_equal_mileage(self):
        """This test will pass if two objects have NOT the same attribute mileage"""
        for value in self.comparison:
            self.car1.mileage = value
            self.assertFalse(self.car1.equality(self.car3))

    def test_equality_not_equal_uuid(self):
        """This test will pass if two objects have NOT the same attribute uuid"""
        self.car1.uuid = uuid.uuid4()
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_not_equal_producer(self):
        """This test will pass if two objects have NOT the same attribute producer"""
        self.car1.producer = "Dodge"
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_not_equal_type(self):
        """This test will pass if two objects have NOT the same attribute car_type"""
        self.car1.car_type = "Coupe"
        self.assertFalse(self.car1.equality(self.car3))

    def test_equality_not_equal_garage(self):
        """This test will pass if two objects have NOT the same attribute garage numb"""
        self.car1.garage_numb = 1
        self.assertFalse(self.car1.equality(self.car3))



class GarageTest(unittest.TestCase):
    pass


class CesarTest(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
