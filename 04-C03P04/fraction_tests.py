import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    def test_str(self):
        fraction = Fraction(3, 5)
        expected = '3/5'
        self.assertEqual(expected, fraction.__str__())
        self.assertEqual(expected, fraction.__repr__())

    def test_equality(self):
        fraction1 = Fraction(1, 2)
        fraction2 = Fraction(5, 8)
        self.assertTrue(fraction1 == fraction2)

    def test_add1(self):
        fraction1 = Fraction(1, 5)
        fraction2 = Fraction(2, 5)
        expected = '3/5'
        self.assertEqual(expected, fraction1.__add__(fraction2))

    def test_add2(self):
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 2)
        expected = '11/10'
        self.assertEqual(expected, fraction1.__add__(fraction2))

    def test_sub1(self):
        fraction1 = Fraction(4, 5)
        fraction2 = Fraction(2, 5)
        expected = '2/5'
        self.assertEqual(expected, fraction1.__sub__(fraction2))

    def test_sub2(self):
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 2)
        expected = '1/10'
        self.assertEqual(expected, fraction1.__sub__(fraction2))

    def test_mul(self):
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(7, 8)
        expected = '21/40'
        self.assertEqual(expected, fraction1.__mul__(fraction2))

    def test_simplify1(self):
        fraction = Fraction(36, 144)
        expected = '1/4'
        self.assertEqual(expected, fraction.simplify())

    def test_simplify2(self):
        fraction = Fraction(1890, 2940)
        expected = '9/14'
        self.assertEqual(expected, fraction.simplify())

    def test_is_simplify1(self):
        fraction = Fraction(36, 144)
        self.assertTrue(fraction.is_simplified())

    def test_is_simplify2(self):
        fraction = Fraction(1, 4)
        self.assertFalse(fraction.is_simplified())

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(5, 0)


if __name__ == '__main__':
    unittest.main()
