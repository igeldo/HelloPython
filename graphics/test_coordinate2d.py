from unittest import TestCase

from graphics.coordinate2d import Coordinate2D


class TestCoordinate2D(TestCase):

    def setUp(self):
        self.cut = Coordinate2D(2, 3)

    def test_get_x(self):
        # act
        result = self.cut.getX()

        # assert
        self.assertEqual(2, result)

    def test_get_y(self):
        # act
        result = self.cut.getY()

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
