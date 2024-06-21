import math
def isPrime(s):
    for i in range(2 ,int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return s > 1
def check(s):
    for i in range(len(s)):
        if (isPrime(i) and not isPrime(int(s[i]))) or ( not isPrime(i) and  isPrime(int(s[i]))):
            return 'NO'
    return 'YES'
t = int(input())
while t > 0:
    s = input()
    print(check(s))
    t -= 1