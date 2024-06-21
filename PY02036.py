import math
n = int(input())
a = sorted([int(i) for i in input().split()])
for i in range(n):
    for j in range(i + 1 , n):
        if math.gcd(a[i] , a[j]) == 1:
            print(str(a[i]) + ' ' + str(a[j]))
