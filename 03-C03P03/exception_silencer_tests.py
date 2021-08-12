import unittest
from exception_silencer import ExceptionSilencer


class ExceptionSilencerTest(unittest.TestCase):

    def test_exceptions(self):
        with self.subTest('result is true'):
            exception = ValueError
            with ExceptionSilencer(exception):
                int('aa')

            exception = IndexError
            with ExceptionSilencer(exception):
                random_list = [1, 2, 3]
                print(random_list[5])

            exception = KeyError
            with ExceptionSilencer(exception):
                random_dict = {'ke1': 1, 'key2': 2}
                print(random_dict['aaa'])

            exception = TypeError
            with ExceptionSilencer(exception):
                int([1, 2, 3])

            exception = NameError
            with ExceptionSilencer(exception):
                print(temp_name)

            exception = ZeroDivisionError
            with ExceptionSilencer(exception):
                result = 5/0

        with self.subTest('result is false'):
            with self.assertRaises(ValueError):
                with ExceptionSilencer(TypeError):
                    int('aa')

            with self.assertRaises(IndexError):
                with ExceptionSilencer(TypeError):
                    random_list = [1, 2, 3]
                    print(random_list[5])

            with self.assertRaises(KeyError):
                with ExceptionSilencer(TypeError):
                    random_dict = {'ke1': 1, 'key2': 2}
                    print(random_dict['aaa'])

            with self.assertRaises(TypeError):
                with ExceptionSilencer(KeyError):
                    int([1, 2, 3])

            with self.assertRaises(NameError):
                with ExceptionSilencer(KeyError):
                    print(temp_name)

            with self.assertRaises(ZeroDivisionError):
                with ExceptionSilencer(KeyError):
                    result = 5/0


if __name__ == '__main__':
    unittest.main()