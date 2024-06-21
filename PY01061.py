import math
def isPrime(s):
    for i in range(2 , int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    s = input()
    if isPrime(int(s[:3])) and isPrime(int(s[-3:])):
        print('YES')
    else:
        print('NO')
    t -= 1


