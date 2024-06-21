t = int(input())
def Laixuatnganhang(n , x , m):
    r = x / 100
    nam = 0
    while n < m :
        n = n * (1 + r)
        nam += 1
    return nam
while t > 0 :
    [n , x , m] = list(map(float,input().split()))
    print(Laixuatnganhang(n , x , m))
    t -= 1