t = int(input())
while t > 0:
    n = int(input())
    a = input().split()
    a.sort(key = lambda s: (sum(int(i)for i in s), int(s)))
    print(*a)
    t -= 1