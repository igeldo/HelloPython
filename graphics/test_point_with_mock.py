from unittest import TestCase
from unittest.mock import Mock

from graphics.point import Point
from graphics.vector import Vector


class TestPoint(TestCase):

    def setUp(self):
        self.cut = Point(2, 3)

    def test_add_succeeds_for_vector(self):
        # Arrange
        v = Mock()
        v.__class__ = Vector
        v.getX.return_value = 4
        v.getY.return_value = 5

        # Act
        result = self.cut + v

        # Assert
        self.assertEqual(Point(6, 8), result)
        v.getX.assert_called_once()
        v.getY.assert_called_once()

    def test_add_fails_for_point(self):
        # Arrange
        p = Mock()
        p.__class__ = Point

        # Act & Assert
        with self.assertRaises(TypeError):
            self.cut + p

        # Assert
        p.getX.assert_not_called()
        p.getY.assert_not_called()
