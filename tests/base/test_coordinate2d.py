from unittest import TestCase

from graphics.base.coordinate2d import Coordinate2D


class TestCoordinate2D(TestCase):

    def setUp(self):
        self.cut = Coordinate2D(2, 3)

    def test_init_fails_for_wrong_x_type(self):
        # arrange
        x = 'I am a string'
        y = 42

        # act & assert
        with self.assertRaisesRegex(TypeError, 'x can only be a float or int'):
            Coordinate2D(x, y)

    def test_init_fails_for_wrong_y_type(self):
        # arrange
        x = 42
        y = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'y can only be a float or int'):
            Coordinate2D(x, y)

    def test_get_x(self):
        # act
        result = self.cut.get_x()

        # assert
        self.assertEqual(2, result)

    def test_get_y(self):
        # act
        result = self.cut.get_y()

        # assert
        self.assertEqual(3, result)

    def test_equal_gives_false_for_wrong_type(self):
        # arrange
        other = "I am a string"

        # act & assert
        self.assertFalse(self.cut == other)

    def test_equal_gives_false_for_different_x(self):
        # arrange
        other = Coordinate2D(3, 3)

        # act & assert
        self.assertFalse(self.cut == other)

    def test_equal_gives_false_for_different_y(self):
        # arrange
        other = Coordinate2D(2, 4)

        # act & assert
        self.assertFalse(self.cut == other)

    def test_equal_gives_true_for_same_x_y(self):
        # arrange
        other = Coordinate2D(2, 3)

        # act & assert
        self.assertTrue(self.cut == other)

    def test_not_equal_gives_true_for_wrong_type(self):
        # arrange
        other = "I am a string"

        # act & assert
        self.assertTrue(self.cut != other)

    def test_not_equal_gives_true_for_different_x(self):
        # arrange
        other = Coordinate2D(42, 3)

        # act & assert
        self.assertTrue(self.cut != other)

    def test_not_equal_gives_true_for_different_y(self):
        # arrange
        other = Coordinate2D(2, 42)

        # act & assert
        self.assertTrue(self.cut != other)

    def test_not_equal_gives_false_for_same_x_y(self):
        # arrange
        other = Coordinate2D(2, 3)

        # act & assert
        self.assertFalse(self.cut != other)
