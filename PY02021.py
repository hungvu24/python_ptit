t = int(input())
for _ in range(t):

    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d, e, f = {}, {}, {}
    for i in a:
        d[i] = 1
    for i in b:
        e[i] = 1
    for i in c:
        f[i] = 1
    for i in sorted(list(d)):
        if i in e:
            if i in f:
                print(i, end=" ")

        else:
            print("NO")
        print()
