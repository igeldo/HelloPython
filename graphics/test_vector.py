from unittest import TestCase

from graphics.point import Point
from graphics.vector import Vector


class TestVector(TestCase):

    def setUp(self):
        self.cut = Vector(5, 6)

    def test_get_x(self):
        # Act
        result = self.cut.getX()

        # Assert
        self.assertEqual(5, result)

    def test_get_y(self):
        # Act
        result = self.cut.getY()

        # Assert
        self.assertEqual(6, result)

    def test_str(self):
        # Act
        result = str(self.cut)

        # Assert
        self.assertEqual("Vector(5,6)", result)

    def test_add_succeeds_for_vector(self):
        # Arrange
        v = Vector(4, 5)

        # Act
        result = self.cut + v

        # Assert
        self.assertEqual(Vector(9, 11), result)

    def test_add_fails_for_point(self):
        # Arrange
        p = Point(4, 5)

        # Act & Assert
        with self.assertRaises(TypeError):
            self.cut + p

    def test_equal_gives_false_for_wrong_type(self):
        # Arrange
        p = Point(3, 4)

        # Act & Assert
        self.assertFalse(self.cut == p)

    def test_equal_gives_false_for_different_x(self):
        # Arrange
        v = Vector(42, 6)

        # Act & Assert
        self.assertFalse(self.cut == v)

    def test_equal_gives_false_for_different_y(self):
        # Arrange
        v = Vector(5, 42)

        # Act & Assert
        self.assertFalse(self.cut == v)

    def test_equal_gives_true_for_same_x_y(self):
        # Arrange
        v = Vector(5, 6)

        # Act & Assert
        self.assertTrue(self.cut == v)

    def test_not_equal_gives_true_for_wrong_type(self):
        # Arrange
        p = Point(3, 4)

        # Act & Assert
        self.assertTrue(self.cut != p)

    def test_not_equal_gives_true_for_different_x(self):
        # Arrange
        v = Vector(42, 6)

        # Act & Assert
        self.assertTrue(self.cut != v)

    def test_not_equal_gives_true_for_different_y(self):
        # Arrange
        v = Vector(5, 42)

        # Act & Assert
        self.assertTrue(self.cut != v)

    def test_not_equal_gives_false_for_same_x_y(self):
        # Arrange
        v = Vector(5, 6)

        # Act & Assert
        self.assertFalse(self.cut != v)
