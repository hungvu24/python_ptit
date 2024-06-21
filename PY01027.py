def kt1(s):
    a = [int(i) for i in s]
    for i in a:
        if i != 6 and i != 8:
            return 0
    return 1


def kt2(s):
    a = [int(i) for i in s]
    for i in range(len(s)):
        if a[0] == 8:
            return 0
        if a[i] == 8 and a[i - 1] != 6 and a[i - 1] != 8:
            return 0
        if i > 1 and a[i] == 8 and a[i - 1] == 8 and a[i - 2] != 6:
            return 0
    return 1


s = input()
if kt1(s) == 1 and kt2(s) == 1:
    print("YES")
else:
    print("NO")
