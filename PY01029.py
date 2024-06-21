import math
t = int(input())
while t > 0 :
    s = input()
    a = []
    if math.gcd(int(s) , int(s[::-1])) == 1 :
        print('YES')
    else:
        print('NO')