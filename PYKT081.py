def Solve(s):
    if len(s) < 4:
        return 0
    for i in s :
        if i.isdigit():
            if int(i) < 0 or int(i) > 255 :
                return 0
        else: return 0
    return 1
t = int(input())
for _ in range(t):
    a = input().split('.')
    if Solve(a) == 1:
        print('YES')
    else:
        print('NO')