t = int(input())
def check(s):
    if len(s) < 3:
        return 'NO'
    a = list(int(i) for i in s)
    up = True
    for i in range(1 , len(a)):
        if up and a[i] <= a[i-1]:
            up = False
        elif not up and a[i] >= a[i-1]:
            return 'NO'
    return 'YES'
while t > 0:
    s=input()
    print(check(s))
    t -= 1