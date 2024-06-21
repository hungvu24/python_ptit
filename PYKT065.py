while (True):
    a = [int(i) for i in input().split()]
    if a[0] == -1:
        break
    n = int(input())
    a.sort()
    cnt = 0
    for num in range (a):
        for i in range (2 , n+1):
            if num % i == 1:
                cnt += 1
    print(cnt)


