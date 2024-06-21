import math
class Point :
    def __init__(self , x1 , y1):
        self.x1 = x1
        self.y1 = y1
    def distance(self,Point):
        dist = math.sqrt((self.x1 - Point.x1)**2 + (self.y1 -Point.y1)**2)
        return "%.4f"%dist
def Decimal(n):
    n = float(n)
    return n
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1