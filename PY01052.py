import math
def isPrime(s):
    for i in range(2 , int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if isPrime(sum):
        print('YES')
    else:
        print('NO')
    t -= 1