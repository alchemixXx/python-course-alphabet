import calc
from fractions import Fraction
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        assert calc.add(1, 4) == 5, "Should be 5"

    def test_add_fraction(self):
        """That function tests sum a list of fraction"""
        data = [Fraction(1, 4), Fraction(1, 4)]
        result = calc.add(data[0], data[1])
        self.assertEqual(result, Fraction(2, 4))

    def test_bad_type(self):
        data = 'vagina'
        with self.assertRaises(TypeError) as context:
            result = calc.add(data, 1)
        self.assertTrue("Both should be int or float, not str, list. dict or tuple" in context.exception.args)


if __name__ == "__main__":
    unittest.main()
    print("Ok")
