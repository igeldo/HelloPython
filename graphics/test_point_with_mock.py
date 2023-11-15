from unittest import TestCase
from unittest.mock import Mock

from graphics.point import Point
from graphics.vector import Vector


class TestPoint(TestCase):

    def setUp(self):
        self.cut = Point(2, 3)

    def test_add_succeeds_for_vector(self):
        # arrange
        other = Mock()
        other.__class__ = Vector
        other.getX.return_value = 4
        other.getY.return_value = 5

        # act
        result = self.cut + other

        # assert
        self.assertEqual(Point(6, 8), result)
        other.getX.assert_called_once()
        other.getY.assert_called_once()

    def test_add_fails_for_point(self):
        # arrange
        other = Mock()
        other.__class__ = Point

        # act & assert
        with self.assertRaises(TypeError):
            self.cut + other

        # assert
        other.getX.assert_not_called()
        other.getY.assert_not_called()
