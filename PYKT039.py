def check(n, a, b) :
    for i in range(n) :
        if a[i] > b[i] : return 0
    return 1

t = int(input())
for z in range(t) :
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    if check(n, a, b) == 1 : print("YES")
    else : print("NO")