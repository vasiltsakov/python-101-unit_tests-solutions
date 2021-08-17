import unittest
from fraction import Fraction

a = Fraction(1, 2)
b = Fraction(1, 2)
a2 = Fraction(3, 5)
b2 = Fraction(1, 2)


class FractionTest(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_str(self):
        self.assertEqual('1/2', str(a))
        self.assertEqual('1/2', str(b))

    def test_repr(self):
        self.assertEqual('Fraction(1, 2)', repr(a))
        self.assertEqual('Fraction(1, 2)', repr(b))

    def test_equality(self):
        with self.subTest('Test 1'):
            self.assertTrue(a == b)

        with self.subTest('Test 2'):
            self.assertTrue(Fraction(1, 2) == Fraction(2, 4))

        with self.subTest('Test 3'):
            self.assertFalse(a2 == b2)

        with self.subTest('Test 4'):
            with self.assertRaises(TypeError):
                a == [1, 2, 3]

    def test_add(self):
        with self.subTest('Test 1'):
            c = a + b
            self.assertEqual('2/2', str(c))
            self.assertEqual('1/1', str(c.simplify()))
            self.assertFalse(c.is_simplified())
            self.assertTrue(c.simplify().is_simplified())

        with self.subTest('Test 2'):
            c2 = a2 + b2
            self.assertEqual('11/10', str(c2))
            self.assertEqual('11/10', str(c2.simplify()))
            self.assertTrue(c2.is_simplified())
            self.assertTrue(c2.simplify().is_simplified())

        with self.subTest('Test 3'):
            with self.assertRaises(TypeError):
                5 + a

        with self.subTest('Test 4'):
            with self.assertRaises(TypeError):
                'string' + a

        with self.subTest('Test 4'):
            with self.assertRaises(AttributeError):
                a + 'string'

        with self.subTest('Test 5'):
            with self.assertRaises(AttributeError):
                a + [1, 1, 1]

        with self.subTest('Test 5'):
            with self.assertRaises(TypeError):
                [1, 1, 1] + a

    def test_sub(self):
        with self.subTest('Test 1'):
            d = a - b
            self.assertEqual('0', str(d))
            self.assertEqual('0', str(d.simplify()))
            self.assertTrue(d.is_simplified())

        with self.subTest('Test 2'):
            d2 = a2 - b2
            self.assertEqual('1/10', str(d2))
            self.assertEqual('1/10', str(d2.simplify()))
            self.assertTrue(d2.is_simplified())

        with self.subTest('Test 3'):
            with self.assertRaises(TypeError):
                5 - a

    def test_mul(self):
        with self.subTest('Test 1'):
            e = a * b
            self.assertEqual('1/4', str(e))
            self.assertEqual('1/4', str(e.simplify()))
            self.assertTrue(e.is_simplified())

        with self.subTest('Test 2'):
            with self.assertRaises(TypeError):
                5 * a

    def test_sorted(self):
        with self.subTest('Test 1'):
            unsorted_fractions = [Fraction(3, 4), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)]
            expected_sorted_fraction = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
            sorted_fractions = a.sorted(unsorted_fractions)
            self.assertEqual(expected_sorted_fraction, sorted_fractions)

        with self.subTest('Test 2'):
            unsorted_fractions = [Fraction(3, 4), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)]
            expected_sorted_fraction = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
            sorted_fractions = Fraction.sorted(unsorted_fractions)
            self.assertEqual(expected_sorted_fraction, sorted_fractions)

        with self.subTest('Test 3'):
            unsorted_fractions = [Fraction(3, 4), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)]
            expected_sorted_fraction = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
            sorted_fractions = sorted(unsorted_fractions)
            self.assertEqual(expected_sorted_fraction, sorted_fractions)


if __name__ == '__main__':
    unittest.main()

