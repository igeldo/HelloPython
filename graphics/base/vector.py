from __future__ import annotations

from graphics.base.coordinate2d import Coordinate2D


class Vector(Coordinate2D):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"Vector({self._x},{self._y})"

    def __add__(self, other) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("you can only add Vector to Vector")
        return Vector(self.get_x() + other.get_x(), self.get_y() + other.get_y())
