from graphics.coordinate2d import Coordinate2D


class Vector(Coordinate2D):

    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"Vector({self._x},{self._y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("you can only add Vector to Vector")
        else:
            return Vector(self.getX() + other.getX(), self.getY() + other.getY())
