from __future__ import annotations

from graphics.coordinate2d import Coordinate2D
from graphics.vector import Vector


class Point(Coordinate2D):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"Point({self._x},{self._y})"

    def __add__(self, other: Vector) -> Point:
        if not isinstance(other, Vector):
            raise TypeError("you can only add Vector to Point")
        else:
            return Point(self.getX() + other.getX(), self.getY() + other.getY())
