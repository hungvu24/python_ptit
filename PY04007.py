import math
class Matrix:
    def __init__(self, n , m , a):
        self.n = n
        self.m = m
        self.a = a
    def chuyenvi(self):
        for i in range(self.n):
            for j in range(self.n):
                x = 0
                for k in range (self.m):
                    x += (self.a[i][k] * self.a[j][k])
                print(x, end =' ')
            print()
for i in range(int(input())):
    n , m = map(int , input().split())
    a=[]
    for i in range (n):
        a.append([int(i)for i in input().split()])
    matran = Matrix(n , m , a)
    matran.chuyenvi()
