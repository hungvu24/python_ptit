import math


class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def distance(self, Point):
        dist = math.sqrt((self.x1 - Point.x1) ** 2 + (self.y1 - Point.y1) ** 2)
        return dist

    def Triangle(self, a, b):
        xy = self.distance(a)
        yz = a.distance(b)
        xz = self.distance(b)
        if xy + yz > xz and xy + xz > yz and xz + yz > xy:
            return '%.2f' % (1 / 4 * math.sqrt((xy + xz + yz) * (xy + xz - yz) * (xz + yz - xy) * (xy + yz - xz)))
        else:
            return 'INVALID'


t = int(input())
while t > 0:
    a = [float(i) for i in input().split()]
    p1 = Point(a[0], a[1])
    p2 = Point(a[2], a[3])
    p3 = Point(a[4], a[5])
    for i in a:
        if abs(i) >= 1000:
            print('INVALID')
    else:
        print(p1.Triangle(p2, p3))
    t -= 1
