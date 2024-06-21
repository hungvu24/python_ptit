import math
def isPrime(s):
    if s < 2:
        return False
    for i in range(2 , int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return True
def check(s):
    cnt = 0
    if not isPrime(len(s)):
        return 'NO'
    for i in s :
        if isPrime(int(i)):
            cnt += 1
    num_not_prime = len(s) - cnt
    if (num_not_prime >= cnt):
        return 'NO'
    return 'YES'
t = int(input())
while t > 0:
    s = input()
    print(check(s))
    t -= 1
