from imaplib import Int2AP
import math
def isPrime(s):
    if s < 2 :
        return False
    for i in range(2 , int(math.sqrt(s))+1 ):
        if s % i == 0:
            return False
    return True
n = int(input())
a = [int(i) for i in input().split()]
m = {}
for i in a :
    if isPrime(i):
        if i in m :
            m[i] += 1
        else :
            m[i] = 1
for i in a :
    if i in m and m[i] > 0:
        print(i , m[i])
        m[i] = 0