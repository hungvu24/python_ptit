def gcd(a , b):
    if a < b:
        temp = a
        a = b
        b = temp
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a

def solve(a , b , m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        b //= 2
        a = (a * a) % m
    return res

def gcd_extend(a , b):
    u1 , u2 , u3 = 1 , 0 , a
    v1 , v2 , v3 = 0 , 1 , b
    while v3 != 0:
        q = u3 // v3
        t1 , t2 , t3 = u1 - q * v1 , u2 - q * v2 , u3 - q * v3
        u1 , u2 , u3 = v1 , v2 , v3
        v1 , v2 , v3 = t1 , t2 , t3
    return u1 , u2 , u3

def get_d(e , phi):
    d = gcd_extend(e , phi)[0]
    if d < 0:
        d += phi
    return d


a = 999999999999999999999999
b = 999999999999999999999999
m = 99999999999999999999
res = solve(a , b , m)
print(res)