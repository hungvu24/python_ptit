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
        if max(xy, yz, xz) * 2 >= (xy + yz + xz):
            return 'INVALID'
        else:
            return '%.3f' % (xy + yz + xz)


t = int(input())
c=[]
while t > 0:
    a = [[int(i) for i in input().split()]]
    c = []
    p1 = Point(a[0], a[1])
    p2 = Point(a[2], a[3])
    p3 = Point(a[4], a[5])
    for i in a:
        if abs(i) >= 1000:
            c.append('INVALID')
    else:
        c.append(p1.Triangle(p2, p3))
    t -= 1
for i in range(len(c)):
    print()