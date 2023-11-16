from abc import ABC


class Coordinate2D(ABC):
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.get_x() == other.get_x() and self.get_y() == other.get_y()
        else:
            return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
