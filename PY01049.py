import math
t = int(input())
def isPrime (s):
    for i in range ( 2 ,int(math.sqrt(s))+1 ):
        if s % i == 0:
            return False
    return True
while t > 0:
    n = input()
    cnt = 0
    for i in n :
        if isPrime(int(i)):
            cnt +=1
    not_prime =len(n) - cnt
    if isPrime(len(n)) and cnt > not_prime:
        print('YES')
    else:
        print('NO')
    t -= 1