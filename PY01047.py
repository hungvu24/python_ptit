import math
def check(s):
    for i in range(2 , int(math.sqrt(s))+1):
        if s % i == 0:
            return 'NO'
    return 'YES' if s > 1 else 'NO'
t = int(input())
while t > 0:

    s = input()
    print(check(int(s[-4:])))
    t-=1