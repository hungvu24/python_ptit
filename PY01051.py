def check(s):
    if len(s) < 1 or s != s[::-1]:
        return False
    return True
t = int(input())
while t > 0:
    s = str(sum(int(i)for i in input()))

    if check(str(s)):
        print('YES')
    else:
        print('NO')
    t-=1

