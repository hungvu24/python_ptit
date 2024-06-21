import math
def check(s):
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2:
            return 'NO'
    n = sum(int(i) for i in s)
    for i in range (2 , int(math.sqrt(n))+1):
        if n % i == 0:
            return 'NO'
    return 'YES' if n > 1 else 'NO'
t = int(input())
while t > 0:
    s = input()
    print(check(s))
    t -= 1