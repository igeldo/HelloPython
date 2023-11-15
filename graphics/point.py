from graphics.vector import Vector


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def __str__(self):
        return f"Point({self._x},{self._y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("you can only add Vector to Point")
        else:
            return Point(self.getX() + other.getX(), self.getY() + other.getY())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getX() == other.getX()  and self.getY() == other.getY()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
