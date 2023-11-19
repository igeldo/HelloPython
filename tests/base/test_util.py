from unittest import TestCase

from graphics.base.util import check_float, check_float_positive


class Test(TestCase):

    def test_check_float_accepts_int(self):
        # arrange
        value = 42

        # act
        result = check_float(value)

        # assert
        self.assertTrue(isinstance(result, float))
        self.assertEqual(42.0, result)

    def test_check_float_accepts_float(self):
        # arrange
        value = 4.2

        # act
        result = check_float(value)

        # assert
        self.assertTrue(isinstance(result, float))
        self.assertEqual(4.2, result)

    def test_check_float_fails_for_string(self):
        # arrange
        value = "I am a string"

        # act & assert
        with self.assertRaisesRegex(TypeError, 'coordinate can only be a float or int'):
            check_float(value, 'coordinate')

    def test_check_float_positive_accepts_int(self):
        # arrange
        value = 42

        # act
        result = check_float_positive(value)

        # assert
        self.assertTrue(isinstance(result, float))
        self.assertEqual(42.0, result)

    def test_check_float_positive_accepts_float(self):
        # arrange
        value = 4.2

        # act
        result = check_float_positive(value)

        # assert
        self.assertTrue(isinstance(result, float))
        self.assertEqual(4.2, result)

    def test_check_float_positive_fails_for_string(self):
        # arrange
        value = "I am a string"

        # act & assert
        with self.assertRaisesRegex(TypeError, 'coordinate can only be a float or int'):
            check_float(value, 'coordinate')

    def test_check_float_positive_fails_for_zero(self):
        # arrange
        value = 0

        # act & assert
        with self.assertRaisesRegex(ValueError, 'coordinate must be greater than zero'):
            check_float_positive(value, 'coordinate')

    def test_check_float_positive_fails_for_negative(self):
        # arrange
        value = -1

        # act & assert
        with self.assertRaisesRegex(ValueError, 'value must be greater than zero'):
            check_float_positive(value)
