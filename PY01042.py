def check(s):
    for i in s:
        if int(i) != 0 and int(i) != 1 and int(i) != 2:
            return 'NO'
    return 'YES'


t = int(input())
while t > 0:
    s = input()
    print(check(s))
    t -= 1
