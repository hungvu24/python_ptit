def mul(s):
    x = 1
    for i in s :
        x *= int(i)
    return x
t = int(input())
while t > 0:
    n = int(input())
    a = input().split()
    a.sort(key = lambda s:(mul(int(i) for i in s), int(s)))
    print(*a)
    t -= 1