from graphics.base.point import Point
from graphics.base.vector import Vector


class Main:
    def run(self):
        p = Point(1, 2)
        print(f"p: {p}")

        v = Vector(3, 4)
        print(f"v: {v}")

        print(f"p + v: {p + v}")
        print(f"v + v: {v + v}")


if __name__ == '__main__':
    main = Main()
    main.run()
