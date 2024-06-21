import math


class Phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def Rutgon(self):
        tmp = math.gcd(self.tu, self.mau)
        self.tu = self.tu / tmp
        self.mau = self.mau / tmp
    def __str__(self):
        return "{}/{}".format(int(self.tu), int(self.mau))


if __name__ == '__main__':
    tu, mau =  list(map(int, input().split()))
    A = Phanso(tu , mau)
    A.Rutgon()
    print(A)
