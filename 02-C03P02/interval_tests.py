import unittest
from interval import Interval


class IntervalTests(unittest.TestCase):
    def test_stringify_all_closed_produces_correct_result(self):
        interval = Interval(1, 10)
        expected = "[1, 10]"

        self.assertEqual(expected, interval.stringify())

    def test_stringify_start_opened_produces_correct_result(self):
        interval = Interval(1, 10, True)
        expected = "(1, 10]"

        self.assertEqual(expected, interval.stringify())

    def test_stringify_end_opened_produces_correct_result(self):
        interval = Interval(1, 10, False, True)
        expected = "[1, 10)"

        self.assertEqual(expected, interval.stringify())

    def test_stringify_all_opened_produces_correct_result(self):
        interval = Interval(1, 10, True, True)
        expected = "(1, 10)"

        self.assertEqual(expected, interval.stringify())


    def test_is_inside_all_closed_produces_correct_results(self):
        interval = Interval(1, 10)

        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(10))
        self.assertFalse(interval.is_inside(11))
        self.assertFalse(interval.is_inside(0))

    def test_is_inside_start_opened_produces_correct_results(self):
        interval = Interval(1, 10, True)

        self.assertFalse(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(10))
        self.assertFalse(interval.is_inside(11))
        self.assertFalse(interval.is_inside(0))

    def test_is_inside_end_opened_produces_correct_results(self):
        interval = Interval(1, 10, False, True)

        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertFalse(interval.is_inside(10))
        self.assertFalse(interval.is_inside(11))
        self.assertFalse(interval.is_inside(0))

    def test_is_inside_all_opened_produces_correct_results(self):
        interval = Interval(1, 10, True, True)

        self.assertFalse(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertFalse(interval.is_inside(10))
        self.assertFalse(interval.is_inside(11))
        self.assertFalse(interval.is_inside(0))



if __name__ == '__main__':
    unittest.main()