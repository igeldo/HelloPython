from graphics.point import Point
from graphics.vector import Vector


class Main:
    def run(self):
        p = Point(1, 2)
        print(p)

        v = Vector(3,4)
        print(v)

        p2 = p + v
        print (p2)

        v2 = v +v
        print(v2)

        print(p+v2)

if __name__ == '__main__':
    main = Main()
    main.run()
