from abc import ABC


class Coordinate2D(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getX() == other.getX() and self.getY() == other.getY()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
