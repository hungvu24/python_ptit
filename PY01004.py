import math


def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


t = int(input())
while t > 0:
    n = int(input())
    k = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            k += 1
    if isPrime(k) == 1:
        print('YES')
    else:
        print('NO')
    t -= 1
