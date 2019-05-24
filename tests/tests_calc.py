import unittest
import calc


class CalcTest(unittest.TestCase):

    """Calc tests"""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up for class"""
        print('setUpClass')
        print("++++++++++")

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down for class"""
        print('tearDownClass')
        print("++++++++++")

    def setUp(self) -> None:
        """Set for test"""
        print(f'setUp for [{self.shortDescription()}]')

    def tearDown(self) -> None:
        """Tear down for test"""
        print(f'Tear down for [{self.shortDescription()}]')

    def test_add(self):
        """test_add"""
        self.assertEqual(calc.add(1,2), 3)

    def test_sub(self):
        """test_sub"""
        self.assertEqual(calc.sub(5,2), 3)

    def test_mult(self):
        """test_mult"""
        self.assertEqual(calc.mult(5,2), 10)

    def test_div(self):
        """test_div"""
        self.assertEqual(calc.div(8,4), 2)



if __name__ == "__main__":
    unittest.main()