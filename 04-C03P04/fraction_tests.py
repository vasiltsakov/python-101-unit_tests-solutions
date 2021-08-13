import unittest
from fraction import Fraction

a = Fraction(1, 2)
b = Fraction(1, 2)
a2 = Fraction(3, 5)
b2 = Fraction(1, 2)


class FractionTest(unittest.TestCase):
    def test_str(self):
        self.assertEqual('1/2', a.__str__())
        self.assertEqual('1/2', b.__str__())

    def test_equality1(self):
        self.assertTrue(a == b)

    def test_equality2(self):
        self.assertFalse(a2 == b2)

    def test_add1(self):
        c = a + b
        self.assertEqual('2/2', c.__str__())
        self.assertEqual('1/1', c.simplify().__str__())
        self.assertFalse(c.is_simplified())
        self.assertTrue(c.simplify().is_simplified())

    def test_add2(self):
        c2 = a2 + b2
        self.assertEqual('11/10', c2.__str__())
        self.assertEqual('11/10', c2.simplify().__str__())
        self.assertTrue(c2.is_simplified())
        self.assertTrue(c2.simplify().is_simplified())

    def test_sub(self):
        d = a - b
        self.assertEqual('0', d.__str__())
        self.assertEqual('0', d.simplify().__str__())
        self.assertTrue(d.is_simplified())

    def test_mul(self):
        e = a * b
        self.assertEqual('1/4', e.__str__())
        self.assertEqual('1/4', e.simplify().__str__())
        self.assertTrue(e.is_simplified())


if __name__ == '__main__':
    unittest.main()

