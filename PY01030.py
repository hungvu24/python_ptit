import math
n , k = [int(i) for i in input().split()]
lowernum = 10**(k-1)
uppernum = 10**k
cnt = 0
for i in range (lowernum, uppernum):
    if math.gcd(int(n),i) == 1:
        print(i, end =' ')
        cnt += 1
        if cnt % 10 == 0:
            print()
            cnt = 0

