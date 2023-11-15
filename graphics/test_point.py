from unittest import TestCase

from graphics.point import Point
from graphics.vector import Vector


class TestPoint(TestCase):

    def setUp(self):
        self.cut = Point(2, 3)

    def test_get_x(self):
        # Act
        result = self.cut.getX()

        # Assert
        self.assertEqual(result, 2)

    def test_get_y(self):
        # Act
        result = self.cut.getY()

        # Assert
        self.assertEqual(result, 3)

    def test_str(self):
        # Act
        result = str(self.cut)

        # Assert
        self.assertEqual(result, "Point(2,3)")

    def test_add_succeeds_for_vector(self):
        # Arrange
        v = Vector(4, 5)

        # Act
        result = self.cut + v

        # Assert
        self.assertEqual(result, Point(6, 8))

    def test_add_fails_for_point(self):
        # Arrange
        p = Point(4, 5)

        # Act & Assert
        with self.assertRaises(TypeError):
            self.cut + p

    def test_equal_gives_false_for_wrong_type(self):
        # Arrange
        v = Vector(3, 4)

        # Act & Assert
        self.assertFalse(self.cut == v)

    def test_equal_gives_false_for_different_x(self):
        # Arrange
        p = Point(3, 3)

        # Act & Assert
        self.assertFalse(self.cut == p)

    def test_equal_gives_false_for_different_y(self):
        # Arrange
        p = Point(2, 4)

        # Act & Assert
        self.assertFalse(self.cut == p)

    def test_equal_gives_true_for_same_x_y(self):
        # Arrange
        p = Point(2, 3)

        # Act & Assert
        self.assertTrue(self.cut == p)

    def test_not_equal_gives_true_for_wrong_type(self):
        # Arrange
        v = Vector(3, 4)

        # Act & Assert
        self.assertTrue(self.cut != v)

    def test_not_equal_gives_true_for_different_x(self):
        # Arrange
        p = Point(42, 3)

        # Act & Assert
        self.assertTrue(self.cut != p)

    def test_not_equal_gives_true_for_different_y(self):
        # Arrange
        p = Point(2, 42)

        # Act & Assert
        self.assertTrue(self.cut != p)

    def test_not_equal_gives_false_for_same_x_y(self):
        # Arrange
        p = Point(2, 3)

        # Act & Assert
        self.assertFalse(self.cut != p)
