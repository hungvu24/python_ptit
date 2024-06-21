import math
def isPrime(s):
    if s < 2 :
        return 0
    for i in range(2 , int(math.sqrt(s))+1 ):
        if s % i == 0:
            return 0
    return 1
n, m = [int(i) for i in input().split()]
for i in range (n):
    list = [isPrime(int(i)) for i in input().split()]
    print(*list)
