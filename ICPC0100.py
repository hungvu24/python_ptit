t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    dem = 0
    for j in range ( n - 1):
        Min = min(a[j],a[j+1])
        Max = max(a[j],a[j+1])
        while Min*2 < Max :
            dem = dem + 1
            Min *= 2
    print(dem)