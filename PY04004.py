import math
def ob(tuso,mauso):
    return PS(tuso,mauso)
class PS:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Rutgon(self):
        tmp = math.gcd(self.x , self.y)
        self.x = self.x/tmp
        self.y = self.y/tmp
    def add(self,PS):
        tuso = self.x * PS.y + self.y * PS.x
        mauso = self.y * PS.y
        return ob(tuso , mauso)


    def __str__(self):
        return "{}/{}".format(int(self.x),int(self.y))
if __name__ == '__main__':
    a  = [int(i) for i in input().split()]
    A = PS(a[0],a[1])
    B = PS(a[2],a[3])
    C = A.add(B)
    C.Rutgon()

    print(C)


